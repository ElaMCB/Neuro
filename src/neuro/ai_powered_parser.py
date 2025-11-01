"""
AI-Powered Natural Language Parser for Neuro
Uses LLMs to understand intent from natural language
Supports: DeepSeek, OpenAI, and other providers
"""
import os
import json
import re
from typing import Dict, Any

# Optional: Use OpenAI-compatible API for AI-powered parsing
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

class AIPoweredParser:
    """Uses LLMs to parse natural language into Neuro intent"""
    
    def __init__(self):
        # Check for DeepSeek first, then OpenAI
        self.deepseek_key = os.getenv('DEEPSEEK_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        
        # Determine which provider to use
        if self.deepseek_key and OPENAI_AVAILABLE:
            self.provider = "deepseek"
            self.client = OpenAI(
                api_key=self.deepseek_key,
                base_url="https://api.deepseek.com"
            )
            self.model = "deepseek-chat"
            self.enabled = True
            print("✓ AI parsing enabled with DeepSeek")
        elif self.openai_key and OPENAI_AVAILABLE:
            self.provider = "openai"
            self.client = OpenAI(api_key=self.openai_key)
            self.model = "gpt-4"
            self.enabled = True
            print("✓ AI parsing enabled with OpenAI GPT-4")
        else:
            self.provider = None
            self.enabled = False
            if not OPENAI_AVAILABLE:
                print("⚠️  Install openai package: pip install openai")
            else:
                print("⚠️  AI parsing disabled. Set DEEPSEEK_API_KEY or OPENAI_API_KEY to enable.")
            print("   Falling back to pattern-based parsing.")
    
    def parse_goal(self, goal: str) -> Dict[str, Any]:
        """Parse natural language goal into structured intent"""
        
        if not self.enabled:
            return self._fallback_parse(goal)
        
        try:
            # Use LLM to understand intent (DeepSeek or GPT-4)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": """You are a parser for the Neuro programming language.
Extract structured intent from natural language goals.

Return JSON with:
- intent_type: (job_search, model_training, data_analysis, etc.)
- parameters: extracted parameters
- inferred: things user implied but didn't say explicitly

Be helpful - infer reasonable defaults."""
                    },
                    {
                        "role": "user",
                        "content": f"Parse this Neuro goal:\n\n{goal}"
                    }
                ],
                response_format={"type": "json_object"}
            )
            
            parsed = json.loads(response.choices[0].message.content)
            print(f"✓ AI-powered parsing successful ({self.provider})")
            return parsed
            
        except Exception as e:
            print(f"⚠️  AI parsing failed: {e}")
            print("   Falling back to pattern matching")
            return self._fallback_parse(goal)
    
    def _fallback_parse(self, goal: str) -> Dict[str, Any]:
        """Simple pattern-based parsing (no AI required)"""
        
        goal_lower = goal.lower()
        
        # Detect intent type
        if 'job' in goal_lower or 'position' in goal_lower:
            intent_type = 'job_search'
        elif 'train' in goal_lower or 'model' in goal_lower:
            intent_type = 'model_training'
        elif 'analyze' in goal_lower or 'data' in goal_lower:
            intent_type = 'data_analysis'
        else:
            intent_type = 'unknown'
        
        return {
            "intent_type": intent_type,
            "parameters": {},
            "inferred": {}
        }
    
    def clarify_ambiguous_intent(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        """Ask AI to generate clarification questions"""
        
        if not self.enabled:
            return intent
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "Generate clarification questions for ambiguous intents."
                    },
                    {
                        "role": "user",
                        "content": f"""
Intent: {intent}

What clarifications would help execute this better?
Generate 2-3 helpful questions.
Return as JSON: {{"questions": ["q1", "q2"]}}
"""
                    }
                ],
                response_format={"type": "json_object"}
            )
            
            clarifications = json.loads(response.choices[0].message.content)
            intent['clarifications'] = clarifications.get('questions', [])
            return intent
            
        except Exception as e:
            print(f"⚠️  Clarification generation failed: {e}")
            return intent

# Example usage
if __name__ == "__main__":
    parser = AIPoweredParser()
    
    # Test natural language parsing
    goals = [
        "Find me a remote AI job at a startup",
        "Train a sentiment classifier on my reviews data",
        "yo find some ml gigs asap"
    ]
    
    for goal in goals:
        print(f"\nGoal: {goal}")
        result = parser.parse_goal(goal)
        print(f"Parsed: {json.dumps(result, indent=2)}")

