#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Neuro Runner - Actually uses your .neuro files
Executes real job searches from Neuro syntax
"""

import re
import json
import os
import sys
from datetime import datetime

# Fix Windows encoding issues
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

class NeuroRunner:
    """Runs Neuro pipeline files and provides actionable job search help"""
    
    def run_pipeline(self, neuro_file):
        """Run a .neuro file and execute job search"""
        with open(neuro_file, 'r') as f:
            content = f.read()
        
        # Parse the Neuro file
        pipeline = self.parse_neuro(content)
        
        # Actually execute the advanced job search if available
        if self.has_advanced_search():
            print("🧠 EXECUTING NEURO JOB SEARCH PIPELINE")
            print("=" * 60)
            return self.execute_advanced_search(pipeline)
        else:
            # Fallback to plan generation
            return self.generate_plan(pipeline)
    
    def has_advanced_search(self):
        """Check if advanced job search system is available"""
        return os.path.exists("advanced_job_search.py") and os.path.exists("profile_config.json")
    
    def parse_neuro(self, content):
        """Simple parser for Neuro syntax"""
        pipeline = {
            'goal': '',
            'target_roles': [],
            'locations': [],
            'skills': [],
            'actions': []
        }
        
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            
            if line.startswith('goal:'):
                pipeline['goal'] = line.split('goal:')[1].strip().strip('"')
            elif line.startswith('target_roles:'):
                # Extract array: ["prompt engineer", "ai engineer"]
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    roles = [r.strip().strip('"') for r in match.group(1).split(',')]
                    pipeline['target_roles'] = roles
            elif line.startswith('locations:'):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    locations = [l.strip().strip('"') for l in match.group(1).split(',')]
                    pipeline['locations'] = locations
            elif line.startswith('skills:'):
                match = re.search(r'\[([^\]]+)\]', line)
                if match:
                    skills = [s.strip().strip('"') for s in match.group(1).split(',')]
                    pipeline['skills'] = skills
            elif line.startswith('actions:'):
                # Extract actions like search_job_boards()
                actions = re.findall(r'(\w+\(\))', line)
                pipeline['actions'] = actions
        
        return pipeline
    
    def generate_plan(self, pipeline):
        """Generate actionable job search plan from Neuro pipeline"""
        
        plan = f"""
🧠 NEURO JOB SEARCH ASSISTANT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
============================================

YOUR GOAL: {pipeline['goal']}

🎯 TARGET ROLES: {', '.join(pipeline['target_roles'])}

📍 LOCATIONS: {', '.join(pipeline['locations'])}

🛠️ KEY SKILLS: {', '.join(pipeline['skills'])}

📋 ACTION PLAN:
"""
        
        # Convert Neuro actions to real steps
        action_steps = {
            'search_job_boards': "1. 🔍 SEARCH JOB BOARDS:\n   - LinkedIn Jobs (filter: Remote, AI/ML)\n   - Indeed (keywords: 'prompt engineer', 'AI engineer')\n   - AngelList (remote-first startups)\n   - Company career pages (OpenAI, Anthropic, etc.)",
            
            'filter_remote_first': "2. 🏠 FILTER REMOTE-FIRST COMPANIES:\n   - GitLab, Zapier, Automatic, Doist, Buffer\n   - Check: https://remote-first.companies.dev\n   - Look for 'distributed team' in descriptions",
            
            'match_skills': "3. 🔗 MATCH YOUR SKILLS:\n   - Update LinkedIn with: {skills}\n   - Highlight projects with: LLMs, GPT, transformers\n   - Create portfolio with prompt engineering examples",
            
            'generate_applications': "4. 📝 GENERATE APPLICATIONS:\n   - Customize cover letters for each role\n   - Use Neuro to draft personalized applications\n   - Highlight remote work experience",
            
            'track_responses': "5. 📊 TRACK RESPONSES:\n   - Use spreadsheet: Company | Role | Applied | Response\n   - Follow up after 7 days\n   - Analyze which applications get responses"
        }
        
        for action in pipeline['actions']:
            action_name = action.replace('()', '')
            if action_name in action_steps:
                plan += f"\n{action_steps[action_name]}\n"
        
        plan += f"""
🎯 WEEKLY TARGETS:
   - Apply to 10 positions
   - Research 15 new companies
   - Send 5 LinkedIn connection requests
   - Practice 2 technical interviews

🚀 IMMEDIATE NEXT STEPS:
1. Install dependencies: pip install -r requirements_job_search.txt
2. Configure profile: edit profile_config.json
3. Run advanced search: python run_advanced_job_search.py
4. Set up weekly scheduler: python schedule_job_search.py --run-now

