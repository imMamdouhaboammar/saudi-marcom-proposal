---
name: commercial-modeler
description: "Build capacity-aware commercial models, BOQs, financial proposals, payment schedules, and pricing-basis ledgers for Saudi MarCom bids. Use when translating technical scope into priced units, staffing coverage, supplier pass-throughs, tax treatment, payment milestones, and commercial assumptions. Do NOT use to invent market rates, write technical methodology, or alter prescribed buyer BOQ structures."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - deliverable_map
  - acceptance_map
  - pricing_inputs
  - regulatory_source_ledger
  - buyer_forms
requires:
  - source_grounding
produces:
  - capacity_model
  - pricing_basis_ledger
  - pricing_engine
  - client_boq
  - payment_milestones
  - commercial_assumptions
gates:
  - zero_unsourced_final_pricing
  - mandatory_boq_preservation
  - internal_cost_isolation
  - capacity_supports_scope
neural_links:
  precursors: [technical-architect, regulatory-scout]
  continuations: [scope-reconciliation]
  lateral_peers: [technical-architect]
  recovery: commercial-modeler
---

# Commercial and Capacity Modeler

Price the actual operating model, not a generic service list.

## Allowed final pricing bases

Every final-priced line must cite one:
- approved bidder rate card
- verified bidder cost basis
- current supplier or freelancer quote
- client contractual schedule or prescribed rate
- explicit commercial assumption authorized for this bid

Historical prices and public market estimates may support planning scenarios, but cannot silently become final bid rates.

## Pricing-basis ledger

For each price line record:
- line ID
- mapped deliverable IDs
- unit
- quantity
- cost driver
- source type
- source reference and date
- currency
- internal cost basis
- overhead/risk/margin treatment if authorized
- client unit price
- tax treatment source
- confidence: `FINAL | PROVISIONAL | INPUT_REQUIRED`
- client visibility: `CLIENT | INTERNAL`

If confidence is `INPUT_REQUIRED`, preserve the gap visibly.

## Capacity model

Build workload before price when capacity matters.

Examples:
- monthly content volume -> writer/designer/editor effort
- 24/7 monitoring -> shifts, handover, escalation, backup
- event coverage -> crew by venue, stage, hours, live outputs, turnaround
- multilingual content -> language volume, translator/editor QA, approval effort
- crisis response -> baseline retainer + surge/on-call treatment
- AI/digital product -> discovery, build, testing, hosting, support, data/security work
- media buying -> management fee or labor basis separated from media spend

Read `references/commercial-unit-library.md`.

## Unit selection

Prefer units that match buyer evaluation and delivery reality:
- item
- report
- post/content asset
- video
- finished minute
- production day
- shooting hour
- person-day
- person-month
- month
- campaign
- event
- platform
- dashboard
- license
- integration
- workshop
- supplier package

Do not hide a multi-driver scope inside `Lump Sum` unless the buyer requires it or the commercial logic is genuinely indivisible.

## Tax and statutory treatment

Tax is an input with provenance, not a hardcoded constant.

Use:
- buyer-prescribed BOQ treatment
- current official tax evidence from `regulatory_source_ledger`
- explicit commercial instruction

If treatment conflicts, block finalization.

Foreign suppliers, withholding, e-invoicing, local-content requirements, or permit fees are relevance-gated. Do not assume them.

## Optional, excluded, and client-supplied work

Each scope item must have one treatment:
- priced
- included at no additional fee
- optional
- excluded
- client supplied
- pricing input required

Never use "included" to hide substantial uncosted labor.

## Payment milestones

Link payments to observable acceptance events where the commercial context allows it.

Record:
- milestone
- acceptance trigger
- amount or percentage
- tax treatment
- dependency
- retention/guarantee condition if applicable
- invoice timing

Do not copy milestone percentages from prior bids.

## Scenario pricing

Planning scenarios are allowed only when clearly labeled and user-authorized.

A scenario must show:
- assumptions
- ranges or variable inputs
- what must be replaced before final submission

Never relabel a scenario as a final offer.

## Failure taxonomy

- final rate with no source
- technical 24/7 promise priced as business-hours labor
- media spend mixed into agency fee
- influencer/vendor pass-through hidden inside labor
- tax hardcoded despite buyer conflict
- mandatory BOQ redesigned
- client file leaks internal margin
- scope change not propagated to quantities or payment milestones

## Handoff

Append `capacity_model`, `pricing_basis_ledger`, and client BOQ to `bid_state`.

Continue to `scope-reconciliation`.
