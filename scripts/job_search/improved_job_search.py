#!/usr/bin/env python3
"""
Better Job Search - Only gets AI/ML/Prompt Engineering jobs
Much stricter filtering for relevant positions only
"""
import requests
import json
import re
from datetime import datetime
from pathlib import Path

def is_ai_ml_job(title, description):
    """Check if job is AI/ML related - includes ANY role with AI in it"""
    
    # Convert to lowercase for matching
    title_lower = title.lower()
    desc_lower = description.lower() if description else ""
    
    # Check for "AI" in title with word boundaries
    # This catches: AI Engineer, AI Manager, AI Test Engineer, AI Implementation, etc.
    if re.search(r'\bai\b', title_lower):
        # Exclude false positives
        if not any(x in title_lower for x in ['email', 'gmail', 'detail', 'retail', 'mla ', 'nail', 'hair', 'waiter', 'waitr']):
            return True
    
    # Comprehensive AI/ML keywords that must appear in title or description
    ai_ml_keywords = [
        'artificial intelligence',
        'machine learning',
        'deep learning',
        'neural network',
        'prompt engineer',
        'llm',
        'large language model',
        'gpt',
        'transformer',
        'nlp',
        'natural language processing',
        'computer vision',
        'ml engineer',
        'ml ops',
        'mlops',
        'data scientist',
        'research scientist',
        'conversational ai',
        'generative ai',
        'ai/ml',
    ]
    
    # Check title for any AI/ML keyword
    for keyword in ai_ml_keywords:
        if keyword in title_lower:
            return True
    
    # Check for ML with word boundaries
    if re.search(r'\bml\b', title_lower):
        if not any(x in title_lower for x in ['email', 'gmail', 'html', 'xml', 'yaml']):
            return True
    
    # For description, need strong indicators (at least 2 matches)
    # This catches jobs that don't have AI in title but are AI-focused
    matches = sum(1 for keyword in ai_ml_keywords if keyword in desc_lower)
    if matches >= 2:
        return True
    
    return False

def search_ai_ml_jobs():
    """Search and get ALL AI-related jobs (any role with AI in title)"""
    
    print("Searching for ALL AI-related jobs...")
    print("Includes: AI Engineers, AI Managers, AI Test Engineers, etc.")
    print("=" * 60)
    
    all_jobs = []
    
    # 1. RemoteOK - Get ALL jobs and filter for AI/ML only
    print("\n1. RemoteOK - Filtering for AI/ML positions...")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get('https://remoteok.com/api', headers=headers, timeout=10)
        data = r.json()
        
        # Skip metadata (first entry)
        jobs = data[1:] if len(data) > 0 and data[0].get('id') == '0' else data
        
        print(f"   Downloaded {len(jobs)} jobs, filtering for AI-related positions...")
        
        for job in jobs:
            position = job.get('position', '')
            company = job.get('company', '')
            description = job.get('description', '')
            
            # Convert description from HTML to text if needed
            if isinstance(description, str) and '<' in description:
                # Simple HTML strip
                description = re.sub(r'<[^>]+>', ' ', description)
            
            # Apply AI/ML filter (now includes any role with AI in title)
            if is_ai_ml_job(position, description):
                # Score based on how directly AI-related
                match_score = 90.0 if 'ai' in position.lower() or 'machine learning' in position.lower() else 85.0
                
                all_jobs.append({
                    "title": position,
                    "company": company,
                    "location": "Remote",
                    "url": f"https://remoteok.com{job.get('url', '')}",
                    "description": (description[:500] if isinstance(description, str) else ''),
                    "platform": "remoteok",
                    "posted_date": job.get('date', None),
                    "match_score": match_score,
                    "required_skills": [],
                    "preferred_skills": []
                })
        
        print(f"   SUCCESS: Found {len(all_jobs)} AI-related jobs!")
        
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # 2. Add AI-specific curated search links
    print("\n2. Adding AI/ML specific search links...")
    
    # Wellfound - AI specific
    ai_roles = ["ai-engineer", "machine-learning-engineer", "prompt-engineer"]
    for role in ai_roles:
        all_jobs.append({
            "title": f"{role.replace('-', ' ').title()} - Wellfound",
            "company": "Wellfound (Browse Startups)",
            "location": "Remote/Global",
            "url": f"https://wellfound.com/role/l/{role}",
            "description": f"Browse {role.replace('-', ' ')} positions at top startups on Wellfound",
            "platform": "wellfound",
            "posted_date": None,
            "match_score": 75.0,
            "required_skills": [role.replace('-', ' ')],
            "preferred_skills": []
        })
    
    # Y Combinator - AI focused
    all_jobs.append({
        "title": "AI/ML Engineer - Y Combinator Startups",
        "company": "Y Combinator",
        "location": "Remote/Global",
        "url": "https://www.workatastartup.com/jobs?searchTerm=ai+ml+engineer",
        "description": "Browse AI and ML engineering roles at Y Combinator funded startups",
        "platform": "yc",
        "posted_date": None,
        "match_score": 80.0,
        "required_skills": ["ai", "ml"],
        "preferred_skills": []
    })
    
    # LinkedIn - AI/ML specific searches
    linkedin_searches = [
        ("Prompt Engineer", "prompt%20engineer"),
        ("AI Engineer", "ai%20engineer"),
        ("Machine Learning Engineer", "machine%20learning%20engineer")
    ]
    
    for title, query in linkedin_searches:
        all_jobs.append({
            "title": f"{title} - LinkedIn",
            "company": "LinkedIn (Browse)",
            "location": "remote",
            "url": f"https://www.linkedin.com/jobs/search/?keywords={query}&location=remote&f_WT=2",
            "description": f"Browse {title} positions on LinkedIn with remote filter",
            "platform": "linkedin",
            "posted_date": None,
            "match_score": 70.0,
            "required_skills": [title.lower()],
            "preferred_skills": []
        })
    
    curated_count = len(all_jobs) - len([j for j in all_jobs if j['platform'] == 'remoteok'])
    print(f"   Added {curated_count} curated AI/ML search links")
    
    # Create summary
    summary = {
        "total_jobs": len(all_jobs),
        "high_matches": len([j for j in all_jobs if j['match_score'] >= 70]),
        "medium_matches": len([j for j in all_jobs if 40 <= j['match_score'] < 70]),
        "low_matches": len([j for j in all_jobs if j['match_score'] < 40]),
        "real_jobs": len([j for j in all_jobs if j['platform'] == 'remoteok']),
        "search_links": curated_count
    }
    
    # Save results
    results = {
        "search_date": datetime.now().isoformat(),
        "profile": {
            "name": "Elena Mereanu",
            "email": "elena.mereanu@gmail.com",
            "target_roles": ["prompt engineer", "ai engineer", "ml engineer"],
            "skills": ["python", "pytorch", "llm", "gpt", "transformers"],
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
    output_file = "ai_ml_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'='*60}")
    print(f"RESULTS:")
    print(f"  Total jobs: {summary['total_jobs']}")
    print(f"  Real AI/ML jobs from RemoteOK: {summary['real_jobs']}")
    print(f"  Curated search links: {summary['search_links']}")
    print(f"  High matches (70%+): {summary['high_matches']}")
    print(f"\nSaved to: {output_file}")
    print(f"\nTo view: python convert_my_results.py {output_file}")
    
    return results

if __name__ == "__main__":
    search_ai_ml_jobs()

