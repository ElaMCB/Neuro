# Using Neuro Files for Job Search

Now you can write your job search intent in **Neuro syntax** (`.neuro` files) and it will automatically execute the advanced job search system!

## How It Works

1. **Write your intent** in a `.neuro` file using Neuro syntax
2. **Run the Neuro file** - `python run_neuro.py my_job_search.neuro`
3. **Neuro executes** the advanced job search system automatically!

## Example: Your `my_job_search.neuro` File

```neuro
// My AI Job Search Assistant
pipeline FindAIPositions {
    goal: "Find prompt engineer and AI engineer jobs with remote-first companies in US"
    
    // Your specific requirements
    target_roles: ["prompt engineer", "ai engineer", "ml engineer"]
    locations: ["remote", "US", "Boston", "New York"]
    company_policy: "remote first"
    skills: ["python", "pytorch", "llm", "gpt", "transformers"]
    experience: "junior level"
    
    // What you want Neuro to do
    actions: [
        search_job_boards(),
        filter_remote_first(),
        match_skills(),
        generate_applications(),
        track_responses()
    ]
    
    // Success metrics
    targets: {
        applications_per_week: 10,
        companies_researched: 50,
        interviews_target: 5
    }
}
```

## Running Your Neuro File

```bash
python run_neuro.py my_job_search.neuro
```

This will:
- ✅ Parse your Neuro syntax
- ✅ Build your profile from the Neuro file
- ✅ Search all platforms (Wellfound, RemoteOK, Indeed, LinkedIn, startup boards)
- ✅ Score jobs against your profile
- ✅ Generate a detailed report
- ✅ Optionally prepare tailored resumes (if `generate_applications()` is in actions)
- ✅ Save all results

## What Happens

When you run a `.neuro` file:

1. **Neuro parses** your intent from the file
2. **Extracts parameters**:
   - `target_roles` → Your desired job titles
   - `locations` → Where you want to work
   - `skills` → Your technical skills
   - `experience` → Your experience level
   - `company_policy` → Company preferences (e.g., "remote first")
   - `actions` → What to do (search, match, generate applications, etc.)

3. **Combines with profile config** (`profile_config.json`) for:
   - Your name, email
   - Resume path
   - GitHub, LinkedIn URLs

4. **Executes the advanced job search** system

5. **Returns results** and saves everything

## Neuro Syntax Explained

### Pipeline Declaration
```neuro
pipeline FindAIPositions {
    // Your settings here
}
```

### Available Fields

- `goal:` - Your overall objective (optional)
- `target_roles:` - Array of job titles: `["prompt engineer", "ai engineer"]`
- `locations:` - Where to search: `["remote", "US", "Boston"]`
- `skills:` - Your technical skills: `["python", "pytorch", "llm"]`
- `experience:` - Your level: `"junior level"`, `"mid level"`, `"senior level"`
- `company_policy:` - Company preference: `"remote first"`, `"flexible"`, etc.
- `actions:` - What to do:
  - `search_job_boards()` - Search all platforms
  - `filter_remote_first()` - Filter for remote-first companies
  - `match_skills()` - Match jobs against your skills
  - `generate_applications()` - Prepare tailored resumes for top matches
  - `track_responses()` - Track applications (future feature)

## Integration with Profile Config

Your `profile_config.json` provides:
- Personal info (name, email)
- Resume file path
- GitHub/LinkedIn URLs
- Default settings

The Neuro file **overrides** these with specific search parameters:
- `target_roles` from Neuro → Used for search
- `skills` from Neuro → Used for matching
- `experience` from Neuro → Used for filtering

## Examples

### Basic Search
```neuro
pipeline BasicSearch {
    target_roles: ["ai engineer"]
    locations: ["remote"]
    skills: ["python", "pytorch"]
    actions: [search_job_boards()]
}
```

### Full Featured Search with Resume Prep
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

## Output

When you run a Neuro file, you get:

1. **Console output**: Real-time search progress and results
2. **JSON results**: `job_search_results/job_search_YYYYMMDD_HHMMSS.json`
3. **Text report**: `job_search_reports/weekly_report_YYYYMMDD_HHMMSS.txt`
4. **Tailored resumes** (if `generate_applications()` in actions):
   - `resume_templates/resume_company_title_YYYYMMDD.txt`
   - `resume_templates/cover_company_title_YYYYMMDD.txt`

## Benefits of Neuro Syntax

✅ **Intent-based**: Describe what you want, not how to do it
✅ **Readable**: Human-readable syntax
✅ **Reusable**: Edit the file and run again
✅ **Declarative**: Declare your requirements, Neuro figures out the rest

## Next Steps

1. Edit `my_job_search.neuro` with your preferences
2. Ensure `profile_config.json` has your resume path
3. Install dependencies: `pip install -r requirements_job_search.txt`
4. Run: `python run_neuro.py my_job_search.neuro`
5. Review results and apply to top matches!

---

**That's the power of Neuro - write intent, get results! 🚀**

