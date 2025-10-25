#!/usr/bin/env python3
"""Run a minimal Neuro resume pipeline demo.

This script reads `resume_pipeline.neuro`, parses the actions, reads the master resume
(`resume_prompt_engineer_2page.txt`) and produces two variants in `outputs/`.
"""
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
MASTER = BASE.parent.parent.joinpath('resume_prompt_engineer_2page.txt')
NEURO = BASE.joinpath('resume_pipeline.neuro')
OUT = BASE.joinpath('outputs')


def parse_neuro_file(path):
    data = {'goal': '', 'target_roles': [], 'actions': []}
    text = path.read_text(encoding='utf-8')
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('goal:'):
            data['goal'] = line.split('goal:')[1].strip().strip('"')
        elif line.startswith('target_roles:'):
            m = re.search(r'\[([^\]]+)\]', line)
            if m:
                data['target_roles'] = [s.strip().strip('"') for s in m.group(1).split(',')]
        elif line.startswith('actions:'):
            acts = re.findall(r'(\w+)\(\)', line)
            data['actions'] = acts
    return data


def extract_section(text, section_name):
    # Find a UPPERCASE heading and return following lines until next uppercase heading
    pattern = rf'^{re.escape(section_name)}\n(.*?)(?:\n^[A-Z .()\-]+:\n|\Z)'
    m = re.search(pattern, text, flags=re.S | re.M)
    if not m:
        # fallback: find the line and then collect until blank line
        lines = text.splitlines()
        try:
            i = next(i for i,l in enumerate(lines) if l.strip()==section_name)
            out = []
            for l in lines[i+1:]:
                if not l.strip():
                    break
                out.append(l)
            return '\n'.join(out).strip()
        except StopIteration:
            return ''
    return m.group(1).strip()


def shorten_summary(master_text):
    summary = extract_section(master_text, 'PROFESSIONAL SUMMARY')
    # Take the first 2 sentences or first 200 chars
    sentences = re.split(r'(?<=[.!?])\s+', summary)
    short = ' '.join(sentences[:2]).strip()
    if len(short) < 40:
        short = summary.split('\n')[0][:200]
    return short


PROMPT_KEYWORDS = [
    'Prompt Engineering', 'LLMOps', 'Model Evaluation', 'RAG', 'Data Validation', 'Model Monitoring'
]


def add_prompt_keywords(master_text):
    # Emphasize keywords in PROFESSIONAL SUMMARY and CORE COMPETENCIES
    summary = extract_section(master_text, 'PROFESSIONAL SUMMARY')
    competencies = extract_section(master_text, 'CORE COMPETENCIES')

    kw_sentence = 'Key focus: ' + ', '.join(PROMPT_KEYWORDS) + '.'
    # If kw sentence already present, skip
    if kw_sentence not in summary:
        new_summary = summary + '\n\n' + kw_sentence
    else:
        new_summary = summary

    # add keywords at start of competencies
    new_comp = competencies
    if PROMPT_KEYWORDS[0] not in competencies:
        new_comp = ' • '.join(PROMPT_KEYWORDS) + '\n' + competencies

    return new_summary, new_comp


def produce_variants(master_text, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    # Variant 1: short summary
    short = shorten_summary(master_text)
    v1 = master_text
    v1 = re.sub(r'(PROFESSIONAL SUMMARY\n)(.*?)(\n\n|$)', r"\1" + short + "\n\n", v1, flags=re.S)
    Path(out_dir).joinpath('resume_prompt_engineer_short.txt').write_text(v1, encoding='utf-8')

    # Variant 2: keywords emphasized
    new_summary, new_comp = add_prompt_keywords(master_text)
    v2 = master_text
    v2 = re.sub(r'(PROFESSIONAL SUMMARY\n)(.*?)(\n\n|$)', r"\1" + new_summary + "\n\n", v2, flags=re.S)
    v2 = re.sub(r'(CORE COMPETENCIES\n)(.*?)(\n\n|$)', r"\1" + new_comp + "\n\n", v2, flags=re.S)
    Path(out_dir).joinpath('resume_prompt_engineer_keywords.txt').write_text(v2, encoding='utf-8')

    return [
        Path(out_dir).joinpath('resume_prompt_engineer_short.txt'),
        Path(out_dir).joinpath('resume_prompt_engineer_keywords.txt')
    ]


def main():
    neuro = parse_neuro_file(NEURO)
    print(f"Running Neuro pipeline: {neuro['goal']}")
    print('Actions:', neuro['actions'])

    master_text = MASTER.read_text(encoding='utf-8')
    outputs = produce_variants(master_text, OUT)

    print('Wrote variants:')
    for p in outputs:
        print(' -', p)


if __name__ == '__main__':
    main()
