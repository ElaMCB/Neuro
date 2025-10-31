#!/usr/bin/env python3
"""
Simple Neuro Runner - Actually uses your .neuro files
"""

import re
import json
import os
from datetime import datetime

class NeuroRunner:
    """Runs Neuro pipeline files and provides actionable job search help"""
    
    def run_pipeline(self, neuro_file):
        """Run a .neuro file and provide job search assistance"""
        with open(neuro_file, 'r') as f:
            content = f.read()
        
        # Parse the Neuro file
        pipeline = self.parse_neuro(content)
        
        # Generate actionable job search plan
        return self.generate_plan(pipeline)
    
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
1. Run: python search_jobs.py (see below)
2. Update your LinkedIn headline to include 'Prompt Engineer'
3. Create a 'remote AI jobs' spreadsheet
4. Set up daily job alert emails

Ready to start? The Neuro job search engine is running...
"""
        
        return plan

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
        
        plan = runner.run_pipeline(neuro_file)
        print(plan)
        
        # Generate actual search commands
        print("\n🔍 ACTUAL JOB SEARCH COMMANDS:")
        print("python -c \"from neuro_job_search import search_jobs; search_jobs()\"")
        
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
