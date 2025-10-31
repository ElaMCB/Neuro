"""
Actual job search functionality for Neuro
"""

import webbrowser
import requests
from datetime import datetime

def search_linkedin_jobs():
    """Open LinkedIn with pre-configured searches"""
    searches = [
        "https://www.linkedin.com/jobs/search/?keywords=prompt%20engineer&location=United%20States&remote=true",
        "https://www.linkedin.com/jobs/search/?keywords=ai%20engineer&location=United%20States&remote=true",
        "https://www.linkedin.com/jobs/search/?keywords=llm%20engineer&location=United%20States&remote=true"
    ]
    
    print("🔗 Opening LinkedIn job searches...")
    for url in searches:
        webbrowser.open(url)

def search_remote_first_companies():
    """List remote-first companies hiring AI roles"""
    companies = [
        "OpenAI", "Anthropic", "GitLab", "Zapier", "Automattic",
        "Hugging Face", "Cohere", "Scale AI", "AssemblyAI"
    ]
    
    print("\n🏠 Remote-First Companies Hiring:")
    for company in companies:
        print(f"   - {company}: https://{company.lower().replace(' ', '')}.com/careers")

def generate_application_templates():
    """Generate application templates"""
    template = """
APPLICATION TEMPLATE FOR {role} at {company}


I'm excited to apply for the {role} position at {company}. With my experience in {skills}, I'm confident I can contribute to your AI initiatives.

Key qualifications:
- Experience with {technologies}
- Background in prompt engineering and LLM development
- Remote work experience with distributed teams

As a developer of Neuro (an intent-driven AI language), I'm passionate about making AI more accessible.

Best regards,
[Your Name]
"""
    print("\n📝 Application Template Generated")
    return template

def search_jobs():
    """Main job search function"""
    print("🧠 NEURO JOB SEARCH ENGINE")
    print("=" * 40)
    
    search_linkedin_jobs()
    search_remote_first_companies()
    
    template = generate_application_templates()
    print(template)
    
    print("\n✅ Job search initiated!")
    print("Next: Check your browser for LinkedIn searches")

if __name__ == "__main__":
    search_jobs()
