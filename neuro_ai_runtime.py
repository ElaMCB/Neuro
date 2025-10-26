#!/usr/bin/env python3
"""
Neuro AI Runtime - Main executable for AI-powered Neuro
"""

import os
import sys
import json
import re
from typing import Dict, List, Any

# Import our AI engine
try:
    from src.neuro.ai_engine import NeuroAIEngine
except ImportError:
    # Fallback if not installed as package
    sys.path.append('./src')
    from neuro.ai_engine import NeuroAIEngine

class NeuroRuntime:
    """Neuro execution runtime with AI understanding"""
    
    def __init__(self):
        self.ai = NeuroAIEngine()
        self.execution_history = []
    
    def execute_file(self, filename: str) -> str:
        """Execute a .neuro file with AI understanding"""
        if not os.path.exists(filename):
            return f"Error: {filename} not found"
        
        print(f"🧠 Reading Neuro file: {filename}")
        with open(filename, 'r') as f:
            neuro_code = f.read()
        
        print("🔍 Analyzing intent with AI...")
        # Use AI to understand intent
        understanding = self.ai.understand_neuro_intent(neuro_code)
        
        # Store execution history
        self.execution_history.append({
            'file': filename,
            'understanding': understanding,
            'timestamp': self.get_timestamp()
        })
        
        # Generate execution plan
        return self.generate_execution_plan(understanding, neuro_code)
    
    def execute_code(self, neuro_code: str) -> str:
        """Execute Neuro code directly"""
        print("🔍 Analyzing Neuro code with AI...")
        understanding = self.ai.understand_neuro_intent(neuro_code)
        
        return self.generate_execution_plan(understanding, neuro_code)
    
    def generate_execution_plan(self, understanding: Dict[str, Any], original_code: str) -> str:
        """Generate human-executable plan from AI understanding"""
        
        plan = f"""
🧠 NEURO AI EXECUTION PLAN
{'='*60}

🎯 PRIMARY GOAL:
{understanding.get('goal', 'Goal not specified')}

🤖 AI ANALYSIS:
{understanding.get('analysis', 'No detailed analysis available')}

📋 EXECUTION STRATEGY:
{understanding.get('strategy', 'No specific strategy provided')}

🚀 REQUIRED ACTIONS:
"""
        
        actions = understanding.get('actions', [])
        if actions:
            for i, action in enumerate(actions, 1):
                plan += f"  {i}. {action}\n"
        else:
            plan += "  No specific actions identified\n"
        
        # Add context from original code
        plan += f"""
{'='*60}
📝 ORIGINAL NEURO CODE:
{original_code}

💡 NEURO AI INSIGHTS:
• This analysis was generated using free AI models
• The more you use Neuro, the better it understands your patterns
• Consider saving this execution plan for future reference

🎯 NEXT STEPS:
1. Review the AI-generated plan above
2. Execute the listed actions in sequence  
3. Document your results and learnings
4. Refine your Neuro code based on outcomes

📊 EXECUTION STATUS: Ready to begin
"""
        
        return plan
    
    def get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def show_history(self):
        """Show execution history"""
        if not self.execution_history:
            return "No executions recorded yet."
        
        history = "📊 NEURO EXECUTION HISTORY\n" + "="*40 + "\n"
        for i, execution in enumerate(self.execution_history, 1):
            history += f"\n{i}. {execution['file']} at {execution['timestamp']}\n"
            history += f"   Goal: {execution['understanding'].get('goal', 'N/A')}\n"
        
        return history

def interactive_mode():
    """Run Neuro in interactive mode"""
    runtime = NeuroRuntime()
    
    print("🧠 Neuro AI Runtime - Interactive Mode")
    print("Type 'quit' to exit, 'history' to see previous executions")
    print("=" * 50)
    
    while True:
        user_input = input("\nneuro> ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Thank you for using Neuro AI!")
            break
        elif user_input.lower() == 'history':
            print(runtime.show_history())
        elif user_input.lower() == 'help':
            print_help()
        elif user_input.endswith('.neuro'):
            # Execute Neuro file
            if os.path.exists(user_input):
                result = runtime.execute_file(user_input)
                print(result)
            else:
                print(f"❌ File not found: {user_input}")
        elif user_input:
            # Execute direct Neuro code
            result = runtime.execute_code(user_input)
            print(result)
        else:
            continue

def print_help():
    """Print help information"""
    help_text = """
NEURO AI RUNTIME - COMMANDS:

• <filename>.neuro    - Execute a Neuro file
• <neuro code>        - Execute Neuro code directly
• history            - Show execution history  
• help               - Show this help message
• quit               - Exit Neuro

EXAMPLES:
  apply_alphaxiv.neuro    - Execute a specific file
  "find ai engineer jobs" - Execute direct Neuro code

NEURO FILE FORMAT:
  Create .neuro files with your intent in natural language.
  Neuro AI will understand and generate execution plans.
"""
    print(help_text)

def main():
    """Main Neuro runtime entry point"""
    runtime = NeuroRuntime()
    
    print("🧠 Neuro AI Runtime v1.0")
    print("Free AI-Powered Intent Execution")
    print("=" * 50)
    
    # Check command line arguments
    if len(sys.argv) == 1:
        # No arguments - start interactive mode
        interactive_mode()
        return
    
    # Handle command line execution
    neuro_file = sys.argv[1]
    
    if neuro_file == "interactive":
        interactive_mode()
    elif neuro_file == "history":
        print(runtime.show_history())
    elif neuro_file == "help":
        print_help()
    else:
        # Execute specific file
        if os.path.exists(neuro_file):
            result = runtime.execute_file(neuro_file)
            print(result)
        else:
            print(f"❌ File not found: {neuro_file}")
            print(f"📁 Current directory: {os.getcwd()}")
            print(f"📋 Available .neuro files:")
            for file in os.listdir('.'):
                if file.endswith('.neuro'):
                    print(f"  - {file}")

if __name__ == "__main__":
    main()
