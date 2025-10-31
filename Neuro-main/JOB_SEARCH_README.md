# Advanced Job Search System for Neuro

This enhanced job search system extends Neuro to help you find positions as a prompt engineer or AI engineer at the junior level. It searches multiple platforms, matches your profile, and prepares tailored resumes.

## Features

### 🔍 Multi-Platform Search
- **Wellfound** (formerly AngelList) - Startup and tech jobs
- **RemoteOK** - Remote positions worldwide
- **Indeed** - Major job board
- **LinkedIn** - Professional network
- **Startup Boards** - Y Combinator, Techstars, Work at a Startup

### 🎯 Profile Matching
- Scores each job against your profile (0-100%)
- Matches based on:
  - Job title relevance
  - Required skills
  - Location preferences
  - Experience level
  - Remote preferences

### 📝 Resume Preparation
- Tailors your resume for specific job postings
- Extracts keywords from job descriptions
- Generates customized cover letters
- Highlights relevant experience

### 📅 Weekly Automation
- Automatically runs job searches on a schedule
- Saves results and generates reports
- Prepares resumes for top matches

## Quick Start

### 1. Configure Your Profile

Edit `profile_config.json` to match your profile:

```json
{
  "name": "Your Name",
  "email": "your.email@example.com",
  "target_roles": ["prompt engineer", "ai engineer"],
  "skills": ["python", "pytorch", "llm"],
  "experience_level": "junior",
  "locations": ["remote", "US"],
  "remote_preference": true,
  "resume_path": "path/to/your/resume.txt"
}
```

### 2. Run a Job Search

```bash
python run_advanced_job_search.py
```

This will:
- Search all configured platforms
- Score and rank jobs by match
- Generate a detailed report
- Optionally prepare tailored resumes for top matches

### 3. Set Up Weekly Searches

```bash
# Run immediately
python schedule_job_search.py --run-now

# Schedule for every Monday at 9 AM
python schedule_job_search.py --day monday --time 09:00
```

## Usage

### One-Time Search

```bash
python run_advanced_job_search.py
```

### Weekly Scheduled Search

```bash
# Start the scheduler (runs every Monday at 9 AM by default)
python schedule_job_search.py

# Custom schedule
python schedule_job_search.py --day friday --time 18:00

# Run immediately without scheduling
python schedule_job_search.py --run-now
```

### Prepare Resume for Specific Job

```python
from resume_preparer import ResumePreparer

preparer = ResumePreparer("path/to/your/resume.txt")
prepared = preparer.prepare_for_job(
    job_title="AI Engineer",
    company="Example Company",
    job_description="Job description text...",
    job_url="https://example.com/job"
)

# Files saved in resume_templates/
```

## Output Structure

```
job_search_results/
  └── job_search_YYYYMMDD_HHMMSS.json    # Full search results

job_search_reports/
  └── weekly_report_YYYYMMDD_HHMMSS.txt   # Human-readable reports

resume_templates/
  ├── resume_company_title_YYYYMMDD.txt  # Tailored resumes
  └── cover_company_title_YYYYMMDD.txt    # Cover letters
```

## Integration with Neuro

The system works with your `my_job_search.neuro` file. When you run:

```bash
python run_neuro.py my_job_search.neuro
```

It will use the advanced job search system if available, falling back to basic search otherwise.

## Customization

### Adding New Job Platforms

Edit `advanced_job_search.py` and add a new search method:

```python
def search_new_platform(self) -> List[JobListing]:
    """Search a new platform"""
    jobs = []
    # Your search logic here
    return jobs
```

Then add it to `search_all_platforms()`.

### Adjusting Match Scoring

Edit the `_calculate_match_score()` method in `JobSearchEngine` to adjust how jobs are scored against your profile.

### Resume Tailoring

Customize resume preparation in `resume_preparer.py`:
- `_tailor_resume()` - Main tailoring logic
- `_enhance_skills_section()` - Skills matching
- `_generate_cover_letter()` - Cover letter generation

## Tips for Success

1. **Keep your profile updated**: Update `profile_config.json` as you gain new skills
2. **Review top matches weekly**: Focus on jobs with >70% match scores
3. **Customize resumes**: Use the prepared resumes as a starting point, but customize them further
4. **Track applications**: Keep a spreadsheet of where you've applied
5. **Follow up**: Follow up on applications after 1 week

## Uploading Your Resume

To use your own formatted resume:

1. Place your resume file in the project directory
2. Update `resume_path` in `profile_config.json` to point to your file
3. The system will use it for all resume preparations

Supported formats: `.txt`, `.md` (text-based formats work best for keyword matching)

## Troubleshooting

### No jobs found
- Check your internet connection
- Some platforms may require manual search (links are generated)
- Try running `--run-now` to see immediate results

### Resume preparation fails
- Ensure your resume file path is correct in `profile_config.json`
- Check that the file exists and is readable
- Verify the file is in a text-based format

### Scheduler not running
- Make sure the `schedule` package is installed: `pip install schedule`
- Check that you're running Python 3.8+
- The scheduler runs continuously - press Ctrl+C to stop

## Next Steps

- [ ] Set up weekly email notifications
- [ ] Integrate with job board APIs (when available)
- [ ] Add application tracking database
- [ ] Create interview preparation tools
- [ ] Add more startup job boards

## Support

For issues or questions:
1. Check the `examples/` directory for usage examples
2. Review the code comments in each module
3. Update your Neuro intent file (`my_job_search.neuro`) to match your goals

---

**Happy job hunting! 🚀**

