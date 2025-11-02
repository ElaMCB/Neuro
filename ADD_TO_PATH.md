# Adding Neuro to System PATH

## Quick Setup (Windows)

1. **Copy the Neuro directory path:**
   ```
   C:\Users\elena\OneDrive\Documents\GitHub\Neuro
   ```

2. **Add to PATH:**
   - Press `Win + X`, select "System"
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "User variables", find "Path" and click "Edit"
   - Click "New" and paste: `C:\Users\elena\OneDrive\Documents\GitHub\Neuro`
   - Click OK on all dialogs

3. **Restart your terminal**, then you can use:
   ```bash
   neuro my_job_search.neuro
   ```
   
   From any directory!

## OR: One-Time PowerShell Setup
```powershell
$env:Path += ";C:\Users\elena\OneDrive\Documents\GitHub\Neuro"
```

(This lasts only for current session)

