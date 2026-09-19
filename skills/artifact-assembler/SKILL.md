---
name: artifact-assembler
description: "Assemble approved Saudi MarCom proposal content into client-safe technical, financial, and supporting artifacts while preserving buyer templates, RTL/LTR behavior, separation rules, and submission packaging. Use only after proposal QC is READY or when the user explicitly requests a non-final draft artifact. Do NOT use to invent scope, claims, or pricing."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - submission_status
  - buyer_forms
  - technical_outline
  - client_boq
  - client_safe_evidence
requires:
  - source_grounding
produces:
  - final_handoff
  - render_validation
gates:
  - client_boundary
  - mandatory_format_fidelity
  - rtl_ltr_integrity
  - render_validation
neural_links:
  precursors: [proposal-qc]
  continuations: [submission-complete]
  recovery: artifact-assembler
---

# Artifact Assembler

Turn approved content into submission artifacts without changing substance.

## Release boundary

For a final package, require `submission_status: READY`.

For a user-requested draft, label every artifact `DRAFT - NOT SUBMISSION READY` and preserve unresolved blockers.

## Artifact contract

Determine required outputs from the RFP or user:
- technical proposal DOCX/PPTX/PDF
- financial proposal XLSX/PDF
- mandatory buyer forms
- appendices/CVs/case evidence
- cover letter
- separate encrypted/compressed package if instructed

Do not combine technical and financial content unless the submission instructions permit it.

## Mandatory form fidelity

If the buyer supplies a form:
- preserve sheet/tab/column/order structure
- populate only allowed fields
- do not redesign it for visual consistency
- keep formulas or protected structure intact where possible
- validate after write

## Client-safe boundary

Exclude unless explicitly required:
- internal pricing engine
- salaries and buy rates
- margin/markup
- private benchmark data
- source ledgers containing confidential prior-client content
- internal red-team comments
- bank details not required by submission
- private working notes

## Arabic and bilingual output

Validate:
- true RTL paragraph and table behavior for Arabic
- correct Arabic punctuation and numeral policy per artifact
- no accidental LTR ordering in Arabic tables
- English remains LTR
- bilingual tables maintain column logic
- fonts render consistently
- Arabic text is not converted to disconnected glyphs

## Render validation

For each final artifact:
- open/render it
- check page/slide overflow
- check clipping and table breaks
- check formulas and totals in spreadsheets
- verify required logos/titles/IDs
- verify file naming
- verify client-safe content boundary

A file existing on disk is not proof that it renders correctly.

## Final handoff

Return:
- file inventory
- submission purpose of each file
- status
- unresolved caveats if draft
- render-validation receipt
- checksum or stable identifier when available
