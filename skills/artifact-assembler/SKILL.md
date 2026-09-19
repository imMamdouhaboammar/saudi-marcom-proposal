---
name: artifact-assembler
description: "Assemble, format, and package final Saudi proposal submission deliverables in DOCX, PPTX, XLSX, PDF, or structured Markdown. Use when compiling validated technical proposals, financial BOQs, compliance matrices, and supporting ledgers into client-ready submission packages adhering to Arabic RTL layouts and portal file caps. Do NOT use for narrative generation, price estimation, or quality auditing."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - technical_outline
  - client_boq
  - requirement_ledger
  - qc_report
requires:
  - source_grounding
produces:
  - technical_proposal_doc
  - financial_proposal_doc
  - ledgers_bundle
  - final_handoff
gates:
  - format_specification_compliance
  - rtl_layout_fidelity
  - portal_submission_packaging
neural_links:
  precursors:
    - proposal-qc
  continuations:
    - submission-complete
  lateral_peers: []
  recovery: proposal-qc
---

# Deliverable Production & Artifact Assembler

Compile, format, and package client-ready proposal submission deliverables.

## Mission

Take validated technical copy, reconciled financial models, compliance matrices, and ledgers, and compile them into clean, beautifully formatted submission artifacts adhering to Saudi typography, RTL standards, and portal submission packaging requirements.

## Activation Contract

Activate when:
- Compiling approved proposal texts into final document formats (DOCX, PPTX, XLSX, PDF, Markdown)
- Formatting Arabic or bilingual documents with proper Right-to-Left (RTL) hierarchy and typography
- Bundling technical and financial offers into separate or combined archives according to tender rules
- Verifying file size limits and naming conventions for portal upload (e.g., Etimad, Ariba)

Do NOT activate for:
- Writing or revising technical scope (use `technical-architect`)
- Re-calculating financial lines or discounts (use `commercial-modeler`)
- Conducting quality control reviews (use `proposal-qc`)

## Non-Negotiable Invariants

1. **Separation of Offers**: By default, technical and financial deliverables must be saved into separate files/folders unless the client explicitly requests a merged file.
2. **Form Preservation**: Mandatory government templates and vendor declaration sheets must retain their original structure and layout.
3. **RTL & Bidi Fidelity**: Arabic headings, body text, tables, and page numbering must strictly align Right-to-Left without font distortion or reversed bracket artifacts.

## Execution Procedure

### Step 1: Format & Platform Verification
Inspect submission constraints from `source-intake`:
- Requested file types: Word (.docx), PowerPoint (.pptx), Excel (.xlsx), PDF (.pdf)
- Portal file size limits (e.g., Etimad 50MB per attachment, email 15MB cap)
- Separate or single submission archive

### Step 2: Technical Proposal Assembly
Assemble the technical document:
- Front matter: Cover page, Table of Contents, Document Control, Executive Summary
- Core sections: Methodology, Scope, Deliverables, Team, Schedule, Risk Register
- Appendices: Compliance Matrix, Case Studies, Certifications, CVs
- Apply formal Arabic typography (e.g., DIN Next LT Arabic, GE SS Unique, Arial) with clean hierarchy (H1, H2, H3)

### Step 3: Financial Offer & BOQ Assembly
Assemble the financial document:
- Formal financial cover letter / commercial declaration on company letterhead
- Populated Client BOQ (`templates/boq.csv` or `templates/pricing-model.xlsx`)
- Milestone cashflow schedule and price validity clause
- Clear 15% VAT statement and payment terms

### Step 4: Ledger Bundle Generation
Compile internal verification ledgers into an audit-ready appendix:
- `templates/requirement-ledger.csv`
- `templates/compliance-matrix.csv`
- `templates/risk-register.csv`
- `templates/assumptions-register.csv`
- `templates/source-ledger.csv`
- `templates/final-qc-checklist.md` (QC report)

### Step 5: Final Submission Package & Naming
Apply clean, descriptive naming conventions:
- `[BidderName]_[ProjectName]_Technical_Proposal_v1.0.pdf`
- `[BidderName]_[ProjectName]_Financial_Proposal_v1.0.pdf`
- `[BidderName]_[ProjectName]_Audit_Ledgers_v1.0.zip`

## Neural Handoff Contract

When complete, output:
- `technical_proposal_doc`: Final technical artifact
- `financial_proposal_doc`: Final commercial artifact
- `ledgers_bundle`: Complete traceability folder
- `final_handoff`: Delivery package ready for client/portal submission

## Progressive Resources
- `tools/artifact-output-contract.md`
- `references/writing-and-rtl.md`
- `templates/technical-proposal-outline.md`
- `templates/financial-offer-outline.md`
