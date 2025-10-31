# Quick Start Guide - Advanced Job Search

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements_job_search.txt
```

Or manually:
```bash
pip install schedule requests
```

### Step 2: Configure Your Profile

Your profile is already configured in `profile_config.json`! You can edit it to customize:

- **Target roles**: What positions you're looking for
- **Skills**: Your technical skills
- **Experience level**: junior, mid, or senior
- **Resume path**: Path to your resume file

### Step 3: Run Your First Search

```bash
python run_advanced_job_search.py
```

That's it! The system will:
- Search multiple platforms (Wellfound, RemoteOK, Indeed, LinkedIn, startup boards)
- Score each job against your profile
- Generate a detailed report
- Optionally prepare tailored resumes for top matches

## 📅 Set Up Weekly Automatic Searches

```bash
# Run immediately
python schedule_job_search.py --run-now

# Schedule for every Monday at 9 AM (default)
python schedule_job_search.py

# Custom schedule: Every Friday at 6 PM
python schedule_job_search.py --day friday --time 18:00
```

## 📝 Upload Your Resume

You mentioned you did the resume yourself - great! To use it:

1. **Place your resume file** in the project directory (or anywhere you prefer)
2. **Update `profile_config.json`** - change the `resume_path` to point to your file:
   ```json
   "resume_path": "path/to/your/resume.txt"
   ```

The system will automatically use your resume for all tailored applications!

### Supported Resume Formats

- **`.txt`** - Plain text (best for keyword matching)
- **`.md`** - Markdown
- The system works best with text-based formats

### Example Resume Path

If your resume is at `C:\Users\elena\Downloads\my_resume.txt`, update the config:

```json
"resume_path": "C:\\Users\\elena\\Downloads\\my_resume.txt"
```

Or use a relative path if it's in the project folder:
```json
"resume_path": "my_resume.txt"
```

## 🎯 What Gets Generated

### Job Search Results
- `job_search_results/job_search_YYYYMMDD_HHMMSS.json` - Full search results
- `job_search_reports/weekly_report_YYYYMMDD_HHMMSS.txt` - Human-readable report

### Tailored Application Packages
- `resume_templates/resume_company_title_YYYYMMDD.txt` - Customized resume
- `resume_templates/cover_company_title_YYYYMMDD.txt` - Tailored cover letter

## 💡 Pro Tips

1. **Review top matches weekly**: Focus on jobs with >70% match scores
2. **Customize the prepared resumes**: Use them as a starting point, but add personal touches
3. **Track your applications**: Keep a spreadsheet of where you've applied
4. **Follow up**: Follow up on applications after 1 week

## 🔧 Troubleshooting

### "Module not found" errors
```bash
pip install schedule requests
```

### "Profile config not found"
Run `schedule_job_search.py` once - it will create a default profile config:
```bash
python schedule_job_search.py --run-now
```

### Resume not found
- Check the path in `profile_config.json`
- Use absolute path (full Windows path with backslashes escaped: `\\` or use forward slashes: `/`)
- Or use relative path if resume is in project folder

## 🆘 Need Help?

See `JOB_SEARCH_README.md` for full documentation.

## 🎉 Next Steps

1. ✅ Install dependencies
2. ✅ Upload your resume path to `profile_config.json`
3. ✅ Run your first search
4. ✅ Set up weekly scheduler
5. ✅ Apply to top matches!

Good luck with your job search! 🚀

