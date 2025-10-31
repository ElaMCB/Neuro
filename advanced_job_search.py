"""
Advanced Job Search System for Neuro
Searches multiple platforms, matches profile, and prepares applications
"""

import os
import json
import re
import time
import requests
import urllib.parse
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path
import webbrowser
from urllib.parse import quote, urlencode

# BeautifulSoup for web scraping
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("⚠️  BeautifulSoup4 not installed. Install with: pip install beautifulsoup4")

@dataclass
class JobListing:
    """Represents a job listing"""
    title: str
    company: str
    location: str
    url: str
    description: str
    platform: str
    posted_date: Optional[str] = None
    match_score: float = 0.0
    required_skills: List[str] = None
    preferred_skills: List[str] = None
    
    def __post_init__(self):
        if self.required_skills is None:
            self.required_skills = []
        if self.preferred_skills is None:
            self.preferred_skills = []

@dataclass
class UserProfile:
    """User's profile for matching"""
    name: str
    email: str
    target_roles: List[str]
    skills: List[str]
    experience_level: str  # "junior", "mid", "senior"
    locations: List[str]
    remote_preference: bool
    resume_path: Optional[str] = None
    github_url: Optional[str] = None
    linkedin_url: Optional[str] = None

class JobSearchEngine:
    """Multi-platform job search engine"""
    
    def __init__(self, user_profile: UserProfile):
        self.profile = user_profile
        self.jobs: List[JobListing] = []
        self.searches_performed = []
        
    def search_all_platforms(self) -> List[JobListing]:
        """Search all configured job platforms"""
        print("🔍 Starting multi-platform job search...")
        print("=" * 60)
        
        all_jobs = []
        
        # Search each platform
        all_jobs.extend(self.search_wellfound())
        time.sleep(1)  # Rate limiting
        
        all_jobs.extend(self.search_remoteok())
        time.sleep(1)
        
        all_jobs.extend(self.search_indeed())
        time.sleep(1)
        
        all_jobs.extend(self.search_linkedin())
        time.sleep(1)
        
        all_jobs.extend(self.search_startup_jobs())
        
        # Remove duplicates based on title + company
        unique_jobs = self._deduplicate_jobs(all_jobs)
        
        # Score and sort by match
        scored_jobs = self.score_jobs(unique_jobs)
        
        self.jobs = scored_jobs
        return scored_jobs
    
    def search_wellfound(self) -> List[JobListing]:
        """Search Wellfound (formerly AngelList) for startup jobs"""
        print("🔍 Searching Wellfound (startup jobs)...")
        jobs = []
        
        for role in self.profile.target_roles:
            # Wellfound search URL structure
            search_term = quote(role)
            url = f"https://wellfound.com/role/l/{search_term}"
            
            # For now, generate search URL (actual scraping would require their API)
            # Wellfound has an API but requires authentication
            job = JobListing(
                title=f"{role.title()} - Startup",
                company="Wellfound Search",
                location="Remote/Global",
                url=url,
                description=f"Search results for {role} on Wellfound - startup and tech jobs",
                platform="wellfound",
                required_skills=[role]
            )
            jobs.append(job)
        
        print(f"   ✓ Found {len(jobs)} Wellfound search links")
        return jobs
    
    def search_remoteok(self) -> List[JobListing]:
        """Search RemoteOK for remote positions - ACTUAL SCRAPING"""
        print("🔍 Searching RemoteOK...")
        
        if not BS4_AVAILABLE:
            return self._search_remoteok_fallback()
        
        jobs = []
        
        for role in self.profile.target_roles:
            try:
                # RemoteOK API endpoint (they have a JSON API)
                search_term = quote(role.lower())
                url = f"https://remoteok.com/api?tags={search_term}"
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                # RemoteOK returns JSON
                data = response.json()
                
                # Skip first item (it's metadata)
                if isinstance(data, list) and len(data) > 0:
                    job_listings = data[1:] if data[0].get('id') == '0' else data
                    
                    for job_data in job_listings[:15]:  # Limit to 15 per role
                        try:
                            if not job_data.get('id'):
                                continue
                            
                            title = job_data.get('position', role.title())
                            company = job_data.get('company', 'Unknown')
                            location = "Remote"
                            job_url = f"https://remoteok.com{job_data.get('url', '')}"
                            
                            # Get description
                            description = job_data.get('description', '')
                            if isinstance(description, str):
                                # Clean HTML from description
                                desc_soup = BeautifulSoup(description, 'html.parser')
                                description = desc_soup.get_text(strip=True)[:1000]
                            else:
                                description = str(description)[:1000]
                            
                            # Extract skills
                            required_skills = self._extract_skills_from_description(description + " " + title)
                            
                            job = JobListing(
                                title=title,
                                company=company,
                                location=location,
                                url=job_url,
                                description=description,
                                platform="remoteok",
                                required_skills=required_skills
                            )
                            jobs.append(job)
                        except Exception as e:
                            continue
                
                time.sleep(0.5)  # Rate limiting
                
            except requests.RequestException as e:
                print(f"   ⚠️  Error scraping RemoteOK for {role}: {e}")
                continue
            except Exception as e:
                print(f"   ⚠️  Unexpected error scraping RemoteOK: {e}")
                continue
        
        print(f"   ✓ Scraped {len(jobs)} actual jobs from RemoteOK")
        return jobs
    
    def _search_remoteok_fallback(self):
        """Fallback to URL generation"""
        jobs = []
        for role in self.profile.target_roles:
            search_term = quote(role)
            url = f"https://remoteok.com/remote-{search_term}-jobs"
            job = JobListing(
                title=f"Remote {role.title()}",
                company="RemoteOK Search",
                location="Remote",
                url=url,
                description=f"Remote {role} positions from RemoteOK",
                platform="remoteok",
                required_skills=[role]
            )
            jobs.append(job)
        return jobs
    
    def search_indeed(self) -> List[JobListing]:
        """Search Indeed for job listings - ACTUAL SCRAPING"""
        print("🔍 Searching Indeed...")
        
        if not BS4_AVAILABLE:
            return self._search_indeed_fallback()
        
        jobs = []
        
        for role in self.profile.target_roles:
            location = self.profile.locations[0] if self.profile.locations else "United States"
            
            # Build search URL
            params = {
                'q': role,
                'l': location,
                'fromage': '7',  # Last 7 days
                'sort': 'date'
            }
            
            if self.profile.remote_preference:
                params['remote'] = 'true'
            
            url = f"https://www.indeed.com/jobs?{urlencode(params)}"
            
            try:
                # Add headers to appear more like a browser
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Referer': 'https://www.indeed.com/'
                }
                
                # Use session to maintain cookies
                session = requests.Session()
                session.headers.update(headers)
                
                response = session.get(url, timeout=10)
                
                # If we get blocked, fall back to URL generation
                if response.status_code == 403 or response.status_code == 429:
                    print(f"   ⚠️  Indeed blocked automated requests (common). Using search URLs instead.")
                    return self._search_indeed_fallback()
                
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Find job cards - Indeed uses different selectors
                job_cards = soup.find_all('div', class_='job_seen_beacon') or \
                           soup.find_all('div', {'data-jk': True})
                
                if not job_cards:
                    # Try alternative selectors
                    job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard') or \
                               soup.find_all('a', {'data-jk': True})
                
                for card in job_cards[:20]:  # Limit to 20 jobs per role
                    try:
                        # Extract title
                        title_elem = card.find('h2', class_='jobTitle') or \
                                   card.find('a', class_='jcs-JobTitle')
                        if not title_elem:
                            title_elem = card.find('h2') or card.find('a')
                        
                        if not title_elem:
                            continue
                        
                        title = title_elem.get_text(strip=True)
                        
                        # Extract company
                        company_elem = card.find('span', class_='companyName') or \
                                     card.find('span', {'data-testid': 'company-name'})
                        if not company_elem:
                            company_elem = card.find('span', class_='company')
                        company = company_elem.get_text(strip=True) if company_elem else "Unknown"
                        
                        # Extract link
                        link_elem = title_elem.find('a') if title_elem.name != 'a' else title_elem
                        if link_elem and link_elem.get('href'):
                            link = link_elem['href']
                            if link.startswith('/'):
                                link = 'https://www.indeed.com' + link
                        else:
                            continue
                        
                        # Extract location
                        location_elem = card.find('div', class_='companyLocation') or \
                                      card.find('div', {'data-testid': 'job-location'})
                        job_location = location_elem.get_text(strip=True) if location_elem else location
                        
                        # Extract date
                        date_elem = card.find('span', class_='date') or \
                                  card.find('span', {'data-testid': 'myJobsStateDate'})
                        posted_date = date_elem.get_text(strip=True) if date_elem else None
                        
                        # Extract snippet/description
                        snippet_elem = card.find('div', class_='job-snippet') or \
                                      card.find('div', class_='summary')
                        description = snippet_elem.get_text(strip=True) if snippet_elem else ""
                        
                        # Try to get full description by visiting the link
                        try:
                            job_session = requests.Session()
                            job_session.headers.update(headers)
                            job_page = job_session.get(link, timeout=5)
                            job_soup = BeautifulSoup(job_page.content, 'html.parser')
                            job_session.close()
                            desc_div = job_soup.find('div', id='jobDescriptionText') or \
                                      job_soup.find('div', class_='jobsearch-jobDescriptionText')
                            if desc_div:
                                description = desc_div.get_text(strip=True)
                        except:
                            pass  # Use snippet if full description fails
                        
                        # Extract skills from description
                        required_skills = self._extract_skills_from_description(description + " " + title)
                        
                        job = JobListing(
                            title=title,
                            company=company,
                            location=job_location,
                            url=link,
                            description=description[:1000],  # Limit description length
                            platform="indeed",
                            posted_date=posted_date,
                            required_skills=required_skills
                        )
                        jobs.append(job)
                        
                    except Exception as e:
                        # Skip jobs that fail to parse
                        continue
                
                # Rate limiting
                time.sleep(1)
                
                # Close session after scraping
                session.close()
                
            except requests.RequestException as e:
                if '403' in str(e) or 'Forbidden' in str(e):
                    print(f"   ⚠️  Indeed blocked scraping for {role}. Using search URL instead.")
                    # Add fallback job
                    fallback_job = JobListing(
                        title=f"{role.title()} - Indeed",
                        company="Indeed",
                        location=location,
                        url=url,
                        description=f"Search results for {role} positions. Indeed blocks automated scraping - visit the URL to see actual listings.",
                        platform="indeed",
                        required_skills=[role]
                    )
                    jobs.append(fallback_job)
                else:
                    print(f"   ⚠️  Error scraping Indeed for {role}: {e}")
                continue
            except Exception as e:
                print(f"   ⚠️  Unexpected error scraping Indeed: {e}")
                continue
        
        print(f"   ✓ Scraped {len(jobs)} actual jobs from Indeed")
        return jobs
    
    def _search_indeed_fallback(self):
        """Fallback to URL generation if BeautifulSoup not available"""
        jobs = []
        for role in self.profile.target_roles:
            location = self.profile.locations[0] if self.profile.locations else "US"
            params = {'q': role, 'l': location}
            if self.profile.remote_preference:
                params['remote'] = 'true'
            url = f"https://www.indeed.com/jobs?{urlencode(params)}"
            
            job = JobListing(
                title=f"{role.title()} - Indeed",
                company="Indeed Search",
                location=location,
                url=url,
                description=f"{role} positions from Indeed",
                platform="indeed",
                required_skills=[role]
            )
            jobs.append(job)
        return jobs
    
    def search_linkedin(self) -> List[JobListing]:
        """Search LinkedIn Jobs"""
        print("🔍 Searching LinkedIn...")
        jobs = []
        
        for role in self.profile.target_roles:
            location = self.profile.locations[0] if self.profile.locations else "United%20States"
            keywords = quote(role)
            remote = "&remote=true" if self.profile.remote_preference else ""
            
            url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}{remote}"
            
            job = JobListing(
                title=f"{role.title()} - LinkedIn",
                company="LinkedIn Search",
                location=location.replace("%20", " "),
                url=url,
                description=f"{role} positions from LinkedIn",
                platform="linkedin",
                required_skills=[role]
            )
            jobs.append(job)
        
        print(f"   ✓ Found {len(jobs)} LinkedIn search links")
        return jobs
    
    def search_startup_jobs(self) -> List[JobListing]:
        """Search startup-specific job boards"""
        print("🔍 Searching startup job boards...")
        jobs = []
        
        startup_boards = {
            "Y Combinator": "https://www.ycombinator.com/jobs",
            "Techstars": "https://jobs.techstars.com/",
            "Work at a Startup": "https://www.workatastartup.com/"
        }
        
        for company, url in startup_boards.items():
            for role in self.profile.target_roles:
                job = JobListing(
                    title=f"{role.title()} - {company}",
                    company=company,
                    location="Remote/Global",
                    url=url,
                    description=f"{role} positions at {company}",
                    platform="startup_board",
                    required_skills=[role]
                )
                jobs.append(job)
        
        print(f"   ✓ Found {len(jobs)} startup board links")
        return jobs
    
    def _deduplicate_jobs(self, jobs: List[JobListing]) -> List[JobListing]:
        """Remove duplicate jobs based on title + company"""
        seen = set()
        unique = []
        
        for job in jobs:
            key = (job.title.lower(), job.company.lower())
            if key not in seen:
                seen.add(key)
                unique.append(job)
        
        return unique
    
    def score_jobs(self, jobs: List[JobListing]) -> List[JobListing]:
        """Score jobs based on profile match"""
        print("\n📊 Scoring jobs against your profile...")
        
        for job in jobs:
            score = self._calculate_match_score(job)
            job.match_score = score
        
        # Sort by match score (highest first)
        sorted_jobs = sorted(jobs, key=lambda x: x.match_score, reverse=True)
        
        print(f"   ✓ Scored {len(sorted_jobs)} jobs")
        return sorted_jobs
    
    def _calculate_match_score(self, job: JobListing) -> float:
        """Calculate how well a job matches the user profile - NOW WITH REAL DESCRIPTIONS!"""
        score = 0.0
        
        # Combine title and description for better matching
        full_text = (job.title + " " + job.description).lower()
        job_title_lower = job.title.lower()
        job_desc_lower = job.description.lower()
        
        # Title match (35 points) - more weight on exact matches
        for role in self.profile.target_roles:
            role_lower = role.lower()
            if role_lower in job_title_lower:
                # Exact match gets full points
                if role_lower == job_title_lower or job_title_lower.startswith(role_lower):
                    score += 35
                else:
                    # Partial match gets less
                    score += 25
                break
        
        # Skills match (35 points) - NOW USING REAL DESCRIPTIONS!
        matched_skills = 0
        skill_matches = []
        
        # Check for user's skills in description
        for skill in self.profile.skills:
            skill_lower = skill.lower()
            # Check if skill appears in title or description
            if skill_lower in full_text:
                matched_skills += 1
                skill_matches.append(skill)
        
        # Also check required_skills from job
        if job.required_skills:
            for req_skill in job.required_skills:
                if any(user_skill.lower() in req_skill.lower() or 
                       req_skill.lower() in user_skill.lower() 
                       for user_skill in self.profile.skills):
                    if req_skill not in skill_matches:
                        matched_skills += 1
                        skill_matches.append(req_skill)
        
        # Calculate skill match ratio
        if len(self.profile.skills) > 0:
            skill_match_ratio = min(matched_skills / len(self.profile.skills), 1.0)
            score += 35 * skill_match_ratio
        
        # Location match (20 points)
        job_location_lower = job.location.lower()
        if "remote" in job_location_lower and self.profile.remote_preference:
            score += 20
        elif "remote" in job_desc_lower and self.profile.remote_preference:
            score += 15  # Remote mentioned in description
        else:
            for location in self.profile.locations:
                loc_lower = location.lower()
                if loc_lower in job_location_lower:
                    score += 20
                    break
                elif loc_lower in job_desc_lower:
                    score += 10  # Location mentioned in description
                    break
        
        # Experience level match (10 points) - NOW CHECKING DESCRIPTIONS
        exp_keywords = {
            "junior": ["junior", "entry", "entry level", "graduate", "new grad"],
            "mid": ["mid", "intermediate", "experienced", "3+ years", "2+ years"],
            "senior": ["senior", "lead", "principal", "architect", "5+ years", "7+ years"]
        }
        
        user_exp = self.profile.experience_level.lower()
        if user_exp in exp_keywords:
            for keyword in exp_keywords[user_exp]:
                if keyword in full_text:
                    score += 10
                    break
        
        # Platform bonus (startups favored for junior roles)
        if self.profile.experience_level == "junior":
            if job.platform in ["wellfound", "startup_board"]:
                score += 5
        
        return min(score, 100.0)  # Cap at 100
    
    def _extract_skills_from_description(self, description: str) -> List[str]:
        """Extract skills mentioned in job description"""
        if not description:
            return []
        
        description_lower = description.lower()
        found_skills = []
        
        # Common tech skills to look for
        skill_keywords = [
            'python', 'javascript', 'typescript', 'java', 'c++', 'c#', 'go', 'rust',
            'pytorch', 'tensorflow', 'keras', 'scikit-learn', 'pandas', 'numpy',
            'llm', 'gpt', 'openai', 'transformer', 'nlp', 'natural language processing',
            'machine learning', 'deep learning', 'neural network', 'ml', 'ai',
            'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'cloud',
            'api', 'rest', 'graphql', 'sql', 'nosql', 'mongodb', 'postgresql',
            'git', 'github', 'ci/cd', 'jenkins', 'terraform', 'ansible',
            'prompt engineering', 'fine-tuning', 'rag', 'embeddings'
        ]
        
        for skill in skill_keywords:
            if skill.lower() in description_lower:
                found_skills.append(skill)
        
        # Also check if user's skills are mentioned
        for skill in self.profile.skills:
            if skill.lower() in description_lower and skill not in found_skills:
                found_skills.append(skill)
        
        return list(set(found_skills))[:10]  # Return top 10 unique skills
    
    def generate_report(self) -> str:
        """Generate a detailed job search report"""
        report = f"""
🧠 NEURO ADVANCED JOB SEARCH REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'=' * 60}

📊 SUMMARY:
   Total jobs found: {len(self.jobs)}
   High matches (>70%): {len([j for j in self.jobs if j.match_score >= 70])}
   Medium matches (50-69%): {len([j for j in self.jobs if 50 <= j.match_score < 70])}
   Low matches (<50%): {len([j for j in self.jobs if j.match_score < 50])}

🎯 YOUR PROFILE:
   Target Roles: {', '.join(self.profile.target_roles)}
   Skills: {', '.join(self.profile.skills)}
   Experience: {self.profile.experience_level}
   Locations: {', '.join(self.profile.locations)}
   Remote: {'Yes' if self.profile.remote_preference else 'No'}

🏆 TOP MATCHES (Score >= 70%):
"""
        
        top_jobs = [j for j in self.jobs if j.match_score >= 70][:10]
        if top_jobs:
            for i, job in enumerate(top_jobs, 1):
                report += f"""
   {i}. {job.title} at {job.company}
      Match Score: {job.match_score:.1f}%
      Platform: {job.platform}
      Location: {job.location}
      URL: {job.url}
"""
        else:
            report += "   No high-matching jobs found this week.\n"
        
        report += f"""
📋 ALL JOBS BY PLATFORM:
"""
        
        # Group by platform
        by_platform = {}
        for job in self.jobs:
            if job.platform not in by_platform:
                by_platform[job.platform] = []
            by_platform[job.platform].append(job)
        
        for platform, jobs in by_platform.items():
            report += f"\n   {platform.upper()}: {len(jobs)} jobs"
            for job in jobs[:5]:  # Show top 5 per platform
                report += f"\n      • {job.title} ({job.match_score:.1f}%)"
        
        report += f"""

🚀 RECOMMENDED ACTIONS:
   1. Review top matches and prioritize applications
   2. Tailor your resume for each high-match position
   3. Set up job alerts on these platforms
   4. Apply to at least 5 positions this week
   5. Track applications in your spreadsheet

💡 NEXT STEPS:
   - Run: python prepare_resume.py --job-url <URL>
   - Schedule weekly search: python schedule_job_search.py
"""
        
        return report
    
    def save_results(self, output_dir: str = "job_search_results"):
        """Save search results to JSON file"""
        Path(output_dir).mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(output_dir, f"job_search_{timestamp}.json")
        
        results = {
            "search_date": datetime.now().isoformat(),
            "profile": asdict(self.profile),
            "jobs": [asdict(job) for job in self.jobs],
            "summary": {
                "total_jobs": len(self.jobs),
                "high_matches": len([j for j in self.jobs if j.match_score >= 70]),
                "medium_matches": len([j for j in self.jobs if 50 <= j.match_score < 70]),
                "low_matches": len([j for j in self.jobs if j.match_score < 50])
            }
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Results saved to: {filename}")
        return filename

