# Email Setup for Weekly Job Search

The weekly job search workflow can now send results directly to your email. Here's how to set it up:

## Required GitHub Secrets

To enable email notifications, you need to add the following secrets to your GitHub repository:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:

### `SENDER_EMAIL`
Your Gmail address (e.g., `yourname@gmail.com`)

### `SENDER_PASSWORD`
Your Gmail App Password (NOT your regular password)

### `RECIPIENT_EMAIL` (Optional)
The email address to receive notifications. If not set, defaults to `elena.mereanu@gmail.com`

## How to Get Gmail App Password

1. Go to your Google Account settings: https://myaccount.google.com/
2. Navigate to **Security**
3. Enable **2-Step Verification** if not already enabled
4. Under **2-Step Verification**, click **App passwords**
5. Select **Mail** and **Other (Custom name)** → enter "GitHub Actions"
6. Click **Generate**
7. Copy the 16-character password (this is your App Password)
8. Use this password (not your regular Gmail password) as `SENDER_PASSWORD`

## Alternative: Custom SMTP Server

If you want to use a different email provider, you can modify `send_job_search_email.py`:

```python
send_job_search_email(
    smtp_server="smtp.your-provider.com",
    smtp_port=587,  # or 465 for SSL
    # ... other parameters
)
```

## Testing

After adding the secrets, you can:
1. Manually trigger the workflow: **Actions** → **Weekly Job Search** → **Run workflow**
2. Check the workflow logs to see if email was sent successfully
3. If email fails, check that:
   - All secrets are correctly set
   - Gmail App Password is used (not regular password)
   - 2-Step Verification is enabled on Gmail

## Email Content

The email will include:
- Summary of job search results
- Top matching jobs with links
- Attachments: Results JSON and report files (if available)

## Security Note

Never commit email credentials to the repository. Always use GitHub Secrets for sensitive information.

