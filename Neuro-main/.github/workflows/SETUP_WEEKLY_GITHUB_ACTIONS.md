# Setting Up Weekly Job Search in GitHub Actions

Your weekly job search can now run automatically on GitHub every Monday!

## What Was Created

✅ **`.github/workflows/weekly_job_search.yml`**
- Runs every Monday at 9:00 AM UTC
- Can also be triggered manually
- Saves results as artifacts
- Generates summary reports

## Setup Instructions

### 1. Configure Secrets (Optional)

For email in profile config, add to GitHub Secrets:

1. Go to: `Settings` → `Secrets and variables` → `Actions`
2. Click "New repository secret"
3. Add secret:
   - Name: `USER_EMAIL`
   - Value: `elena.mereanu@gmail.com`

### 2. Update Profile Config

The workflow uses a template profile config. You can:

**Option A**: Use secrets for email (recommended)
- Email comes from `USER_EMAIL` secret
- Keeps email private

**Option B**: Hardcode in workflow file
- Less secure but simpler
- Update the `profile_config.json` creation step

### 3. Add Resume Path (Optional)

If you want resume tailoring, you need to:

1. Upload your resume to a private location
2. Or add it as a secret (base64 encoded)
3. Or skip resume tailoring in Actions (jobs will still be found)

## How It Works

### Schedule
- **When**: Every Monday at 9:00 AM UTC
- **What**: Runs `python run_neuro.py my_job_search.neuro`
- **Results**: Saved as GitHub Actions artifacts

### Manual Trigger
You can also trigger it manually:
1. Go to `Actions` tab
2. Select "Weekly Job Search"
3. Click "Run workflow"
4. Click green button

### Artifacts
Results are saved as downloadable artifacts:
- `job_search_results/` - JSON results
- `job_search_reports/` - Text reports
- `resume_templates/` - Tailored resumes (if enabled)

### Retention
- Artifacts kept for 30 days
- Download before they expire

## Benefits of GitHub Actions

✅ **Automatic** - Runs without your computer
✅ **Cloud-based** - No need to keep your PC on
✅ **Reliable** - Runs even if you're busy
✅ **History** - All runs saved as artifacts
✅ **Notifications** - Get GitHub notifications on failures

## Comparison: GitHub Actions vs Windows Task Scheduler

| Feature | GitHub Actions | Windows Task Scheduler |
|---------|----------------|------------------------|
| **Requires PC on** | ❌ No | ✅ Yes |
| **Cloud-based** | ✅ Yes | ❌ No |
| **Access from anywhere** | ✅ Yes | ❌ No |
| **History tracking** | ✅ Yes | ⚠️ Limited |
| **Email notifications** | ✅ Yes | ⚠️ Manual |
| **Free** | ✅ Yes (2000 min/month) | ✅ Yes |

## Customization

### Change Schedule

Edit `.github/workflows/weekly_job_search.yml`:

```yaml
schedule:
  - cron: '0 9 * * 1'  # Monday 9 AM UTC
```

Cron format: `minute hour day month day-of-week`

Examples:
- `0 9 * * 1` - Monday 9 AM
- `0 14 * * 5` - Friday 2 PM
- `0 9 * * *` - Every day 9 AM

### Add Email Notifications

Add step to workflow:

```yaml
- name: Send email notification
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USER }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: Weekly Job Search Results
    to: ${{ secrets.USER_EMAIL }}
    body: |
      Weekly job search completed!
      Download results from GitHub Actions.
```

### Add Resume Tailoring

If you want tailored resumes in Actions:

1. Upload resume to private repo or secret
2. Decode in workflow step
3. Save to workspace
4. Resume preparer will use it

## Troubleshooting

### Workflow doesn't run
- Check Actions tab for errors
- Verify cron syntax
- Check if repository secrets are set

### No results generated
- Check profile_config.json was created
- Verify my_job_search.neuro exists
- Check Actions logs for errors

### Results not visible
- Check artifacts tab in Actions
- Verify files were created
- Check retention period (30 days)

## Security Notes

⚠️ **Important:**
- Don't commit `profile_config.json` with personal info
- Use GitHub Secrets for sensitive data
- Resume files should be private
- Consider using private repository

## Next Steps

1. ✅ Commit the workflow file
2. ✅ Push to GitHub
3. ✅ Wait for Monday (or trigger manually)
4. ✅ Check Actions tab for results
5. ✅ Download artifacts

---

**Your weekly job search will now run automatically in the cloud every Monday!** ☁️🚀

