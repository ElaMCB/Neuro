"""
Weekly Job Search Scheduler
Automatically runs job searches on a schedule
"""

import os
import json
import schedule
import time
from datetime import datetime
from pathlib import Path
from advanced_job_search import JobSearchEngine, UserProfile
from resume_preparer import ResumePreparer

class WeeklyJobSearchScheduler:
    """Manages weekly automated job searches"""
    
    def __init__(self, profile_config_path: str = "profile_config.json"):
        self.profile_config_path = profile_config_path
        self.profile = self._load_profile()
        self.search_engine = JobSearchEngine(self.profile)
        self.resume_preparer = ResumePreparer()
        
    def _load_profile(self) -> UserProfile:
        """Load user profile from config file"""
        if os.path.exists(self.profile_config_path):
            with open(self.profile_config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return UserProfile(**config)
        else:
            # Create default profile (user should customize)
            return self._create_default_profile()
    
    def _create_default_profile(self) -> UserProfile:
        """Create a default profile - user should customize"""
        print("📝 Creating default profile configuration...")
        print("   Please edit 'profile_config.json' to customize your profile.")
        
        profile = UserProfile(
            name="Elena Mereanu",
            email="elena.mereanu@gmail.com",
            target_roles=["prompt engineer", "ai engineer", "ml engineer"],
            skills=["python", "pytorch", "llm", "gpt", "transformers", "nlp"],
            experience_level="junior",
            locations=["remote", "US", "Boston", "New York"],
            remote_preference=True,
            resume_path="examples/resume/outputs/resume_prompt_engineer_short.txt",
            github_url="https://github.com/ElaMCB/Neuro",
            linkedin_url="linkedin.com/in/elenamereanu"
        )
        
        # Save default config
        self._save_profile(profile)
        
        return profile
    
    def _save_profile(self, profile: UserProfile):
        """Save profile to config file"""
        config = {
            "name": profile.name,
            "email": profile.email,
            "target_roles": profile.target_roles,
            "skills": profile.skills,
            "experience_level": profile.experience_level,
            "locations": profile.locations,
            "remote_preference": profile.remote_preference,
            "resume_path": profile.resume_path,
            "github_url": profile.github_url,
            "linkedin_url": profile.linkedin_url
        }
        
        with open(self.profile_config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
    
    def run_weekly_search(self):
        """Execute weekly job search"""
        print("\n" + "=" * 60)
        print(f"🔄 WEEKLY JOB SEARCH - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        # Search all platforms
        jobs = self.search_engine.search_all_platforms()
        
        # Generate report
        report = self.search_engine.generate_report()
        print(report)
        
        # Save results
        results_file = self.search_engine.save_results()
        
        # Prepare resumes for top matches
        self._prepare_top_resumes(jobs)
        
        # Send notification (could be email, file, etc.)
        self._send_notification(report, results_file)
        
        print("\n✅ Weekly job search completed!")
        return jobs
    
    def _prepare_top_resumes(self, jobs):
        """Prepare tailored resumes for top matching jobs"""
        top_jobs = [j for j in jobs if j.match_score >= 70][:5]
        
        if not top_jobs:
            print("\n⚠️  No high-matching jobs found to prepare resumes for.")
            return
        
        print(f"\n📝 Preparing tailored resumes for {len(top_jobs)} top matches...")
        
        for job in top_jobs:
            try:
                prepared = self.resume_preparer.prepare_for_job(
                    job_title=job.title,
                    company=job.company,
                    job_description=job.description,
                    job_url=job.url
                )
                print(f"   ✓ Prepared application package for {job.company}")
            except Exception as e:
                print(f"   ⚠️  Error preparing resume for {job.company}: {e}")
    
    def _send_notification(self, report: str, results_file: str):
        """Send notification about search results"""
        # Save report to file
        reports_dir = "job_search_reports"
        Path(reports_dir).mkdir(exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(reports_dir, f"weekly_report_{timestamp}.txt")
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
            f.write(f"\n\nFull results JSON: {results_file}\n")
        
        print(f"\n📧 Report saved to: {report_file}")
        print("   (Configure email notifications in the future)")
    
    def start_scheduler(self, day_of_week: str = "monday", time_str: str = "09:00"):
        """Start the scheduler for weekly job searches"""
        print(f"\n📅 Scheduling weekly job searches...")
        print(f"   Day: {day_of_week.title()}")
        print(f"   Time: {time_str}")
        print("\n   To run immediately: python schedule_job_search.py --run-now")
        print("   Press Ctrl+C to stop the scheduler\n")
        
        # Schedule weekly job search
        getattr(schedule.every(), day_of_week.lower()).at(time_str).do(self.run_weekly_search)
        
        # Run scheduler loop
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Weekly Job Search Scheduler')
    parser.add_argument('--run-now', action='store_true', 
                       help='Run job search immediately instead of scheduling')
    parser.add_argument('--day', default='monday',
                       help='Day of week to run (default: monday)')
    parser.add_argument('--time', default='09:00',
                       help='Time to run (default: 09:00)')
    
    args = parser.parse_args()
    
    scheduler = WeeklyJobSearchScheduler()
    
    if args.run_now:
        print("🚀 Running job search immediately...\n")
        scheduler.run_weekly_search()
    else:
        print("📅 Starting weekly scheduler...")
        print(f"   Next search: Every {args.day} at {args.time}")
        try:
            scheduler.start_scheduler(day_of_week=args.day, time_str=args.time)
        except KeyboardInterrupt:
            print("\n\n👋 Scheduler stopped.")

if __name__ == "__main__":
    main()

