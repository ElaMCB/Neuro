# Setting Up Your Resume

The system now supports Word documents (`.docx`), text files (`.txt`), and Markdown (`.md`).

## How to Update Your Resume Path

### Option 1: Edit `profile_config.json` directly

Open `profile_config.json` and update the `resume_path` field:

**For a Word document (.docx):**
```json
{
  "resume_path": "C:\\Users\\elena\\Downloads\\Elena Mereanu Resume.docx"
}
```

**For a text file (.txt):**
```json
{
  "resume_path": "C:\\Users\\elena\\Downloads\\resume.txt"
}
```

**For a file in the project folder:**
```json
{
  "resume_path": "my_resume.docx"
}
```

### Option 2: Windows Path Format

**Important**: In Windows paths, use double backslashes (`\\`) or forward slashes (`/`):

✅ **Correct:**
```json
"resume_path": "C:\\Users\\elena\\Documents\\Resume.docx"
"resume_path": "C:/Users/elena/Documents/Resume.docx"
```

❌ **Wrong:**
```json
"resume_path": "C:\Users\elena\Documents\Resume.docx"  // Single backslash won't work
```

## Current Setup

Your current resume path is set to:
```json
"resume_path": "C:\\Users\\elena\\Downloads\\Elena Mereanu PromptAI.pdf"
```

**To change to a Word document**, simply update this to point to your `.docx` file:

```json
"resume_path": "C:\\Users\\elena\\Downloads\\Elena Mereanu Resume.docx"
```

## Installing Word Document Support

If you want to use a Word document (`.docx`), install the required library:

```bash
pip install python-docx
```

Or install all requirements:
```bash
pip install -r requirements_job_search.txt
```

## Supported Formats

| Format | Extension | Support | Notes |
|--------|-----------|---------|-------|
| Word Document | `.docx` | ✅ Full | Requires `python-docx` |
| Text File | `.txt` | ✅ Full | Best for keyword matching |
| Markdown | `.md` | ✅ Full | Text-based format |
| PDF | `.pdf` | ⚠️ Limited | May need additional setup |

## How It Works

1. **The system reads your resume** from the path you specify
2. **Extracts text content** (from paragraphs and tables if Word doc)
3. **Uses it as a base** for tailoring resumes to specific jobs
4. **Generates customized versions** for each job application

## Tips

- **Use Word (.docx)** for formatted resumes - the system will extract all text
- **Use text files (.txt)** for best keyword matching
- **Keep your resume updated** in the file - the system uses it as a template
- **Place in project folder** for easier relative paths: `"resume_path": "my_resume.docx"`

## Testing Your Resume Setup

After updating the path, test it:

```bash
python run_advanced_job_search.py
```

The system will try to load your resume when preparing applications. If there's an error, check:
1. The file path is correct
2. The file exists at that location
3. You have `python-docx` installed (for .docx files)

---

**Quick Change**: Just edit `profile_config.json` and change the `resume_path` to your Word document path!

