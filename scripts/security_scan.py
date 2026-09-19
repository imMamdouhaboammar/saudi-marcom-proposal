#!/usr/bin/env python3
from pathlib import Path
import argparse
import json
import re
import sys

import yaml

DEFAULT_ROOT = Path(__file__).resolve().parents[1]

SECRET_PATTERNS = {
    "private_key": r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY",
    "openai_style_key": r"\bsk-[A-Za-z0-9_-]{20,}\b",
    "github_token": r"\bgh[pousr]_[A-Za-z0-9]{30,}\b",
    "aws_access_key": r"\bAKIA[0-9A-Z]{16}\b",
    "google_api_key": r"\bAIza[A-Za-z0-9_-]{20,}\b",
    "saudi_iban": r"\bSA\d{22}\b",
}

BINARY_SUFFIXES = {
    ".xlsx", ".xls", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".zip", ".gz", ".tar", ".woff", ".woff2", ".ttf", ".otf", ".ico",
    ".mp3", ".mp4", ".mov", ".avi", ".bin", ".pyc",
}

DANGEROUS_WORKFLOW_PATTERNS = {
    "pull_request_target": r"(?m)^\s*pull_request_target\s*:",
    "curl_pipe_shell": r"curl\s+[^\n|]+\|\s*(?:ba)?sh",
    "wget_pipe_shell": r"wget\s+[^\n|]+\|\s*(?:ba)?sh",
}


def read_text_candidate(path):
    if path.suffix.lower() in BINARY_SUFFIXES:
        return None
    try:
        raw = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in raw:
        return None
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return None


def iter_scannable_files(root):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if any(part in {".git", "__pycache__", ".pytest_cache"} for part in rel.parts):
            continue
        text = read_text_candidate(path)
        if text is not None:
            yield path, rel, text


def permission_findings(value, scope, rel):
    findings = []
    if value in (None, {}):
        return findings
    if isinstance(value, str):
        if value.lower() == "write-all":
            findings.append(f"workflow {rel} grants write-all at {scope}")
        return findings
    if not isinstance(value, dict):
        findings.append(f"workflow {rel} has invalid permissions block at {scope}")
        return findings
    for name, level in value.items():
        if str(level).lower() in {"write", "admin"}:
            findings.append(f"workflow {rel} grants {name}:{level} at {scope}; justify or narrow it")
    return findings


def scan_repository(root):
    root = Path(root).resolve()
    errors = []
    scanned = 0

    scanner_path = (root / "scripts" / "security_scan.py").resolve()

    for path, rel, text in iter_scannable_files(root):
        scanned += 1
        if path.resolve() == scanner_path:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            if re.search(pattern, text):
                errors.append(f"{label} pattern found in {rel}")

    workflow_dir = root / ".github" / "workflows"
    workflow_count = 0
    if workflow_dir.exists():
        for path in workflow_dir.glob("*.y*ml"):
            workflow_count += 1
            text = path.read_text(encoding="utf-8")
            rel = path.relative_to(root)

            for label, pattern in DANGEROUS_WORKFLOW_PATTERNS.items():
                if re.search(pattern, text, re.IGNORECASE):
                    errors.append(f"{label} found in {rel}")

            try:
                data = yaml.safe_load(text) or {}
            except yaml.YAMLError as exc:
                errors.append(f"workflow parse failure in {rel}: {exc}")
                continue

            errors.extend(permission_findings(data.get("permissions"), "workflow", rel))

            jobs = data.get("jobs", {})
            if not isinstance(jobs, dict):
                errors.append(f"workflow {rel} jobs must be a mapping")
                continue
            for job_name, job in jobs.items():
                if not isinstance(job, dict):
                    continue
                errors.extend(
                    permission_findings(
                        job.get("permissions"),
                        f"job:{job_name}",
                        rel,
                    )
                )

    agent_contract = root / "agents" / "AGENT_CONTRACT.md"
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

    reviewer_contract = root / "tools" / "reviewer-adapter-contract.md"
    if reviewer_contract.exists():
        text = reviewer_contract.read_text(encoding="utf-8").lower()
        if "do not send unrelated private drive documents" not in text:
            errors.append("reviewer adapter lacks private-source minimization rule")

    return {
        "root": str(root),
        "files_scanned": scanned,
        "workflows_scanned": workflow_count,
        "secret_patterns": len(SECRET_PATTERNS),
        "workflow_policy_checks": len(DANGEROUS_WORKFLOW_PATTERNS),
        "errors": errors,
        "status": "PASS" if not errors else "FAIL",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()
    result = scan_repository(args.root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
