---
name: technical-architect
description: "Architect and draft the technical proposal (العرض الفني) for Saudi MarCom bids after requirements, service routing, and bid strategy are grounded. Use for solution methodology, workstreams, deliverable units, schedule, governance, quality, KPIs, risk, and assumptions. Do NOT use for pricing, raw clause extraction, or artifact formatting."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs: [requirement_ledger, active_service_modules, regulatory_source_ledger, response_strategy, evidence_plan]
requires: [source_grounding]
produces: [technical_outline, deliverable_map, schedule, governance_model, risk_register, assumptions_register]
gates: [evidence_before_claims, executable_deliverable_units, 100_percent_requirement_traceability, strategy_alignment]
neural_links:
  precursors: [service-router, bid-strategist, regulatory-scout]
  continuations: [commercial-modeler, scope-reconciliation]
  lateral_peers: [commercial-modeler]
  recovery: bid-strategist
---

# Technical Architect

Turn grounded requirements and strategy into an executable technical response.

## Preconditions

Do not draft a weighted/scored bid until:
- requirement ledger is materially complete
- active service modules are known
- applicable regulatory blockers are identified
- response strategy and evidence plan exist

A direct technical-only brief without scoring can use a lighter strategy record, but still needs a clear problem, scope, audience, and evidence boundary.

## Architecture

Select sections based on the RFP, not a fixed table of contents.

Common components:
1. executive summary
2. context and objectives
3. response principles / strategic approach
4. workstreams
5. methodology
6. deliverables and acceptance
7. operating model and governance
8. schedule
9. team and capacity
10. quality and SLA
11. measurement
12. risks, assumptions, dependencies
13. evidence/cases
14. compliance cross-reference where useful or required

## Service-module loading

Load every active `references/service-modules/*.md` before defining deliverables.

For multi-service bids create a cross-module interface table:
- producer
- output
- consumer
- cadence
- approval owner
- commercial owner

## Deliverable model

Every promised item needs:
- deliverable_id
- requirement_ids
- service_module
- name
- unit
- quantity or frequency
- owner
- acceptance criterion
- delivery timing
- dependency
- revision/approval rule where relevant
- commercial treatment placeholder

Vague "ongoing support" is invalid.

## Methodology standard

A methodology step must contain:
- input
- action
- owner
- output
- control/quality check
- exit condition

Do not use generic Discover, Design, Deliver phases unless the actual work inside each is specific.

## Evidence discipline

Use the bid strategist's evidence plan:
- claim only verified facts
- case evidence must be relevant
- executive-summary promises must be expanded in the body
- outcome KPIs need baseline/control assumptions
- unsupported superiority language is removed

## Team and capacity

Map roles to workload:
- volume
- coverage hours
- languages
- locations
- response SLA
- concurrent workstreams

Do not place CV names unless verified bidder evidence supplies them.

## Governance

Define:
- single accountable project lead
- client counterpart assumptions
- meeting cadence
- approval path
- urgent path
- sensitive escalation
- decision log
- change control
- reporting cadence

## Risk engineering

Risk entries need:
- trigger
- probability/impact or qualitative severity
- preventive control
- contingency
- owner
- commercial implication if material

Avoid decorative risk tables with generic items.

## Handoff

Output technical outline, deliverable map, schedule, governance, risk register, and assumptions.

Hand to commercial-modeler and scope-reconciliation.

## Resources

- references/technical-proposal-anatomy.md
- references/buyer-and-bid-strategy.md
- references/evaluation-engineering.md
- references/risk-assumptions-and-governance.md
- references/writing-and-rtl.md
- references/service-modules/*.md
