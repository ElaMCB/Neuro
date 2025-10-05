"""
Neuro Intent Parser - Converts natural language to structured intent
"""

import re
from typing import Dict, Any, List

class Intent:
    """Base class for all intents"""
    def __init__(self, type: str, parameters: Dict[str, Any]):
        self.type = type
        self.parameters = parameters
    
    def __repr__(self):
        return f"Intent({self.type}, {self.parameters})"

class NeuroIntentParser:
    def __init__(self):
        self.patterns = {
            'job_search': [
                r'(find|search for|look for).*job',
                r'.*job.*(in|at|near).*',
                r'.*hire.*.*position'
            ],
            'model_training': [
                r'(train|build|create).*model',
                r'.*neural network.*',
                r'.*machine learning.*'
            ],
            'data_analysis': [
                r'analyze.*data',
                r'.*dataset.*',
                r'clean.*process.*data'
            ]
        }
    
    def parse(self, text: str) -> Intent:
        """Parse natural language into structured intent"""
        text = text.lower().strip()
        
        # Job search intent
        if any(re.search(pattern, text) for pattern in self.patterns['job_search']):
            return self._parse_job_search(text)
        
        # Model training intent  
        elif any(re.search(pattern, text) for pattern in self.patterns['model_training']):
            return self._parse_model_training(text)
        
        # Data analysis intent
        elif any(re.search(pattern, text) for pattern in self.patterns['data_analysis']):
            return self._parse_data_analysis(text)
        
        # Default fallback
        else:
            return Intent('unknown', {'text': text})
    
    def _parse_job_search(self, text: str) -> Intent:
        """Extract job search parameters from text"""
        parameters = {}
        
        # Extract location
        location_match = re.search(r'(in|at|near)\s+([a-zA-Z\s]+)', text)
        if location_match:
            parameters['location'] = location_match.group(2).strip()
        
        # Extract skills/technologies
        skills = []
        tech_keywords = ['python', 'pytorch', 'tensorflow', 'ml', 'machine learning', 
                        'ai', 'neural', 'deep learning', 'computer vision', 'nlp']
        for keyword in tech_keywords:
            if keyword in text:
                skills.append(keyword)
        if skills:
            parameters['skills'] = skills
        
        # Extract job type
        if 'remote' in text:
            parameters['remote'] = True
        if 'full.time' in text or 'full time' in text:
            parameters['employment_type'] = 'full_time'
        elif 'part.time' in text or 'part time' in text:
            parameters['employment_type'] = 'part_time'
        
        return Intent('job_search', parameters)
    
    def _parse_model_training(self, text: str) -> Intent:
        """Extract model training parameters from text"""
        parameters = {}
        
        # Extract model type
        if 'classif' in text:
            parameters['task'] = 'classification'
        elif 'regress' in text:
            parameters['task'] = 'regression'
        elif 'neural' in text or 'deep' in text:
            parameters['model_type'] = 'neural_network'
        
        # Extract dataset mention
        dataset_match = re.search(r'(on|using|with)\s+([a-zA-Z0-9\s]+)(dataset|data)', text)
        if dataset_match:
            parameters['dataset'] = dataset_match.group(2).strip()
        
        return Intent('model_training', parameters)
    
    def _parse_data_analysis(self, text: str) -> Intent:
        """Extract data analysis parameters from text"""
        parameters = {}
        
        if 'clean' in text:
            parameters['action'] = 'clean'
        elif 'analyze' in text:
            parameters['action'] = 'analyze'
        elif 'process' in text:
            parameters['action'] = 'process'
            
        return Intent('data_analysis', parameters)

def parse_intent(text: str) -> Intent:
    """Convenience function to parse text into intent"""
    parser = NeuroIntentParser()
    return parser.parse(text)

# Quick test
if __name__ == "__main__":
    test_queries = [
        "find me machine learning jobs in Boston",
        "train a neural network for image classification",
        "analyze my sales data"
    ]
    
    parser = NeuroIntentParser()
    for query in test_queries:
        intent = parser.parse(query)
        print(f"'{query}' -> {intent}")
