---
name: source-intake
description: "Ingest, inventory, version, and confidentiality-screen Saudi MarCom bid sources before any proposal reasoning begins. Use when receiving RFPs, addenda, briefs, meeting notes, buyer forms, bidder evidence, prior references, rate cards, or supplier quotes. Do NOT use for clause analysis, technical drafting, price invention, or unrelated tender domains."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - rfp_documents
  - organization_context
  - bidder_evidence
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
  continuations: [rfp-forensics]
  recovery: source-intake
---

# Source Intake

Establish what is known, where it came from, and what is safe to reuse.

## Source classes

Classify every received item:
- current buyer RFP / TOR
- addendum or formal clarification
- mandatory buyer form
- meeting/email/brief evidence
- verified bidder-owned fact
- approved rate card or commercial policy
- supplier quote
- past proposal/reference pattern
- public source
- assumption

## Source receipt

For every material source record:
- source ID
- title/filename
- source class
- issuer/owner
- version or issued date
- received/fetched date
- effective date if relevant
- authority/preference level
- confidentiality level
- allowed use: factual / structural-only / pricing-only / client-output-safe
- supersedes / superseded-by relationship

No phantom source may enter the state.

## Situation classification

Populate:
- operating mode
- buyer type
- output required
- deadline
- submission channel
- languages
- service families indicated
- evidence health
- pricing health
- personal-data sensitivity
- mandatory buyer forms present/missing
- addenda/clarification status

## Confidentiality quarantine

Past proposals and private references are structural-only by default.

Quarantine:
- prior client names where reuse is not authorized
- rates and margins
- bank/account information
- private performance claims
- proprietary language tied to another engagement
- personal data not needed for the bid

A quarantined source may still teach structure, never facts.

## Contradiction preflight

Detect obvious source-level conflicts:
- two RFP versions
- addendum vs original clause
- buyer form vs narrative
- user brief vs mandatory buyer instruction

Do not decide the substantive requirement here. Mark the conflict and hand it to rfp-forensics.

## Failure taxonomy

- Stale pack: newer addendum exists but old RFP is treated as current
- Source laundering: a prior proposal becomes current factual evidence
- Confidentiality contamination: sensitive old-client material enters the active corpus
- Missing mandatory form: drafting proceeds without the buyer's required template
- Untraceable meeting fact: an informal note is presented as formal buyer instruction
- Commercial ambiguity: a price input exists but ownership/date/currency is unknown

## Handoff

Append source receipts, situation classification, confidentiality flags, and visible source conflicts to bid_state.

Continue only when the material source set is cataloged enough for requirement extraction.
