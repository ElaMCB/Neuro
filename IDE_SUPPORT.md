# Using Neuro in Your IDE

## ✅ **YES! Neuro works in IDEs!**

Currently supported:
- ✅ **VS Code** - Full support
- ✅ **Cursor** - Full support (VS Code-based)
- ✅ **Sublime Text** - Basic support
- ✅ **Any text editor** - Always works!

---

## 🎯 **VS Code / Cursor (Best Experience)**

### **Features Available:**

✅ **Syntax Highlighting**
- Keywords: `pipeline`, `goal`, `data`, etc.
- Strings: Colored differently
- Comments: `//` and `/* */`
- Functions: `search_jobs()`, `filter_remote_first()`

✅ **Auto-Complete Snippets**
- Type `pipeline` → Full pipeline template
- Type `job-search` → Job search template
- Type `train-model` → ML training template
- Type `goal` → Goal statement

✅ **Smart Brackets**
- Auto-close `{}`, `[]`, `()`
- Auto-indent
- Bracket matching

✅ **Code Folding**
- Collapse/expand pipelines
- Organize large files

---

## 🚀 **Setup in VS Code / Cursor**

### **Option 1: Auto-Detection (Easiest)**

**The files are already configured!**

1. Open your Neuro repository in VS Code/Cursor
2. Open any `.neuro` file
3. Syntax highlighting activates automatically!

**Done!** ✓

---

### **Option 2: Install as Extension (Future)**

We can publish Neuro as a VS Code extension:

```bash
# In your repo
npm install -g vsce
vsce package
# Creates: neuro-language-0.1.0.vsix

# Install in VS Code
code --install-extension neuro-language-0.1.0.vsix
```

**Or publish to VS Code Marketplace:**
- Available to everyone
- Automatic updates
- Ratings and reviews

---

## 🎨 **What You Get in VS Code/Cursor:**

### **Syntax Highlighting:**

```neuro
pipeline FindJobs {           ← "pipeline" in purple, "FindJobs" in yellow
    goal: "Find AI jobs"      ← "goal" in blue, string in green
    target_roles: ["ai"]      ← "target_roles" in blue, array in orange
    // This is a comment       ← Gray
}
```

### **Auto-Complete:**

Type `pipe` and press Tab:
```neuro
pipeline Name {
    goal: "What you want to achieve"
    
}
```

Type `job` and press Tab:
```neuro
pipeline FindJobs {
    goal: "Find ai engineer jobs at remote companies"
    target_roles: ["ai engineer", "ml engineer"]
    locations: ["remote", "US"]
    skills: ["python", "pytorch"]
}
```

---

## 🛠️ **Running Neuro from IDE**

### **VS Code Tasks**

Create `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Neuro",
      "type": "shell",
      "command": "py",
      "args": ["-3.11", "neuro", "${file}"],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
```

**Then:**
- Press `Ctrl+Shift+B` to run current `.neuro` file
- Or right-click → "Run Task" → "Run Neuro"

---

### **Cursor Integration**

Cursor (which you're using!) already supports VS Code extensions!

**Your `.neuro` files should have:**
- ✅ Syntax highlighting (configured)
- ✅ File association (configured)
- ✅ Auto-complete snippets (ready)

**Plus Cursor AI features:**
- Ask Cursor: "Explain this Neuro pipeline"
- Ask Cursor: "Convert this to a job search"
- Ask Cursor: "Add error handling"

---

## 📝 **IDE Feature Comparison**

| Feature | VS Code/Cursor | Sublime | Vim | Any Editor |
|---------|----------------|---------|-----|------------|
| Syntax Highlighting | ✅ | ✅ | ⚙️ | ❌ |
| Auto-Complete | ✅ | ⚙️ | ❌ | ❌ |
| Snippets | ✅ | ⚙️ | ❌ | ❌ |
| Run/Execute | ✅ | ✅ | ✅ | ✅ |
| Debugging | ⏳ | ❌ | ❌ | ❌ |
| LSP Support | ⏳ | ⏳ | ⏳ | ❌ |

✅ = Available now  
⚙️ = Manual setup  
⏳ = Planned  
❌ = Not available

---

## 🎓 **Current Setup:**

**You already have:**
1. `.vscode/settings.json` - VS Code configuration ✓
2. `.vscode/extensions.json` - Recommended extensions ✓
3. `syntaxes/neuro.tmLanguage.json` - Syntax grammar ✓
4. `language-configuration.json` - Language features ✓
5. `snippets/neuro.json` - Code snippets ✓

**Just open a `.neuro` file in Cursor/VS Code - it works!**

---

## 🚀 **Try It Now:**

1. **Open** `my_job_search.neuro` in Cursor
2. **See** syntax highlighting
3. **Type** `pipeline` and press Tab
4. **Run** with `Ctrl+Shift+B`

---

## 🌟 **Future IDE Features (Roadmap):**

### **Language Server Protocol (LSP)**
- Real-time error checking
- IntelliSense
- Go to definition
- Refactoring

### **Debugger**
- Breakpoints in `.neuro` files
- Step through execution
- Inspect variables

### **AI-Powered Assistance**
- Cursor AI understands Neuro syntax
- Autocomplete from natural language
- Intent suggestions

---

## 📚 **More IDE Options:**

### **Sublime Text:**
Copy `syntaxes/neuro.tmLanguage.json` to:
```
~/.config/sublime-text/Packages/User/Neuro.tmLanguage.json
```

### **Vim:**
Create `~/.vim/syntax/neuro.vim`:
```vim
syn keyword neuroKeyword pipeline goal data model
syn region neuroString start='"' end='"'
syn match neuroComment '//.*$'
```

### **JetBrains (IntelliJ/PyCharm):**
File → Settings → Editor → File Types → Add `*.neuro`

---

## 🎯 **Summary:**

**YES! You can use Neuro in IDEs!**

**Working now in VS Code/Cursor:**
- Syntax highlighting ✓
- Snippets ✓
- Auto-complete ✓
- Run tasks ✓

**Your Cursor IDE should recognize `.neuro` files immediately!**

---

**Want me to commit these IDE configuration files?** 🚀

