---
name: proposal-qc
description: "Independently red-team Saudi MarCom proposal packages for compliance, evidence, evaluator usability, technical-commercial consistency, confidentiality, arithmetic, and submission readiness. Use for final reviews, audit requests, finished-file checks, or pre-submission gates. Do NOT use as the primary drafting or pricing skill."
version: 0.4.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - bid_state
  - technical_outline
  - client_boq
  - reconciliation_certificate
  - evaluator_readability_report
requires:
  - source_grounding
produces:
  - qc_report
  - submission_status
gates:
  - independent_review
  - blocker_zero
  - evaluator_navigation
  - client_boundary
neural_links:
  precursors: [evaluator-simulator]
  continuations: [artifact-assembler]
  recovery: proposal-qc
---

# Proposal QC and Red Team

Try to disqualify, misunderstand, or break the proposal before the evaluator can.

Evaluator-simulation findings are advisory evidence. An unresolved mandatory-requirement gap remains a blocker even if the simulator labels it only as a question.

## Review order

1. submission and mandatory forms
2. pass/fail qualifications
3. source and claim integrity
4. evaluation coverage
5. technical executability
6. technical-financial parity
7. commercial formulas and treatment
8. Saudi regulatory freshness when relevant
9. confidentiality and client boundary
10. evaluator navigation and artifact clarity

## Finding severity

- `BLOCKER`: could disqualify, invalidate price, breach confidentiality, or make delivery materially impossible
- `MAJOR`: meaningful evaluation, delivery, or commercial risk
- `MINOR`: correctable weakness with limited impact
- `POLISH`: readability or presentation improvement

## Mandatory falsification checks

Attempt to find:
- an RFP clause with no response location
- a mandatory attachment missing or transformed incorrectly
- a case claim with no evidence receipt
- a current regulatory statement with no effective-state receipt
- a deliverable with no commercial treatment
- a price line with no technical purpose
- a 24/7 or rapid-response promise with insufficient capacity
- a quantity, language, location, or revision mismatch
- an internal margin, bank detail, old client name, or private commercial term in client artifacts
- a total, VAT, or milestone inconsistency
- a stale assumption that should have been superseded by an addendum

## Evaluator usability

A compliant proposal can still underperform if evidence is hard to find.

Check:
- high-weight criteria have visible, evidence-backed coverage
- executive summary reflects the actual solution
- requirements cross-reference is navigable
- differentiators are specific and proven
- long sections have clear decision logic
- optional ideas are labeled and do not contaminate base scope

Do not invent a score for opaque criteria. You may assess coverage quality against known criteria.

## Release states

`READY`:
- zero blockers
- reconciliation certificate is current and passing
- mandatory requirements covered
- client artifacts contain no internal leakage

`REVISIONS_REQUIRED`:
- no disqualifying blocker, but major issues remain

`BLOCKED`:
- any unresolved blocker

## External reviewer adapters

Independent external reviewers may add findings through `tools/reviewer-adapter-contract.md`.

Their results are evidence, not automatic truth. Normalize and deduplicate them before changing release status.

## Handoff

Only `READY` continues to `artifact-assembler`.
