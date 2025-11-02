# Repository Cleanup Plan

## 🚨 Critical Issues Found

### 1. DUPLICATE DIRECTORY (Biggest Issue)
- **`Neuro-main/`** - Complete duplicate of the entire repo (50+ files)
- **Action:** DELETE immediately
- **Reason:** Accidentally included, probably from GitHub zip download

### 2. Generated Output Files (Should NOT be in Git)
- `ai_ml_results.json` - Generated job search results
- `improved_results.json` - Generated job search results  
- `my_downloaded_results.json` - Generated job search results
- `my_job_search_report.html` - Generated HTML report
- `view_results.html` - Template/output (gitignore says keep it?)
- **Action:** Remove from Git, add to .gitignore
- **Reason:** These are user-specific outputs that change on every run

### 3. Redundant Python Scripts (Confusing)
- `advanced_job_search.py`
- `better_job_search.py`
- `improved_job_search.py`
- **Action:** Keep ONE (probably `improved_job_search.py`), delete others OR move to archive/
- **Reason:** Multiple similar files confuse users about which to use

### 4. Duplicate Language Files
- `neuro.tmLanguage.json` (root)
- `syntaxes/neuro.tmLanguage.json`
- **Action:** Keep only `syntaxes/neuro.tmLanguage.json`, delete root version
- **Reason:** VSCode expects it in syntaxes/ folder

### 5. Too Many Documentation Files
- `JOB_SEARCH_README.md`
- `IMPROVED_SEARCH_README.md`
- Multiple overlapping guides
- **Action:** Consolidate into main README sections or move to docs/
- **Reason:** Users don't know which doc to read

### 6. Personal/Example Files in Root
- `my_job_search.neuro` - Personal example
- `apply_alphaxiv.neuro` - Personal example
- **Action:** Move to examples/ directory
- **Reason:** Keep root clean, examples should be in examples/

## Recommended Structure

```
Neuro/
├── src/                      # Core language implementation
├── examples/                 # ALL .neuro example files
├── docs/                     # Consolidated documentation
├── tests/                    # Test files
├── scripts/                  # Helper scripts (job search, etc.)
├── README.md                 # Main entry point
├── QUICK_START.md           # How to get started
├── CONTRIBUTING.md          # How to contribute
├── LICENSE                  # License
├── install_neuro.ps1        # Installation script
├── neuro                    # Main executable
├── neuro.bat               # Windows launcher
├── package.json            # VSCode extension config
└── .gitignore              # Updated to ignore all generated files
```

## Cleanup Commands

```bash
# 1. Delete duplicate directory
rm -rf Neuro-main/

# 2. Remove generated files from Git
git rm --cached *.json  # Only specific ones
git rm --cached my_job_search_report.html

# 3. Update .gitignore
# Add: *.json (except package.json)
# Add: *_results.json
# Add: Neuro-main/

# 4. Consolidate scripts
mkdir -p scripts/job_search/
mv *job_search*.py scripts/job_search/

# 5. Move examples
mv apply_alphaxiv.neuro examples/
mv my_job_search.neuro examples/

# 6. Consolidate docs
mkdir -p docs/
mv HOW_AI_WORKS.md docs/
mv INTERPRETER_DESIGN.md docs/
# etc.
```

## Benefits After Cleanup

- ✅ 50% smaller repo size
- ✅ Clear structure
- ✅ No confusion about which files to use
- ✅ Professional appearance
- ✅ Easier for contributors to navigate
- ✅ No personal data in Git

