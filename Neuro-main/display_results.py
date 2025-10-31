#!/usr/bin/env python3
"""
Display Job Search Results in Terminal
Shows results in a nice, readable format
"""

import json
import os
import sys
from pathlib import Path
from typing import List, Dict

def display_results(json_file: str = None):
    """Display job search results from JSON file"""
    
    # Find the most recent results file if not specified
    if json_file is None:
        results_dir = Path("job_search_results")
        if not results_dir.exists():
            print("❌ No job search results directory found.")
            print("   Run: python run_neuro.py my_job_search.neuro")
            return
        
        # Get all JSON files sorted by modification time
        json_files = sorted(
            results_dir.glob("job_search_*.json"),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
        
        if not json_files:
            print("❌ No job search results found.")
            print("   Run: python run_neuro.py my_job_search.neuro")
            return
        
        json_file = json_files[0]
        print(f"📁 Displaying results from: {json_file.name}\n")
    
    # Load and display results
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        display_results_data(data)
        
    except Exception as e:
        print(f"❌ Error reading results file: {e}")
        sys.exit(1)

def display_results_data(data: Dict):
    """Display results from loaded JSON data"""
    
    # Header
    print("=" * 70)
    print("🧠 NEURO JOB SEARCH RESULTS")
    print("=" * 70)
    print(f"\n📅 Search Date: {data.get('search_date', 'Unknown')}")
    
    # Summary
    summary = data.get('summary', {})
    print(f"\n📊 SUMMARY:")
    print(f"   Total Jobs Found: {summary.get('total_jobs', 0)}")
    print(f"   High Matches (>70%): {summary.get('high_matches', 0)}")
    print(f"   Medium Matches (50-69%): {summary.get('medium_matches', 0)}")
    print(f"   Low Matches (<50%): {summary.get('low_matches', 0)}")
    
    # Profile info
    profile = data.get('profile', {})
    if profile:
        print(f"\n👤 YOUR PROFILE:")
        print(f"   Name: {profile.get('name', 'N/A')}")
        print(f"   Target Roles: {', '.join(profile.get('target_roles', []))}")
        print(f"   Experience: {profile.get('experience_level', 'N/A')}")
        print(f"   Remote Preference: {'Yes' if profile.get('remote_preference') else 'No'}")
        print(f"   Skills: {', '.join(profile.get('skills', [])[:5])}")
        if len(profile.get('skills', [])) > 5:
            print(f"             {', '.join(profile.get('skills', [])[5:])}")
    
    # Jobs by match score
    jobs = data.get('jobs', [])
    if not jobs:
        print("\n⚠️  No jobs found in results.")
        return
    
    # Sort by match score
    sorted_jobs = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)
    
    # High matches
    high_matches = [j for j in sorted_jobs if j.get('match_score', 0) >= 70]
    if high_matches:
        print(f"\n🏆 HIGH MATCHES (>70%): {len(high_matches)} jobs")
        print("-" * 70)
        for i, job in enumerate(high_matches[:10], 1):
            display_job(job, i)
    
    # Medium matches
    medium_matches = [j for j in sorted_jobs if 50 <= j.get('match_score', 0) < 70]
    if medium_matches:
        print(f"\n✅ MEDIUM MATCHES (50-69%): {len(medium_matches)} jobs")
        print("-" * 70)
        for i, job in enumerate(medium_matches[:15], 1):
            display_job(job, i)
    
    # Low matches
    low_matches = [j for j in sorted_jobs if j.get('match_score', 0) < 50]
    if low_matches:
        print(f"\n📋 LOW MATCHES (<50%): {len(low_matches)} jobs")
        print("-" * 70)
        for i, job in enumerate(low_matches[:10], 1):
            display_job(job, i)
    
    # Group by platform
    print(f"\n📊 JOBS BY PLATFORM:")
    print("-" * 70)
    by_platform = {}
    for job in sorted_jobs:
        platform = job.get('platform', 'unknown')
        if platform not in by_platform:
            by_platform[platform] = []
        by_platform[platform].append(job)
    
    for platform, platform_jobs in sorted(by_platform.items()):
        print(f"\n   {platform.upper()}: {len(platform_jobs)} jobs")
        for job in platform_jobs[:5]:
            score = job.get('match_score', 0)
            title = job.get('title', 'N/A')[:50]
            company = job.get('company', 'N/A')[:30]
            print(f"      • {title} at {company} ({score:.1f}%)")
        if len(platform_jobs) > 5:
            print(f"      ... and {len(platform_jobs) - 5} more")

def display_job(job: Dict, index: int = None):
    """Display a single job in readable format"""
    
    title = job.get('title', 'N/A')
    company = job.get('company', 'N/A')
    location = job.get('location', 'N/A')
    url = job.get('url', 'N/A')
    platform = job.get('platform', 'N/A')
    score = job.get('match_score', 0)
    posted_date = job.get('posted_date', '')
    description = job.get('description', '')
    required_skills = job.get('required_skills', [])
    
    if index:
        print(f"\n{index}. {title}")
    else:
        print(f"\n{title}")
    
    print(f"   Company: {company}")
    print(f"   Location: {location}")
    if posted_date:
        print(f"   Posted: {posted_date}")
    print(f"   Platform: {platform}")
    print(f"   Match Score: {score:.1f}%")
    
    if required_skills:
        skills_str = ', '.join(required_skills[:5])
        print(f"   Skills: {skills_str}")
        if len(required_skills) > 5:
            print(f"           {', '.join(required_skills[5:])}")
    
    if description:
        desc_preview = description[:200].replace('\n', ' ')
        if len(description) > 200:
            desc_preview += "..."
        print(f"   Description: {desc_preview}")
    
    print(f"   URL: {url}")
    print("-" * 70)

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Display job search results')
    parser.add_argument('file', nargs='?', help='JSON results file (optional - uses most recent)')
    
    args = parser.parse_args()
    
    # Fix Windows encoding
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    
    display_results(args.file)

if __name__ == "__main__":
    main()

