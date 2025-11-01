"""
Neuro Interpreter - Executes .neuro files directly
No compilation step needed!
"""
import os
import sys
from pathlib import Path

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv not required

from .parser import NeuroIntentParser

class NeuroInterpreter:
    """Interprets and executes Neuro code directly"""
    
    def __init__(self):
        self.parser = NeuroIntentParser()
        self.context = {}
        
    def run(self, neuro_file: str):
        """Read, parse, and execute a .neuro file"""
        print(f"Neuro Interpreter v0.1")
        print(f"Executing: {neuro_file}\n")
        
        # Read file
        with open(neuro_file, 'r') as f:
            code = f.read()
        
        # Parse intent
        intent = self.parse_neuro_code(code)
        
        # Execute based on intent type
        self.execute(intent)
    
    def parse_neuro_code(self, code: str):
        """Parse Neuro code into executable intent"""
        # Simple parser for now
        intent = {
            'type': 'unknown',
            'goal': '',
            'parameters': {}
        }
        
        # Extract pipeline name and goal
        import re
        
        # Find pipeline declaration
        pipeline_match = re.search(r'pipeline\s+(\w+)\s*{', code)
        if pipeline_match:
            intent['pipeline_name'] = pipeline_match.group(1)
        
        # Find goal
        goal_match = re.search(r'goal:\s*"([^"]+)"', code)
        if goal_match:
            intent['goal'] = goal_match.group(1)
            
            # Determine intent type from goal
            goal_lower = intent['goal'].lower()
            if 'job' in goal_lower or 'position' in goal_lower:
                intent['type'] = 'job_search'
            elif 'train' in goal_lower or 'model' in goal_lower:
                intent['type'] = 'model_training'
            elif 'analyze' in goal_lower or 'data' in goal_lower:
                intent['type'] = 'data_analysis'
        
        # Extract target_roles
        roles_match = re.search(r'target_roles:\s*\[([^\]]+)\]', code)
        if roles_match:
            roles_str = roles_match.group(1)
            roles = [r.strip().strip('"\'') for r in roles_str.split(',')]
            intent['parameters']['target_roles'] = roles
        
        # Extract locations
        locations_match = re.search(r'locations:\s*\[([^\]]+)\]', code)
        if locations_match:
            locs_str = locations_match.group(1)
            locations = [l.strip().strip('"\'') for l in locs_str.split(',')]
            intent['parameters']['locations'] = locations
        
        # Extract skills
        skills_match = re.search(r'skills:\s*\[([^\]]+)\]', code)
        if skills_match:
            skills_str = skills_match.group(1)
            skills = [s.strip().strip('"\'') for s in skills_str.split(',')]
            intent['parameters']['skills'] = skills
        
        return intent
    
    def execute(self, intent):
        """Execute the parsed intent"""
        print(f"Intent: {intent['type']}")
        print(f"Goal: {intent['goal']}\n")
        
        if intent['type'] == 'job_search':
            self.execute_job_search(intent)
        elif intent['type'] == 'model_training':
            self.execute_model_training(intent)
        elif intent['type'] == 'data_analysis':
            self.execute_data_analysis(intent)
        else:
            print(f"WARNING: Unknown intent type: {intent['type']}")
            print("Supported: job_search, model_training, data_analysis")
    
    def execute_job_search(self, intent):
        """Execute job search intent"""
        print("Executing job search...")
        
        # Import the job search module
        try:
            # Try improved search first
            if os.path.exists('improved_job_search.py'):
                print("   Using improved AI job search engine\n")
                import subprocess
                result = subprocess.run(['python', 'improved_job_search.py'], 
                                      capture_output=True, text=True)
                print(result.stdout)
                
                # Generate HTML report
                if os.path.exists('improved_results.json'):
                    print("\nGenerating report...")
                    result = subprocess.run(['python', 'convert_my_results.py', 
                                           'improved_results.json'],
                                          capture_output=True, text=True)
                    print(result.stdout)
            else:
                print("   Job search module not found")
                print("   Install: pip install -r requirements_job_search.txt")
        except Exception as e:
            print(f"   Error: {e}")
    
    def execute_model_training(self, intent):
        """Execute model training intent"""
        print("Model training not yet implemented")
        print("   This will train ML models based on your specification")
    
    def execute_data_analysis(self, intent):
        """Execute data analysis intent"""
        print("Data analysis not yet implemented")
        print("   This will analyze datasets based on your goals")

# For backwards compatibility
def run_neuro_file(filename: str):
    """Legacy function for running neuro files"""
    interpreter = NeuroInterpreter()
    interpreter.run(filename)

