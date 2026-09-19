#!/usr/bin/env python3
from pathlib import Path
import json, sys
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'evals/scenarios.json').read_text(encoding='utf-8'))
required={'id','family','public_prompt','expected_route','must_do','must_not_do','pass_criteria'}
errors=[]
for i,s in enumerate(data.get('scenarios',[]),1):
    miss=required-set(s)
    if miss: errors.append(f'scenario {i} missing {sorted(miss)}')
    if not s.get('must_do'): errors.append(f'scenario {i} has no must_do')
    if not s.get('must_not_do'): errors.append(f'scenario {i} has no must_not_do')
families=sorted({s['family'] for s in data.get('scenarios',[]) if 'family' in s})
print(json.dumps({'scenarios':len(data.get('scenarios',[])),'families':families,'errors':errors,'status':'PASS' if not errors else 'FAIL'},ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
