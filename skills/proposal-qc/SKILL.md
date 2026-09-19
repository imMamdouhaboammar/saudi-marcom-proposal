---
name: proposal-qc
description: "Conduct independent adversarial red-team review and final quality assurance for Saudi MarCom technical and financial proposals. Use when auditing a completed bid package before client submission to falsify compliance, catch ungrounded claims, detect confidential data leakage, verify arithmetic, and prevent disqualifications. Do NOT use for initial drafting, price estimation, or routine spelling fixes."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - technical_outline
  - deliverable_map
  - client_boq
  - requirement_ledger
  - reconciliation_certificate
requires:
  - source_grounding
produces:
  - qc_report
  - submission_status
  - blocker_log
gates:
  - zero_unresolved_blockers
  - zero_client_data_leakage
  - compliance_falsification
neural_links:
  precursors:
    - scope-reconciliation
  continuations:
    - artifact-assembler
  lateral_peers: []
  recovery: proposal-qc
---

# Proposal Red-Team & Quality Control

Execute independent adversarial falsification before proposal submission.

## Mission

Act as an independent client evaluator and legal/commercial red team to challenge and audit the entire proposal package, discovering compliance flaws, ungrounded claims, arithmetic defects, or confidential data leaks before the client sees them.

## Activation Contract

Activate when:
- Conducting final quality assurance on a completed proposal draft
- Evaluating compliance against RFP evaluation criteria and mandatory qualification gates
- Auditing the text for residual competitor names, prior client identifiers, or placeholder tags
- Issuing the formal `qc_report` and go/no-go `submission_status`

Do NOT activate for:
- Initial requirement analysis (use `rfp-forensics`)
- Proposal narrative authoring (use `technical-architect`)
- Packaging documents into final file formats (use `artifact-assembler`)

## Non-Negotiable Invariants

1. **Independent Evaluation Lens**: Red-team review must attempt to disqualify or penalize the proposal as a tough government evaluator would. Never rubber-stamp a draft.
2. **Blocking Finding Veto**: Any critical finding (e.g., missed mandatory clause, arithmetic mismatch, client data leak, missing portal attachment) immediately blocks final release (`STATUS: BLOCKED`).
3. **Evidence Requirement**: Every assertion of failure or pass must cite exact line numbers, clause references, or formula checks.

## Execution Procedure

### Step 1: Compliance Falsification Audit
Check against `requirement_ledger` and `templates/compliance-matrix.csv`:
- Is every mandatory requirement explicitly and visibly answered?
- Are all requested company certifications, licenses, and permits attached?
- Does the team CV structure satisfy minimum years of experience and Saudization rules?
- Are mandatory submission forms and signed declarations present?

### Step 2: Factual Grounding & Anti-Hallucination Scan
Audit every factual statement in the technical proposal:
- Flag ungrounded claims (e.g., "we have 99% reach", "we guarantee zero negative sentiment")
- Check that all cited case studies are verified and authorized
- Flag invented dates, fictitious client quotes, or unsupported performance metrics

### Step 3: Confidentiality & Leakage Scrub
Execute comprehensive pattern search:
- Search for names of past clients, unredacted third-party rates, internal cost estimates
- Search for lingering template markers: `[CLIENT NAME]`, `[DATE]`, `[XXX]`, `TODO`
- Verify that metadata in source files (author properties, revision history) is scrubbed

### Step 4: Arithmetic & Financial Consistency Check
Confirm `reconciliation_certificate` validity:
- Re-verify BOQ totals and VAT line items
- Verify that no conflicting numbers appear in the executive summary or technical text

### Step 5: Arabic Language, RTL & Presentation Review
- Check Arabic grammar, tone (formal official Arabic suitable for Saudi ministries/PIF entities)
- Ensure bidirectional text (English acronyms embedded in Arabic sentences) renders with correct punctuation and flow
- Check that table alignments and numbering sequences are consistent

### Step 6: Verdict & Blocker Log Generation
Compile `templates/final-qc-checklist.md` into `qc_report`:
- **BLOCKING ISSUES**: Disqualifying items that halt release
- **MAJOR ISSUES**: Significant risks that weaken evaluation score
- **POLISH ITEMS**: Minor stylistic or aesthetic improvements
- Set `submission_status`: `READY` | `REVISIONS_REQUIRED` | `BLOCKED`

## Neural Handoff Contract

When complete, output:
- `qc_report`: Detailed audit findings (`templates/final-qc-checklist.md`)
- `submission_status`: Go / No-Go verdict
- `blocker_log`: Action items for remediation
- Target Continuations: Hand off to **`artifact-assembler`** on `READY`; route back to originating skill on `BLOCKED`.

## Progressive Resources
- `references/final-qc.md`
- `references/writing-and-rtl.md`
- `templates/final-qc-checklist.md`
