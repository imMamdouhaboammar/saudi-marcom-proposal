---
name: scope-reconciliation
description: "Falsify and reconcile technical scope against commercial scope for Saudi proposals. Use when checking that every promise has a commercial treatment, every charge has a technical purpose, and quantity, SLA, timing, language, geography, rights, revisions, operating coverage, and capacity agree. Do NOT use for initial solution design, price invention, or formatting."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
  - deliverable_map
  - acceptance_map
  - capacity_model
  - pricing_basis_ledger
  - client_boq
requires:
  - source_grounding
produces:
  - scope_price_map
  - mismatch_report
  - reconciliation_certificate
  - change_impact_log
gates:
  - bidirectional_coverage
  - semantic_parity
  - arithmetic_integrity
  - change_propagation
neural_links:
  precursors: [technical-architect, commercial-modeler]
  continuations: [proposal-qc]
  recovery: scope-reconciliation
---

# Semantic Scope Reconciliation

Treat reconciliation as a falsification step, not a checkbox.

## Forward trace: technical to commercial

For every deliverable verify:
- commercial treatment exists
- unit and quantity are compatible
- languages and locations are covered
- turnaround and SLA are funded
- revision rounds are funded
- rights/licensing/pass-throughs are handled
- operating window and staffing are supportable
- dependencies and client responsibilities are consistent

Unresolved item types:
- `UNPRICED_COMMITMENT`
- `CAPACITY_GAP`
- `RIGHTS_OR_LICENSE_GAP`
- `DEPENDENCY_GAP`

## Backward trace: commercial to technical

For every BOQ line verify:
- technical purpose exists
- buyer requirement or bidder option is identified
- quantity basis is visible
- supplier/pass-through treatment is disclosed where appropriate
- no internal-only cost line leaks into client-facing scope

Unresolved item types:
- `UNSUPPORTED_CHARGE`
- `DUPLICATE_CHARGE`
- `CLIENT_INTERNAL_LEAK`

## Semantic parity dimensions

Compare:
- quantity
- unit
- duration
- frequency
- service window
- response time
- languages
- geography
- deliverable format
- review/revision count
- acceptance criteria
- handover/ownership rights
- supplier responsibility
- permit dependency
- team coverage
- optional/excluded status

A numeric match is insufficient if service semantics differ.

## Change propagation

When one side changes:
1. identify dependent deliverables, BOQ lines, milestones, risks, assumptions, and schedule entries
2. update the change-impact log
3. invalidate prior reconciliation certificate
4. re-run only affected checks plus totals

Do not preserve a stale certificate after mutation.

## Certificate

Issue `PASS` only when:
- no material mismatch remains
- formulas/totals are valid
- all final-priced lines have a pricing basis
- all mandatory deliverables have a commercial treatment

Otherwise issue `FAIL` with machine-readable mismatch IDs.

## Handoff

Only a passing certificate continues to `proposal-qc`.
