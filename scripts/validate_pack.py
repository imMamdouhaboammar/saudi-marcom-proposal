#!/usr/bin/env python3
from pathlib import Path
import json, re, sys, yaml

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
# Expected name is saudi-marcom-proposal
if not name or name.group(1).strip() != 'saudi-marcom-proposal':
    errors.append(f"frontmatter name must be 'saudi-marcom-proposal', got '{name.group(1).strip() if name else None}'")
desc = re.search(r'^description:\s*"([\s\S]*?)"\nversion:', skill, re.M)
if desc and len(desc.group(1)) > 1024: errors.append('description exceeds 1024 chars')
for token in ['neural_links:', 'gates:', 'produces:', 'requires:']:
    if token not in skill: errors.append(f'SKILL.md missing {token}')

# Parse Neural Graph YAML with strict schema validation
graph_path = ROOT / 'neural-links/graph.yaml'
manifest_path = ROOT / 'manifest.json'
atomic_skills_validated = 0

if graph_path.exists() and manifest_path.exists():
    try:
        graph_data = yaml.safe_load(graph_path.read_text(encoding='utf-8'))
        nodes = graph_data.get('nodes', {})
        if not isinstance(nodes, dict) or len(nodes) < 9:
            errors.append(f'graph.yaml must define at least 9 nodes in dictionary, got {len(nodes)}')
            
        manifest_data = json.loads(manifest_path.read_text(encoding='utf-8'))
        manifest_skills = {s.get('name'): s for s in manifest_data.get('skills', [])}
        
        # Cross-validate graph nodes with manifest
        for node_id, node_def in nodes.items():
            if node_id not in manifest_skills:
                errors.append(f"graph node '{node_id}' missing from manifest.json skills")
            
            node_path_str = node_def.get('path', '')
            node_path = ROOT / node_path_str
            if not node_path.exists():
                errors.append(f"node '{node_id}' references non-existent path: {node_path_str}")
                continue
                
            # Verify edges connect to known nodes or valid terminals
            for precursor in node_def.get('precursors', []):
                if precursor not in nodes:
                    errors.append(f"node '{node_id}' references unknown precursor '{precursor}'")
            for continuation in node_def.get('continuations', []):
                if continuation not in nodes and continuation != 'submission-complete':
                    errors.append(f"node '{node_id}' references unknown continuation '{continuation}'")
                    
            # Validate individual atomic SKILL.md
            content = node_path.read_text(encoding='utf-8')
            line_count = content.count('\n') + 1
            if line_count >= 500:
                errors.append(f"atomic skill {node_id} exceeds 500 lines ({line_count} lines)")
            if not content.startswith('---\n'):
                errors.append(f"atomic skill {node_id} missing YAML frontmatter")
                
            s_name = re.search(r'^name:\s*([^\n]+)', content, re.M)
            if not s_name or s_name.group(1).strip() != node_id:
                errors.append(f"atomic skill {node_id} frontmatter name mismatch: {s_name.group(1).strip() if s_name else None}")
                
            s_desc = re.search(r'description:\s*"([\s\S]*?)"', content)
            if s_desc:
                desc_val = s_desc.group(1)
                if len(desc_val) > 1024:
                    errors.append(f"atomic skill {node_id} description exceeds 1024 chars")
                if "Use when" not in desc_val or "Do NOT use for" not in desc_val:
                    errors.append(f"atomic skill {node_id} description must include 'Use when' and 'Do NOT use for'")
            else:
                errors.append(f"atomic skill {node_id} missing description")
                
            for token in ['neural_links:', 'gates:', 'produces:', 'inputs:']:
                if token not in content:
                    errors.append(f"atomic skill {node_id} missing token '{token}'")
                    
            for sec in ['## Mission', '## Activation Contract', '## Non-Negotiable Invariants', '## Execution Procedure', '## Neural Handoff Contract']:
                if sec not in content:
                    errors.append(f"atomic skill {node_id} missing section '{sec}'")
                    
            atomic_skills_validated += 1
            
    except Exception as e:
        errors.append(f"YAML/JSON parsing failure in graph/manifest: {e}")

# Secret patterns scan
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
  'atomic_skills_validated': atomic_skills_validated,
  'reference_files': len(refs),
  'warnings': warnings,
  'errors': errors,
  'status': 'PASS' if not errors else 'FAIL'
}, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
