---
name: commercial-modeler
description: "Engineer commercial models, client Bill of Quantities (BOQ / جدول الكميات والأسعار), financial proposals (العرض المالي), and payment schedules for Saudi bids. Use when building pricing workbooks, mapping labor rates, calculating production vendor costs, structuring VAT and milestone cashflows, and enforcing commercial assumptions. Do NOT use for inventing rates without source inputs or writing technical narratives."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - deliverable_map
  - boq_templates
  - pricing_inputs
  - regulatory_source_ledger
requires:
  - source_grounding
produces:
  - pricing_engine
  - client_boq
  - payment_milestones
  - commercial_assumptions
gates:
  - zero_unsourced_pricing
  - mandatory_boq_preservation
  - internal_cost_isolation
neural_links:
  precursors:
    - technical-architect
    - regulatory-scout
  continuations:
    - scope-reconciliation
  lateral_peers:
    - technical-architect
  recovery: commercial-modeler
---

# Commercial Modeler & Financial Proposal

Engineer the pricing model, client BOQ, and commercial proposal (العرض المالي).

## Mission

Translate the technical deliverable map into an airtight commercial model, preserving mandatory client BOQ tables, applying authorized labor and production rate cards, calculating statutory VAT, and structuring cashflow milestones.

## Activation Contract

Activate when:
- Pricing a Saudi MarCom bid, retainer, campaign, or event
- Populating a mandatory government BOQ table or financial offer template
- Calculating labor costs, vendor pass-throughs, management fees, risk buffers, and margins
- Structuring billing terms, payment milestones, and VAT treatment (15%)
- Formulating commercial exclusions and price validity assumptions

Do NOT activate for:
- Writing the technical approach (use `technical-architect`)
- Reconciling technical scope vs financial lines (use `scope-reconciliation`)
- Guessing or inventing market prices when inputs are absent

## Non-Negotiable Invariants

1. **Zero Unsourced Pricing**: Never fabricate a rate or lump sum. Missing commercial inputs MUST remain explicitly flagged as `PRICING INPUT REQUIRED` or scenario-bounded with user authorization.
2. **Preserve Prescribed BOQ**: Never reformat, reorder, or alter columns of a client's mandatory BOQ sheet.
3. **Internal Cost Isolation**: Client-facing financial files must never disclose internal costs, staff salaries, contractor buy rates, or profit margins unless explicitly mandated by the RFP (e.g., cost-plus contracts).

## Execution Procedure

### Step 1: Internal Pricing Engine Construction
Build the calculation layer using `templates/pricing-model.xlsx`:
- **Labor Layer**: Role title, seniority, daily/monthly rate, allocated days/months per deliverable
- **Direct Costs**: Venue rental, staging, AV gear, catering, paid media budget, printing, third-party software licenses
- **Allowances & Contingencies**: Explicitly authorized risk buffers or contingency pools
- **Overhead & Margin**: Standard agency markup or agreed profit percentage
- **Statutory Taxes**: Saudi 15% VAT calculation (clearly labeled as exclusive or inclusive per tender rules)

### Step 2: Client BOQ Generation
Map internal calculation lines to the client-facing BOQ (`templates/boq.csv`):
- `line_id`: Matches client BOQ numbering (Item 1.1, 1.2...)
- `item_description`: Formal deliverable title and service specification
- `unit`: Month / Day / Event / Report / Unit / Lump Sum
- `quantity`: Quantity matching technical proposal
- `unit_price_sar`: Sourced quote price in SAR (exclusive of VAT)
- `total_price_sar`: Unit price $\times$ Quantity
- `vat_sar`: 15% VAT amount
- `grand_total_sar`: Total inclusive of VAT

### Step 3: Payment Milestones & Commercial Conditions
Structure payment terms linked to verifiable technical deliverables:
- Milestone 1: Mobilization / Kick-off (e.g., 10-20% upon contract signing / advance payment guarantee)
- Progress Milestones: Linked to accepted deliverables (e.g., approval of strategy, monthly reports, event completion)
- Close-out Milestone: Final payment upon formal sign-off / handover (e.g., 10%)
- Define price validity (e.g., 90 or 120 days from bid submission)

### Step 4: Commercial Assumptions & Exclusions Register
Populate `templates/assumptions-register.csv`:
- Assumptions that directly govern pricing (e.g., client provides venue access, paid media ad spend billed directly to client credit card)
- Explicit exclusions (e.g., government permit fees, hotel accommodation for external VIPs)

## Neural Handoff Contract

When complete, output:
- `pricing_engine`: Internal calculation model (`templates/pricing-model.xlsx`)
- `client_boq`: Populated `templates/boq.csv`
- `payment_milestones`: Cashflow schedule
- `commercial_assumptions`: Commercial terms and exclusions
- Target Continuation: Hand off directly to **`scope-reconciliation`**

## Progressive Resources
- `references/financial-modeling.md`
- `templates/pricing-model.xlsx`
- `templates/boq.csv`
- `templates/assumptions-register.csv`
