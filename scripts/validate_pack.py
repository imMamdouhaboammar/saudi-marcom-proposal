#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
EDGE_LIST_FIELDS = ('precursors', 'continuations', 'lateral_peers', 'on_pass', 'on_fail')
TERMINALS = {'submission-complete'}
errors = []
warnings = []

def read_frontmatter(path):
    content = path.read_text(encoding='utf-8')
    if not content.startswith('---\n'):
        raise ValueError('missing YAML frontmatter')
    end = content.find('\n---\n', 4)
    if end == -1:
        raise ValueError('unterminated YAML frontmatter')
    metadata = yaml.safe_load(content[4:end])
    if not isinstance(metadata, dict):
        raise ValueError('frontmatter must be a mapping')
    return content, metadata

def validate_skill(path, expected_name, label, required_fields):
    try:
        content, metadata = read_frontmatter(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f'{label} {exc}')
        return None
    line_count = content.count('\n') + 1
    if line_count >= 500:
        errors.append(f'{label} must stay under 500 lines ({line_count} lines)')
    if metadata.get('name') != expected_name:
        errors.append(f"{label} frontmatter name must be '{expected_name}'")
    desc = metadata.get('description')
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f'{label} missing description')
    elif len(desc) > 1024:
        errors.append(f'{label} description exceeds 1024 chars')
    for field in required_fields:
        if field not in metadata:
            errors.append(f"{label} missing frontmatter field '{field}'")
    return metadata

def validate_graph(graph_data, manifest_data):
    nodes = graph_data.get('nodes') if isinstance(graph_data, dict) else None
    entries = manifest_data.get('skills') if isinstance(manifest_data, dict) else None
    if not isinstance(nodes, dict):
        errors.append('graph.yaml nodes must be a mapping')
        return 0
    if not isinstance(entries, list):
        errors.append('manifest.json skills must be a list')
        return 0
    manifest = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get('name'), str):
            errors.append('manifest skill entries need string names')
            continue
        manifest[entry['name']] = entry
    if set(nodes) != set(manifest):
        for n in sorted(set(nodes)-set(manifest)):
            errors.append(f"graph node '{n}' missing from manifest.json skills")
        for n in sorted(set(manifest)-set(nodes)):
            errors.append(f"manifest skill '{n}' missing from graph.yaml nodes")
    validated = 0
    for node_id, node in nodes.items():
        if not isinstance(node, dict):
            errors.append(f"graph node '{node_id}' must be a mapping")
            continue
        path_str = node.get('path')
        if not isinstance(path_str, str):
            errors.append(f"graph node '{node_id}' must define a path")
            continue
        if node_id in manifest and manifest[node_id].get('path') != path_str:
            errors.append(f"graph node '{node_id}' path differs from manifest.json")
        for field in EDGE_LIST_FIELDS:
            targets = node.get(field, [])
            if not isinstance(targets, list) or not all(isinstance(t, str) for t in targets):
                errors.append(f"graph node '{node_id}' field '{field}' must be a list of strings")
                continue
            allowed = set(nodes) | TERMINALS if field == 'continuations' else set(nodes)
            for target in targets:
                if target not in allowed:
                    errors.append(f"graph node '{node_id}' field '{field}' references unknown target '{target}'")
        recovery = node.get('recovery')
        if recovery is not None and recovery not in nodes:
            errors.append(f"graph node '{node_id}' recovery references unknown target '{recovery}'")
        node_path = ROOT / path_str
        if not node_path.is_file():
            errors.append(f"graph node '{node_id}' references non-existent path: {path_str}")
            continue
        validate_skill(node_path, node_id, f'atomic skill {node_id}', ('inputs','produces','gates','neural_links'))
        validated += 1
    for signal, target in (graph_data.get('recovery') or {}).items():
        if target not in nodes:
            errors.append(f"graph recovery '{signal}' references unknown target '{target}'")
    return validated

required = [
    'SKILL.md','README.md','manifest.json','requirements.txt',
    'routers/state-router.yaml','routers/intent-router.yaml','routers/service-router.yaml','routers/source-precedence.yaml',
    'neural-links/graph.yaml','references/rfp-forensics-and-compliance.md',
    'references/buyer-and-bid-strategy.md','references/evaluation-engineering.md',
    'references/financial-modeling.md','references/saudi-regulatory-freshness.md',
    'templates/pricing-model.xlsx','evals/scenarios.json','evals/rubric.md'
]
for rel in required:
    if not (ROOT/rel).exists():
        errors.append(f'missing: {rel}')

skill_path = ROOT/'SKILL.md'
skill = skill_path.read_text(encoding='utf-8') if skill_path.exists() else ''
if skill_path.exists():
    validate_skill(skill_path,'saudi-marcom-proposal','SKILL.md',('requires','produces','gates','neural_links'))

validated=0
try:
    graph=yaml.safe_load((ROOT/'neural-links/graph.yaml').read_text(encoding='utf-8'))
    manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))
    validated=validate_graph(graph,manifest)
    state=yaml.safe_load((ROOT/'routers/state-router.yaml').read_text(encoding='utf-8'))
    if not isinstance(state.get('states'),dict) or len(state['states']) < 6:
        errors.append('state-router must define at least 6 evidence states')
except Exception as exc:
    errors.append(f'YAML/JSON parsing failure: {exc}')

secret_patterns={
    'IBAN':r'\bSA\d{20,24}\b',
    'API key':r'\b(?:sk-[A-Za-z0-9_-]{16,}|AIza[A-Za-z0-9_-]{20,})\b',
    'private key':r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY'
}
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md','.yaml','.yml','.json','.jsonl','.csv','.py','.txt'}:
        txt=path.read_text(encoding='utf-8',errors='ignore')
        for label,pattern in secret_patterns.items():
            if re.search(pattern,txt):
                errors.append(f'{label} pattern found in {path.relative_to(ROOT)}')
        if path.name != 'validate_pack.py' and ('/Users/' in txt or '/home/' in txt):
            warnings.append(f'machine-specific path found in {path.relative_to(ROOT)}')

try:
    data=json.loads((ROOT/'evals/scenarios.json').read_text(encoding='utf-8'))
    scenarios=data.get('scenarios',[])
    families={s.get('family') for s in scenarios}
    if len(scenarios) < 12:
        errors.append('need at least 12 behavioral scenarios')
    if len(families) < 8:
        errors.append('need at least 8 semantic eval families')
except Exception as exc:
    errors.append(f'eval parse failure: {exc}')

refs=[p for p in (ROOT/'references').rglob('*.md') if p.is_file()]
if not any(p.stat().st_size >= 1000 for p in refs):
    errors.append('need at least one substantial progressive reference >=1000 bytes')

print(json.dumps({
    'root':str(ROOT),
    'orchestrator_lines':skill.count('\n')+1 if skill else 0,
    'atomic_skills_validated':validated,
    'reference_files':len(refs),
    'warnings':warnings,
    'errors':errors,
    'status':'PASS' if not errors else 'FAIL'
},indent=2,ensure_ascii=False))
sys.exit(1 if errors else 0)
