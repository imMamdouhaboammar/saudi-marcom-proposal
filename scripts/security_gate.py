#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

SURFACES = [
    ROOT / "SKILL.md",
    ROOT / ".coderabbit.yaml",
]
SURFACES += list((ROOT / "skills").rglob("*.md"))
SURFACES += list((ROOT / "agents").glob("*.md"))
SURFACES += list((ROOT / "routers").glob("*.yaml"))
SURFACES += list((ROOT / "neural-links").glob("*.yaml"))
SURFACES += list((ROOT / ".github" / "workflows").glob("*.yml"))

SECRET_PATTERNS = {
    "private_key": r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY",
    "openai_key": r"\bsk-[A-Za-z0-9_-]{16,}\b",
    "google_api_key": r"\bAIza[A-Za-z0-9_-]{20,}\b",
    "github_token": r"\bgh[pousr]_[A-Za-z0-9]{20,}\b",
    "aws_access_key": r"\bAKIA[0-9A-Z]{16}\b",
    "saudi_iban": r"\bSA\d{22}\b",
    "authorization_header": r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._-]{12,}",
}

DANGEROUS_AGENT_PATTERNS = {
    "pipe_remote_shell": r"(?i)(?:curl|wget)[^\n|]{0,200}\|\s*(?:sh|bash|zsh)\b",
    "destructive_root_delete": r"(?i)\brm\s+-rf\s+/(?:\s|$)",
    "force_push_default_branch": r"(?i)git\s+push[^\n]{0,120}--force[^\n]{0,120}\b(?:main|master)\b",
    "world_writable": r"(?i)chmod\s+777\b",
}

findings = []

for path in sorted(set(p for p in SURFACES if p.is_file())):
    text = path.read_text(encoding="utf-8", errors="ignore")
    rel = str(path.relative_to(ROOT))
    for name, pattern in SECRET_PATTERNS.items():
        if re.search(pattern, text):
            findings.append({"severity":"blocker","type":name,"path":rel})
    for name, pattern in DANGEROUS_AGENT_PATTERNS.items():
        if re.search(pattern, text):
            findings.append({"severity":"blocker","type":name,"path":rel})

result = {
    "surface_files_scanned": len([p for p in set(SURFACES) if p.is_file()]),
    "findings": findings,
    "status": "PASS" if not findings else "FAIL",
    "scope": "agent/skill/router/CI configuration secret and dangerous-instruction regression scan"
}
print(json.dumps(result, indent=2))
sys.exit(1 if findings else 0)
