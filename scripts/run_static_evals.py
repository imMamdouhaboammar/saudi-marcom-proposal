#!/usr/bin/env python3
from pathlib import Path
import json
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

data = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
graph = yaml.safe_load((ROOT / "neural-links/graph.yaml").read_text(encoding="utf-8"))
service_router = yaml.safe_load((ROOT / "routers/service-router.yaml").read_text(encoding="utf-8"))

scenarios = data.get("scenarios", [])
required = {"id", "family", "public_prompt", "expected_route", "must_do", "must_not_do", "pass_criteria"}

node_ids = set((graph.get("nodes") or {}).keys())
service_ids = set((service_router.get("service_routes") or {}).keys())
lens_ids = set((service_router.get("cross_cutting_lenses") or {}).keys())
special_routes = {"do-not-trigger", "minimal-formatting", "do-not-trigger-or-minimal"}
allowed_routes = node_ids | service_ids | lens_ids | special_routes

ids = []
families = []
prompts = []

for index, scenario in enumerate(scenarios, 1):
    missing = required - set(scenario)
    if missing:
        errors.append(f"scenario {index} missing {sorted(missing)}")
        continue

    ids.append(scenario["id"])
    families.append(scenario["family"])
    prompts.append(scenario["public_prompt"].strip())

    if not scenario["must_do"]:
        errors.append(f"{scenario['id']} has no must_do")
    if not scenario["must_not_do"]:
        errors.append(f"{scenario['id']} has no must_not_do")
    if not scenario["expected_route"]:
        errors.append(f"{scenario['id']} has no expected_route")

    unknown = [route for route in scenario["expected_route"] if route not in allowed_routes]
    if unknown:
        errors.append(f"{scenario['id']} has unknown routes {unknown}")

if len(ids) != len(set(ids)):
    errors.append("scenario IDs must be unique")
if len(prompts) != len(set(prompts)):
    errors.append("public prompts must be unique")
if len(scenarios) < 16:
    errors.append("need at least 16 behavioral scenarios")
if len(set(families)) < 12:
    errors.append("need at least 12 semantic eval families")

required_families = {
    "non-trigger",
    "pricing-pressure",
    "contradictory-evidence",
    "procurement-law-transition",
    "mandatory-form-fidelity",
    "proof-laundering",
    "capacity-stress",
}
missing_families = sorted(required_families - set(families))
if missing_families:
    errors.append(f"missing critical eval families {missing_families}")

print(json.dumps({
    "scenarios": len(scenarios),
    "semantic_families": len(set(families)),
    "known_routes": len(allowed_routes),
    "errors": errors,
    "status": "PASS" if not errors else "FAIL",
}, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
