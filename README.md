# Saudi MarCom Proposal Skill Pack

A provider-neutral agentic system for building and auditing Saudi technical and financial proposals across corporate communications, media, marketing, events, crisis and reputation, digital and AI, monitoring, production, and adjacent services.

## Why this exists

Most proposal automation fails in one of two ways:

1. it writes polished generic prose before understanding the RFP
2. it produces technical and financial files that drift apart

This pack uses a state-aware DAG:

`sources -> requirements -> regulation/service context -> bid strategy -> technical design -> commercial model -> reconciliation -> adversarial QC -> artifacts`

## v0.3 architecture

The pack contains 10 atomic skills:

1. source-intake
2. rfp-forensics
3. regulatory-scout
4. service-router
5. bid-strategist
6. technical-architect
7. commercial-modeler
8. scope-reconciliation
9. proposal-qc
10. artifact-assembler

Routing is state-first. A "final" request cannot bypass a contradictory requirement, stale regulatory check, missing pricing basis, technical-financial mismatch, or QC blocker.

## What Bid Strategist adds

Compliance is not the same as a tailored response.

The strategy layer converts:
- evaluation weights
- buyer type
- decision audience
- bidder evidence
- service architecture
- commercial constraints

into:
- scoring coverage plan
- evidence plan
- win themes
- executive message map
- weak-evidence risks

It never invents buyer preferences or competitor weaknesses.

## Saudi freshness layer

The pack live-checks only regulations relevant to the active scope. Current routing covers:

- Ministry of Finance / Etimad procurement
- LCGPA local content
- ZATCA VAT
- SDAIA PDPL and data governance
- DGA government digital standards and accessibility
- NCA cybersecurity controls
- GAMR media and advertising
- GEA event and entertainment permits

The repository stores routing knowledge, not frozen legal conclusions.

## Commercial rule

A final price must come from an approved commercial basis:

1. rate card
2. vendor quote
3. approved internal cost basis
4. authorized normalized historical basis
5. user-approved scenario assumption

Otherwise the output remains `PRICING INPUT REQUIRED`.

## Validation

```bash
python3 -m pip install -r requirements.txt

# Focused agent/config security regression scan
python3 scripts/security_gate.py

# Structural contracts
python3 scripts/validate_pack.py

# Eval schema and semantic-family checks
python3 scripts/run_static_evals.py

# Regression suite
python3 -m unittest discover -s tests
```

The security gate checks agent, skill, router and CI configuration surfaces for credential patterns and a small set of dangerous executable-instruction patterns. It is focused evidence for this repository shape, not a substitute for organization-level secret scanning or platform security controls.

Behavioral maturity still requires a real model harness run. Static validation does not prove model behavior.

## Client boundary

Internal ledgers, margins, buy rates, bank data, reviewer notes, private benchmark sources, comments, hidden sheets/slides, and tracked changes must never enter the client package unless explicitly required.
