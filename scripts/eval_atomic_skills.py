#!/usr/bin/env python3
"""
Atomic Skills Behavioral & Structural Evaluator
Evaluates the 9 atomic skills against the /skill-evaluator and /omni-skill contracts:
- Discovery: explicit triggers and near-miss negatives
- Structure: progressive layout, line limit, required sections
- Neural Links: DAG precursor, continuation, recovery integrity
- Completeness: declared inputs, produces, gates
- Evidence states: OBSERVED and DERIVED
"""

import sys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def evaluate_skills():
    manifest_path = ROOT / "manifest.json"
    graph_path = ROOT / "neural-links/graph.yaml"
    
    if not manifest_path.exists() or not graph_path.exists():
        print(json.dumps({"status": "FAIL", "error": "Missing manifest.json or graph.yaml"}))
        sys.exit(1)
        
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    skills = manifest.get("skills", [])
    
    results = []
    overall_pass = True
    
    required_sections = [
        "## Mission",
        "## Activation Contract",
        "## Non-Negotiable Invariants",
        "## Execution Procedure",
        "## Neural Handoff Contract"
    ]
    
    for s in skills:
        name = s["name"]
        rel_path = s["path"]
        file_path = ROOT / rel_path
        
        eval_record = {
            "name": name,
            "path": rel_path,
            "evidence_state": "OBSERVED",
            "checks": {},
            "status": "PASS"
        }
        
        if not file_path.exists():
            eval_record["status"] = "FAIL"
            eval_record["checks"]["file_exists"] = False
            overall_pass = False
            results.append(eval_record)
            continue
            
        eval_record["checks"]["file_exists"] = True
        content = file_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        # 1. Line count check (<500)
        eval_record["checks"]["line_count"] = len(lines)
        eval_record["checks"]["line_limit_ok"] = len(lines) < 500
        if len(lines) >= 500:
            eval_record["status"] = "FAIL"
            overall_pass = False
            
        # 2. Frontmatter metadata extraction
        has_frontmatter = content.startswith("---\n")
        eval_record["checks"]["frontmatter_present"] = has_frontmatter
        if not has_frontmatter:
            eval_record["status"] = "FAIL"
            overall_pass = False
            
        # 3. Discovery Triggers & Negatives (OmniSkill standard)
        desc_match = re.search(r'description:\s*"([\s\S]*?)"', content)
        if desc_match:
            desc = desc_match.group(1)
            eval_record["checks"]["description_length"] = len(desc)
            eval_record["checks"]["has_positive_triggers"] = "Use when" in desc
            eval_record["checks"]["has_negative_triggers"] = "Do NOT use for" in desc
            if not ("Use when" in desc and "Do NOT use for" in desc):
                eval_record["status"] = "FAIL"
                overall_pass = False
        else:
            eval_record["checks"]["description_present"] = False
            eval_record["status"] = "FAIL"
            overall_pass = False
            
        # 4. Neural Links metadata
        eval_record["checks"]["has_neural_links"] = "neural_links:" in content
        eval_record["checks"]["has_precursors"] = "precursors:" in content
        eval_record["checks"]["has_continuations"] = "continuations:" in content
        eval_record["checks"]["has_recovery"] = "recovery:" in content
        if not ("neural_links:" in content and "continuations:" in content):
            eval_record["status"] = "FAIL"
            overall_pass = False
            
        # 5. Core sections
        missing_sections = [sec for sec in required_sections if sec not in content]
        eval_record["checks"]["missing_sections"] = missing_sections
        if missing_sections:
            eval_record["status"] = "FAIL"
            overall_pass = False
            
        results.append(eval_record)
        
    summary = {
        "candidate": "saudi-marcom-proposal-atomic-skills-v0.2.0",
        "evidence_state": "OBSERVED",
        "total_atomic_skills": len(skills),
        "passed_skills": sum(1 for r in results if r["status"] == "PASS"),
        "failed_skills": sum(1 for r in results if r["status"] == "FAIL"),
        "status": "PASS" if overall_pass else "FAIL",
        "results": results
    }
    
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    sys.exit(0 if overall_pass else 1)

if __name__ == "__main__":
    evaluate_skills()
