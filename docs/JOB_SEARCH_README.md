# Neuro Job Search System

Automated job search that searches multiple platforms, matches your profile, and prepares applications.

## 🚀 Quick Start

### 1. Configure Your Profile

Create or edit `profile_config.json`:

```json
{
  "name": "Your Name",
  "email": "your.email@gmail.com",
  "target_roles": ["prompt engineer", "ai engineer", "ml engineer"],
  "skills": ["python", "pytorch", "llm", "gpt", "transformers"],
  "experience_level": "junior",
  "locations": ["remote", "US", "Boston", "New York"],
  "remote_preference": true,
  "resume_path": "examples/resume/outputs/resume_prompt_engineer_short.txt",
  "github_url": "https://github.com/yourusername/yourproject",
  "linkedin_url": "linkedin.com/in/yourprofile"
}
```

### 2. Run Job Search

```bash
# Advanced search (searches multiple platforms)
python run_advanced_job_search.py

# Or use the simple Neuro version
python run_neuro.py my_job_search.neuro
```

### 3. View Results

```bash
# Display results in terminal
python display_results.py

# Or open the JSON file
cat job_search_results/job_search_*.json
```

## 📊 What Gets Searched

The advanced job search system searches:

1. **Wellfound (AngelList)** - Startup jobs
2. **RemoteOK** - Remote-first positions
3. **Indeed** - Traditional job board
4. **LinkedIn** - Professional network jobs
5. **Y Combinator** - YC startup jobs

## 🎯 Features

- **Profile Matching**: Scores jobs based on your skills and requirements
- **Smart Filtering**: Finds remote-first companies automatically
- **Resume Preparation**: Generates tailored resumes for top matches
- **Duplicate Removal**: Intelligently removes duplicate postings
- **Results Tracking**: Saves all results to JSON for review

## 📧 Weekly Automation

### GitHub Actions (Recommended)

The weekly job search runs automatically every Monday via GitHub Actions.

**Setup:**
1. Go to Repository Settings → Secrets → Actions
2. Add email credentials (see [EMAIL_SETUP.md](EMAIL_SETUP.md))
3. The workflow will:
   - Search all platforms weekly
   - Generate reports
   - Email you the results
   - Upload artifacts you can download

### Local Scheduling

For local automation:

```bash
# Run immediately
python schedule_job_search.py --run-now

# Schedule for every Monday at 9 AM
python schedule_job_search.py --day monday --time 09:00
```

## 📁 Output Files

After running, you'll find:

```
job_search_results/
  └── job_search_20251031_143025.json    # All jobs found

job_search_reports/
  └── weekly_report_20251031_143025.txt  # Summary report

resume_templates/
  └── application_OpenAI_Senior_Engineer.txt  # Tailored applications
```

## 🔧 Advanced Configuration

### Custom Search Parameters

Edit `my_job_search.neuro` to customize:

```neuro
pipeline FindAIPositions {
    goal: "Find prompt engineer jobs with remote-first companies"
    target_roles: ["prompt engineer", "ai engineer"]
    locations: ["remote", "US"]
    company_policy: "remote first"
    skills: ["python", "pytorch", "llm"]
    experience: "mid to senior level"
}
```

### Adding More Platforms

Edit `advanced_job_search.py` to add more job platforms:

```python
def search_new_platform(self) -> List[JobListing]:
    # Your scraping logic here
    return jobs
```

## ⚠️ Important Notes

### Rate Limiting
The system adds delays between searches to respect rate limits. Don't remove the `time.sleep()` calls.

### Web Scraping Ethics
- The system uses public APIs and web scraping
- No authentication credentials are stored
- Respects robots.txt
- Rate-limited to avoid overwhelming servers

### LinkedIn Limitations
LinkedIn has strict anti-scraping policies. The LinkedIn search:
- Opens browser searches instead of scraping
- Requires manual review
- Can't be fully automated

## 🐛 Troubleshooting

### No Results Found

**Issue**: Search runs but finds 0 jobs

**Solutions**:
1. Check internet connection
2. Verify `profile_config.json` exists
3. Some platforms may be blocking requests - try with VPN
4. Check that BeautifulSoup4 is installed: `pip install beautifulsoup4`

### Email Not Sending

**Issue**: Email notification fails

**Solution**: See [EMAIL_SETUP.md](EMAIL_SETUP.md) for setup instructions

### Import Errors

**Issue**: `ModuleNotFoundError` when running

**Solution**:
```bash
pip install -r requirements_job_search.txt
```

## 📈 Tips for Best Results

1. **Update Skills Regularly**: Keep your `skills` list current
2. **Broad Search First**: Start with general roles, then narrow down
3. **Review Match Scores**: Focus on jobs with >70% match
4. **Customize Applications**: Use the generated templates as starting points
5. **Track Applications**: Keep notes on which companies you've applied to

## 🤝 Contributing

Found a bug or want to add a new job platform? See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

