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

# Validate Master Orchestrator SKILL.md
skill = (ROOT/'SKILL.md').read_text(encoding='utf-8') if (ROOT/'SKILL.md').exists() else ''
if skill.count('\n') + 1 >= 500: errors.append('SKILL.md must stay under 500 lines')
if not skill.startswith('---\n'): errors.append('SKILL.md missing YAML frontmatter')
name = re.search(r'^name:\s*([^\n]+)', skill, re.M)
if not name or name.group(1).strip() != ROOT.name: errors.append('frontmatter name must match directory name')
desc = re.search(r'^description:\s*"([\s\S]*?)"\nversion:', skill, re.M)
if desc and len(desc.group(1)) > 1024: errors.append('description exceeds 1024 chars')
for token in ['neural_links:', 'gates:', 'produces:', 'requires:']:
    if token not in skill: errors.append(f'SKILL.md missing {token}')

# Validate Neural Links Graph & Manifest Consistency
manifest_path = ROOT/'manifest.json'
graph_path = ROOT/'neural-links/graph.yaml'
atomic_skills = []
if manifest_path.exists() and graph_path.exists():
    manifest_data = json.loads(manifest_path.read_text(encoding='utf-8'))
    atomic_skills = manifest_data.get('skills', [])
    if len(atomic_skills) < 9:
        errors.append(f'expected at least 9 atomic skills in manifest, found {len(atomic_skills)}')
    
    graph_text = graph_path.read_text(encoding='utf-8')
    for s in atomic_skills:
        s_name = s.get('name')
        s_path = ROOT / s.get('path')
        if not s_path.exists():
            errors.append(f'atomic skill file missing: {s.get("path")}')
            continue
        
        # Verify node presence in graph.yaml
        if f'{s_name}:' not in graph_text:
            errors.append(f'atomic skill {s_name} not declared as node in neural-links/graph.yaml')
        
        # Validate individual atomic SKILL.md
        s_content = s_path.read_text(encoding='utf-8')
        if s_content.count('\n') + 1 >= 500:
            errors.append(f'atomic skill {s_name} exceeds 500 lines ({s_content.count(chr(10))+1} lines)')
        if not s_content.startswith('---\n'):
            errors.append(f'atomic skill {s_name} missing YAML frontmatter')
        s_name_match = re.search(r'^name:\s*([^\n]+)', s_content, re.M)
        if not s_name_match or s_name_match.group(1).strip() != s_name:
            errors.append(f'atomic skill {s_name} frontmatter name mismatch')
        s_desc_match = re.search(r'^description:\s*"([\s\S]*?)"\nversion:', s_content, re.M)
        if s_desc_match and len(s_desc_match.group(1)) > 1024:
            errors.append(f'atomic skill {s_name} description exceeds 1024 chars')
        for token in ['neural_links:', 'gates:', 'produces:', 'inputs:']:
            if token not in s_content:
                errors.append(f'atomic skill {s_name} missing {token}')

# Package should never carry common secret/account patterns from private benchmark sources
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
  'root':str(ROOT),
  'orchestrator_lines': skill.count('\n')+1 if skill else 0,
  'atomic_skills_validated': len(atomic_skills),
  'reference_files': len(refs),
  'warnings': warnings,
  'errors': errors,
  'status': 'PASS' if not errors else 'FAIL'
}, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
