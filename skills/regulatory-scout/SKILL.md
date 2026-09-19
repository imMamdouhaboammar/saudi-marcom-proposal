---
name: regulatory-scout
description: "Research and verify Saudi regulatory requirements, procurement procedures, tax rules, and operational permits relevant to MarCom proposals. Use when validating Etimad government procurement rules, local content requirements, ZATCA VAT/e-invoicing rules, PDPL data privacy, GCAM media licensing, or GEA event permits. Do NOT use for generic market research, creative copywriting, or legal opinions."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
  - situation_classification
requires:
  - source_grounding
produces:
  - regulatory_source_ledger
  - applicability_flags
  - compliance_citations
gates:
  - relevance_gated_only
  - authority_url_verification
  - non_legal_advice_boundary
neural_links:
  precursors:
    - rfp-forensics
  continuations:
    - technical-architect
    - commercial-modeler
  lateral_peers:
    - rfp-forensics
  recovery: regulatory-scout
---

# Saudi Regulatory & Freshness Scout

Verify and cite live Saudi regulatory rules strictly relevant to proposal scope.

## Mission

Ensure the proposal adheres to current Saudi Arabian laws, authority decrees, tax codes, data privacy guidelines, media regulations, and event permitting procedures without bloating the bid with generic research.

## Activation Contract

Activate when:
- Government tenders requiring Etimad procurement compliance or Local Content declarations
- Commercial offers requiring ZATCA VAT treatment (15%) or e-invoicing provisions
- Solutions handling personal data, audience monitoring, or AI databases requiring PDPL compliance
- Communications scopes involving advertising licensing (Mawthooq, GCAM permits)
- Event management requiring GEA, civil defense, or municipal permits

Do NOT activate for:
- Writing general project methodology (use `technical-architect`)
- Unrelated legal drafting or corporate bylaws
- Endless generic Vision 2030 macro summaries with no bearing on tender evaluation

## Non-Negotiable Invariants

1. **Relevance Gating**: Never research or cite a regulation that does not directly impact the scope, risk, compliance, or pricing of this specific tender.
2. **Freshness & Provenance**: Every cited regulation must include the issuing authority name, decree/document title, verified URL, and date checked.
3. **No Unlicensed Legal Advice**: If regulatory applicability is disputed or ambiguous, flag it as a contractual dependency for client confirmation.

## Execution Procedure

### Step 1: Regulatory Domain Mapping
Check which regulatory domains are triggered by the requirement ledger:
- **Government Procurement**: Government Tender & Procurement Law (GTPL) via Etimad portal
- **Local Content**: Local Content & Government Procurement Authority (LCGPA) baseline and mandatory lists
- **Taxation**: ZATCA 15% VAT, withholding tax on foreign suppliers, e-invoicing Phase 2 requirements
- **Data Protection**: Saudi Personal Data Protection Law (PDPL) & SDAIA regulations regarding data residency, consent, and cross-border transfer
- **Media & Advertising**: General Authority of Media Regulation (GCAM) content licenses and Mawthooq influencer advertiser permits
- **Events & Entertainment**: General Entertainment Authority (GEA) licensing, filming permits, drone approvals, and safety requirements

### Step 2: Live Authority Verification
For each triggered domain:
- Verify the current statutory requirement
- Check whether recent amendments alter bidding eligibility or cost calculations
- Record findings in `templates/source-ledger.csv`:
  - `domain`: e.g., Tax / Media / Privacy / Events
  - `authority`: e.g., ZATCA, GCAM, SDAIA, Etimad
  - `citation`: Law name / Article number / Portal guideline
  - `timestamp`: Date verified
  - `bid_implication`: Exact effect on technical scope or financial pricing

### Step 3: Synthesis for Downstream Nodes
- **For `technical-architect`**: Provide exact regulatory compliance language, operational safety measures, and governance controls.
- **For `commercial-modeler`**: Provide statutory cost lines (permit fees, withholding taxes, VAT inclusion/exclusion rules, local content baseline commitments).

## Neural Handoff Contract

When complete, output:
- `regulatory_source_ledger`: Log of verified regulations and citations
- `applicability_flags`: Boolean flags for active regulatory gates
- `compliance_citations`: Formatted text blocks for proposal insertion
- Target Continuations: Hand off to **`technical-architect`** and **`commercial-modeler`**

## Progressive Resources
- `references/saudi-regulatory-freshness.md`
- `templates/source-ledger.csv`
