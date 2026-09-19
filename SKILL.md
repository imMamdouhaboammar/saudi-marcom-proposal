---
name: saudi-marcom-proposal
description: "Orchestrate evidence-grounded Saudi MarCom technical and financial proposals across corporate communications, media, marketing, promotion, events, crisis and reputation, digital and AI, monitoring, production, and adjacent services. Use for Saudi RFP responses, tenders, pitches, retainers, proposal reviews, or bid packages that need requirements, response strategy, technical architecture, commercial modeling, reconciliation, and submission QC. Do NOT use for civil/MEP tenders, legal opinions, generic sales decks, or bare quote formatting."
version: 0.3.0
pack: proposal
inputs: [rfp_documents, organization_context, reference_work, pricing_inputs]
requires: [source_grounding]
produces: [requirement_ledger, compliance_matrix, response_strategy, scoring_coverage_plan, technical_proposal, financial_proposal, assumptions_register, risk_register, source_ledger, qc_report]
gates: [evidence_before_claims, no_unsourced_pricing, regulatory_freshness, technical_financial_reconciliation, confidentiality, evaluation_weight_alignment]
fallback: source-intake
mutatesWorkspace: false
parallelSafe: false
neural_links:
  architecture: state-aware-neural-dag
  graph: neural-links/graph.yaml
  state_router: routers/state-router.yaml
  nodes: [source-intake, rfp-forensics, regulatory-scout, service-router, bid-strategist, technical-architect, commercial-modeler, scope-reconciliation, proposal-qc, artifact-assembler]
  continuations: [source-intake]
  recovery: source-intake
---

# Saudi MarCom Proposal

Build a bid from evidence and operating decisions, not from a proposal template.

## Core model

`sources -> requirements -> applicability -> service architecture -> bid strategy -> technical design -> commercial model -> reconciliation -> adversarial QC -> artifacts`

The canonical topology is in `neural-links/graph.yaml`. Final-state routing is controlled by `routers/state-router.yaml`.

## Invariants

1. Source before prose.
2. Every requirement retains provenance.
3. Every scored criterion has an explicit response and evidence plan.
4. No credentials, results, staffing facts, permits, or certifications are invented.
5. No final price appears without an authorized rate, vendor quote, cost basis, or explicitly approved scenario assumption.
6. Every technical promise has commercial treatment.
7. Every client-facing price line has technical purpose.
8. Technical and financial submissions remain separate unless the buyer says otherwise.
9. Prescribed BOQ and qualification forms are not redesigned.
10. Regulatory checks are relevance-gated and current.
11. Past proposal material is structural reference only unless its facts are independently verified for this bid.
12. Internal margins, buy rates, bank details, private contacts, comments, tracked changes, and hidden sheets never cross the client boundary.

## State-first routing

Before obeying a request such as "final", "ready", "submit", or "finish", read `routers/state-router.yaml`.

Hard blockers outrank intent:
- source/confidentiality conflict
- contradictory mandatory requirements
- stale applicable regulation
- scored bid with no response strategy
- missing commercial basis
- technical-financial mismatch
- unresolved QC blocker

Do not reroute a bounded specialist merely because the user's wording changed.

## Phases

### Phase 1: Source intake
Use `source-intake`.

Output:
- source inventory
- buyer and bid classification
- confidentiality flags
- missing-input list
- required output: Technical / Financial / Both

### Phase 2: RFP forensics
Use `rfp-forensics`.

Extract:
- pass/fail conditions
- scored criteria and weights
- quantities and units
- SLAs
- mandatory forms
- qualification evidence
- submission mechanics
- contradictions and clarification questions

No silent conflict resolution.

### Phase 3: Parallel context
Run only applicable branches:

`regulatory-scout`
- procurement
- local content
- VAT/tax presentation
- PDPL/data
- DGA government digital requirements
- NCA cybersecurity
- GAMR media/advertising
- GEA events

`service-router`
- Media & Corporate Comms
- Marketing & Promotion
- Events & Experiences
- Crisis & Reputation
- Digital & AI
- Monitoring & Intelligence

### Phase 4: Bid strategy
For weighted evaluations, executive pitches, or any request for a highly tailored response, use `bid-strategist` before technical drafting.

It must produce:
- scoring coverage plan
- evidence plan
- win themes
- executive message map
- weak-evidence risks

A win theme must connect buyer priority, mechanism, evidence, and consequence.

### Phase 5: Technical architecture
Use `technical-architect`.

Every deliverable must specify:
- ID and mapped requirement
- name
- unit
- quantity/frequency
- owner
- acceptance criterion
- timing
- dependency
- commercial treatment

Methodology must show decisions and controls, not rephrase the RFP.

### Phase 6: Commercial model
Use `commercial-modeler`.

Pricing source order:
1. approved rate card
2. current vendor quote
3. approved internal cost basis
4. authorized normalized historical basis
5. user-approved planning scenario

Otherwise use `PRICING INPUT REQUIRED`.

Keep internal cost and margin mechanics out of the client BOQ.

### Phase 7: Reconciliation
Use `scope-reconciliation`.

For Both:
- technical -> financial
- financial -> technical
- quantity/unit parity
- schedule/duration parity
- SLA/staffing parity
- optional/included/excluded treatment
- VAT arithmetic

For a single-stream request, reconcile against the requirement ledger without inventing the missing counterpart.

### Phase 8: Proposal QC
Use `proposal-qc`.

QC must falsify:
- mandatory coverage
- scoring coverage
- evidence support
- client-name leakage
- stale references
- arithmetic
- scope-price parity
- attachment completeness
- unfunded value-add
- hidden document content

Only `READY` may continue to assembly.

### Phase 9: Artifact assembly
Use `artifact-assembler`.

Generate only requested formats and preserve the buyer's forms. Validate Arabic RTL, filenames, file separation, metadata, comments, notes, hidden sheets/slides, and bundle contents.

## Accelerated bid mode

Deadlines do not remove controls. Compress ideation, not:
- requirement extraction
- mandatory forms
- scoring/evidence plan
- scope-price reconciliation
- arithmetic
- confidentiality
- final checklist

## Progressive resources

Core:
- `references/rfp-forensics-and-compliance.md`
- `references/buyer-and-bid-strategy.md`
- `references/evaluation-engineering.md`
- `references/source-and-evidence-policy.md`
- `references/technical-proposal-anatomy.md`
- `references/financial-modeling.md`
- `references/saudi-regulatory-freshness.md`
- `references/risk-assumptions-and-governance.md`
- `references/final-qc.md`

Service depth:
- `references/service-modules/*.md`

## Completion

A polished file is not completion.

Completion requires:
- mandatory requirements covered
- scored criteria traceable
- current applicable regulation checked
- claims supported
- price inputs grounded
- technical/financial parity verified
- zero blocking QC findings
- rendered package checked against submission constraints
