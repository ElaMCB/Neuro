#!/usr/bin/env python3
"""
Neuro AI Runtime - Main executable for AI-powered Neuro
"""

import os
import sys
import json
import re
from typing import Dict, List, Any

# FIX: Add current directory to Python path first
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
sys.path.insert(0, os.path.join(current_dir, 'src'))

# Import our AI engine
try:
    from neuro.ai_engine import NeuroAIEngine
    print("✅ Using local Neuro AI engine")
except ImportError as e:
    print(f"❌ Error importing Neuro AI engine: {e}")
    sys.exit(1)

# Import Neuro executor for real-world actions
try:
    from neuro_executor import NeuroExecutor
    NEURO_EXECUTOR_AVAILABLE = True
    print("✅ Neuro Executor loaded - REAL execution enabled")
except ImportError as e:
    NEURO_EXECUTOR_AVAILABLE = False
    print(f"⚠️  Neuro executor not available: {e}")

class NeuroRuntime:
    """Neuro execution runtime with AI understanding and REAL execution"""
    
    def __init__(self):
        self.ai = NeuroAIEngine()
        self.execution_history = []
    
    def execute_file(self, filename: str) -> str:
        """Execute a .neuro file with AI understanding and REAL execution"""
        if not os.path.exists(filename):
            return f"Error: {filename} not found"
        
        print(f"🧠 Reading Neuro file: {filename}")
        with open(filename, 'r') as f:
            neuro_code = f.read()
        
        print("🔍 Analyzing intent with AI...")
        # Use AI to understand intent
        understanding = self.ai.understand_neuro_intent(neuro_code)
        
        # Execute real actions based on intent
        execution_result = self.execute_real_actions(neuro_code, understanding)
        
        # Store execution history
        self.execution_history.append({
            'file': filename,
            'code': neuro_code,
            'understanding': understanding,
            'execution_result': execution_result
        })
        
        return execution_result

    def execute_real_actions(self, neuro_code: str, ai_understanding: str) -> str:
        """Execute real-world actions based on Neuro code intent"""
        if not NEURO_EXECUTOR_AVAILABLE:
            return self.format_analysis_only(ai_understanding, neuro_code)
        
        executor = NeuroExecutor()
        neuro_upper = neuro_code.upper()
        
        # Detect job application intent
        if any(keyword in neuro_upper for keyword in ['COMPANY:', 'POSITION:', 'APPLY', 'JOB', 'HIRING']):
            print("🎯 DETECTED JOB APPLICATION INTENT")
            print("🚀 EXECUTING REAL APPLICATION PLAN...")
            print("=" * 60)
            
            # This actually generates real files!
            executor.execute_application_plan(ai_understanding, neuro_code)
            
            print("=" * 60)
            return self.format_execution_complete(ai_understanding)
        
        # For other intents, return AI analysis only for now
        return self.format_analysis_only(ai_understanding, neuro_code)

    def format_analysis_only(self, understanding: str, neuro_code: str) -> str:
        """Format output when only AI analysis is available"""
        return f"""
🧠 NEURO AI ANALYSIS COMPLETE
============================================================

📝 ORIGINAL NEURO CODE:
{neuro_code}

💡 AI UNDERSTANDING:
{understanding}

🎯 NEXT STEPS:
1. Review the AI-generated understanding above
2. Consider adding specific intent markers like:
   - COMPANY: [Company Name]
   - POSITION: [Job Title]
   - GOAL: [Your objective]

📊 EXECUTION STATUS: Analysis Complete - Add specific intent for real execution
"""

    def format_execution_complete(self, understanding: str) -> str:
        """Format output when real execution completed"""
        return f"""
🧠 NEURO EXECUTION COMPLETE!
============================================================

💡 AI UNDERSTANDING:
{understanding}

✅ REAL FILES GENERATED:
• cover_letter_[company].txt - Professional cover letter
• resume_optimization_guide.txt - AI engineering resume strategy  
• neuro_project_description.txt - Project documentation

🎯 YOUR APPLICATION PACKAGE IS READY!
Next steps are outlined in the generated files.

📊 EXECUTION STATUS: Real-world actions completed successfully!
"""

    def interactive_mode(self):
        """Interactive Neuro session"""
        print("🧠 Neuro AI Runtime - Interactive Mode")
        print("Type 'quit' to exit, 'history' to see previous executions")
        print("==================================================")
        
        while True:
            try:
                user_input = input("neuro> ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    break
                elif user_input == 'history':
                    self.show_history()
                elif user_input.endswith('.neuro'):
                    result = self.execute_file(user_input)
                    print(result)
                else:
                    # Direct analysis
                    understanding = self.ai.understand_neuro_intent(user_input)
                    print(f"🧠 AI Understanding: {understanding}")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")

    def show_history(self):
        """Show execution history"""
        if not self.execution_history:
            print("No execution history yet.")
            return
        
        print("\n📚 Execution History:")
        for i, item in enumerate(self.execution_history[-5:], 1):
            print(f"{i}. {item['file']} - {len(item['code'])} chars")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Neuro AI Runtime')
    parser.add_argument('filename', nargs='?', help='Neuro file to execute')
    parser.add_argument('--interactive', action='store_true', help='Start interactive mode')
    
    args = parser.parse_args()
    
    runtime = NeuroRuntime()
    
    print("🧠 Neuro AI Runtime v1.0")
    print("Free AI-Powered Intent Execution")
    print("==================================================")
    
    if args.interactive:
        runtime.interactive_mode()
    elif args.filename:
        result = runtime.execute_file(args.filename)
        print(result)
    else:
        print("Usage: python neuro_ai_runtime.py <file.neuro>")
        print("       python neuro_ai_runtime.py --interactive")

if __name__ == "__main__":
    main()
