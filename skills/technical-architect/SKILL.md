---
name: technical-architect
description: "Architect, write, and structure the technical proposal (العرض الفني) for Saudi MarCom bids. Use when designing the solution methodology, workstreams, deliverable units, project schedule, team governance, quality assurance processes, and risk registers for media, marketing, event, digital, and crisis proposals. Do NOT use for financial modeling, client BOQ pricing, or clause extraction."
version: 0.2.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
  - active_service_modules
  - regulatory_source_ledger
requires:
  - source_grounding
produces:
  - technical_outline
  - deliverable_map
  - schedule
  - governance_model
  - risk_register
  - assumptions_register
gates:
  - evidence_before_claims
  - executable_deliverable_units
  - 100_percent_requirement_traceability
neural_links:
  precursors:
    - service-router
    - regulatory-scout
  continuations:
    - commercial-modeler
    - scope-reconciliation
  lateral_peers:
    - commercial-modeler
  recovery: rfp-forensics
---

# Solution Design & Technical Architect

Architect and draft decision-ready Saudi technical proposals (العرض الفني).

## Mission

Transform requirements, service models, and regulatory constraints into an executable, persuasive, and 100% compliant technical proposal tailored to Saudi procurement standards and cultural context.

## Activation Contract

Activate when:
- Designing the strategic methodology and work breakdown structure for a Saudi bid
- Drafting proposal sections: Executive Summary, Context Understanding, Scope of Work, Governance, Team Structure, Work Plan, Risk Register
- Building the exhaustive `deliverable_map` with discrete units, frequencies, and acceptance criteria
- Crafting Arabic or bilingual proposal copy aligned with Vision 2030 objectives

Do NOT activate for:
- Standalone pricing calculations or financial BOQs (use `commercial-modeler`)
- Raw clause extraction from tender documents (use `rfp-forensics`)
- Document formatting or desktop publishing export (use `artifact-assembler`)

## Non-Negotiable Invariants

1. **Evidence Before Claims**: Never assert credentials, case results, audience reach, or performance statistics without verified evidence in the source inventory.
2. **Executable Deliverable Units**: Every promised deliverable must have an explicit quantity/unit, timeline/frequency, owner, and objective acceptance criterion (no vague promises like "provide ongoing support").
3. **Traceable Coverage**: Every mandatory requirement in the ledger must map to an explicit section and deliverable in the technical proposal.

## Execution Procedure

### Step 1: Technical Proposal Architecture
Construct the proposal outline following Saudi public/private evaluation standards:
1. Cover & Bid Identity (RFP title, tender number, bidder identity)
2. Executive Summary (Strategic value proposition, core methodology, key differentiators)
3. Understanding of the Context & Objectives (Client landscape, strategic stakes, success metrics)
4. Strategic Approach & Creative Concept (Guiding principles, overarching narrative)
5. Detailed Scope of Work & Workstreams (Step-by-step execution across activated modules)
6. Deliverables Matrix & Acceptance Criteria (Discrete units, specifications, review cycles)
7. Project Management & Operating Model (Governance, client approvals, RACI matrix, escalation)
8. Implementation Timeline & Work Plan (Gantt milestones, critical path, key dependencies)
9. Team Structure & Key Personnel (Organizational chart, CV summaries, Saudization quotas)
10. Quality Assurance & Performance Metrics (SLA tracking, KPI dashboard, reporting cadence)
11. Risk Management & Assumptions Register (Anticipated risks, mitigation plans, dependencies)
12. Compliance & Evaluation Cross-Reference (Traceability matrix mapping RFP clauses to sections)

### Step 2: Deliverable Unit Modeling
For every work item, generate the formal `deliverable_map`:
- `deliv_id`: D-01, D-02...
- `mapped_req_id`: REQ-01, REQ-02...
- `deliverable_name`: e.g., Monthly Sentiment Analysis Report
- `unit_of_measure`: Report / Video / Event / Campaign / Man-month
- `quantity`: Exact count or baseline frequency
- `acceptance_criteria`: Measurable specification required for client sign-off
- `delivery_milestone`: Phase 1, Monthly, Event Day, etc.

### Step 3: Risk & Assumptions Engineering
Build the operational risk register (`templates/risk-register.csv`) and assumptions register (`templates/assumptions-register.csv`):
- Technical dependencies, client review turnaround limits, scope boundaries
- Severity, probability, impact score
- Proactive mitigation protocol and contingency fallback

## Neural Handoff Contract

When complete, output:
- `technical_outline`: Comprehensive narrative text (`templates/technical-proposal-outline.md`)
- `deliverable_map`: Exhaustive deliverable ledger
- `schedule`: Work plan and milestone calendar
- `risk_register`: Populated `templates/risk-register.csv`
- `assumptions_register`: Populated `templates/assumptions-register.csv`
- Target Continuations: Hand off to **`commercial-modeler`** (for pricing) and **`scope-reconciliation`**

## Progressive Resources
- `references/technical-proposal-anatomy.md`
- `references/risk-assumptions-and-governance.md`
- `references/writing-and-rtl.md`
- `templates/technical-proposal-outline.md`
- `templates/risk-register.csv`
- `templates/assumptions-register.csv`
