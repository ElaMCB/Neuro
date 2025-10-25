Resume Neuro demo
=================

This example demonstrates a minimal Neuro pipeline that produces text variants from the master resume source.

Files
- `resume_pipeline.neuro` — intent-driven pipeline describing goal and actions.
- `run_pipeline.py` — small runner that parses the `.neuro` file and emits text variants in `outputs/`.
- `outputs/` — generated resume variants.

How to run

From the repository root:

```bash
python3 examples/resume/run_pipeline.py
```

This will create two files under `examples/resume/outputs/`:
- `resume_prompt_engineer_short.txt` — condensed professional summary variant
- `resume_prompt_engineer_keywords.txt` — variant with prompt-engineering keywords emphasized

Notes
- This demo is intentionally lightweight to showcase Neuro intent as the source of truth; the runner interprets actions in the `.neuro` file and applies deterministic, non-sensitive transformations to the master resume (`resume_prompt_engineer_2page.txt`).
