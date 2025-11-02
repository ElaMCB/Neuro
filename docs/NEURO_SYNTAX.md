# Neuro Syntax - Simple & Precise

## 📐 The Core Principle

**Neuro has ONE concept: The Pipeline**

```neuro
pipeline WhatYouWant {
    goal: "What you want to achieve"
    // How you want it done
}
```

That's it. Everything in Neuro is a pipeline.

---

## 🎯 Syntax in 3 Lines

```neuro
pipeline Name {                    // 1. Declare what you're building
    goal: "Your objective"         // 2. State your goal
    parameters: values             // 3. Provide specifics
}
```

**Example:**
```neuro
pipeline FindAIJobs {
    goal: "Find AI engineer jobs at remote companies"
    target_roles: ["ai engineer", "ml engineer"]
    locations: ["remote", "US"]
}
```

**Run it:**
```bash
neuro my_task.neuro
```

**Result:** Jobs found, report generated, done.

---

## 🏗️ Architecture in One Diagram

```
┌─────────────┐
│  .neuro     │  ← You write in natural language + structure
│   file      │
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ Interpreter │  ← Understands your intent
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ AI Engine   │  ← Figures out how to do it
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  Results    │  ← Immediate execution, no compilation
└─────────────┘
```

---

## 📝 Complete Syntax Reference

### **1. Pipeline Declaration**
```neuro
pipeline PipelineName {
    // Everything goes here
}
```

### **2. Goal (Required)**
```neuro
goal: "What you want to achieve"
```

### **3. Parameters (Optional)**

#### **Strings:**
```neuro
name: "value"
```

#### **Arrays:**
```neuro
items: ["item1", "item2", "item3"]
```

#### **Objects:**
```neuro
config: {
    key1: value1,
    key2: value2
}
```

#### **Actions:**
```neuro
actions: [
    action1(),
    action2(),
    action3()
]
```

### **4. Comments**
```neuro
// This is a comment
/* This is a 
   multi-line comment */
```

---

## 🎨 The Three Pipeline Types

### **Type 1: Search Pipeline**
```neuro
pipeline FindThings {
    goal: "Find something"
    target: "what to find"
    filters: ["filter1", "filter2"]
}
```

**Example:**
```neuro
pipeline FindJobs {
    goal: "Find AI engineering jobs"
    target_roles: ["ai engineer"]
    locations: ["remote"]
}
```

### **Type 2: Transform Pipeline**
```neuro
pipeline TransformData {
    goal: "Change something"
    input: "source"
    output: "destination"
    operations: [transform1(), transform2()]
}
```

**Example:**
```neuro
pipeline OptimizeResume {
    goal: "Tailor resume for AI roles"
    input: "my_resume.txt"
    optimize_for: ["keywords", "ATS"]
}
```

### **Type 3: Build Pipeline**
```neuro
pipeline BuildModel {
    goal: "Create something"
    data: "data source"
    constraints: {accuracy: >95%}
}
```

**Example:**
```neuro
pipeline TrainClassifier {
    goal: "Predict customer churn"
    data: "customers.csv"
    constraints: {accuracy: >90%, latency: <100ms}
}
```

---

## 💡 Simplicity Rules

### **Rule 1: Goal First**
Always start with what you want:
```neuro
goal: "What you want"  // Clear and specific
```

### **Rule 2: Parameters Are Self-Explanatory**
```neuro
target_roles: ["ai engineer"]     // Clear what it does
locations: ["remote", "US"]        // Clear what it filters
skills: ["python", "pytorch"]      // Clear what it matches
```

### **Rule 3: Natural Language Accepted**
```neuro
goal: "Find me a remote AI job at a startup in Boston"
// Neuro understands this!
```

---

## 🔄 How It Works (Simple)

### **Step 1: You Write Intent**
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
}
```

### **Step 2: Interpreter Parses**
```
Intent detected: job_search
Goal: "Find AI jobs"
Parameters: (inferred from context)
```

### **Step 3: AI Executes**
```
→ Searching RemoteOK...
→ Filtering for AI roles...
→ Found 8 jobs
→ Generating report...
```

### **Step 4: Results Delivered**
```
✓ 8 AI jobs found
✓ Report: my_job_search_report.html
✓ Opened in browser
```

---

## 📊 Complexity Hidden, Simplicity Exposed

### **What You Write:**
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
    locations: ["remote"]
}
```
**5 lines**

### **What Neuro Does:**
- Connects to 5+ job boards
- Parses 100+ job listings
- Filters by AI/ML keywords
- Scores matches by relevance
- Removes duplicates
- Generates HTML report
- Opens in browser

**~500 lines of Python you didn't write**

---

## 🎯 Mental Model

Think of Neuro as **giving instructions to a smart assistant:**

**Traditional Code:**
```python
# You tell the computer HOW to do each step
import requests
response = requests.get(url)
data = response.json()
filtered = [x for x in data if 'ai' in x['title']]
# ... 200 more lines
```

**Neuro:**
```neuro
// You tell Neuro WHAT you want
pipeline FindJobs {
    goal: "Find AI jobs"
}
```

