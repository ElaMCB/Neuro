#!/usr/bin/env python3
"""
Test if we can get REAL job listings from RemoteOK
"""
import requests
import json
from urllib.parse import quote

def test_remoteok():
    """Test RemoteOK API - should return real jobs"""
    print("Testing RemoteOK API...")
    
    roles = ["prompt engineer", "ai engineer", "ml engineer"]
    
    for role in roles:
        try:
            search_term = quote(role.lower())
            url = f"https://remoteok.com/api?tags={search_term}"
            
            print(f"\nSearching for: {role}")
            print(f"URL: {url}")
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if isinstance(data, list) and len(data) > 1:
                # Skip metadata
                jobs = data[1:] if data[0].get('id') == '0' else data
                
                print(f"  SUCCESS: Found {len(jobs)} real jobs!")
                
                # Show first 3
                for i, job in enumerate(jobs[:3], 1):
                    print(f"\n  {i}. {job.get('position', 'N/A')}")
                    print(f"     Company: {job.get('company', 'N/A')}")
                    print(f"     URL: https://remoteok.com{job.get('url', '')}")
            else:
                print(f"  WARNING: No jobs found")
                
        except Exception as e:
            print(f"  ERROR: {e}")

if __name__ == "__main__":
    test_remoteok()

