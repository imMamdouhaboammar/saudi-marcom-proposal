#!/usr/bin/env python3
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []

required = [
    'SKILL.md','README.md','manifest.json',
    'routers/intent-router.yaml','routers/service-router.yaml','neural-links/graph.yaml',
    'references/rfp-forensics-and-compliance.md','references/financial-modeling.md',
    'references/saudi-regulatory-freshness.md','templates/pricing-model.xlsx',
    'evals/scenarios.json','evals/rubric.md'
]
for rel in required:
    if not (ROOT/rel).exists(): errors.append(f'missing: {rel}')

skill = (ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
if skill.count('\n') + 1 >= 500: errors.append('SKILL.md must stay under 500 lines')
if not skill.startswith('---\n'): errors.append('SKILL.md missing YAML frontmatter')
name = re.search(r'^name:\s*([^\n]+)', skill, re.M)
if not name or name.group(1).strip() != ROOT.name: errors.append('frontmatter name must match directory name')
desc = re.search(r'^description:\s*"([\s\S]*?)"\nversion:', skill, re.M)
if desc and len(desc.group(1)) > 1024: errors.append('description exceeds 1024 chars')
for token in ['neural_links:', 'gates:', 'produces:', 'requires:']:
    if token not in skill: errors.append(f'SKILL.md missing {token}')

# package should never carry common secret/account patterns from private benchmark sources
secret_patterns = {
    'IBAN': r'\bSA\d{20,24}\b',
    'API key': r'\b(?:sk-[A-Za-z0-9_-]{16,}|AIza[A-Za-z0-9_-]{20,})\b',
    'private key': r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY'
}
for p in ROOT.rglob('*'):
    if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.jsonl','.csv','.py','.txt'}:
        txt=p.read_text(encoding='utf-8',errors='ignore')
        for label,pat in secret_patterns.items():
            if re.search(pat,txt): errors.append(f'{label} pattern found in {p.relative_to(ROOT)}')
        if p.name != 'validate_pack.py' and ('/Users/' in txt or '/home/' in txt): warnings.append(f'machine-specific path found in {p.relative_to(ROOT)}')

sc_path=ROOT/'evals/scenarios.json'
if sc_path.exists():
    data=json.loads(sc_path.read_text(encoding='utf-8'))
    scenarios=data.get('scenarios',[])
    families={s.get('family') for s in scenarios}
    if len(scenarios)<8: errors.append('need at least 8 behavioral scenarios')
    if len(families)<6: errors.append('need at least 6 semantic eval families')

refs=[p for p in (ROOT/'references').rglob('*.md') if p.is_file()]
if not any(p.stat().st_size>=1000 for p in refs): errors.append('need at least one substantial progressive reference >=1000 bytes')

print(json.dumps({
  'root':str(ROOT), 'errors':errors, 'warnings':warnings,
  'skill_lines': skill.count('\n')+1 if skill else 0,
  'reference_files':len(refs),
  'status':'PASS' if not errors else 'FAIL'
}, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
