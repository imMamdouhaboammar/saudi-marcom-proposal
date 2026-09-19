---
name: technical-architect
description: "Architect and draft executable Saudi MarCom technical proposals using the requirement ledger, service modules, regulatory evidence, buyer strategy, and bidder proof. Use for methodology, workstreams, deliverables, acceptance criteria, governance, schedule, team model, KPIs, assumptions, and risk. Do NOT use for raw RFP extraction, final price creation, or document formatting."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
  - active_service_modules
  - cross_cutting_lenses
  - regulatory_source_ledger
  - evaluation_strategy
  - proof_plan
requires:
  - source_grounding
produces:
  - technical_outline
  - deliverable_map
  - acceptance_map
  - schedule
  - governance_model
  - risk_register
  - assumptions_register
gates:
  - evidence_before_claims
  - executable_deliverable_units
  - requirement_traceability
  - evaluation_alignment
neural_links:
  precursors: [service-router, regulatory-scout, bid-strategist]
  continuations: [commercial-modeler, scope-reconciliation]
  lateral_peers: [commercial-modeler]
  recovery: rfp-forensics
---

# Technical Solution Architect

Design an offer a delivery team could actually run.

## Inputs that must be present

Before drafting:
- requirement ledger
- buyer/evaluation strategy
- active service modules
- relevant regulatory implications
- verified bidder facts and proof gaps

If any are materially missing, produce a bounded draft and mark the missing dependency. Do not fill gaps with generic agency prose.

## Response architecture

Use the buyer's required structure when specified.

Otherwise select sections from:
1. executive decision summary
2. understanding of the buyer's context and requested outcomes
3. response principles and solution architecture
4. detailed workstreams
5. deliverable and acceptance matrix
6. governance, approvals, RACI, and escalation
7. staffing and coverage model
8. implementation plan and dependencies
9. measurement and reporting
10. quality assurance
11. risks, assumptions, exclusions, and fallbacks
12. requirement/evaluation cross-reference
13. bidder evidence and relevant case proof

Do not add Vision 2030 language unless it is directly relevant to the buyer or RFP.

## Deliverable contract

Every material deliverable requires:
- ID
- mapped requirement
- service family
- description
- unit
- quantity or frequency
- languages
- geography/location
- operating window or turnaround
- owner
- dependencies
- acceptance criteria
- acceptance evidence
- revision allowance
- rights/hand-over requirement
- commercial treatment status

A statement like "ongoing support" is invalid unless its operating window, response expectation, and capacity model are defined.

## KPI discipline

Classify each KPI:
- buyer-mandated
- contractual SLA
- bidder-proposed operational KPI
- outcome aspiration

Never invent an uplift target simply because a proposal "needs numbers."

For every KPI, define:
- formula
- source
- cadence
- owner
- baseline if known
- target source
- decision it supports

## Staffing and coverage

Describe roles from workload, not from a standard org chart.

For 24/7, multilingual, live-event, or rapid-response promises, define:
- coverage windows
- shift or on-call model
- handover
- backup
- approval availability
- peak/surge behavior

Commercial modeler must be able to cost this model.

## Governance

At minimum define:
- single accountable project lead
- client decision owner
- approval SLA
- escalation path
- recurring governance cadence
- urgent route
- version/change control

## Risk and assumptions

Each assumption must show:
- what is assumed
- why it matters
- owner
- deadline to validate
- impact if false
- affected deliverables and price lines

## Failure taxonomy

- generic methodology not tied to requirements
- decorative team chart with no workload logic
- aspirational KPI presented as commitment
- case-study proof copied from another client
- SLA with no capacity model
- hidden client dependency
- duplicated scope across service modules
- value-add that quietly creates unpriced scope

## Handoff

Write the solution into `bid_state` as structured deliverables and acceptance evidence before producing polished narrative.

Continue to `commercial-modeler` and `scope-reconciliation`.
