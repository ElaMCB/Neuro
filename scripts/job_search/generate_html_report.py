#!/usr/bin/env python3
"""
Generate a beautiful HTML report from job search results JSON
"""
import json
import sys
from pathlib import Path

def generate_html_report(json_file: str = None, output_file: str = None):
    """Generate HTML report from JSON results"""
    
    # Find most recent results if not specified
    if json_file is None:
        results_dir = Path("job_search_results")
        if not results_dir.exists():
            print("❌ No job search results directory found")
            return False
        
        json_files = sorted(
            results_dir.glob("job_search_*.json"),
            key=lambda x: x.stat().st_mtime,
            reverse=True
        )
        
        if not json_files:
            print("❌ No job search results found")
            return False
        
        json_file = str(json_files[0])
        print(f"📁 Using results file: {Path(json_file).name}")
    
    # Load JSON data
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ Error reading JSON file: {e}")
        return False
    
    # Read HTML template
    template_file = Path(__file__).parent / "view_results.html"
    if not template_file.exists():
        print(f"❌ Template file not found: {template_file}")
        return False
    
    with open(template_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Embed JSON data into HTML
    json_str = json.dumps(data, indent=2)
    html_content = html_content.replace('JSON_DATA_PLACEHOLDER', json_str)
    
    # Determine output filename
    if output_file is None:
        output_file = "job_search_report.html"
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ HTML report generated: {output_file}")
    print(f"   Open in your browser to view")
    
    # Try to open in browser
    import webbrowser
    try:
        webbrowser.open(f"file://{Path(output_file).absolute()}")
        print(f"🌐 Opening in browser...")
    except:
        pass
    
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "job_search_report.html"
        generate_html_report(json_file, output_file)
    else:
        generate_html_report()

