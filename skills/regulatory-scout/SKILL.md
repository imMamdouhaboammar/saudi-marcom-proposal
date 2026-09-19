---
name: regulatory-scout
description: "Resolve current Saudi regulatory and procurement obligations that materially affect a MarCom bid, including procurement, local content, tax, personal data, media/advertising, events, and triggered digital controls. Use when a proposal contains a current compliance claim, permit dependency, tax treatment, government submission rule, or regulated data/media activity. Do NOT use for generic legal research, legal opinions, or unrelated macro summaries."
version: 0.3.0
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
  - regulatory_effective_state
gates:
  - relevance_gated_only
  - official_source_preference
  - effective_state_verified
  - non_legal_advice_boundary
neural_links:
  precursors: [rfp-forensics]
  continuations: [technical-architect, commercial-modeler]
  lateral_peers: [service-router, bid-strategist]
  recovery: regulatory-scout
---

# Saudi Regulatory Effective-State Resolver

Research only regulatory domains that change scope, risk, submission, or price.

## Core rule

An announcement is not an effective rule until the effective state is verified.

Read `references/regulatory-state-resolver.md` before making a current compliance claim.

## Trigger map

Potential domains:
- government procurement and Etimad
- local content and mandatory lists
- VAT, withholding, e-invoicing, or other tax treatment
- PDPL and cross-border personal data transfer
- media, publishing, advertising, influencer, or content licensing
- entertainment/event permits and supplier accreditation
- cybersecurity or telecom controls when the technical scope actually triggers them
- sector-specific buyer rules named in the RFP

Do not activate every domain by default.

## Source hierarchy

Prefer:
1. current RFP, addenda, and buyer submission instructions for bid-specific obligations
2. official Saudi authority pages, regulations, gazette publications, and official service pages
3. official government news for announcements
4. secondary legal commentary only to locate issues that must then be verified against primary sources

## Effective-state record

For each material rule, record:
- `reg_id`
- domain
- authority
- instrument or service
- status: `ANNOUNCED | ENACTED | EFFECTIVE | SUPERSEDED | UNKNOWN`
- publication date if known
- effective date if verified
- checked timestamp
- official URL
- exact bid implication
- technical implication
- commercial implication
- unresolved question

If status is `ANNOUNCED`, `ENACTED`, or `UNKNOWN`, do not write "we comply with the current requirement" unless the obligation is independently shown to apply.

## Current authority naming

Use the authority name shown on the current official source. Do not preserve stale acronyms from old proposals.

For media regulation, verify the current General Authority for Media Regulation source and service name before inserting licensing language.

## Tax behavior

Never treat a tax percentage as timeless configuration.

Commercial modeling receives tax parameters from:
- current official tax source
- prescribed buyer BOQ
- explicit buyer instruction

If they conflict, block finalization and request resolution.

## Data and AI behavior

When personal data is in scope:
- identify controller/processor questions
- classify data categories and purpose
- identify hosting and cross-border transfer
- identify retention and access assumptions
- verify applicable SDAIA/DGP requirements
- pass technical safeguards and commercial dependencies downstream

Do not claim PDPL compliance solely because a cloud vendor advertises compliance.

## Events behavior

For event or entertainment scope:
- classify the actual event type first
- verify the relevant current official permit/service
- record application lead time and supplier prerequisites only from current sources
- propagate permit lead time into schedule and pricing assumptions

## Failure taxonomy

- stale authority naming
- announced-vs-effective confusion
- regulation dumping with no scope relevance
- secondary-source-only legal claim
- permit assumed without event classification
- tax hardcoding
- privacy claim with no data-flow evidence

## Handoff

Append the effective-state ledger and applicability flags to `bid_state`.

Downstream nodes receive implications, not a generic legal memo.