**The assistant figures out the HOW.**

---

## 📖 Complete Example with All Features

```neuro
pipeline ComprehensiveJobSearch {
    // The goal - what you want to achieve
    goal: "Find AI engineer positions at remote-first startups"
    
    // Target roles - what positions you're looking for
    target_roles: [
        "ai engineer",
        "ml engineer", 
        "prompt engineer"
    ]
    
    // Locations - where you want to work
    locations: ["remote", "US", "Boston", "New York"]
    
    // Skills - what you know
    skills: [
        "python",
        "pytorch",
        "llm",
        "gpt",
        "transformers"
    ]
    
    // Experience level
    experience: "junior to mid level"
    
    // Company preference
    company_policy: "remote first"
    
    // Actions to perform
    actions: [
        search_job_boards(),
        filter_remote_first(),
        match_skills(),
        generate_applications(),
        track_responses()
    ]
    
    // Success metrics
    targets: {
        applications_per_week: 10,
        interviews_target: 5,
        response_rate: >20%
    }
    
    // Output preferences
    output: {
        format: "html",
        email_results: true,
        frequency: "weekly"
    }
}
```

**Run:**
```bash
neuro comprehensive.neuro
```

**Gets:**
- Job search results
- Tailored applications
- HTML report
- Email notification
- Progress tracking

---

## 🧩 Composition (Advanced)

**Pipelines can reference other pipelines:**

```neuro
pipeline PrepareApplication {
    goal: "Create job application package"
    resume: "my_resume.txt"
    job_url: $input
}

pipeline JobSearchWithApplications {
    goal: "Find jobs and prepare applications"
    
    // Find jobs
    search_jobs()
    
    // For each result
    for_each_result: {
        // Prepare application
        run_pipeline(PrepareApplication, job_url)
    }
}
```

---

## 🎓 Learning Neuro (5 Minutes)

### **Minute 1:** Understand the concept
```
One concept: Pipeline
One required field: goal
Everything else: parameters
```

### **Minute 2:** Write your first pipeline
```neuro
pipeline Hello {
    goal: "Say hello"
}
```

### **Minute 3:** Add parameters
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
    locations: ["remote"]
}
```

### **Minute 4:** Run it
```bash
neuro my_task.neuro
```

### **Minute 5:** See results
```
✓ Found 8 jobs
✓ Report generated
✓ Done!
```

**You've learned Neuro!**

---

## 🔑 Key Insights

### **1. Declarative, Not Imperative**
```neuro
// Don't say HOW
for job in jobs:
    if "ai" in job.title:
        results.append(job)

// Say WHAT
target_roles: ["ai engineer"]
```

### **2. Intent-Driven**
```neuro
// Your intent
goal: "Find remote AI jobs"

// Neuro infers
→ Need to search job boards
→ Need to filter for remote
→ Need to filter for AI
→ Need to generate report
```

### **3. Natural + Structured**
```neuro
// Natural language goal
goal: "Find me a great AI job"

// Structured parameters
target_roles: ["ai engineer"]
```

Best of both worlds.

---

## 📏 Syntax Rules (Simple)

1. **Everything is a pipeline**
2. **Every pipeline has a goal**
3. **Parameters are `key: value`**
4. **Arrays use `[item1, item2]`**
5. **Objects use `{key: value}`**
6. **Strings use `"quotes"`**
7. **Comments use `//` or `/* */`**
8. **Actions end with `()`**

**That's the entire syntax!**

---

## 🎯 Design Philosophy

### **Principle 1: Minimize Syntax**
Only essential syntax. No `{}` unless grouping, no `;`, no complex rules.

### **Principle 2: Maximize Clarity**
```neuro
target_roles: ["ai engineer"]  // Clear!
```
Better than:
```
roles = ["ai engineer"]        // Less clear
r: ["ai engineer"]             // Unclear!
```

### **Principle 3: Intent Over Implementation**
```neuro
goal: "Find jobs"              // What you want
// Not how to do it
```

### **Principle 4: Smart Defaults**
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
    // Neuro infers:
    // - Search common job boards
    // - Filter for AI keywords
    // - Generate standard report
}
```

---

## 🌟 The Promise

### **You Write:**
```neuro
pipeline FindJobs {
    goal: "Find AI jobs"
}
```

### **Neuro Delivers:**
- ✓ Multi-platform search
- ✓ Smart filtering
- ✓ Beautiful reports
- ✓ Email notifications
- ✓ Automated weekly runs

### **You Saved:**
- ✗ 500+ lines of code
- ✗ Hours of debugging
- ✗ Managing dependencies
- ✗ Writing documentation

---

## 📚 Summary

**Neuro in one sentence:**
> "Write what you want in structured natural language, Neuro figures out how to do it."

**Syntax in one line:**
> `pipeline Name { goal: "What" }`

**Architecture in one line:**
> `Intent → Interpreter → AI → Results`

**Learning curve:**
> 5 minutes to first result

**Power:**
> Production-ready applications from 5 lines of code

---

**That's Neuro. Simple to write. Powerful to use.** 🚀

