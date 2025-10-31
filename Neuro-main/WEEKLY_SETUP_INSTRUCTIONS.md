# Setting Up Weekly Job Search - Simple Guide

## Easy Setup for Windows

### Method 1: Windows Task Scheduler (Recommended - No script needs to run continuously)

1. **Open Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, press Enter

2. **Create Basic Task**
   - Right-click "Task Scheduler Library" → "Create Basic Task"
   - Name: `Neuro Weekly Job Search`
   - Description: `Automatically searches for jobs every week`

3. **Set Trigger**
   - When: Weekly
   - Day: Monday (or your choice)
   - Time: 9:00 AM (or your choice)
   - Recur every: 1 weeks

4. **Set Action**
   - Action: Start a program
   - Program/script: `python`
   - Add arguments: `run_neuro.py my_job_search.neuro`
   - Start in: `C:\Users\elena\Downloads\Neuro-main\Neuro-main`

5. **Click Finish**

**That's it!** Your job search will run automatically every week.

---

### Method 2: Using the Batch File (Even Easier)

1. **Use the batch file** (`run_weekly_job_search.bat`)

2. **In Task Scheduler**:
   - Program/script: `C:\Users\elena\Downloads\Neuro-main\Neuro-main\run_weekly_job_search.bat`
   - Start in: `C:\Users\elena\Downloads\Neuro-main\Neuro-main`
   - (No arguments needed)

---

### Method 3: Python Schedule Module (If it works on your system)

```bash
# Test first
python schedule_job_search.py --run-now

# If that works, start scheduler
python schedule_job_search.py --day monday --time 09:00

# (Note: This needs to run continuously)
```

---

## What Happens Weekly

Every week, the system will:

1. ✅ Search all platforms (Wellfound, RemoteOK, Indeed, LinkedIn, startup boards)
2. ✅ Score jobs against your profile  
3. ✅ Generate detailed report
4. ✅ Save results to JSON
5. ✅ Prepare tailored resumes for top matches (if enabled)

## Where to Find Results

- **Results**: `job_search_results\job_search_YYYYMMDD_HHMMSS.json`
- **Reports**: `job_search_reports\weekly_report_YYYYMMDD_HHMMSS.txt`
- **Resumes**: `resume_templates\` (if enabled)

## View Results After Weekly Run

```bash
cd C:\Users\elena\Downloads\Neuro-main\Neuro-main
python display_results.py
```

This shows the most recent results.

---

## Quick Test

Before setting up automation, test it works:

```bash
cd C:\Users\elena\Downloads\Neuro-main\Neuro-main
python run_neuro.py my_job_search.neuro
```

If this works, Task Scheduler will work too!

---

## Troubleshooting

### Python not found in Task Scheduler
- Use full path: `C:\Users\elena\AppData\Local\Programs\Python\Python311\python.exe`
- Or use the batch file method

### Wrong directory
- Make sure "Start in" is set to: `C:\Users\elena\Downloads\Neuro-main\Neuro-main`

### Want email notifications
- Can be added later - for now, just check the results files

---

**Recommendation**: Use Method 1 (Task Scheduler) - it's the most reliable and doesn't need any scripts running continuously!

