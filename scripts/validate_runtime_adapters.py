#!/usr/bin/env python3
from pathlib import Path
import json
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

registry = yaml.safe_load((ROOT / "tools/tool-registry.yaml").read_text(encoding="utf-8"))
adapter_map = yaml.safe_load((ROOT / "tools/runtime-adapter-map.example.yaml").read_text(encoding="utf-8"))
fixtures = json.loads((ROOT / "evals/fixtures/runtime-adapter-cases.json").read_text(encoding="utf-8"))

capabilities = set((registry.get("capabilities") or {}).keys())
mapped = set((adapter_map.get("adapters") or {}).keys())

required_registry = {
    "connected_source_search",
    "connected_source_read",
    "public_web_search",
    "public_web_fetch",
    "spreadsheet_compute",
    "document_artifact",
    "presentation_artifact",
    "deterministic_validator",
    "independent_reviewer",
}

missing_registry = required_registry - capabilities
if missing_registry:
    errors.append(f"tool registry missing {sorted(missing_registry)}")

missing_map = required_registry - mapped
if missing_map:
    errors.append(f"runtime adapter example missing {sorted(missing_map)}")

case_ids = []
for case in fixtures.get("cases", []):
    case_id = case.get("id")
    case_ids.append(case_id)

    unknown = set(case.get("available", [])) - capabilities
    if unknown:
        errors.append(f"{case_id}: unknown capabilities {sorted(unknown)}")

    if "expected_finalizable" not in case:
        errors.append(f"{case_id}: expected_finalizable missing")
    if not isinstance(case.get("expected_limitations", []), list):
        errors.append(f"{case_id}: expected_limitations must be a list")

if len(case_ids) != len(set(case_ids)):
    errors.append("runtime adapter case IDs must be unique")

required_cases = {
    "full-capability",
    "no-public-web",
    "no-private-source",
    "no-spreadsheet",
    "no-artifact-renderer",
    "no-external-reviewer",
}
missing_cases = required_cases - set(case_ids)
if missing_cases:
    errors.append(f"runtime fixtures missing {sorted(missing_cases)}")

no_reviewer = next((c for c in fixtures.get("cases", []) if c.get("id") == "no-external-reviewer"), None)
if no_reviewer:
    if not no_reviewer.get("expected_finalizable"):
        errors.append("external reviewer must remain optional to core finalization")
    if "deterministic_validator" not in no_reviewer.get("available", []):
        errors.append("no-external-reviewer case must retain deterministic validation")

result = {
    "registered_capabilities": len(capabilities),
    "mapped_capabilities": len(mapped),
    "runtime_cases": len(case_ids),
    "errors": errors,
    "status": "PASS" if not errors else "FAIL",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
