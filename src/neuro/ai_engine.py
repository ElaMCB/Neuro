#!/usr/bin/env python3
"""
Neuro AI Engine - Powered by Free Open-Source Models
"""

import os
import sys
import requests
import json
from typing import Dict, List, Any
import re

class NeuroAIEngine:
    """Neuro core powered by free AI models"""
    
    def __init__(self):
        self.loaded_models = {}
        self.free_apis = {
            "huggingface": "https://api-inference.huggingface.co/models",
            "deepseek": "https://api.deepseek.com/chat/completions"  # Free tier
        }
        self.setup_ai_models()
    
    def setup_ai_models(self):
        """Setup free AI models for Neuro"""
        try:
            # Try to use local models first
            self.setup_local_models()
        except Exception as e:
            print(f"Local models not available: {e}")
            self.use_api_fallback = True
    
    def setup_local_models(self):
        """Setup local free models"""
        try:
            from transformers import pipeline
            
            # Try to load a small free model
            print("Loading free AI models for Neuro...")
            
            # Text understanding model
            self.nlp = pipeline(
                "text-generation",
                model="microsoft/DialoGPT-small",  # Free, small model
                device=-1  # Use CPU
            )
            self.loaded_models['understanding'] = True
            print("✅ AI understanding model loaded")
            
        except ImportError:
            print("Transformers not installed. Using API fallback.")
            self.use_api_fallback = True
        except Exception as e:
            print(f"Model loading failed: {e}")
            self.use_api_fallback = True
    
    def understand_neuro_intent(self, neuro_code: str) -> Dict[str, Any]:
        """Use AI to understand Neuro intent"""
        if hasattr(self, 'use_api_fallback') and self.use_api_fallback:
            return self.free_api_understanding(neuro_code)
        
        try:
            # Use local model for understanding
            prompt = self.create_understanding_prompt(neuro_code)
            response = self.nlp(prompt, max_length=800, do_sample=True, temperature=0.7)
            
            analysis = response[0]['generated_text']
            return self.parse_ai_response(analysis)
            
        except Exception as e:
            print(f"AI understanding failed: {e}")
            return self.free_api_understanding(neuro_code)
    
    def free_api_understanding(self, neuro_code: str) -> Dict[str, Any]:
        """Use free APIs for understanding"""
        try:
            # Try Hugging Face free inference API
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {"Authorization": "Bearer hf_your_free_token_here"}
            
            payload = {
                "inputs": self.create_understanding_prompt(neuro_code),
                "parameters": {"max_length": 500}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload)
            if response.status_code == 200:
                result = response.json()
                return self.parse_ai_response(result[0]['generated_text'])
            else:
                return self.rule_based_understanding(neuro_code)
                
        except Exception as e:
            print(f"API failed: {e}")
            return self.rule_based_understanding(neuro_code)
    
   
    def create_understanding_prompt(self, neuro_code: str) -> str:
    """Create better prompt for AI understanding"""
    return f"""
Analyze this Neuro programming intent and provide ONLY the analysis:

NEURO CODE:
{neuro_code}

ANALYSIS REQUEST:
- Primary goal and objective
- Key components and elements  
- Execution strategy
- Required specific actions
- Expected outcomes

Provide concise, structured analysis without repeating the prompt.
"""
    def parse_ai_response(self, response: str) -> Dict[str, Any]:
        """Parse AI response into structured data"""
        try:
            # Try to extract JSON if present
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            
            # Otherwise structure the response
            return {
                "analysis": response,
                "goal": self.extract_goal(response),
                "actions": self.extract_actions(response),
                "strategy": self.extract_strategy(response)
            }
        except:
            return {"raw_analysis": response}
    
    def extract_goal(self, text: str) -> str:
        """Extract goal from AI response"""
        goal_patterns = [
            r'PRIMARY GOAL[:\s]*(.*?)(?=KEY COMPONENTS|EXECUTION|$)',
            r'goal[:\s]*(.*?)(?=action|strategy|$)',
            r'main objective[:\s]*(.*?)(?=component|action|$)'
        ]
        
        for pattern in goal_patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return "Goal extraction failed"
    
    def extract_actions(self, text: str) -> List[str]:
        """Extract actions from AI response"""
        action_patterns = [
            r'ACTIONS[:\s]*(.*?)(?=STRATEGY|OUTCOME|$)',
            r'steps[:\s]*(.*?)(?=strategy|outcome|$)',
            r'required actions[:\s]*(.*?)(?=expected|strategy|$)'
        ]
        
        for pattern in action_patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                actions_text = match.group(1)
                # Split by numbers or bullets
                actions = re.split(r'\d+\.|\-|\*', actions_text)
                return [action.strip() for action in actions if action.strip()]
        
        return ["Actions extraction failed"]
    
    def extract_strategy(self, text: str) -> str:
        """Extract strategy from AI response"""
        strategy_patterns = [
            r'STRATEGY[:\s]*(.*?)(?=ACTIONS|OUTCOME|$)',
            r'execution strategy[:\s]*(.*?)(?=actions|outcome|$)',
            r'approach[:\s]*(.*?)(?=steps|actions|$)'
        ]
        
        for pattern in strategy_patterns:
            match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1).strip()
        
        return "Strategy extraction failed"
    
    def rule_based_understanding(self, neuro_code: str) -> Dict[str, Any]:
        """Fallback rule-based understanding"""
        neuro_lower = neuro_code.lower()
        
        if 'apply' in neuro_lower and 'job' in neuro_lower:
            return {
                "goal": "Job application automation",
                "strategy": "Generate tailored application materials",
                "actions": [
                    "Analyze job requirements",
                    "Generate cover letter",
                    "Optimize resume",
                    "Prepare application package"
                ],
                "analysis": "Neuro detected job application intent"
            }
        elif 'find' in neuro_lower and 'job' in neuro_lower:
            return {
                "goal": "Job search automation", 
                "strategy": "Intelligent job matching and application",
                "actions": [
                    "Search relevant job boards",
                    "Match skills to positions",
                    "Generate applications",
                    "Track progress"
                ],
                "analysis": "Neuro detected job search intent"
            }
        else:
            return {
                "goal": "General intent execution",
                "strategy": "AI-powered goal achievement",
                "actions": ["Analyze intent", "Generate plan", "Execute actions"],
                "analysis": f"Neuro processing: {neuro_code[:100]}..."
            }

