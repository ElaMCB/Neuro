"""
Actual job search functionality for Neuro
Integrates with advanced job search system when available
"""

import webbrowser
import requests
from datetime import datetime
import os

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
    """Main job search function - uses advanced system if available"""
    print("🧠 NEURO JOB SEARCH ENGINE")
    print("=" * 40)
    
    # Try to use advanced job search if available
    if os.path.exists("advanced_job_search.py") and os.path.exists("profile_config.json"):
        try:
            print("🚀 Using Advanced Job Search System...\n")
            from run_advanced_job_search import run_advanced_job_search
            run_advanced_job_search()
            return
        except ImportError as e:
            print(f"⚠️  Advanced system not fully available: {e}")
            print("   Falling back to basic search...\n")
    else:
        print("ℹ️  Advanced system not configured.")
        print("   Run: python run_advanced_job_search.py")
        print("   Or edit profile_config.json and install: pip install -r requirements_job_search.txt\n")
    
    # Fallback to basic search
    print("📋 Running Basic Job Search...\n")
    search_linkedin_jobs()
    search_remote_first_companies()
    
    template = generate_application_templates()
    print(template)
    
    print("\n✅ Job search initiated!")
    print("💡 Tip: Set up advanced search for multi-platform search and profile matching")
    print("   Run: python run_advanced_job_search.py")

if __name__ == "__main__":
    search_jobs()
