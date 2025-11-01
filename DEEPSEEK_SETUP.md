# Use DeepSeek with Neuro

## 🚀 Why DeepSeek?

DeepSeek is an excellent choice for powering Neuro:

✅ **Cost-Effective** - Often cheaper than OpenAI  
✅ **High Performance** - Competitive with GPT-4  
✅ **Fast** - Low latency responses  
✅ **OpenAI-Compatible API** - Easy to integrate  

---

## ⚡ Quick Setup (3 Steps)

### **1. Get DeepSeek API Key**

1. Visit: https://platform.deepseek.com
2. Sign up / Log in
3. Go to API Keys
4. Create new API key
5. Copy the key (starts with `sk-...`)

### **2. Set Environment Variable**

**Windows (PowerShell):**
```powershell
$env:DEEPSEEK_API_KEY="sk-your-key-here"
```

**Windows (Command Prompt):**
```cmd
set DEEPSEEK_API_KEY=sk-your-key-here
```

**Mac/Linux:**
```bash
export DEEPSEEK_API_KEY=sk-your-key-here
```

**Permanent (add to .env file):**
```bash
echo "DEEPSEEK_API_KEY=sk-your-key-here" > .env
pip install python-dotenv
```

### **3. Run Neuro**

```bash
python neuro my_job_search.neuro
```

You'll see:
```
✓ AI parsing enabled with DeepSeek
```

**That's it! AI is now active!** 🎉

---

## 📊 DeepSeek vs OpenAI

| Feature | DeepSeek | OpenAI GPT-4 |
|---------|----------|--------------|
| **Cost** | ~$0.14 per 1M tokens | ~$30 per 1M tokens |
| **Speed** | Fast | Fast |
| **Quality** | Excellent (comparable to GPT-4) | Excellent |
| **API** | OpenAI-compatible | Native |
| **Privacy** | China-based | US-based |

**DeepSeek is ~200x cheaper!** 💰

---

## 🎯 What AI Enables

Once DeepSeek is configured, you can use **natural language**:

### **Before (Without AI):**
```neuro
// Must follow exact syntax
pipeline FindJobs {
    goal: "Find AI engineer jobs"
    target_roles: ["ai engineer", "ml engineer"]
    locations: ["remote", "US"]
}
```

### **After (With DeepSeek):**
```neuro
// Natural language works!
goal: "yo find me some remote ai jobs, i know python and pytorch"
```

**DeepSeek understands:**
- "yo" = casual greeting
- "find me" = search action
- "remote ai jobs" = remote AI engineer positions
- "i know python and pytorch" = skills filter

**Neuro automatically:**
- Searches job boards
- Filters for Python/PyTorch requirements
- Prioritizes remote positions
- Generates report

---

## 💡 Example Usage

### **Input:**
```neuro
"I'm transitioning from QA to AI engineering, find me entry-level remote positions"
```

### **DeepSeek Parses:**
```json
{
  "intent_type": "job_search",
  "target_roles": ["ai engineer"],
  "experience_level": "entry-level",
  "locations": ["remote"],
  "inferred": {
    "current_role": "qa engineer",
    "career_transition": true,
    "needs": ["resume_help", "skill_gap_analysis"]
  }
}
```

### **Neuro Executes:**
- ✓ Searches for entry-level AI jobs
- ✓ Prioritizes remote positions
- ✓ Generates transition-focused resume suggestions
- ✓ Provides skill recommendations

---

## 🔧 Technical Details

### **How DeepSeek Integration Works:**

```python
from openai import OpenAI

# DeepSeek uses OpenAI-compatible API
client = OpenAI(
    api_key=os.getenv('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# Use deepseek-chat model
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "Parse Neuro intent"},
        {"role": "user", "content": goal}
    ]
)
```

**It's that simple!** Same OpenAI client library, different endpoint.

---

## 💰 Cost Comparison

### **Typical Neuro Usage:**

**Per Job Search Run:**
- Parse intent: ~1,000 tokens
- Cost with DeepSeek: ~$0.0001
- Cost with OpenAI: ~$0.02

**Monthly (30 runs):**
- DeepSeek: ~$0.003 (basically free!)
- OpenAI: ~$0.60

**DeepSeek is 200x cheaper!** 🎯

---

## 🌟 Priority Order

Neuro checks for API keys in this order:

1. **DEEPSEEK_API_KEY** - Preferred (cheap, fast)
2. **OPENAI_API_KEY** - Fallback (more expensive)
3. **Pattern matching** - No API needed (free, works offline)

**Set DeepSeek first for best value!**

---

## 🔒 Security

### **Store API Keys Safely**

**❌ Don't:**
```python
api_key = "sk-1234..."  # Hard-coded in code
```

**✅ Do:**
```bash
# Environment variable
export DEEPSEEK_API_KEY=sk-...

# Or .env file
DEEPSEEK_API_KEY=sk-...
```

**For GitHub Actions:**
Add as repository secret:
- Settings → Secrets → Actions → New secret
- Name: `DEEPSEEK_API_KEY`
- Value: Your API key

---

## 🎓 Getting Started

### **Option 1: DeepSeek (Recommended - Cheap!)**

```bash
# 1. Get key from https://platform.deepseek.com
# 2. Set environment variable
export DEEPSEEK_API_KEY=sk-your-key

# 3. Install package
pip install openai

# 4. Run
python neuro my_task.neuro
```

### **Option 2: OpenAI (Alternative)**

```bash
# 1. Get key from https://platform.openai.com
# 2. Set environment variable
export OPENAI_API_KEY=sk-your-key

# 3. Install package
pip install openai

# 4. Run
python neuro my_task.neuro
```

### **Option 3: No AI (Free)**

```bash
# No setup needed!
# Works offline
# Use structured syntax

python neuro my_task.neuro
```

---

## 📚 More Information

- [AI Integration Details](AI_INTEGRATION.md)
- [How AI Works in Neuro](HOW_AI_WORKS.md)
- [General AI Enable Guide](ENABLE_AI.md)

---

## 🎯 Summary

**DeepSeek Setup:**
1. Get API key: https://platform.deepseek.com
2. Set: `DEEPSEEK_API_KEY=sk-...`
3. Run: `python neuro my_task.neuro`

**Cost:** ~$0.0001 per run (basically free!)

**Benefit:** Natural language goals, smart inference, helpful clarifications

**Perfect for Neuro!** 🚀

