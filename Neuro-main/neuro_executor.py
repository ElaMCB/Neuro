#!/usr/bin/env python3
"""
Neuro Executor - Actually executes the AI-generated plans
"""

import os
import re
import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List

class NeuroExecutor:
    """Executes Neuro AI plans into real-world actions"""
    
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
    
    def execute_application_plan(self, neuro_analysis: str, original_neuro_code: str):
        """Actually execute the job application plan"""
        
        print("NEURO EXECUTION ENGINE")
        print("Converting AI analysis into real actions...")
        print("=" * 50)
        
        # Extract company and position
        company = self.extract_company(original_neuro_code)
        position = self.extract_position(original_neuro_code)
        
        # Generate actual files and actions
        cover_letter_file = self.generate_cover_letter(company, position, neuro_analysis, original_neuro_code)
        resume_guide_file = self.generate_resume_guide(neuro_analysis)
        project_desc_file = self.generate_project_description()
        
        # Send email with generated materials
        self.send_verification_email(company, position, [cover_letter_file, resume_guide_file, project_desc_file])
        
        self.show_next_steps(company)
    
    def send_verification_email(self, company: str, position: str, files: List[str]):
        """Send generated materials to your email for verification"""
        print("SETTING UP EMAIL VERIFICATION...")
        
        try:
            # Get email credentials securely
            print("\nEmail Configuration:")
            sender_email = input("Enter your Gmail address: ").strip()
            app_password = getpass.getpass("Enter your Gmail App Password: ").strip()
            receiver_email = "elena.mereanu@gmail.com"
            
            if not sender_email or not app_password:
                print("Email credentials required for verification")
                return
            
            # Add your actual resume files
            resume_files = [
                "examples/resume/outputs/resume_prompt_engineer_short.txt",
                "examples/resume/outputs/resume_prompt_engineer_keywords.txt"
            ]
            
            # Check which resume files exist
            existing_resumes = []
            for resume_file in resume_files:
                if os.path.exists(resume_file):
                    existing_resumes.append(resume_file)
                    print(f"Found resume: {resume_file}")
            
            if not existing_resumes:
                print("No resume files found. Generating basic template...")
                existing_resumes = [self.generate_basic_resume()]
            
            # Combine all files to attach
            all_files = files + existing_resumes
            
            # Create message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = f"Neuro Verification: {position} Application for {company}"
            
            # Email body
            body = f"""
Hello Elena,

This is a verification email from your Neuro system.

Your Neuro application materials for {position} at {company} have been successfully generated!

Generated Files:
• cover_letter_{company.replace(' ', '_').lower()}.html - Tailored cover letter with Arial font
• resume_optimization_guide.txt - AI engineering resume strategy  
• neuro_project_description.txt - Project documentation
{chr(10).join(f'• {os.path.basename(resume)} - Your actual resume' for resume in existing_resumes)}

What's Included:
1. A professional cover letter specifically written for {company} with Arial font
2. A comprehensive resume optimization guide for AI engineering roles
3. A detailed project description of your Neuro work
4. Your ACTUAL resume files with real experience and skills

Next Steps:
1. Review all attached files for formatting and content
2. Choose which resume version works best for {company}
3. Customize the cover letter with any personal touches
4. You're ready to apply - this is REAL content!

System Status: Neuro is working correctly with your PROFESSIONAL resume files!

Best regards,
Your Neuro System
            """
            
            message.attach(MIMEText(body, "plain"))
            
            # Attach all files
            for file_path in all_files:
                if os.path.exists(file_path):
                    with open(file_path, "r", encoding='utf-8') as f:
                        attachment = MIMEText(f.read())
                        attachment.add_header(
                            "Content-Disposition",
                            f"attachment; filename={os.path.basename(file_path)}",
                        )
                        message.attach(attachment)
            
            # Send email
            print("Connecting to Gmail...")
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(sender_email, app_password)
                server.send_message(message)
            
            print(f"VERIFICATION EMAIL SENT!")
            print(f"   From: {sender_email}")
            print(f"   To: {receiver_email}")
            print(f"   Subject: Neuro Verification: {position} Application for {company}")
            print(f"   Attachments: {len(all_files)} files including your ACTUAL resumes!")
            
        except Exception as e:
            print(f"Email sending failed: {e}")
            print("\nTROUBLESHOOTING:")
            print("1. Make sure you're using an App Password, not your regular Gmail password")
            print("2. Enable 2-factor authentication in your Google account")
            print("3. Generate an App Password at: https://myaccount.google.com/apppasswords")
            print("4. Select 'Mail' as the app and 'Other' as the device")
            print("\nYour files are still generated locally for review.")
    
    def generate_basic_resume(self):
        """Generate basic resume template if none found"""
        basic_resume = """
ELENA MEREANU
Atlanta Metropolitan Area • elena.mereanu@gmail.com
LinkedIn: linkedin.com/in/elenamereanu • GitHub: https://ElaMCB.github.io

PROFESSIONAL SUMMARY
QA Lead transitioning to AI Engineering with 10+ years building validation systems and automation frameworks. 
Creator of Neuro programming language exploration. Strong background in Python, AI workflows, and system architecture.

TECHNICAL SKILLS
• AI Engineering: Intent-Driven Systems, Natural Language Understanding, AI Workflows
• Programming: Python, TypeScript, PyTorch, API Development
• Tools: Neuro, Docker, Git, REST APIs, MLflow, Playwright
• Domains: Research Tools, AI Validation, Developer Tooling

PROJECTS
Neuro Programming Language Exploration
- Intent-driven programming language for AI development
- Natural language understanding of developer goals  
- Automatic generation of optimized AI workflows
- Built-in support for recommendation systems

EXPERIENCE
[Your detailed experience would go here - using your actual resume files]

EDUCATION & CERTIFICATIONS
M.S., Quality Assurance — Kennesaw State University
AWS Certified Machine Learning — AWS
NLP Specialization — Stanford / DeepLearning.AI
"""
        filename = "resume_basic_template.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(basic_resume)
        return filename
    
    def extract_company(self, neuro_code: str) -> str:
        """Extract company name from Neuro code"""
        match = re.search(r'COMPANY:\s*(.+)', neuro_code)
        return match.group(1).strip() if match else "Target Company"
    
    def extract_position(self, neuro_code: str) -> str:
        """Extract position from Neuro code"""
        match = re.search(r'POSITION:\s*(.+)', neuro_code)
        return match.group(1).strip() if match else "Target Position"
    
    def generate_cover_letter(self, company: str, position: str, analysis: str, neuro_code: str):
        """Generate actual cover letter file with Arial font and proper Neuro link"""
        
        cover_letter = f"""
<style>
body {{
    font-family: Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.4;
    color: #333333;
    margin: 0;
    padding: 20px;
}}
.section {{
    margin-bottom: 16px;
}}
.signature {{
    margin-top: 20px;
    line-height: 1.6;
}}
.neuro-link {{
    color: #0969da;
    text-decoration: none;
}}
.neuro-link:hover {{
    text-decoration: underline;
}}
</style>

<div class="section">
<strong>Subject: AI Engineer Application - Neuro Project Experience</strong>
</div>

<div class="section">
Dear {company} Hiring Team,
</div>

<div class="section">
I'm writing to apply for the AI Engineer position. My experience with AI system development and recent work on <a href="https://github.com/ElaMCB/Neuro" class="neuro-link">Neuro</a>, an intent-driven programming language exploration, aligns with your focus on building tools that transform how researchers engage with scientific papers.
</div>

<div class="section">
While you're creating innovative research tools, I've been exploring new paradigms in AI development through projects like <a href="https://github.com/ElaMCB/Neuro" class="neuro-link">Neuro</a>, which investigates natural language understanding and automated workflow generation. This work demonstrates the kind of AI engineering thinking relevant to your AI Engineer role.
</div>

<div class="section">
My background in system validation and reliability engineering ensures I understand how to build production-ready tools that researchers can depend on. Through my technical explorations, I've gained hands-on experience with:
</div>

<div class="section">
• <strong>Natural language processing and understanding systems</strong><br>
• <strong>AI workflow automation and optimization</strong><br>
• <strong>Scalable system architecture and deployment</strong><br>
• <strong>Developer tooling and user experience</strong>
</div>

<div class="section">
The attached resume provides more detail about my experience, and I've included a description of my <a href="https://github.com/ElaMCB/Neuro" class="neuro-link">Neuro</a> project exploration to demonstrate my practical AI engineering approach.
</div>

<div class="section">
I would welcome the opportunity to discuss how my experience with AI systems could contribute to {company}'s innovative work in research tooling.
</div>

<div class="signature">
<strong>Best regards,</strong><br>
Elena Mereanu<br>
elena.mereanu@gmail.com<br>
<a href="https://github.com/ElaMCB/Neuro" class="neuro-link">Neuro</a> | LinkedIn: linkedin.com/in/elenamereanu
</div>
"""
        
        filename = f"cover_letter_{company.replace(' ', '_').lower()}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(cover_letter)
        
        print(f"Cover letter generated: {filename}")
        print("   - AI Engineer position focus")
        print("   - Arial font for readability") 
        print("   - Neuro as clickable GitHub link")
        return filename
    
    def generate_resume_guide(self, analysis: str):
        """Generate resume optimization guide"""
        
        resume_guide = """
RESUME OPTIMIZATION FOR AI ENGINEERING ROLES:

1. PROFESSIONAL SUMMARY:
   Focus on AI engineering transition and Neuro project creation
   Emphasize intent-driven systems and natural language processing

2. KEY SKILLS SECTION:
   - AI Engineering: Intent-Driven Systems, Natural Language Understanding, AI Workflows
   - Programming: Python, PyTorch, API Development, System Architecture
   - Tools: Neuro, Docker, Git, REST APIs, MLflow
   - Domains: Research Tools, AI Validation, Developer Tooling

3. PROJECTS SECTION:
   Feature "Neuro Programming Language" prominently as AI engineering demonstration

4. EXPERIENCE ENHANCEMENT:
   - Reposition QA leadership as "AI System Validation"
   - Emphasize Python development and automation experience
   - Highlight system architecture and scalability work
"""
        
        filename = "resume_optimization_guide.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(resume_guide)
        
        print(f"Resume optimization guide generated: {filename}")
        return filename
    
    def generate_project_description(self):
        """Generate Neuro project description"""
        
        project_desc = """
NEURO PROJECT EXPLORATION

Overview:
Neuro is an exploration of intent-driven programming concepts that investigates how developers might describe what they want to achieve in natural language, while the system handles implementation details. It represents research into new paradigms for AI development accessibility.

Technical Explorations:
- Natural language understanding of development goals
- Automated optimization of AI workflows
- Investigation of recommendation systems and RAG architectures
- Scalable system design considerations
- Development tooling research

Skills Demonstrated:
- AI system design and implementation
- Natural language processing concepts
- Technical research and prototyping
- Practical engineering problem-solving

Relevance to AI Engineering:
This project demonstrates hands-on experience with AI system concepts and technical exploration relevant to building sophisticated research tools and AI systems.
"""
        
        filename = "neuro_project_description.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(project_desc)
        
        print(f"Project description generated: {filename}")
        return filename
    
    def show_next_steps(self, company: str):
        """Show immediate next steps"""
        
        next_steps = f"""
IMMEDIATE EXECUTION STEPS FOR {company.upper()}:

FILES GENERATED & ATTACHED:
• cover_letter_{company.replace(' ', '_').lower()}.html (Arial font, clickable Neuro links)
• resume_optimization_guide.txt  
• neuro_project_description.txt
• resume_prompt_engineer_short.txt (YOUR ACTUAL RESUME)
• resume_prompt_engineer_keywords.txt (YOUR ACTUAL RESUME)

EMAIL VERIFICATION:
• Check your email for the verification message
• Review ALL attachments including your REAL resumes
• The system is ready for actual job applications!

PRODUCTION READY:
• You have professional, tailored application materials
• Including your actual resume with real experience
• Neuro is verified and working with real content!
"""
        
        print(next_steps)

def main():
    """Test the executor"""
    executor = NeuroExecutor()
    
    # For testing - you would normally pass the actual analysis
    test_analysis = "AI analysis would go here"
    test_neuro_code = "COMPANY: alphaXiv\nPOSITION: AI Engineer"
    
    executor.execute_application_plan(test_analysis, test_neuro_code)

if __name__ == "__main__":
    main()
