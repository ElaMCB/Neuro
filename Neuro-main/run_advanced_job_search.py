#!/usr/bin/env python3
"""
Advanced Job Search Runner for Neuro
Runs the enhanced job search system based on Neuro intent
"""

import os
import sys
import json
from advanced_job_search import JobSearchEngine, UserProfile
from resume_preparer import ResumePreparer

def load_profile_from_config(config_path: str = "profile_config.json") -> UserProfile:
    """Load user profile from configuration"""
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            return UserProfile(**config)
    else:
        print(f"❌ Profile config not found: {config_path}")
        print("   Please create profile_config.json or run schedule_job_search.py to generate one.")
        sys.exit(1)

def run_advanced_job_search():
    """Run the advanced job search system"""
    print("🧠 NEURO ADVANCED JOB SEARCH")
    print("=" * 60)
    print("Multi-platform job search with profile matching\n")
    
    # Load profile
    profile = load_profile_from_config()
    
    print(f"👤 Profile loaded: {profile.name}")
    print(f"   Target roles: {', '.join(profile.target_roles)}")
    print(f"   Experience: {profile.experience_level}")
    print(f"   Remote: {'Yes' if profile.remote_preference else 'No'}\n")
    
    # Initialize search engine
    search_engine = JobSearchEngine(profile)
    
    # Search all platforms
    jobs = search_engine.search_all_platforms()
    
    # Generate and display report
    report = search_engine.generate_report()
    print(report)
    
    # Save results
    results_file = search_engine.save_results()
    
    # Ask if user wants to prepare resumes for top matches
    top_matches = [j for j in jobs if j.match_score >= 70][:5]
    if top_matches:
        print(f"\n📝 Found {len(top_matches)} high-matching positions (>70%)")
        response = input("   Would you like to prepare tailored resumes for these? (y/n): ").strip().lower()
        
        if response == 'y':
            print("\n📄 Preparing tailored application packages...")
            resume_preparer = ResumePreparer(profile.resume_path)
            
            for job in top_matches:
                print(f"\n   Processing: {job.title} at {job.company}")
                try:
                    prepared = resume_preparer.prepare_for_job(
                        job_title=job.title,
                        company=job.company,
                        job_description=job.description,
                        job_url=job.url
                    )
                    print(f"   ✓ Application package ready for {job.company}")
                except Exception as e:
                    print(f"   ⚠️  Error: {e}")
    
    print("\n✅ Job search complete!")
    print(f"\n📊 Next steps:")
    print(f"   1. Review results in: {results_file}")
    print(f"   2. Review tailored resumes in: resume_templates/")
    print(f"   3. Set up weekly search: python schedule_job_search.py")
    print(f"   4. Apply to top matches this week!")

if __name__ == "__main__":
    run_advanced_job_search()