class NeuroRuntime:
    """Neuro execution runtime"""
    
    def __init__(self):
        self.ai = NeuroAIEngine()
    
    def execute_file(self, filename: str) -> str:
        """Execute a .neuro file"""
        if not os.path.exists(filename):
            return f"Error: {filename} not found"
        
        with open(filename, 'r') as f:
            neuro_code = f.read()
        
        # Use AI to understand intent
        understanding = self.ai.understand_neuro_intent(neuro_code)
        
        # Generate execution plan
        return self.generate_execution_plan(understanding, neuro_code)
    
    def generate_execution_plan(self, understanding: Dict[str, Any], original_code: str) -> str:
        """Generate human-executable plan"""
        
        plan = f"""
🧠 NEURO AI EXECUTION PLAN
{'='*50}

GOAL: {understanding.get('goal', 'Not specified')}

AI ANALYSIS:
{understanding.get('analysis', 'No analysis available')}

EXECUTION STRATEGY:
{understanding.get('strategy', 'No strategy specified')}

REQUIRED ACTIONS:
"""
        
        for i, action in enumerate(understanding.get('actions', []), 1):
            plan += f"{i}. {action}\n"
        
        plan += f"""
{'='*50}
ORIGINAL NEURO CODE:
{original_code}

NEXT STEPS:
1. Review the AI-generated plan above
2. Execute the listed actions manually
3. Neuro will learn from your execution patterns

💡 Tip: The more you use Neuro, the better it understands your intent!
"""
        
        return plan

def main():
    """Main Neuro runtime"""
    runtime = NeuroRuntime()
    
    print("🧠 Neuro AI Runtime v1.0")
    print("Free AI-Powered Intent Execution")
    print("=" * 50)
    
    # Check for command line argument
    if len(sys.argv) > 1:
        neuro_file = sys.argv[1]
    else:
        neuro_file = "apply_alphaxiv.neuro"
    
    if os.path.exists(neuro_file):
        print(f"Executing: {neuro_file}")
        print("Using AI to understand your intent...")
        print()
        
        result = runtime.execute_file(neuro_file)
        print(result)
        
    else:
        print(f"❌ {neuro_file} not found")
        print("Creating example Neuro file...")
        create_example_file()
        
        print("\n✅ Example file created: apply_alphaxiv.neuro")
        print("Run: python neuro_ai_engine.py")

def create_example_file():
    """Create example Neuro file"""
    example_content = """
APPLY TO AI ENGINEER AT ALPHAXIV

POSITION: AI Engineer - Research Tools & Recommendation Systems
COMPANY: alphaXiv
JOB_DESCRIPTION: Building tools that transform how researchers discover scientific papers

MY BACKGROUND:
- Created Neuro programming language
- 10 years QA/SDET experience
- Python development expertise
- AI system validation

STRATEGY:
- Position Neuro as solution to their challenges
- Connect QA experience to AI system reliability
- Demonstrate practical AI engineering skills

ACTIONS:
- Generate tailored cover letter
- Optimize resume for AI engineering
- Prepare Neuro project description
- Send complete application package
"""
    
    with open("apply_alphaxiv.neuro", "w") as f:
        f.write(example_content)

if __name__ == "__main__":
    main()
