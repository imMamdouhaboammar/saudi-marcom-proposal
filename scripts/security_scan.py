#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
scanned = 0

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".jsonl", ".csv", ".py", ".txt"}
SECRET_PATTERNS = {
    "private_key": r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY",
    "openai_style_key": r"\bsk-[A-Za-z0-9_-]{20,}\b",
    "github_token": r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",
    "aws_access_key": r"\bAKIA[0-9A-Z]{16}\b",
    "saudi_iban": r"\bSA\d{22}\b",
}
DANGEROUS_WORKFLOW_PATTERNS = {
    "pull_request_target": r"(?m)^\s*pull_request_target\s*:",
    "write_all_permissions": r"(?m)^\s*permissions\s*:\s*write-all\s*$",
    "curl_pipe_shell": r"curl\s+[^\n|]+\|\s*(?:ba)?sh",
    "wget_pipe_shell": r"wget\s+[^\n|]+\|\s*(?:ba)?sh",
}

for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
        continue
    scanned += 1
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = path.relative_to(ROOT)

    if rel.as_posix() == "scripts/security_scan.py":
        continue

    for label, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, text):
            errors.append(f"{label} pattern found in {rel}")

workflow_dir = ROOT / ".github" / "workflows"
if workflow_dir.exists():
    for path in workflow_dir.glob("*.y*ml"):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for label, pattern in DANGEROUS_WORKFLOW_PATTERNS.items():
            if re.search(pattern, text, re.IGNORECASE):
                errors.append(f"{label} found in {rel}")
        try:
            data = yaml.safe_load(text) or {}
        except yaml.YAMLError as exc:
            errors.append(f"workflow parse failure in {rel}: {exc}")
            continue
        permissions = data.get("permissions", {})
        if permissions not in (None, {}) and isinstance(permissions, dict):
            for name, level in permissions.items():
                if str(level).lower() in {"write", "admin"}:
                    errors.append(f"workflow {rel} grants {name}:{level}; justify or narrow it")

agent_contract = ROOT / "agents" / "AGENT_CONTRACT.md"
if agent_contract.exists():
    text = agent_contract.read_text(encoding="utf-8")
    required_controls = [
        "invent bidder evidence or rates",
        "clear its own QC finding",
        "mark the final bid READY",
    ]
    for control in required_controls:
        if control not in text:
            errors.append(f"agent contract missing control: {control}")

reviewer_contract = ROOT / "tools" / "reviewer-adapter-contract.md"
if reviewer_contract.exists():
    text = reviewer_contract.read_text(encoding="utf-8").lower()
    if "do not send unrelated private drive documents" not in text:
        errors.append("reviewer adapter lacks private-source minimization rule")

result = {
    "files_scanned": scanned,
    "secret_patterns": len(SECRET_PATTERNS),
    "workflow_policy_checks": len(DANGEROUS_WORKFLOW_PATTERNS),
    "errors": errors,
    "status": "PASS" if not errors else "FAIL",
}
print(json.dumps(result, indent=2, ensure_ascii=False))
sys.exit(1 if errors else 0)
