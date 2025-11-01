# Enable AI Features in Neuro

## 🧠 Turn On AI-Powered Parsing

Neuro can use **DeepSeek**, **OpenAI GPT-4**, or other LLMs to understand natural language goals.

**🌟 Recommended: DeepSeek** (200x cheaper than OpenAI!) → [DeepSeek Setup](DEEPSEEK_SETUP.md)

Here's how to enable it:

---

## 🚀 Quick Setup

### **Option 1: DeepSeek (Recommended - Cheapest!)**

```bash
# 1. Install package
pip install openai

# 2. Get API key from https://platform.deepseek.com

# 3. Set environment variable
# Windows:
set DEEPSEEK_API_KEY=sk-your-key-here

# Mac/Linux:
export DEEPSEEK_API_KEY=sk-your-key-here

# 4. Run Neuro
python neuro my_task.neuro
```

**Cost:** ~$0.0001 per run (200x cheaper than GPT-4!)

**→ [Complete DeepSeek Guide](DEEPSEEK_SETUP.md)**

---

### **Option 2: OpenAI (Alternative)**

```bash
# 1. Install package
pip install openai

# 2. Get API key from https://platform.openai.com

# 3. Set environment variable
# Windows:
set OPENAI_API_KEY=sk-your-key-here

# Mac/Linux:
export OPENAI_API_KEY=sk-your-key-here

# 4. Run Neuro
python neuro my_task.neuro
```

**Cost:** ~$0.02 per run

---

### **Option 3: No AI (Free)**

Works without any API key! Uses pattern matching.

```bash
python neuro my_task.neuro
```

**Cost:** $0.00

---

**Now AI is enabled!** 🎉

---

## 🎯 What AI Enables

### **Before (Without AI):**

```neuro
// Must use exact syntax
pipeline FindJobs {
    goal: "Find jobs"
    target_roles: ["ai engineer"]
    locations: ["remote"]
}
```

### **After (With AI):**

```neuro
// Natural language works!
goal: "yo find me some sweet remote ai gigs in boston"
```

**AI Understands:**
- "yo" = greeting (ignore)
- "find me" = search action
- "sweet" = high-quality (filter for good matches)
- "remote ai gigs" = remote AI engineer positions
- "boston" = location filter

---

## 🔬 How It Works

### **Step 1: You Write Natural Language**
```neuro
goal: "I want to transition from QA to AI engineering"
```

### **Step 2: AI Parses Intent**
```python
# Neuro sends to GPT-4
"Parse this goal: 'I want to transition from QA to AI engineering'"

# GPT-4 returns
{
    "intent_type": "job_search",
    "target_role": "ai engineer",
    "experience_level": "entry-level",
    "inferred_needs": [
        "resume_optimization",
        "skill_gap_analysis",
        "transitioning_advice"
    ]
}
```

### **Step 3: Neuro Executes**
```python
# Searches for entry-level AI jobs
# Generates QA→AI transition resume
# Provides learning resources
# Creates action plan
```

---

## 💡 AI Features Available

### **1. Natural Language Goals**

**Without AI:**
```neuro
goal: "Search job boards for AI engineer positions in remote locations"
```

**With AI:**
```neuro
goal: "find me a dope ai job"
// AI understands informal language!
```

### **2. Intent Inference**

**You Say:**
```neuro
goal: "I'm a QA engineer wanting to switch to AI"
```

**AI Infers:**
- Need: job search
- Level: entry/junior AI roles
- Additional: resume help, skill assessment

### **3. Smart Clarification**

**Ambiguous:**
```neuro
goal: "Train a model"
```

**AI Asks:**
```
I need clarification:
1. What type of model? (classification/regression/LLM)
2. What's your data source?
3. What's your target metric?
```

### **4. Code Generation**

**You Write:**
```neuro
pipeline SentimentAnalysis {
    goal: "Analyze customer sentiment"
    data: "reviews.csv"
}
```

**AI Generates:**
```python
# Automatically generates:
# - Data loading code
# - Sentiment analysis using transformers
# - Result visualization
# - Export to CSV
# ~100 lines of production code
```

---

## 🎓 Example: Job Search with AI

