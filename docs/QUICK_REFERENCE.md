# Neuro Quick Reference

## 🎯 One Concept

```
┌──────────────────────────────────────┐
│         THE PIPELINE                 │
│  Everything in Neuro is a pipeline   │
└──────────────────────────────────────┘
```

---

## ⚡ Minimum Viable Pipeline

```neuro
pipeline Name {
    goal: "What you want"
}
```

**That's it. Run with:** `neuro file.neuro`

---

## 📋 Complete Syntax (Fits on One Page)

### **Structure**
```neuro
pipeline PipelineName {
    goal: "required - your objective"
    
    // Parameters (all optional)
    parameter: "value"
    list: ["item1", "item2"]
    object: {key1: val1, key2: val2}
    actions: [action1(), action2()]
}
```

### **Comments**
```neuro
// Single line
/* Multi
   line */
```

### **Data Types**
```neuro
string: "text"
number: 42
boolean: true
array: [1, 2, 3]
object: {key: value}
```

---

## 🎨 The Three Patterns

### **1. FIND** (Search Pattern)
```neuro
pipeline FindX {
    goal: "Find something"
    target: "what"
    filters: ["criterion1", "criterion2"]
}
```

### **2. TRANSFORM** (Change Pattern)
```neuro
pipeline TransformX {
    goal: "Change something"
    input: "source"
    output: "destination"
}
```

### **3. BUILD** (Create Pattern)
```neuro
pipeline BuildX {
    goal: "Create something"
    data: "source"
    constraints: {quality: >90%}
}
```

---

## 🏗️ Architecture

```
INPUT        PROCESSING           OUTPUT
━━━━━        ━━━━━━━━━━           ━━━━━━

.neuro   →   Interpreter   →   Execution
file          (parses)          (runs)
                ↓
             AI Engine
            (figures out
              the how)
```

**No compilation. Instant execution.**

---

## 💡 Design Principles

```
1. Intent over Implementation
   ├─ Say WHAT, not HOW
   └─ Neuro figures out the steps

2. Natural + Structured
   ├─ Natural language goals
   └─ Structured parameters

3. Smart Defaults
   ├─ Minimal input required
   └─ Maximum functionality delivered

4. Immediate Results
   ├─ No compilation
   └─ Direct execution
```

---

## 📊 Comparison

### **Traditional:**
```python
# 200 lines
import requests, json
response = requests.get(...)
data = parse(response)
filtered = filter(data)
# ... 195 more lines
```

### **Neuro:**
```neuro
# 5 lines
pipeline FindJobs {
    goal: "Find AI jobs"
    locations: ["remote"]
}
```

**Same result. 97.5% less code.**

---

## 🎯 Mental Model

```
Neuro = Smart Assistant

You:     "Find AI jobs in Boston"
Neuro:   ✓ Searches 5 job boards
         ✓ Filters for AI roles
         ✓ Filters for Boston
         ✓ Generates report
         ✓ Opens in browser
```

You say WHAT. Neuro does HOW.

---

## ⚡ Quick Start

### **1. Write** (30 seconds)
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
}
```

### **2. Run** (1 command)
```bash
neuro my_task.neuro
```

### **3. Results** (instant)
```
✓ Found 8 jobs
✓ Report: jobs.html
✓ Done!
```

**Total time: < 1 minute**

---

## 🔑 Key Syntax Elements

| Element | Syntax | Example |
|---------|--------|---------|
| **Pipeline** | `pipeline Name { }` | `pipeline FindJobs { }` |
| **Goal** | `goal: "text"` | `goal: "Find AI jobs"` |
| **String** | `"text"` | `name: "Elena"` |
| **Array** | `[a, b, c]` | `roles: ["ai", "ml"]` |
| **Object** | `{k: v}` | `config: {min: 5}` |
| **Action** | `name()` | `search_jobs()` |
| **Comment** | `// text` | `// This finds jobs` |

---

## 🎓 Learn in 3 Examples

### **Example 1: Basic**
```neuro
pipeline Hello {
    goal: "Find jobs"
}
```

### **Example 2: With Parameters**
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
    locations: ["remote"]
    roles: ["ai engineer"]
}
```

### **Example 3: Complete**
```neuro
pipeline CompleteSearch {
    goal: "Find AI jobs at startups"
    target_roles: ["ai engineer", "ml engineer"]
    locations: ["remote", "US"]
    skills: ["python", "pytorch"]
    experience: "junior"
    actions: [
        search_job_boards(),
        filter_remote_first(),
        generate_applications()
    ]
}
```

**That's the full language!**

---

## 📐 Syntax Diagram

```
pipeline
   ↓
Name ──────→ Required
   ↓
{  ──────────→ Start block
   ↓
goal: "..." ─→ Required: What you want
   ↓
key: value ──→ Optional: Parameters
   ↓
}  ──────────→ End block
```

---

## 🌟 The Formula

```
┌─────────────────────────────────────┐
│  Neuro = Natural Language           │
│          + Simple Structure         │
│          + AI Intelligence          │
│          = Instant Results          │
└─────────────────────────────────────┘
```

---

## 💬 Common Patterns

### **Job Search**
```neuro
goal: "Find [role] jobs at [type] companies in [location]"
target_roles: ["role1", "role2"]
locations: ["loc1", "loc2"]
```

### **Data Processing**
```neuro
goal: "Process [data] to produce [result]"
input: "data source"
operations: [step1(), step2()]
```

### **Model Training**
```neuro
goal: "Train model to [task]"
data: "dataset.csv"
constraints: {accuracy: >90%}
```

---

## 🚀 Power Features

### **Smart Inference**
```neuro
goal: "Find AI jobs"
// Neuro automatically:
// - Determines you want job_search
// - Searches multiple platforms
// - Filters for AI keywords
// - Generates HTML report
```

### **Natural Language**
```neuro
goal: "Find me a remote AI engineer position at a startup"
// Neuro parses:
// - Role: AI engineer
// - Location: remote
// - Company type: startup
```

### **Zero Configuration**
```neuro
pipeline FindJobs {
    goal: "Find jobs"
}
// No setup, no dependencies, just works
```

---

## 📖 Cheat Sheet

```neuro
// Template for any task
pipeline TaskName {
    // Required
    goal: "Clear objective"
    
    // Common parameters
    input: "source"
    output: "destination"
    filters: ["filter1", "filter2"]
    actions: [action1(), action2()]
    constraints: {key: value}
    
    // Job search specific
    target_roles: ["role1", "role2"]
    locations: ["loc1", "loc2"]
    skills: ["skill1", "skill2"]
}
```

---

## 🎯 Remember

1. **One concept**: Pipeline
2. **One requirement**: goal
3. **One command**: `neuro file.neuro`
4. **One minute**: To first result

**Neuro: Complexity hidden. Simplicity exposed.** ⚡

---

## 📚 More Info

- Full Syntax: `NEURO_SYNTAX.md`
- Interpreter Design: `INTERPRETER_DESIGN.md`
- Examples: `examples/`
- Run: `neuro --help`

