"""
Neuro Intent Compiler - Executes structured intents
"""

# Use absolute import when running from root, relative when running from same directory
try:
    from .parser import Intent  # Try relative import first
except ImportError:
    from parser import Intent   # Fallback to absolute import

class NeuroCompiler:
    def __init__(self):
        self.executors = {
            'job_search': JobSearchExecutor(),
            'model_training': ModelTrainingExecutor(), 
            'data_analysis': DataAnalysisExecutor(),
            'unknown': UnknownIntentExecutor()
        }
    
    def compile(self, intent: Intent) -> str:
        """Compile intent into executable action"""
        executor = self.executors.get(intent.type, self.executors['unknown'])
        return executor.execute(intent)

class JobSearchExecutor:
    def execute(self, intent: Intent) -> str:
        params = intent.parameters
        location = params.get('location', 'anywhere')
        skills = params.get('skills', [])
        
        # Build search query
        query_parts = []
        if skills:
            query_parts.append(f"skills: {', '.join(skills)}")
        if location and location != 'anywhere':
            query_parts.append(f"location: {location}")
        
        search_description = " and ".join(query_parts) if query_parts else "all AI/ML positions"
        
        return f"""
Neuro Job Search Agent
Searching for: {search_description}

Actions:
- Scanning LinkedIn, Indeed, company career pages
- Filtering for AI/ML engineering roles  
- Matching against your skill profile
- Ranking by relevance and company culture

Expected results: 15-25 quality matches
Time to complete: 2-3 minutes
""".strip()

class ModelTrainingExecutor:
    def execute(self, intent: Intent) -> str:
        params = intent.parameters
        task = params.get('task', 'unknown task')
        model_type = params.get('model_type', 'neural_network')
        
        return f"""
Neuro Model Training Agent  
Task: {task}
Model: {model_type}

Pipeline:
1. Data loading and preprocessing
2. Feature engineering and selection
3. Model architecture design
4. Hyperparameter optimization
5. Training with validation
6. Performance evaluation

Estimated training time: 10-30 minutes
""".strip()

class DataAnalysisExecutor:
    def execute(self, intent: Intent) -> str:
        action = intent.parameters.get('action', 'analyze')
        
        return f"""
Neuro Data Analysis Agent
Action: {action}

Steps:
1. Data quality assessment
2. Missing value handling  
3. Outlier detection
4. Feature correlation analysis
5. Statistical summary generation
6. Visualization creation

Analysis completion: 2-5 minutes
""".strip()

class UnknownIntentExecutor:
    def execute(self, intent: Intent) -> str:
        return f"""
Neuro Assistant
I understand you said: "{intent.parameters.get('text', '')}"

I can help you with:
• Job search ("find AI jobs in Boston")
• Model training ("train a classifier on iris dataset")  
• Data analysis ("analyze my sales data")

Try being more specific about what you'd like to achieve.
""".strip()

def compile_intent(intent_text: str) -> str:
    """Convenience function: natural language → execution plan"""
    try:
        from .parser import parse_intent
    except ImportError:
        from parser import parse_intent
        
    intent = parse_intent(intent_text)
    compiler = NeuroCompiler()
    return compiler.compile(intent)
