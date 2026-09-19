---
name: rfp-forensics
description: "Extract, catalog, and map every clause, requirement, scoring criterion, and mandatory form from Saudi RFP documents into a Requirement Ledger and Compliance Matrix. Use when analyzing tender documents, RFP specifications, terms of reference (TOR), or client briefs to build full requirement traceability before proposal drafting. Do NOT use for generic text summarization, technical narrative writing, or pricing calculations."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - source_inventory
  - rfp_documents
requires:
  - source_grounding
produces:
  - requirement_ledger
  - compliance_matrix
  - evaluation_map
  - clarification_log
gates:
  - 100_percent_clause_attribution
  - mandatory_form_preservation
  - zero_ungrounded_requirements
neural_links:
  precursors:
    - source-intake
  continuations:
    - regulatory-scout
    - service-router
  lateral_peers:
    - claims-compliance-auditor
  recovery: source-intake
---

# RFP Forensics & Requirement Ledger

Deconstruct RFP clauses into an exhaustive, traceable requirement model.

## Mission

Perform forensic analysis on tender documents to extract all mandatory conditions, technical specifications, evaluation weights, quantities, and submission forms into a structured Requirement Ledger.

## Activation Contract

Activate when:
- Analyzing Saudi RFP packs, terms of reference (TOR), or brief documents
- Extracting technical deliverables, service level agreements (SLAs), and submission requirements
- Mapping evaluation criteria and scoring weights
- Building the formal `requirement_ledger` or `compliance_matrix`
- Logging contradictions or ambiguities for client clarification

Do NOT activate for:
- Writing the narrative solution (use `technical-architect`)
- Commercial pricing models (use `commercial-modeler`)
- Final proofreading or QC (use `proposal-qc`)

## Non-Negotiable Invariants

1. **Every Requirement Sourced**: Never record a requirement without its specific document name, section number, and clause citation.
2. **Preserve Form Integrity**: Never alter, redesign, or skip mandatory government tables or prescribed BOQ formats.
3. **Traceability**: Every item in the ledger must map forward to a proposal section, deliverable ID, and commercial line.

## Execution Procedure

### Step 1: Clause Extraction
Decompose the RFP into structured rows:
- `req_id`: Unique key (REQ-001, REQ-002...)
- `source_ref`: Document name + Section/Clause number
- `category`: Technical / Commercial / Operational / Governance / Mandatory Attachment
- `classification`: Mandatory (Pass/Fail) / Scored (Weight %) / Informational / Ambiguous
- `exact_text`: Verbatim requirement excerpt

### Step 2: Evaluation Scoring Model
Extract the buyer's evaluation rubric:
- Technical scoring criteria, sub-criteria, and percentage weights
- Minimum technical qualification threshold (e.g., 70% or 80%)
- Commercial weight vs Technical weight (e.g., 60/40 or 70/30)
- Highlight high-weight scoring areas for strategic emphasis

### Step 3: Operational Constraints Ledger
Extract all non-functional requirements:
- Delivery locations across Saudi Arabia (e.g., Riyadh, Jeddah, NEOM, Eastern Province)
- Turnaround times, SLAs, and emergency response times (e.g., 2-hour crisis response)
- Team residency and key personnel requirements (e.g., full-time on-site, Saudi national quotas)
- Mandatory portal submission rules (Etimad, vendor portals, email zip caps)

### Step 4: Clarification Log
Identify contradictions, ambiguities, or missing information:
- Document the discrepancy
- Draft the exact inquiry text for formal client submission
- Record working assumptions until clarification is answered

## Neural Handoff Contract

When complete, output:
- `requirement_ledger`: `templates/requirement-ledger.csv` populated
- `compliance_matrix`: `templates/compliance-matrix.csv` initialized
- `evaluation_map`: Scoring breakdown table
- `clarification_log`: Formal inquiry list
- Target Continuations: Hand off concurrently to **`regulatory-scout`** and **`service-router`**

## Progressive Resources
- `references/rfp-forensics-and-compliance.md`
- `templates/requirement-ledger.csv`
- `templates/compliance-matrix.csv`
