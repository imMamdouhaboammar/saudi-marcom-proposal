---
name: proposal-qc
description: "Independently falsify Saudi MarCom proposal readiness across mandatory compliance, evaluation coverage, evidence, technical-commercial parity, arithmetic, confidentiality, and submission integrity. Use for final review or review of existing proposal files. Do NOT create initial scope, invent missing evidence, or silently fix commercial assumptions."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs: [technical_outline, deliverable_map, client_boq, payment_milestones, requirement_ledger, scoring_coverage_plan, reconciliation_certificate]
requires: [source_grounding]
produces: [qc_report, submission_status, blocker_log]
gates: [mandatory_coverage, scoring_coverage, evidence_integrity, reconciliation_integrity, client_boundary]
neural_links:
  precursors: [scope-reconciliation]
  continuations: [artifact-assembler]
  on_fail: [rfp-forensics, bid-strategist, technical-architect, commercial-modeler]
  recovery: proposal-qc
---

# Proposal QC

Try to disprove readiness.

## Status

Return exactly one:
- READY
- REVISIONS_REQUIRED
- BLOCKED

READY means no unresolved submission-blocking defect was found with the evidence available. It is not a guarantee of award.

## Review order

### 1. Mandatory compliance
Check:
- every pass/fail requirement
- forms
- signatures/stamps where required
- qualifications
- mandatory attachments
- submission separation
- filenames/portal constraints

Any missing pass/fail item is BLOCKED.

### 2. Evaluation coverage
For each scored criterion:
- response exists
- location is traceable
- required proof exists
- weight receives proportionate decision-grade coverage
- executive summary aligns to detailed answer

A beautiful proposal with shallow high-weight criteria requires revision.

### 3. Evidence audit
Flag:
- unsupported credentials
- unverified case statistics
- copied client facts
- "leading/best/unique" without proof
- regulatory statements without fresh source
- outcome commitments without baseline/control logic

### 4. Technical feasibility
Check:
- deliverables have units/quantities
- staffing supports volume/SLA/languages
- governance has owners
- dependencies are explicit
- fallback exists for critical dependencies
- activated service-module rules are satisfied

### 5. Commercial integrity
Check:
- no unsourced final price
- mandatory BOQ preserved
- value-add has commercial treatment
- supplier-dependent lines have source/validity
- payment terms are sourced or explicit proposal terms
- internal cost/margin isolated

### 6. Reconciliation
Verify certificate plus spot-check:
- quantity/unit
- duration
- SLA/staffing
- included/optional/excluded
- VAT and totals
- financial-only line has technical purpose

### 7. Confidentiality and artifact boundary
Search for:
- prior client names not intentionally used as verified case evidence
- bank/account data
- private contacts
- internal margins/buy rates
- comments/tracked changes
- speaker notes
- hidden sheets/slides
- stale versions

## Finding format

Each finding contains:
- severity: blocker / major / minor / polish
- source/evidence
- affected requirement/criterion
- failure consequence
- owner
- required correction
- recheck condition

## Handoff

READY -> artifact-assembler.
REVISIONS_REQUIRED or BLOCKED -> earliest owning skill that can resolve the defect.

## Resources

- references/final-qc.md
- references/evaluation-engineering.md
- tools/agent-handoff-contract.md
- templates/final-qc-checklist.md
