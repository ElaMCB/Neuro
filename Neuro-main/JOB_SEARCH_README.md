# Neuro Job Search System

An advanced, intent-driven job search system built with Neuro programming language. Search multiple platforms, match your profile automatically, and prepare tailored resumes - all declared in natural language using Neuro syntax.

## 🎯 What It Does

This system extends Neuro to help you find jobs by:

1. **Multi-Platform Search** - Searches Wellfound, RemoteOK, Indeed, LinkedIn, and startup boards simultaneously
2. **Profile Matching** - Automatically scores jobs (0-100%) against your profile
3. **Resume Tailoring** - Prepares customized resumes for specific job applications
4. **Weekly Automation** - Runs automatically on a schedule
5. **Intent-Driven** - Write your job search requirements in Neuro syntax (`.neuro` files)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements_job_search.txt
```

### 2. Configure Your Profile

Edit `profile_config.json`:

```json
{
  "name": "Your Name",
  "email": "your.email@example.com",
  "target_roles": ["prompt engineer", "ai engineer"],
  "skills": ["python", "pytorch", "llm"],
  "experience_level": "junior",
  "locations": ["remote", "US"],
  "remote_preference": true,
  "resume_path": "path/to/your/resume.docx"
}
```

### 3. Write Your Job Search Intent in Neuro

Create or edit `my_job_search.neuro`:

```neuro
pipeline FindAIPositions {
    goal: "Find prompt engineer and AI engineer jobs with remote-first companies"
    
    target_roles: ["prompt engineer", "ai engineer", "ml engineer"]
    locations: ["remote", "US", "Boston", "New York"]
    company_policy: "remote first"
    skills: ["python", "pytorch", "llm", "gpt", "transformers"]
    experience: "junior level"
    
    actions: [
        search_job_boards(),
        filter_remote_first(),
        match_skills(),
        generate_applications(),
        track_responses()
    ]
}
```

### 4. Run Your Job Search

```bash
python run_neuro.py my_job_search.neuro
```

That's it! Neuro executes your intent and searches for jobs.

## 📋 Features

### Multi-Platform Job Search

Searches across:
- **Wellfound** (formerly AngelList) - Startup jobs
- **RemoteOK** - Remote positions
- **Indeed** - Major job board
- **LinkedIn** - Professional network
- **Startup Boards** - Y Combinator, Techstars, Work at a Startup

### Profile Matching

Automatically scores each job against your profile:
- **Title Match** (35 points) - How well job title matches your target roles
- **Skills Match** (35 points) - Checks job description for your skills
- **Location Match** (20 points) - Remote/location preferences
- **Experience Match** (10 points) - Junior/mid/senior level

### Resume Tailoring

For each job, the system:
- Extracts keywords from job description
- Identifies required skills
- Tailors your resume to highlight relevant experience
- Generates customized cover letters

### Weekly Automation

Set up Windows Task Scheduler to run automatically:
- Every Monday at 9 AM (or your schedule)
- Saves results and generates reports
- Prepares resumes for top matches

## 📖 Documentation

- **[QUICK_START.md](QUICK_START.md)** - Get started in 3 steps
- **[USING_NEURO_FILES.md](USING_NEURO_FILES.md)** - How to write Neuro syntax
- **[WEEKLY_SETUP_INSTRUCTIONS.md](WEEKLY_SETUP_INSTRUCTIONS.md)** - Set up automation
- **[RESUME_SETUP.md](RESUME_SETUP.md)** - Configure your resume
- **[JOB_SEARCH_README.md](JOB_SEARCH_README.md)** - Full documentation (this file)

## 💡 Example Usage

### Basic Search

```neuro
pipeline BasicSearch {
    target_roles: ["ai engineer"]
    locations: ["remote"]
    skills: ["python", "pytorch"]
    actions: [search_job_boards()]
}
```

### Full Featured Search

```neuro
pipeline FullSearch {
    goal: "Find junior AI engineering positions"
    target_roles: ["prompt engineer", "ai engineer"]
    locations: ["remote", "US"]
    skills: ["python", "llm", "gpt", "transformers"]
    experience: "junior level"
    company_policy: "remote first"
    actions: [
        search_job_boards(),
        match_skills(),
        generate_applications()
    ]
}
```

## 🔧 View Results

After running a search:

```bash
# View most recent results
python display_results.py

# View specific results file
python display_results.py job_search_results/job_search_20251030_210201.json
```

## 🤖 Automation

### Weekly Schedule

```bash
# Run immediately (test)
python schedule_job_search.py --run-now

