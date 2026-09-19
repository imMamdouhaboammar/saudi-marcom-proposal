---
name: source-intake
description: "Ingest, catalog, and screen RFP documents, briefs, appendices, rate cards, and prior materials for Saudi MarCom bids. Use when receiving incoming tender files, client meeting notes, pitch briefs, or pricing data to establish a verified source inventory, classify bid parameters, and screen for client confidential leakage. Do NOT use for writing proposal sections, estimating prices, or civil/construction tenders."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - rfp_documents
  - organization_context
  - reference_work
  - pricing_inputs
requires:
  - source_grounding
produces:
  - source_inventory
  - situation_classification
  - confidentiality_flags
gates:
  - zero_client_leakage
  - version_freshness
  - source_precedence_locking
neural_links:
  precursors: []
  continuations:
    - rfp-forensics
  lateral_peers: []
  recovery: proposal-recovery
---

# Source Intake & Preflight

Ingest, inventory, and screen incoming tender materials before drafting starts.

## Mission

Turn raw bid inputs (RFPs, addenda, client brief emails, rate cards, case decks) into a structured, verified `source_inventory` and `situation_classification` while strictly isolating past confidential client data.

## Activation Contract

Activate when:
- Receiving initial RFP documents, briefs, or tender packs for Saudi bids
- Cataloging received files, version dates, addenda, and clarification notes
- Classifying bid constraints (buyer type, deadline, language, required deliverables)
- Screening reference materials to prevent client data leakage

Do NOT activate for:
- Detailed clause-by-clause requirement extraction (use `rfp-forensics`)
- Proposal narrative drafting (use `technical-architect`)
- Commercial calculation (use `commercial-modeler`)

## Non-Negotiable Invariants

1. **Source Precedence Locking**: Order of authority is: (1) signed clarifications/current instructions, (2) current RFP & official addenda, (3) official Saudi authorities, (4) verified bidder facts, (5) prior proposal patterns only.
2. **Confidentiality Quarantine**: Past client names, commercial rates, bank details, or proprietary phrases must be flagged and isolated immediately.
3. **No Phantom Files**: Every cataloged source must have a concrete filename, receipt timestamp, and origin.

## Execution Procedure

### Step 1: Document Cataloging
Inspect all received files in the workspace:
- File name, file format, version date, and source authority
- Record in `templates/source-ledger.csv`:
  - `source_id`: S-01, S-02...
  - `document_name`: e.g., RFP_Main.pdf, Addendum_1.docx
  - `source_type`: RFP / Addendum / Client Q&A / Rate Card / Case Study
  - `effective_date`: Date of issuance
  - `authority_level`: 1 (highest) to 5 (reference only)

### Step 2: Situation Classification
Classify the bid along 8 operational dimensions:
- **Buyer**: Government (Etimad rules) / Semi-Gov / Private
- **Input Quality**: Full RFP / Partial Brief / Meeting Notes
- **Required Output**: Technical Proposal / Financial Proposal / Both
- **Deadline Urgency**: Standard (>10 days) / Accelerated (4-10 days) / Critical (<4 days)
- **Scope Families**: Media & Comms / Marketing / Events / Crisis / Digital & AI / Monitoring
- **Evidence Health**: Complete / Partial / Contradictory
- **Data Sensitivity**: Public / Private Commercial / Personal Data (PDPL)
- **Commercial State**: Rates provided / Quotes pending / Cost model missing

### Step 3: Confidentiality & Leakage Screening
Run static scan across all reference materials:
- Search for past client identifiers, unredacted fee tables, or proprietary competitor names
- Flag any contaminated reference as `QUARANTINED`
- Allow structural reuse only, never factual reuse

### Step 4: Missing Input Ledger
Identify blocking gaps before handoff:
- Missing mandatory BOQ format?
- Missing submission deadline or platform guidelines?
- Missing commercial rates or third-party allowances?

## Neural Handoff Contract

When complete, output:
- `source_inventory`: Validated table of available sources
- `situation_classification`: 8-dimension profile
- `confidentiality_flags`: Quarantine log
- Target Continuation: Hand off directly to **`rfp-forensics`**

## Progressive Resources
- `references/source-and-evidence-policy.md`
- `templates/source-ledger.csv`
- `templates/intake-brief.yaml`
