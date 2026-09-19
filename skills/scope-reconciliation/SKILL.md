---
name: scope-reconciliation
description: "Perform strict bidirectional reconciliation between technical deliverables and commercial pricing lines for Saudi proposals. Use when validating that every technical deliverable is accounted for financially, every line in the BOQ has a technical purpose, quantities and dates match exactly, and arithmetic is verified. Do NOT use for initial solution design, pricing creation, or graphic formatting."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - deliverable_map
  - pricing_engine
  - client_boq
requires:
  - source_grounding
produces:
  - scope_price_map
  - mismatch_report
  - reconciliation_certificate
gates:
  - 100_percent_bidirectional_coverage
  - quantity_and_unit_parity
  - arithmetic_integrity
neural_links:
  precursors:
    - technical-architect
    - commercial-modeler
  continuations:
    - proposal-qc
  lateral_peers: []
  recovery: scope-reconciliation
---

# Scope-Price Reconciliation Engine

Execute rigorous bidirectional reconciliation between technical promises and commercial prices.

## Mission

Guarantee that the technical proposal and financial proposal are 100% harmonized, eliminating unpriced commitments, unsupported price lines, quantity mismatches, and arithmetic defects before independent QC.

## Activation Contract

Activate when:
- Both technical scope (`deliverable_map`) and commercial pricing (`client_boq` / `pricing_engine`) have been drafted
- Verifying whether all promised technical work is funded and accounted for
- Checking that client-facing BOQ lines correspond to tangible technical scope
- Validating arithmetic, unit consistency, VAT formulas, and milestone logic

Do NOT activate for:
- Drafting new technical methodologies (use `technical-architect`)
- Calculating unit rates from scratch (use `commercial-modeler`)
- Conducting general RFP clause extraction (use `rfp-forensics`)

## Non-Negotiable Invariants

1. **Zero Unpriced Commitments**: Every single deliverable in the technical offer must be priced, explicitly marked as included at zero cost, client-supplied, or formally listed as an optional extra.
2. **Zero Unsupported Charges**: Every price item in the BOQ must have a clear technical justification in the technical proposal.
3. **Quantity & Schedule Parity**: Quantities (e.g., number of videos, days of events, monthly reports) and delivery durations must match verbatim across both documents.

## Execution Procedure

### Step 1: Forward Traceability Check (Technical $\to$ Financial)
Iterate through every entry in the `deliverable_map`:
- Does an equivalent line exist in the `client_boq` or internal cost model?
- If not:
  - Is it explicitly documented as "Included at no additional cost"?
  - Is it documented as "Client Responsibility / Supplied by Client"?
  - Is it an "Optional Add-on"?
- If none of the above: **RECONCILIATION FAILS** $\to$ Flag as `UNPRICED TECHNICAL DELIVERABLE`.

### Step 2: Backward Traceability Check (Financial $\to$ Technical)
Iterate through every line item in the `client_boq`:
- Does this line correspond to a deliverable or operational workstream in the technical proposal?
- If not: **RECONCILIATION FAILS** $\to$ Flag as `UNSUPPORTED COMMERCIAL LINE`.

### Step 3: Metric & Quantity Parity Verification
Verify exact numeric agreement:
- Check quantities: Does the technical proposal say "12 monthly reports" while the BOQ prices "10"?
- Check event durations: Does the technical plan say "3-day exhibition" while BOQ prices "2 days"?
- Check staffing levels: Do team roles in the governance section match the FTEs priced in the rate card?

### Step 4: Arithmetic & Tax Formula Audit
Recalculate all formulas independently:
- Unit Price $\times$ Quantity = Line Subtotal
- Sum of Line Subtotals = Total Exclusive of VAT
- VAT = Total Exclusive $\times$ 15% (or 0% if exempt/zero-rated with proof)
- Grand Total = Total Exclusive + VAT
- Check rounding errors (must match to 2 decimal places in SAR)

### Step 5: Disposition & Reconciliation Certificate
- If any discrepancy is found: Generate `mismatch_report` and route back to `technical-architect` or `commercial-modeler` for remediation.
- If 100% matched: Issue `reconciliation_certificate` clearing the proposal for `proposal-qc`.

## Neural Handoff Contract

When complete, output:
- `scope_price_map`: 1:1 cross-reference ledger
- `mismatch_report`: Discrepancy log (if failed)
- `reconciliation_certificate`: Cryptographic/hash clearance token (if passed)
- Target Continuation: Hand off to **`proposal-qc`** on pass; bounce back to **`technical-architect`** / **`commercial-modeler`** on fail.

## Progressive Resources
- `references/financial-modeling.md`
- `references/technical-proposal-anatomy.md`
- `templates/boq.csv`
