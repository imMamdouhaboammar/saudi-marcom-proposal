---
name: artifact-assembler
description: "Assemble, format, and package final Saudi proposal submission deliverables in DOCX, PPTX, XLSX, PDF, or structured Markdown. Use when compiling validated technical proposals, financial BOQs, and required client-facing attachments into submission packages that meet Arabic RTL and portal constraints. Do NOT use for narrative generation, price estimation, or quality auditing."
version: 0.2.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - technical_outline
  - client_boq
  - requirement_ledger
  - qc_report
  - submission_status
requires:
  - source_grounding
produces:
  - technical_proposal_doc
  - financial_proposal_doc
  - final_handoff
gates:
  - verified_qc_ready_status
  - format_specification_compliance
  - rtl_layout_fidelity
  - client_ledger_isolation
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

Take validated technical copy, reconciled financial models, and required client-facing attachments, and compile them into submission artifacts that meet Saudi typography, RTL, and portal requirements.

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

1. **Gate on Verified QC READY Status**: Never begin assembly or release deliverables unless `submission_status` is explicitly verified as `READY` from `proposal-qc`. Any `BLOCKED` status halts assembly immediately.
2. **Strict Internal Ledger Isolation**: Audit ledgers (source ledger, internal assumptions, risk register, QC reports) contain confidential client notes, operational margins, and internal reviewer logs. They must remain in an internal-only archive and NEVER be included in the client submission package unless the RFP explicitly mandates their submission.
3. **Separation of Offers**: By default, technical and financial deliverables must be saved into separate files/folders unless the client explicitly requests a merged file.
4. **Preserve Prescribed Tables**: Mandatory government templates and vendor declaration sheets must retain their original structure and layout.
5. **RTL & Bidi Fidelity**: Arabic headings, body text, tables, and page numbering must strictly align Right-to-Left without font distortion or reversed bracket artifacts.

## Execution Procedure

### Step 1: Quality Gate Verification
Verify preconditions before touching files:
- Inspect `submission_status` from `proposal-qc`. If not `READY`, abort assembly and report blockers.
- Inspect submission constraints from `source-intake` (e.g., Word, PowerPoint, Excel, PDF).
- Check portal file size limits (e.g., Etimad 50MB per attachment, email 15MB cap).

### Step 2: Technical Proposal Assembly
Assemble the technical document:
- Front matter: Cover page, Table of Contents, Document Control, Executive Summary
- Core sections: Methodology, Scope, Deliverables, Team, Schedule, Risk Register
- Appendices: Compliance Matrix, Case Studies, Certifications, Key Personnel CVs
- Apply formal Arabic typography (e.g., DIN Next LT Arabic, GE SS Unique, Arial) with clean hierarchy (H1, H2, H3)

### Step 3: Financial Offer & BOQ Assembly
Assemble the financial document:
- Formal financial cover letter / commercial declaration on company letterhead
- Populated Client BOQ (`templates/boq.csv` or `templates/pricing-model.xlsx`)
- Milestone cashflow schedule and price validity clause
- Clear 15% VAT statement and payment terms

### Step 4: Internal Archive & Release Boundary
Segregate artifacts at the release boundary:
- **Client Submission Package**: Contains ONLY client-facing technical and financial proposals and required public appendices.
- **Internal Governance Archive**: Stores internal ledgers (`requirement-ledger.csv`, `source-ledger.csv`, `assumptions-register.csv`, `final-qc-checklist.md`) for corporate records and audit readiness. Do NOT attach to client portal.

### Step 5: Post-Assembly Quality Verification
Verify the compiled files before marking handoff:
- Reconfirm that `submission_status` is `READY`.
- Match every rendered file and attachment against the RFP submission checklist. Reject missing, extra, stale, or incorrectly separated artifacts.
- Inspect DOCX, PPTX, XLSX, PDF, and archive contents for comments, tracked changes, hidden sheets or slides, speaker notes, embedded files, and document metadata. Remove internal or non-required content.
- Confirm that prescribed forms, signatures, appendices, filenames, versions, and client-authorized ledger attachments are complete and unchanged.
- Verify that PDF/DOCX export preserved RTL text alignment and numbering.
- Verify total bundle file size is within portal limits.
- Apply clean naming conventions:
  - `[BidderName]_[ProjectName]_Technical_Proposal_v1.0.pdf`
  - `[BidderName]_[ProjectName]_Financial_Proposal_v1.0.pdf`
- Run the complete final submission checklist against the rendered package. If any check fails, do not emit `final_handoff`; route the defect to its owning skill.

## Neural Handoff Contract

Only after every post-assembly check passes, output:
- `technical_proposal_doc`: Final technical artifact
- `financial_proposal_doc`: Final commercial artifact
- `final_handoff`: Delivery package ready for client/portal submission
- Target Continuation: Hand off to **`submission-complete`**

## Progressive Resources
- `tools/artifact-output-contract.md`
- `references/writing-and-rtl.md`
- `templates/technical-proposal-outline.md`
- `templates/financial-offer-outline.md`
