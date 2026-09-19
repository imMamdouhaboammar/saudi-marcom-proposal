#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []
TERMINALS = {"submission-complete"}
EDGE_FIELDS = ("precursors", "continuations", "lateral_peers", "on_pass", "on_fail")


def read_frontmatter(path):
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = content.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unterminated YAML frontmatter")
    metadata = yaml.safe_load(content[4:end])
    if not isinstance(metadata, dict):
        raise ValueError("frontmatter must be a mapping")
    return content, metadata


def validate_skill(path, expected_name, label):
    try:
        content, metadata = read_frontmatter(path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"{label}: {exc}")
        return None, ""

    if metadata.get("name") != expected_name:
        errors.append(f"{label}: frontmatter name must be {expected_name}")

    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{label}: missing description")
    else:
        if len(description) > 1024:
            errors.append(f"{label}: description exceeds 1024 chars")
        if "Do NOT use" not in description:
            warnings.append(f"{label}: description has no explicit negative trigger")

    line_count = content.count("\n") + 1
    if line_count >= 500:
        errors.append(f"{label}: must stay under 500 lines ({line_count})")

    for field in ("inputs", "produces", "gates", "neural_links"):
        if field not in metadata:
            errors.append(f"{label}: missing {field}")

    return metadata, content


required_paths = [
    "SKILL.md",
    "README.md",
    "manifest.json",
    "neural-links/graph.yaml",
    "schemas/bid-state.schema.json",
    "routers/intent-router.yaml",
    "routers/buyer-context-router.yaml",
    "routers/service-router.yaml",
    "routers/source-precedence.yaml",
    "routers/precedent-router.yaml",
    "skills/bid-strategist/SKILL.md",
    "references/state-and-handoff-protocol.md",
    "references/regulatory-state-resolver.md",
    "references/commercial-unit-library.md",
    "references/evaluation-and-win-strategy.md",
    "references/precedent-retrieval-and-learning.md",
    "references/evaluator-simulation.md",
    "references/benchmark-provenance.md",
    "references/saudi-authority-map.md",
    "tools/tool-registry.yaml",
    "tools/reviewer-adapter-contract.md",
    "evals/scenarios.json",
    "evals/rubric.md",
    "evals/behavior-harness-contract.md",
    "templates/capacity-model.csv",
    "templates/evidence-plan.csv",
    "templates/change-impact-log.csv",
    "templates/precedent-ledger.csv",
    "templates/evaluator-questions.csv",
    "evals/fixtures/end-to-end-government.json",
    "evals/fixtures/end-to-end-event.json",
]
for rel in required_paths:
    if not (ROOT / rel).exists():
        errors.append(f"missing: {rel}")

try:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    graph = yaml.safe_load((ROOT / "neural-links/graph.yaml").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "schemas/bid-state.schema.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
    errors.append(f"manifest/graph/schema parse failure: {exc}")
    manifest, graph, schema = {}, {}, {}

master_meta, master_content = validate_skill(ROOT / "SKILL.md", "saudi-marcom-proposal", "master skill")

manifest_skills = {
    item.get("name"): item
    for item in manifest.get("skills", [])
    if isinstance(item, dict) and isinstance(item.get("name"), str)
}
graph_nodes = graph.get("nodes", {}) if isinstance(graph, dict) else {}

if set(manifest_skills) != set(graph_nodes):
    errors.append(
        f"manifest/graph skill mismatch: manifest={sorted(manifest_skills)} graph={sorted(graph_nodes)}"
    )

if len(graph_nodes) < 12:
    errors.append("guarded DAG must contain at least 12 atomic skills")

for node_id, node in graph_nodes.items():
    if not isinstance(node, dict):
        errors.append(f"graph node {node_id} must be a mapping")
        continue

    path_str = node.get("path")
    if not isinstance(path_str, str):
        errors.append(f"graph node {node_id} missing path")
        continue

    path = ROOT / path_str
    if not path.is_file():
        errors.append(f"graph node {node_id} references missing {path_str}")
        continue

    meta, _ = validate_skill(path, node_id, f"atomic skill {node_id}")
    if not meta:
        continue

    manifest_path = manifest_skills.get(node_id, {}).get("path")
    if manifest_path != path_str:
        errors.append(f"{node_id}: manifest path differs from graph path")

    graph_outputs = set(node.get("outputs", []))
    meta_outputs = set(meta.get("produces", []))
    if not graph_outputs.issubset(meta_outputs):
        errors.append(f"{node_id}: graph outputs not declared in skill produces")

    if not node.get("exit_guard"):
        errors.append(f"{node_id}: missing exit_guard")

    for field in EDGE_FIELDS:
        values = node.get(field, [])
        if not isinstance(values, list):
            errors.append(f"{node_id}: {field} must be a list")
            continue
        allowed = set(graph_nodes) | (TERMINALS if field == "continuations" else set())
        for target in values:
            if target not in allowed:
                errors.append(f"{node_id}: unknown {field} target {target}")

    recovery = node.get("recovery")
    if recovery and recovery not in graph_nodes:
        errors.append(f"{node_id}: unknown recovery target {recovery}")

if graph.get("state_contract") != "schemas/bid-state.schema.json":
    errors.append("graph must bind schemas/bid-state.schema.json")
if manifest.get("state_contract") != "schemas/bid-state.schema.json":
    errors.append("manifest must bind schemas/bid-state.schema.json")
if schema.get("type") != "object":
    errors.append("bid-state schema root must be object")

service_router_path = ROOT / "routers/service-router.yaml"
if service_router_path.exists():
    service_router = yaml.safe_load(service_router_path.read_text(encoding="utf-8"))
    for route_id, route in (service_router.get("service_routes") or {}).items():
        ref = route.get("reference")
        if not ref or not (ROOT / ref).is_file():
            errors.append(f"service route {route_id} has missing reference {ref}")
    if len(service_router.get("cross_cutting_lenses") or {}) < 5:
        errors.append("service router needs at least 5 cross-cutting lenses")

source_precedence = yaml.safe_load((ROOT / "routers/source-precedence.yaml").read_text(encoding="utf-8"))
if "private_prior_proposal_pattern" not in source_precedence.get("precedence", []):
    errors.append("source precedence must explicitly classify private prior proposals")

tool_registry = yaml.safe_load((ROOT / "tools/tool-registry.yaml").read_text(encoding="utf-8"))
required_capabilities = {
    "connected_source_search", "connected_source_read", "public_web_search",
    "spreadsheet_compute", "document_artifact", "presentation_artifact",
    "deterministic_validator", "independent_reviewer",
}
available_capabilities = set((tool_registry.get("capabilities") or {}).keys())
missing_caps = required_capabilities - available_capabilities
if missing_caps:
    errors.append(f"tool registry missing capabilities {sorted(missing_caps)}")

scenarios = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8")).get("scenarios", [])
if len(scenarios) < 22:
    errors.append("need at least 22 behavioral scenarios")
families = {item.get("family") for item in scenarios}
if len(families) < 16:
    errors.append("need at least 16 semantic eval families")

secret_patterns = {
    "IBAN": r"\bSA\d{20,24}\b",
    "API key": r"\b(?:sk-[A-Za-z0-9_-]{16,}|AIza[A-Za-z0-9_-]{20,})\b",
    "private key": r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY",
}
text_suffixes = {".md", ".yaml", ".yml", ".json", ".jsonl", ".csv", ".py", ".txt"}
for path in ROOT.rglob("*"):
    if path.is_file() and path.suffix.lower() in text_suffixes:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in secret_patterns.items():
            if re.search(pattern, text):
                errors.append(f"{label} pattern found in {path.relative_to(ROOT)}")
        if path.name != "validate_pack.py" and ("/Users/" in text or "/home/" in text):
            warnings.append(f"machine-specific path in {path.relative_to(ROOT)}")

active_files = [
    ROOT / "SKILL.md",
    ROOT / "skills/regulatory-scout/SKILL.md",
    ROOT / "references/saudi-regulatory-freshness.md",
    ROOT / "references/regulatory-state-resolver.md",
]
for path in active_files:
    if path.exists() and re.search(r"\bGCAM\b", path.read_text(encoding="utf-8")):
        errors.append(f"stale media authority acronym GCAM in active regulatory file {path.relative_to(ROOT)}")

refs = list((ROOT / "references").rglob("*.md"))
if len(refs) < 15:
    errors.append("need at least 15 progressive reference files")
if not any(path.stat().st_size >= 3000 for path in refs):
    errors.append("need at least one deep reference >=3000 bytes")

result = {
    "root": str(ROOT),
    "orchestrator_lines": master_content.count("\n") + 1 if master_content else 0,
    "atomic_skills": len(graph_nodes),
    "references": len(refs),
    "scenarios": len(scenarios),
    "semantic_families": len(families),
    "warnings": warnings,
    "errors": errors,
    "status": "PASS" if not errors else "FAIL",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
