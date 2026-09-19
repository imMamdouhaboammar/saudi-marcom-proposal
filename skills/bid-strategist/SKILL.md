---
name: bid-strategist
description: "Convert Saudi RFP scoring, buyer context, evidence strength, scope constraints, and bidder facts into a response strategy before technical drafting. Use when a bid needs evaluation-weighted emphasis, win-theme selection, evidence planning, executive-message architecture, or a bid/no-bid risk view. Do NOT use for clause extraction, final prose, price calculation, or unsupported competitor speculation."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
  - evaluation_map
  - situation_classification
  - active_service_modules
  - bidder_evidence
requires:
  - source_grounding
produces:
  - response_strategy
  - scoring_coverage_plan
  - evidence_plan
  - win_theme_register
  - executive_message_map
gates:
  - evaluation_weight_alignment
  - evidence_supported_differentiation
  - no_competitor_speculation
  - no_unpriced_value_add
neural_links:
  precursors:
    - rfp-forensics
    - service-router
  continuations:
    - technical-architect
    - commercial-modeler
  lateral_peers:
    - regulatory-scout
  recovery: rfp-forensics
---

# Bid Strategist

Design the response strategy before the proposal becomes prose.

## Mission

Turn the buyer's scoring model, mandatory requirements, known organizational context, verified bidder evidence, service architecture, and commercial constraints into a response plan that tells downstream skills what deserves emphasis, what evidence must appear, and where the bid is weak.

A compliant bid can still be generic. This skill exists to prevent that failure.

## Activation

Activate when:
- an RFP has scoring criteria or qualitative evaluation dimensions
- a private or semi-government pitch needs an explicit decision narrative
- the user asks how to make the response more tailored or persuasive
- credentials, cases, team evidence, methodology, and value-add must be allocated to specific evaluation criteria
- a bid has limited page count or presentation time and prioritization matters

Do not activate for:
- raw requirement extraction
- invented competitive intelligence
- final client-facing copy
- unsourced promises or pricing

## Situation Classification

Classify the bid across these dimensions before choosing strategy:

| Dimension | Values | Why it changes the response |
| --- | --- | --- |
| buyer type | government / semi-government / private | changes compliance, evidence and decision emphasis |
| evaluation mode | pass-fail / weighted technical / technical-commercial / negotiated pitch | changes prioritization |
| evidence strength | strong / mixed / weak / missing | controls claim confidence |
| scope certainty | fixed / partially defined / outcome-led | controls assumptions and modularity |
| commercial state | priced / quote-dependent / incomplete | limits value-add and optionality |
| decision audience | procurement / technical / executive / mixed | changes information altitude |
| submission mode | document / deck / portal forms / presentation | changes answer architecture |

## Procedure

### 1. Build the scoring coverage plan

For each scored criterion:
- preserve the buyer's exact criterion and weight
- map mandatory evidence
- assign one primary response section
- assign one proof source
- identify a disqualification or scoring risk
- define what would count as an excellent answer without inventing buyer preferences

Never convert an inferred preference into a stated buyer fact.

### 2. Separate table stakes from differentiators

Create four buckets:
- mandatory compliance
- expected competence
- evidence-backed differentiator
- optional value-add

A differentiator must satisfy all three:
1. relevant to a scored or decision-critical need
2. supported by evidence or an executable mechanism
3. commercially funded or explicitly optional

### 3. Build win themes

A win theme is not a slogan. Use this structure:

`buyer priority -> delivery mechanism -> evidence -> measurable consequence`

Examples:
- "High-volume approvals -> single approval queue and escalation model -> named governance roles -> lower approval ambiguity"
- "Seasonal surge -> shift-based content room with fallback staffing -> verified relevant experience -> sustained coverage under peak load"

Do not write "best", "leading", "unique", or similar claims without proof.

### 4. Allocate proof

For every meaningful claim, choose one:
- RFP fact
- official external source
- verified bidder credential
- verified case result
- operating design that can be inspected
- explicit assumption

If no proof exists, weaken or remove the claim.

### 5. Design executive message architecture

Create:
- one-sentence problem framing
- one-sentence response idea
- 3 to 5 decision pillars
- evidence per pillar
- top risks and how the operating model controls them
- commercial logic summary without exposing price inside a technical-only response

### 6. Run strategy pressure test

Fail the strategy if any of these are true:
- high-weight criteria receive shallow coverage
- low-weight decoration dominates the proposal
- a value-add creates unfunded scope
- a case study is impressive but irrelevant
- a claim relies on generic Vision 2030 language rather than project relevance
- the response copies the RFP without showing operating decisions
- the executive summary promises outcomes unsupported by the delivery model

## Handoff

Output:
- `response_strategy`
- `scoring_coverage_plan`
- `evidence_plan`
- `win_theme_register`
- `executive_message_map`

Hand off to `technical-architect` and, where value-add or optionality affects cost, `commercial-modeler`.

## Progressive Resources

- `references/buyer-and-bid-strategy.md`
- `references/evaluation-engineering.md`
- `references/source-and-evidence-policy.md`
