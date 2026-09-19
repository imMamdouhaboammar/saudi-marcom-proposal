---
name: rfp-forensics
description: "Forensically extract Saudi MarCom RFP requirements, mandatory forms, evaluation criteria, quantities, SLAs, qualifications, submission rules, and contradictions into traceable ledgers. Use after source intake or when reconstructing requirements for a proposal review. Do NOT use for solution prose, final pricing, legal opinions, or generic document summarization."
version: 0.4.0
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
  - material_clause_attribution
  - mandatory_form_preservation
  - zero_silent_contradiction
neural_links:
  precursors: [source-intake]
  continuations: [regulatory-scout, service-router, precedent-miner]
  lateral_peers: [regulatory-scout]
  recovery: source-intake
---

# RFP Forensics

Build the requirement model that every downstream claim and price must trace back to.

## Requirement record

For every material requirement capture:
- requirement ID
- source ID
- exact locator: section, clause, page, table, or row
- concise requirement statement
- exact excerpt when useful
- type: technical / commercial / operational / qualification / submission / form
- status: mandatory / scored / informative / ambiguous
- quantity/unit
- SLA/turnaround
- language/geography
- evidence required
- buyer form dependency
- clarification needed
- downstream owner
- proposal response location
- commercial dependency

Do not split one atomic obligation into unrelated rows when that would hide the full acceptance condition.

## Evaluation map

When explicit scoring exists, capture:
- criterion
- weight
- subcriterion
- threshold/pass-fail condition
- required evidence
- relevant requirement IDs

If weights are absent, store UNKNOWN. Do not infer percentages.

## Mandatory form registry

Record every buyer-supplied form:
- filename
- purpose
- submission stream: technical / financial / qualification
- editable cells/fields if known
- immutable structure requirements
- signature/stamp requirements
- upload format

Mandatory form fidelity is a release gate.

## Contradiction handling

When sources conflict:
1. preserve both source receipts
2. state the exact conflict
3. identify scope/price/submission impact
4. check whether a newer addendum resolves it
5. otherwise add a clarification question
6. if work must continue, create an explicit interim assumption with owner and impact

Never silently select the more reasonable quantity.

## Qualification and submission controls

Extract:
- eligibility/pass-fail conditions
- certificates and attachments
- team/CV requirements
- bonds/guarantees if named
- portal/upload rules
- file separation
- signatures/stamps
- deadline and opening rules
- local-content forms if actually requested

## Failure taxonomy

- missed pass/fail condition
- requirement with no source locator
- scoring weight invented
- buyer form ignored
- contradiction silently normalized
- quantity buried in prose but absent from ledger
- qualification attachment treated as optional
- current addendum not propagated

## Handoff

Append requirement ledger, compliance matrix, evaluation map, form registry, and clarification log to bid_state.

Continue in parallel to regulatory-scout, service-router, and precedent-miner. Bid strategy follows once precedent signals or an explicit empty-precedent result exist.
