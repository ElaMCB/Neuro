# Installing Neuro Language Extension in Cursor/VS Code

## Quick Setup (Recommended)

To enable autocomplete and snippets for `.neuro` files:

### Step 1: Install vsce (VS Code Extension Manager)
```bash
npm install -g @vscode/vsce
```

### Step 2: Package the extension
```bash
vsce package
```
This creates a `.vsix` file.

### Step 3: Install in Cursor
```bash
code --install-extension neuro-language-0.1.0.vsix
```

Or manually:
1. Open Cursor
2. Press `Ctrl+Shift+P`
3. Type "Install from VSIX"
4. Select the `.vsix` file

## What You Get

Once installed, these snippets will work:
- `pipeline` → Full pipeline template
- `job-search` → Job search pipeline
- `train-model` → ML training pipeline
- `goal` → Goal statement
- `roles` → Target roles
- `skills` → Skills list

## Manual Trigger

Even without the extension, you can trigger snippets with:
- `Ctrl+Space` after typing a keyword
- `Tab` after typing a snippet prefix