# Schedule for every Monday at 9 AM
python schedule_job_search.py --day monday --time 09:00
```

### Windows Task Scheduler (Recommended)

1. Open Task Scheduler
2. Create Basic Task → "Neuro Weekly Job Search"
3. Trigger: Weekly, Monday 9 AM
4. Action: Run `run_weekly_job_search.bat`
5. Done!

See [WEEKLY_SETUP_INSTRUCTIONS.md](WEEKLY_SETUP_INSTRUCTIONS.md) for details.

## 🎨 How It Works

### 1. Intent Declaration (Neuro Syntax)

Write what you want in natural language + simple structure:

```neuro
pipeline FindAIPositions {
    target_roles: ["prompt engineer"]
    skills: ["python", "llm"]
    actions: [search_job_boards(), match_skills()]
}
```

### 2. Neuro Execution

Neuro parses your intent and executes the advanced job search system:

```bash
python run_neuro.py my_job_search.neuro
```

### 3. Results

- Searches all platforms
- Scores jobs against your profile
- Generates reports
- Prepares tailored resumes (if enabled)

## 🔍 Job Scraping

The system uses BeautifulSoup to scrape actual job listings:

- **Indeed** - Scrapes job details, descriptions, dates
- **RemoteOK** - Uses their JSON API
- **Other platforms** - Generates search URLs (they block scraping)

**Note**: Some sites block automated scraping (this is normal). The system gracefully falls back to search URLs.

## 📊 Output

### Results Saved To:

- `job_search_results/job_search_YYYYMMDD_HHMMSS.json` - Full results
- `job_search_reports/weekly_report_YYYYMMDD_HHMMSS.txt` - Human-readable report
- `resume_templates/` - Tailored resumes (if enabled)

### View Results:

```bash
python display_results.py
```

Shows:
- Summary statistics
- Jobs sorted by match score
- Jobs grouped by platform
- Full job details

## 🛠️ Requirements

- Python 3.8+
- `beautifulsoup4` - For web scraping
- `requests` - For HTTP requests
- `schedule` - For weekly automation
- `python-docx` - For Word document support

Install all:
```bash
pip install -r requirements_job_search.txt
```

## 🔒 Privacy

Your personal files are protected:
- `profile_config.json` - Not committed (contains your info)
- `job_search_results/` - Not committed (your search history)
- `resume_templates/` - Not committed (tailored resumes)
- `*.pdf`, `*.docx` - Not committed (your resume files)

See `.gitignore` for full list.

## 🌟 Why This Is Better

### vs Traditional Approach (2020 BeautifulSoup/Selenium):

| Feature | Traditional | Neuro System |
|---------|------------|--------------|
| **Ease of Use** | Requires Python knowledge | Intent-driven (`.neuro` files) |
| **Job Scraping** | ✅ Yes | ✅ Yes |
| **Profile Matching** | ❌ None | ✅ Automatic scoring |
| **Resume Prep** | ❌ Manual | ✅ Automatic tailoring |
| **Automation** | ⚠️ Manual | ✅ Weekly scheduler |
| **Multi-Platform** | ⚠️ Single platform | ✅ 5+ platforms |
| **Intent-Driven** | ❌ Python code | ✅ Neuro syntax |

## 📝 Files Structure

```
Neuro/
├── advanced_job_search.py      # Main job search engine
├── resume_preparer.py           # Resume tailoring
├── schedule_job_search.py      # Weekly automation
├── display_results.py           # Results viewer
├── run_neuro.py                 # Neuro executor
├── my_job_search.neuro          # Your job search intent
├── profile_config.json          # Your profile (not committed)
├── requirements_job_search.txt  # Dependencies
└── Documentation/
    ├── QUICK_START.md
    ├── USING_NEURO_FILES.md
    ├── WEEKLY_SETUP_INSTRUCTIONS.md
    └── ...
```

## 🚀 Next Steps

1. ✅ Configure your profile (`profile_config.json`)
2. ✅ Write your job search intent (`my_job_search.neuro`)
3. ✅ Run your first search: `python run_neuro.py my_job_search.neuro`
4. ✅ Set up weekly automation (Windows Task Scheduler)
5. ✅ Apply to top matches!

## 🤝 Contributing

This is part of the Neuro programming language project. Contributions welcome!

## 📄 License

Same license as Neuro project (MIT).

## 🎯 Philosophy

This demonstrates Neuro's core principle: **Intent-Driven Programming**

Instead of writing:
```python
# 200 lines of Python code...
jobs = search_indeed()
jobs += search_remoteok()
for job in jobs:
    score = match_profile(job)
    ...
```

You write:
```neuro
pipeline FindAIPositions {
    target_roles: ["ai engineer"]
    actions: [search_job_boards(), match_skills()]
}
```

**Declare what you want. Neuro figures out how.**

---

**Built with [Neuro](https://github.com/ElaMCB/Neuro) - Making AI development accessible through intent-driven programming.**
