#!/usr/bin/env python3
"""
Improved Job Search - Gets REAL job listings
"""
import requests
import json
from datetime import datetime
from pathlib import Path

def search_real_jobs():
    """Search and get REAL job listings"""
    
    target_roles = ["prompt engineer", "ai engineer", "ml engineer", "machine learning"]
    skills = ["python", "pytorch", "llm", "gpt", "transformers", "ai", "ml"]
    
    print("Searching for REAL job listings...")
    print("=" * 60)
    
    all_jobs = []
    
    # 1. RemoteOK - Get ALL jobs and filter locally
    print("\n1. RemoteOK...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get('https://remoteok.com/api', headers=headers, timeout=10)
        data = r.json()
        
        # Skip metadata (first entry)
        jobs = data[1:] if len(data) > 0 and data[0].get('id') == '0' else data
        
        print(f"   Downloaded {len(jobs)} jobs, filtering...")
        
        for job in jobs:
            position = job.get('position', '').lower()
            company = job.get('company', '')
            description = job.get('description', '').lower() if job.get('description') else ''
            
            # Check if job matches any target role or skill
            matches = False
            for role in target_roles:
                if role.lower() in position or role.lower() in description:
                    matches = True
                    break
            
            if not matches:
                for skill in skills:
                    if skill in position or skill in description:
                        matches = True
                        break
            
            if matches:
                all_jobs.append({
                    "title": job.get('position', 'N/A'),
                    "company": company,
                    "location": "Remote",
                    "url": f"https://remoteok.com{job.get('url', '')}",
                    "description": (job.get('description', '')[:500] if isinstance(job.get('description'), str) else ''),
                    "platform": "remoteok",
                    "posted_date": job.get('date', None),
                    "match_score": 70.0,
                    "required_skills": [],
                    "preferred_skills": []
                })
        
        print(f"   SUCCESS: Found {len(all_jobs)} matching jobs!")
        
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # 2. Add curated search links for other platforms
    print("\n2. Adding curated search links...")
    
    # Wellfound
    for role in target_roles[:3]:  # Just main roles
        all_jobs.append({
            "title": f"{role.title()} - Wellfound",
            "company": "Wellfound (Browse)",
            "location": "Remote/Global",
            "url": f"https://wellfound.com/role/l/{role.replace(' ', '-')}",
            "description": f"Browse {role} startup jobs on Wellfound (formerly AngelList)",
            "platform": "wellfound",
            "posted_date": None,
            "match_score": 65.0,
            "required_skills": [role],
            "preferred_skills": []
        })
    
    # Y Combinator
    all_jobs.append({
        "title": "AI/ML Engineer - Y Combinator",
        "company": "Y Combinator Startups",
        "location": "Remote/Global",
        "url": "https://www.workatastartup.com/jobs?searchTerm=ai+ml+engineer",
        "description": "Browse AI and ML engineering roles at Y Combinator startups",
        "platform": "yc",
        "posted_date": None,
        "match_score": 70.0,
        "required_skills": ["ai", "ml"],
        "preferred_skills": []
    })
    
    # LinkedIn (best for manual browsing)
    for role in target_roles[:3]:
        all_jobs.append({
            "title": f"{role.title()} - LinkedIn",
            "company": "LinkedIn (Browse)",
            "location": "remote",
            "url": f"https://www.linkedin.com/jobs/search/?keywords={role.replace(' ', '%20')}&location=remote&f_WT=2",
            "description": f"Browse {role} positions on LinkedIn with remote filter",
            "platform": "linkedin",
            "posted_date": None,
            "match_score": 60.0,
            "required_skills": [role],
            "preferred_skills": []
        })
    
    print(f"   Added {len(all_jobs) - len([j for j in all_jobs if j['platform'] == 'remoteok'])} curated links")
    
    # Create summary
    summary = {
        "total_jobs": len(all_jobs),
        "high_matches": len([j for j in all_jobs if j['match_score'] >= 70]),
        "medium_matches": len([j for j in all_jobs if 40 <= j['match_score'] < 70]),
        "low_matches": len([j for j in all_jobs if j['match_score'] < 40])
    }
    
    # Save results
    results = {
        "search_date": datetime.now().isoformat(),
        "profile": {
            "name": "Elena Mereanu",
            "email": "elena.mereanu@gmail.com",
            "target_roles": target_roles[:3],
            "skills": skills,
            "experience_level": "junior",
            "locations": ["remote", "US", "Boston", "New York"],
            "remote_preference": True,
            "github_url": "https://github.com/ElaMCB/Neuro",
            "linkedin_url": "linkedin.com/in/elenamereanu"
        },
        "jobs": sorted(all_jobs, key=lambda x: x['match_score'], reverse=True),
        "summary": summary
    }
    
    # Save to file
    output_file = "improved_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"RESULTS:")
    print(f"  Total jobs: {summary['total_jobs']}")
    print(f"  High matches (70%+): {summary['high_matches']}")
    print(f"  Real jobs from RemoteOK: {len([j for j in all_jobs if j['platform'] == 'remoteok'])}")
    print(f"\nSaved to: {output_file}")
    print(f"\nTo view: python convert_my_results.py {output_file}")
    
    return results

if __name__ == "__main__":
    search_real_jobs()