Ready to start? Install dependencies and run the advanced search!
"""
        
        return plan
    
    def execute_advanced_search(self, pipeline):
        """Execute the advanced job search system from Neuro pipeline"""
        try:
            # Import advanced job search components
            from advanced_job_search import JobSearchEngine, UserProfile
            from resume_preparer import ResumePreparer
            
            # Build UserProfile from pipeline + existing config
            profile = self.build_profile_from_pipeline(pipeline)
            
            # Create search engine
            search_engine = JobSearchEngine(profile)
            
            # Execute search
            print(f"\n📋 Parsed from {pipeline.get('goal', 'your Neuro file')}")
            print(f"   Target roles: {', '.join(pipeline['target_roles'])}")
            print(f"   Locations: {', '.join(pipeline['locations'])}")
            print(f"   Skills: {', '.join(pipeline['skills'])}\n")
            
            jobs = search_engine.search_all_platforms()
            
            # Generate report
            report = search_engine.generate_report()
            print(report)
            
            # Save results
            results_file = search_engine.save_results()
            
            # Check if user wants to prepare resumes
            top_matches = [j for j in jobs if j.match_score >= 70][:5]
            if top_matches and any('generate_applications' in str(a) for a in pipeline.get('actions', [])):
                print(f"\n📝 Preparing tailored resumes for {len(top_matches)} top matches...")
                resume_preparer = ResumePreparer(profile.resume_path)
                
                for job in top_matches:
                    try:
                        prepared = resume_preparer.prepare_for_job(
                            job_title=job.title,
                            company=job.company,
                            job_description=job.description,
                            job_url=job.url
                        )
                        print(f"   ✓ Application package ready for {job.company}")
                    except Exception as e:
                        print(f"   ⚠️  Error preparing resume for {job.company}: {e}")
            
            return f"\n✅ Neuro job search completed!\n   Results saved to: {results_file}"
            
        except ImportError as e:
            return f"""
⚠️  Advanced job search not fully available: {e}

Please install dependencies:
   pip install -r requirements_job_search.txt

Then run again.
"""
        except Exception as e:
            return f"""
❌ Error executing job search: {e}

Falling back to plan generation...
"""
    
    def build_profile_from_pipeline(self, pipeline):
        """Build UserProfile from pipeline and existing config"""
        # Load existing config if available
        if os.path.exists("profile_config.json"):
            with open("profile_config.json", 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            # Default config
            config = {
                "name": "Elena Mereanu",
                "email": "elena.mereanu@gmail.com",
                "resume_path": "",
                "github_url": "https://github.com/ElaMCB/Neuro",
                "linkedin_url": "linkedin.com/in/elenamereanu"
            }
        
        # Override with values from Neuro pipeline
        from advanced_job_search import UserProfile
        
        # Determine experience level from pipeline
        experience_level = "junior"
        if pipeline.get('experience', ''):
            exp_text = pipeline['experience'].lower()
            if 'senior' in exp_text:
                experience_level = "senior"
            elif 'mid' in exp_text or 'intermediate' in exp_text:
                experience_level = "mid"
        
        # Determine remote preference
        remote_pref = 'remote' in [loc.lower() for loc in pipeline.get('locations', [])] or \
                      pipeline.get('company_policy', '').lower() == 'remote first'
        
        return UserProfile(
            name=config.get('name', 'Elena Mereanu'),
            email=config.get('email', 'elena.mereanu@gmail.com'),
            target_roles=pipeline.get('target_roles', ['prompt engineer', 'ai engineer']),
            skills=pipeline.get('skills', ['python', 'pytorch', 'llm']),
            experience_level=experience_level,
            locations=pipeline.get('locations', ['remote', 'US']),
            remote_preference=remote_pref,
            resume_path=config.get('resume_path', ''),
            github_url=config.get('github_url', ''),
            linkedin_url=config.get('linkedin_url', '')
        )

def main():
    """Main function to run Neuro job search"""
    runner = NeuroRunner()
    
    print("🧠 Welcome to Neuro Job Search Assistant")
    print("Making AI development accessible through intent-driven programming")
    print()
    
    # Check if Neuro file exists
    neuro_file = "my_job_search.neuro"
    
    if os.path.exists(neuro_file):
        print(f"📁 Found your Neuro file: {neuro_file}")
        print("🔄 Processing your job search intent...")
        print()
        
        result = runner.run_pipeline(neuro_file)
        print(result)
        
    else:
        print(f"❌ No Neuro file found. Please create '{neuro_file}'")
        print("Example content:")
        print('''
pipeline FindAIPositions {
    goal: "Find AI engineering jobs"
    target_roles: ["ai engineer", "prompt engineer"]
    locations: ["remote", "US"]
    actions: [search_job_boards(), generate_applications()]
}''')

if __name__ == "__main__":
    main()
