#!/usr/bin/env python3
"""
Neuro AI Engine - Core AI understanding for Neuro programming language
"""

import os
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from typing import Dict, List, Any, Optional
import re

class NeuroAIEngine:
    """AI engine for understanding Neuro code intent"""
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.generator = None
        self.device = "cpu"
        
    def load_models(self):
        """Load AI models for Neuro understanding"""
        try:
            print("Loading AI models for Neuro understanding...")
            
            # Use a smaller, more available model for testing
            self.generator = pipeline(
                "text-generation",
                model="distilgpt2",
                tokenizer="distilgpt2",
                device=-1  # Use CPU
            )
            
            print("✅ AI models loaded successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error loading AI models: {e}")
            print("🔄 Using fallback rule-based understanding...")
            self.generator = None
            return False
    
    def understand_neuro_intent(self, neuro_code: str) -> str:
        """Understand the intent behind Neuro code using AI"""
        
        # First try AI understanding if models are loaded
        if self.generator:
            ai_understanding = self._ai_understand(neuro_code)
            if ai_understanding:
                return ai_understanding
        
        # Fallback to rule-based understanding
        return self._rule_based_understand(neuro_code)
    
    def _ai_understand(self, neuro_code: str) -> Optional[str]:
        """Use AI to understand Neuro intent"""
        try:
            prompt = self._create_neuro_prompt(neuro_code)
            
            # Generate understanding
            result = self.generator(
                prompt,
                max_length=400,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=50256
            )
            
            if result and len(result) > 0:
                generated_text = result[0]['generated_text']
                # Extract just the understanding part
                understanding = self._extract_understanding(generated_text, prompt)
                return understanding
                
        except Exception as e:
            print(f"⚠️  AI understanding failed: {e}")
        
        return None
    
    def _create_neuro_prompt(self, neuro_code: str) -> str:
        """Create better prompt for AI understanding"""
        prompt = f"""
You are Neuro AI, an intent-driven programming language system. 
Analyze this Neuro code and provide structured understanding:

NEURO CODE:
{neuro_code}

Please analyze:
1. PRIMARY GOAL: What is the main objective?
2. KEY COMPONENTS: What elements are involved?
3. EXECUTION STRATEGY: How should this be implemented?
4. REQUIRED ACTIONS: What specific steps are needed?
5. EXPECTED OUTCOME: What result should be achieved?

NEURO AI ANALYSIS:
"""
        return prompt
    
    def _extract_understanding(self, generated_text: str, original_prompt: str) -> str:
        """Extract the understanding from generated text"""
        # Remove the original prompt to get just the analysis
        if generated_text.startswith(original_prompt):
            understanding = generated_text[len(original_prompt):].strip()
        else:
            understanding = generated_text.strip()
        
        # Clean up any incomplete sentences
        understanding = re.split(r'[.!?]', understanding)[0] + '.'
        
        return understanding if understanding else "AI analysis completed."
    
    def _rule_based_understand(self, neuro_code: str) -> str:
        """Rule-based understanding of Neuro code"""
        neuro_lower = neuro_code.lower()
        
        understanding_parts = []
        
        # Detect job application intent
        if any(keyword in neuro_lower for keyword in ['company:', 'position:', 'apply', 'job', 'hiring']):
            company = self._extract_company(neuro_code)
            position = self._extract_position(neuro_code)
            
            understanding_parts.append(f"🎯 PRIMARY GOAL: Apply for {position} at {company}")
            understanding_parts.append("📋 KEY COMPONENTS: Cover letter, resume optimization, project documentation")
            understanding_parts.append("🚀 EXECUTION STRATEGY: Generate tailored application materials")
            understanding_parts.append("🔧 REQUIRED ACTIONS: Create cover letter, resume guide, project description")
            understanding_parts.append("✅ EXPECTED OUTCOME: Professional application package ready for submission")
        
        # Detect code generation intent
        elif any(keyword in neuro_lower for keyword in ['create', 'build', 'generate', 'make']):
            understanding_parts.append("🎯 PRIMARY GOAL: Create or generate something new")
            understanding_parts.append("📋 KEY COMPONENTS: Code structure, dependencies, implementation plan")
            understanding_parts.append("🚀 EXECUTION STRATEGY: Automated code generation based on requirements")
            understanding_parts.append("🔧 REQUIRED ACTIONS: Analyze requirements, generate code, set up project structure")
            understanding_parts.append("✅ EXPECTED OUTCOME: Functional code or project structure")
        
        # General analysis intent
        else:
            understanding_parts.append("🎯 PRIMARY GOAL: Understand and analyze the given Neuro code")
            understanding_parts.append("📋 KEY COMPONENTS: Intent analysis, requirement parsing, execution planning")
            understanding_parts.append("🚀 EXECUTION STRATEGY: Parse natural language intent into actionable steps")
            understanding_parts.append("🔧 REQUIRED ACTIONS: Interpret requirements, plan execution, provide guidance")
            understanding_parts.append("✅ EXPECTED OUTCOME: Clear understanding and execution plan")
        
        return "\n".join(understanding_parts)
    
    def _extract_company(self, neuro_code: str) -> str:
        """Extract company name from Neuro code"""
        match = re.search(r'COMPANY:\s*(.+)', neuro_code, re.IGNORECASE)
        return match.group(1).strip() if match else "target company"
    
    def _extract_position(self, neuro_code: str) -> str:
        """Extract position from Neuro code"""
        match = re.search(r'POSITION:\s*(.+)', neuro_code, re.IGNORECASE)
        return match.group(1).strip() if match else "target position"
    
    def analyze_complexity(self, neuro_code: str) -> Dict[str, Any]:
        """Analyze complexity of Neuro intent"""
        word_count = len(neuro_code.split())
        line_count = len(neuro_code.split('\n'))
        
        complexity = "low"
        if word_count > 100:
            complexity = "high"
        elif word_count > 50:
            complexity = "medium"
        
        return {
            "word_count": word_count,
            "line_count": line_count,
            "complexity": complexity,
            "estimated_actions": max(1, word_count // 20)
        }
    
    def generate_execution_plan(self, neuro_code: str) -> List[str]:
        """Generate step-by-step execution plan"""
        understanding = self.understand_neuro_intent(neuro_code)
        
        plan = [
            "1. Analyze Neuro code intent",
            "2. Parse requirements and constraints", 
            "3. Generate appropriate execution strategy",
            "4. Execute required actions",
            "5. Verify results and provide feedback"
        ]
        
        # Add specific steps based on intent
        neuro_lower = neuro_code.lower()
        if any(keyword in neuro_lower for keyword in ['company:', 'position:', 'apply']):
            plan.extend([
                "6. Generate tailored cover letter",
                "7. Create resume optimization guide",
                "8. Prepare project documentation",
                "9. Provide application next steps"
            ])
        
        return plan

# Test the AI engine
if __name__ == "__main__":
    engine = NeuroAIEngine()
    engine.load_models()
    
    test_code = """
COMPANY: alphaXiv
POSITION: AI Engineer
GOAL: Apply for AI engineering position using Neuro experience
"""
    
    understanding = engine.understand_neuro_intent(test_code)
    print("🧠 Neuro AI Understanding:")
    print(understanding)