### **Natural Language Input**

```neuro
"yo i built this dope ai language called neuro and i want a remote ai job at a startup, 
preferably doing prompt engineering or working with llms, im in boston but open to anywhere"
```

### **What AI Extracts**

```json
{
  "intent_type": "job_search",
  "target_roles": ["prompt engineer", "ai engineer", "llm engineer"],
  "locations": ["remote", "boston"],
  "company_type": "startup",
  "skills": ["neuro", "ai", "llm", "prompt engineering"],
  "experience_level": "mid",
  "remote_preference": true,
  "highlights": ["built ai language (Neuro)"]
}
```

### **What Neuro Does**

```python
# Searches job boards with extracted criteria
# Prioritizes:
# - Startups
# - LLM/Prompt Engineering roles
# - Remote positions
# - Highlights your Neuro project in applications
```

---

## 🔧 Technical Details

### **AI Models Used**

**For Parsing:**
- GPT-4 (best understanding)
- Claude 3 (alternative)
- Local LLM (for privacy)

**For Code Generation:**
- GPT-4 (best code quality)
- Claude 3 Opus (excellent at code)
- CodeLlama (free, local option)

**For Optimization:**
- Local models (fast, free)
- Codegen-2B
- StarCoder

### **API Costs**

**Typical usage:**
- Parse intent: ~$0.001 per run
- Generate code: ~$0.01 per run
- Total: < $0.10 per day for heavy usage

**With caching:**
- First run: Uses API
- Subsequent runs: Uses cache
- Cost: ~$0.01 per day

---

## 🎯 Enabling AI Step-by-Step

### **Minimal Setup (Free Tier)**

```bash
# 1. Get OpenAI API key
# Visit: https://platform.openai.com/api-keys

# 2. Set environment variable
export OPENAI_API_KEY=sk-...

# 3. Run Neuro
python neuro my_task.neuro

# AI is now active! 
```

### **Alternative: Use Claude**

```bash
# Install Anthropic
pip install anthropic

# Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# Modify ai_powered_parser.py to use Claude
```

### **Alternative: Use Local LLM (Free)**

```bash
# Install Ollama
# Download: https://ollama.ai

# Run local model
ollama run llama2

# Point Neuro to local endpoint
export OPENAI_BASE_URL=http://localhost:11434
```

---

## 🌟 The Vision

**Today:**
```neuro
// Structured syntax required
pipeline FindJobs {
    goal: "Find AI jobs"
    target_roles: ["ai engineer"]
}
```

**With AI Enabled:**
```neuro
// Pure natural language
"find me a job"
```

**With Full AI (Future):**
```neuro
// Conversation
"I need a job"

Neuro: What kind of work are you looking for?
You: AI stuff
Neuro: ✓ Searching for AI engineering positions...
      Found 10 jobs. Want me to apply to the top ones?
You: yeah
Neuro: ✓ Applications sent to 3 companies
```

---

## 📊 Current vs Full AI

| Feature | Current (v0.1) | With AI Parser | Full AI (Future) |
|---------|---------------|----------------|------------------|
| **Input** | Structured | Natural language | Conversation |
| **Understanding** | Regex | LLM parsing | Full comprehension |
| **Execution** | Pre-built modules | AI-planned | Generated code |
| **Learning** | None | Pattern learning | Full adaptation |
| **Interaction** | One-shot | Clarification | Multi-turn dialog |

---

## 🎓 Summary

**How Neuro Uses AI:**

**Now (v0.1):**
- AI-inspired design (intent-driven)
- Rule-based execution
- Pattern matching

**With API Key (Immediate):**
- AI-powered natural language parsing ✓
- Intent inference ✓
- Smart clarifications ✓

**Future (Full Integration):**
- Code generation
- Learning system
- Conversational interface
- Automatic optimization

**To Enable:** Just add OpenAI API key and run!

---

## 🚀 Next Steps

1. **Get API Key:** https://platform.openai.com
2. **Set Environment Variable:** `OPENAI_API_KEY`
3. **Run:** `python neuro my_task.neuro`
4. **Use Natural Language:** Write goals however you want!

**AI integration is optional but powerful when enabled.**

