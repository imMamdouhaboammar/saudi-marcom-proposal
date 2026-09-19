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

    description = metadata.get('description')
    if not isinstance(description, str) or not description.strip():
        errors.append(f'{label} missing description')
    elif len(description) > 1024:
        errors.append(f'{label} description exceeds 1024 chars')

    for field in required_fields:
        if field not in metadata:
            errors.append(f"{label} missing frontmatter field '{field}'")
    return metadata


def validate_graph(graph_data, manifest_data):
    graph_nodes = graph_data.get('nodes') if isinstance(graph_data, dict) else None
    manifest_entries = manifest_data.get('skills') if isinstance(manifest_data, dict) else None
    if not isinstance(graph_nodes, dict):
        errors.append('graph.yaml nodes must be a mapping')
        return 0
    if not isinstance(manifest_entries, list):
        errors.append('manifest.json skills must be a list')
        return 0

    manifest_skills = {}
    for entry in manifest_entries:
        if not isinstance(entry, dict) or not isinstance(entry.get('name'), str):
            errors.append('manifest.json skill entries must contain string names')
            continue
        name = entry['name']
        if name in manifest_skills:
            errors.append(f"manifest.json contains duplicate skill '{name}'")
        manifest_skills[name] = entry

    graph_names = set(graph_nodes)
    manifest_names = set(manifest_skills)
    for name in sorted(graph_names - manifest_names):
        errors.append(f"graph node '{name}' missing from manifest.json skills")
    for name in sorted(manifest_names - graph_names):
        errors.append(f"manifest skill '{name}' missing from graph.yaml nodes")

    validated = 0
    for node_id, node_def in graph_nodes.items():
        if not isinstance(node_def, dict):
            errors.append(f"graph node '{node_id}' must be a mapping")
            continue

        node_path_str = node_def.get('path')
        if not isinstance(node_path_str, str) or not node_path_str:
            errors.append(f"graph node '{node_id}' must define a path")
            continue

        manifest_entry = manifest_skills.get(node_id)
        if manifest_entry and manifest_entry.get('path') != node_path_str:
            errors.append(f"graph node '{node_id}' path differs from manifest.json")

        for field in EDGE_LIST_FIELDS:
            targets = node_def.get(field, [])
            if not isinstance(targets, list) or not all(isinstance(target, str) for target in targets):
                errors.append(f"graph node '{node_id}' field '{field}' must be a list of strings")
                continue
            allowed = graph_names | TERMINALS if field == 'continuations' else graph_names
            for target in targets:
                if target not in allowed:
                    errors.append(f"graph node '{node_id}' field '{field}' references unknown target '{target}'")

        recovery = node_def.get('recovery')
        if recovery is not None and (not isinstance(recovery, str) or recovery not in graph_names):
            errors.append(f"graph node '{node_id}' recovery references unknown target '{recovery}'")

        node_path = ROOT / node_path_str
        if not node_path.is_file():
            errors.append(f"graph node '{node_id}' references non-existent path: {node_path_str}")
            continue
        validate_skill(
            node_path,
            node_id,
            f'atomic skill {node_id}',
            ('inputs', 'produces', 'gates', 'neural_links'),
        )
        validated += 1

    recovery_map = graph_data.get('recovery', {})
    if not isinstance(recovery_map, dict):
        errors.append('graph.yaml recovery must be a mapping')
    else:
        for signal, target in recovery_map.items():
            if not isinstance(signal, str) or not isinstance(target, str) or target not in graph_names:
                errors.append(f"graph recovery '{signal}' references unknown target '{target}'")
    return validated


required = [
    'SKILL.md', 'README.md', 'manifest.json', 'requirements.txt',
    'routers/intent-router.yaml', 'routers/service-router.yaml', 'neural-links/graph.yaml',
    'references/rfp-forensics-and-compliance.md', 'references/financial-modeling.md',
    'references/saudi-regulatory-freshness.md', 'templates/pricing-model.xlsx',
    'evals/scenarios.json', 'evals/rubric.md',
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f'missing: {rel}')

skill_path = ROOT / 'SKILL.md'
skill = skill_path.read_text(encoding='utf-8') if skill_path.exists() else ''
if skill_path.exists():
    validate_skill(
        skill_path,
        'saudi-marcom-proposal',
        'SKILL.md',
        ('requires', 'produces', 'gates', 'neural_links'),
    )

graph_path = ROOT / 'neural-links/graph.yaml'
manifest_path = ROOT / 'manifest.json'
atomic_skills_validated = 0
if graph_path.exists() and manifest_path.exists():
    try:
        graph_data = yaml.safe_load(graph_path.read_text(encoding='utf-8'))
        manifest_data = json.loads(manifest_path.read_text(encoding='utf-8'))
        atomic_skills_validated = validate_graph(graph_data, manifest_data)
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        errors.append(f'YAML/JSON parsing failure in graph/manifest: {exc}')

secret_patterns = {
    'IBAN': r'\bSA\d{20,24}\b',
    'API key': r'\b(?:sk-[A-Za-z0-9_-]{16,}|AIza[A-Za-z0-9_-]{20,})\b',
    'private key': r'BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY',
}
for path in ROOT.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.md', '.yaml', '.yml', '.json', '.jsonl', '.csv', '.py', '.txt'}:
        text = path.read_text(encoding='utf-8', errors='ignore')
        for label, pattern in secret_patterns.items():
            if re.search(pattern, text):
                errors.append(f'{label} pattern found in {path.relative_to(ROOT)}')
        if path.name != 'validate_pack.py' and ('/Users/' in text or '/home/' in text):
            warnings.append(f'machine-specific path found in {path.relative_to(ROOT)}')

scenarios_path = ROOT / 'evals/scenarios.json'
if scenarios_path.exists():
    data = json.loads(scenarios_path.read_text(encoding='utf-8'))
    scenarios = data.get('scenarios', [])
    families = {scenario.get('family') for scenario in scenarios}
    if len(scenarios) < 8:
        errors.append('need at least 8 behavioral scenarios')
    if len(families) < 6:
        errors.append('need at least 6 semantic eval families')

refs = [path for path in (ROOT / 'references').rglob('*.md') if path.is_file()]
if not any(path.stat().st_size >= 1000 for path in refs):
    errors.append('need at least one substantial progressive reference >=1000 bytes')

print(json.dumps({
    'root': str(ROOT),
    'orchestrator_lines': skill.count('\n') + 1 if skill else 0,
    'atomic_skills_validated': atomic_skills_validated,
    'reference_files': len(refs),
    'warnings': warnings,
    'errors': errors,
    'status': 'PASS' if not errors else 'FAIL',
}, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
