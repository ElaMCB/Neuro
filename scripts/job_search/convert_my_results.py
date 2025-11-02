#!/usr/bin/env python3
"""
Quick script to convert your downloaded job search JSON into a beautiful HTML report
Just run: python convert_my_results.py <your_json_file.json>
"""
import json
import sys
from pathlib import Path
from datetime import datetime

def create_html_report(json_data):
    """Create a beautiful HTML report from JSON data"""
    
    profile = json_data.get('profile', {})
    jobs = json_data.get('jobs', [])
    summary = json_data.get('summary', {})
    search_date = json_data.get('search_date', '')
    
    # Count platforms
    platforms = set(j.get('platform', '') for j in jobs)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neuro Job Search Results - {search_date[:10]}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header .date {{ opacity: 0.9; font-size: 1.1em; }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px 40px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }}
        .stat-card {{
            text-align: center;
            padding: 20px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .stat-card .number {{ font-size: 2.5em; font-weight: bold; color: #667eea; }}
        .stat-card .label {{ color: #6c757d; margin-top: 5px; }}
        .profile-section {{ padding: 30px 40px; background: #fff; border-bottom: 2px solid #e9ecef; }}
        .profile-section h2 {{ color: #667eea; margin-bottom: 15px; }}
        .tags {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px; }}
        .tag {{
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 15px;
            font-size: 0.9em;
        }}
        .jobs-section {{ padding: 30px 40px; }}
        .jobs-section h2 {{ color: #667eea; margin-bottom: 20px; font-size: 1.8em; }}
        .job-card {{
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
            position: relative;
            transition: all 0.3s;
        }}
        .job-card:hover {{
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.2);
            border-color: #667eea;
            transform: translateY(-2px);
        }}
        .match-badge {{
            position: absolute;
            top: 20px;
            right: 20px;
            padding: 8px 15px;
            border-radius: 20px;
            font-weight: bold;
            color: white;
        }}
        .match-high {{ background: #28a745; }}
        .match-medium {{ background: #ffc107; color: #333; }}
        .match-low {{ background: #dc3545; }}
        .job-title {{ font-size: 1.5em; font-weight: 700; margin-bottom: 10px; padding-right: 120px; }}
        .job-company {{ font-size: 1.1em; color: #667eea; margin-bottom: 10px; font-weight: 600; }}
        .job-meta {{ color: #6c757d; margin: 10px 0; }}
        .job-description {{ color: #495057; line-height: 1.6; margin: 15px 0; }}
        .platform-badge {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: 600;
            margin: 10px 5px 10px 0;
        }}
        .platform-wellfound {{ background: #ffeaa7; }}
        .platform-indeed {{ background: #74b9ff; }}
        .platform-linkedin {{ background: #0077b5; color: white; }}
        .platform-startup_board {{ background: #fd79a8; color: white; }}
        .platform-remoteok {{ background: #a29bfe; color: white; }}
        .btn {{
            display: inline-block;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            margin-top: 15px;
            transition: all 0.3s;
        }}
        .btn:hover {{ background: #5568d3; transform: translateY(-1px); }}
        .footer {{ background: #f8f9fa; padding: 30px; text-align: center; color: #6c757d; }}
        @media (max-width: 768px) {{
            .match-badge {{ position: static; margin-bottom: 10px; }}
            .job-title {{ padding-right: 0; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎯 Neuro Job Search Results</h1>
            <p class="date">Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="number">{summary.get('total_jobs', 0)}</div>
                <div class="label">Total Jobs</div>
            </div>
            <div class="stat-card">
                <div class="number">{summary.get('high_matches', 0)}</div>
                <div class="label">High Matches (>70%)</div>
            </div>
            <div class="stat-card">
                <div class="number">{summary.get('medium_matches', 0)}</div>
                <div class="label">Medium Matches</div>
            </div>
            <div class="stat-card">
                <div class="number">{len(platforms)}</div>
                <div class="label">Platforms</div>
            </div>
        </div>
        
        <div class="profile-section">
            <h2>👤 Your Profile</h2>
            <div>
                <strong>Name:</strong> {profile.get('name', 'N/A')}<br>
                <strong>Experience:</strong> {profile.get('experience_level', 'N/A')}<br>
                <strong>Remote Preference:</strong> {'Yes ✅' if profile.get('remote_preference') else 'No'}
            </div>
            <div style="margin-top: 15px;">
                <strong>Target Roles:</strong>
                <div class="tags">
                    {''.join(f'<span class="tag">{role}</span>' for role in profile.get('target_roles', []))}
                </div>
            </div>
            <div style="margin-top: 15px;">
                <strong>Skills:</strong>
                <div class="tags">
                    {''.join(f'<span class="tag">{skill}</span>' for skill in profile.get('skills', []))}
                </div>
            </div>
            <div style="margin-top: 15px;">
                <strong>Locations:</strong>
                <div class="tags">
                    {''.join(f'<span class="tag">{loc}</span>' for loc in profile.get('locations', []))}
                </div>
            </div>
        </div>
        
        <div class="jobs-section">
            <h2>💼 Job Listings ({len(jobs)} jobs found)</h2>
"""
    
    # Sort jobs by match score
    sorted_jobs = sorted(jobs, key=lambda x: x.get('match_score', 0), reverse=True)
    
    for job in sorted_jobs:
        match_score = job.get('match_score', 0)
        match_class = 'match-high' if match_score >= 70 else 'match-medium' if match_score >= 40 else 'match-low'
        
        html += f"""
            <div class="job-card">
                <div class="match-badge {match_class}">{int(match_score)}% Match</div>
                <h3 class="job-title">{job.get('title', 'N/A')}</h3>
                <div class="job-company">{job.get('company', 'N/A')}</div>
                <div class="job-meta">
                    📍 {job.get('location', 'N/A')}
                    <span class="platform-badge platform-{job.get('platform', '').replace(' ', '_')}">{job.get('platform', 'N/A')}</span>
                </div>
                <div class="job-description">{job.get('description', 'No description available')}</div>
                <a href="{job.get('url', '#')}" target="_blank" class="btn">View Job →</a>
            </div>
"""
    
    html += """
        </div>
        
        <div class="footer">
            <p><strong>Neuro</strong> - The Intent-Driven Language for AI</p>
            <p style="margin-top: 10px;">🔗 <a href="https://github.com/ElaMCB/Neuro" style="color: #667eea;">GitHub</a></p>
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_my_results.py <json_file>")
        print("\nExample: python convert_my_results.py job_search_20251031.json")
        sys.exit(1)
    
    json_file = sys.argv[1]
    
    if not Path(json_file).exists():
        print(f"ERROR: File not found: {json_file}")
        sys.exit(1)
    
    print(f"Reading: {json_file}")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"ERROR: Error reading JSON: {e}")
        sys.exit(1)
    
    print("Generating beautiful HTML report...")
    
    html = create_html_report(data)
    
    output_file = "my_job_search_report.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Report generated: {output_file}")
    print(f"   Double-click the file to open in your browser!")
    
    # Try to open automatically
    import webbrowser
    try:
        abs_path = Path(output_file).absolute()
        webbrowser.open(f"file:///{abs_path}")
        print(f"Opening in browser...")
    except:
        print(f"   Or open manually in your browser")

if __name__ == "__main__":
    main()

