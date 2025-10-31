# Setting Up Weekly Job Search

Your system can automatically run job searches every week!

## Quick Setup

### Option 1: Run Once Per Week (Recommended)

Create a Windows Task Scheduler task to run it weekly:

```bash
# Test it first - run immediately
python schedule_job_search.py --run-now

# If that works, you can set up Windows Task Scheduler
```

### Option 2: Keep Script Running (Continuous)

The scheduler will run continuously and execute weekly:

```bash
# Run every Monday at 9 AM (default)
python schedule_job_search.py

# Custom schedule: Every Friday at 6 PM
python schedule_job_search.py --day friday --time 18:00

# Press Ctrl+C to stop when you're done
```

**Note**: This requires the terminal to stay open.

## Windows Task Scheduler Setup (Best for Weekly Automation)

1. **Open Task Scheduler** (search in Windows Start menu)

2. **Create Basic Task**:
   - Name: "Neuro Weekly Job Search"
   - Description: "Automatically searches for jobs weekly"
   - Trigger: Weekly
   - Day: Monday (or your choice)
   - Time: 9:00 AM (or your choice)

3. **Action**: Start a program
   - Program/script: `python`
   - Arguments: `schedule_job_search.py --run-now`
   - Start in: `C:\Users\elena\Downloads\Neuro-main\Neuro-main`

4. **Conditions**:
   - ✅ Start the task only if the computer is on AC power
   - ✅ Wake the computer to run this task (if you want)

5. **Settings**:
   - ✅ Allow task to be run on demand
   - ✅ Run task as soon as possible after a scheduled start is missed

## What Happens Weekly

Every week, the system will:

1. ✅ Search all platforms (Wellfound, RemoteOK, Indeed, LinkedIn, startup boards)
2. ✅ Score jobs against your profile
3. ✅ Generate detailed reports
4. ✅ Save results to JSON
5. ✅ Prepare tailored resumes for top matches (if enabled)
6. ✅ Email you results (if configured)

## Test It First

Before setting up weekly automation, test it:

```bash
python schedule_job_search.py --run-now
```

This runs the job search immediately to make sure everything works.

## Files Generated Weekly

- `job_search_results/job_search_YYYYMMDD_HHMMSS.json` - Full results
- `job_search_reports/weekly_report_YYYYMMDD_HHMMSS.txt` - Human-readable report
- `resume_templates/` - Tailored resumes (if enabled)

## Troubleshooting

### "ModuleNotFoundError: schedule"
```bash
pip install schedule
```

### Script doesn't run
- Make sure you're in the correct directory
- Check that `profile_config.json` exists
- Verify Python path in Task Scheduler

### Want to change schedule
Just edit the Windows Task Scheduler task, or run with different options:
```bash
python schedule_job_search.py --day tuesday --time 14:00
```

---

**You're all set!** Your job search will now run automatically every week. 🚀

