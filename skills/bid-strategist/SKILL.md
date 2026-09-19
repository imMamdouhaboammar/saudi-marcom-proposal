---
name: bid-strategist
description: "Build the buyer, evaluation, proof, and response strategy for Saudi MarCom bids after requirements are extracted. Use when a proposal needs bid/no-bid evidence, evaluation-weight prioritization, proof placement, differentiator substantiation, decision-role mapping, or a response strategy before drafting. Do NOT use for raw clause extraction, final pricing, visual design, or unsupported persuasion claims."
version: 0.4.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - situation_classification
  - evaluation_map
  - requirement_ledger
  - bidder_evidence
  - benchmark_signals
  - reuse_constraints
requires:
  - source_grounding
produces:
  - bid_posture
  - evaluation_strategy
  - proof_plan
  - response_strategy
gates:
  - buyer_strategy_grounded
  - differentiators_substantiated
  - human_owned_bid_decision
neural_links:
  precursors: [rfp-forensics, precedent-miner]
  continuations: [technical-architect]
  lateral_peers: [service-router, regulatory-scout]
  recovery: rfp-forensics
---

# Bid Strategist

Convert the RFP and bidder evidence into a response strategy before proposal prose is written.

## Activation contract

Activate for:
- evaluation criteria and scoring analysis
- bid/no-bid or conditional bid preparation
- proof planning and evidence gaps
- buyer decision-role mapping
- differentiator selection
- section emphasis and evaluator navigation

Do not activate for:
- requirement extraction
- final pricing
- inventing bidder advantages
- generic brand positioning with no bid context

## Situation classification

Classify the opportunity:
- buyer type
- procurement route
- evaluation transparency: explicit / partial / opaque
- evidence health: strong / mixed / weak
- commercial readiness: grounded / partial / missing
- delivery readiness: proven / plausible / high-risk
- deadline: standard / accelerated / critical

## Decision model

### 1. Bid posture

Return one of:
- `BID`: no known strategic blocker
- `CONDITIONAL`: viable only if named evidence, partner, price, clarification, or delivery dependency is resolved
- `NO_BID_RECOMMENDED`: material qualification or delivery gap exists

The organization owns the final decision. Do not use arbitrary numeric thresholds unless the organization supplied them.

### 2. Evaluation strategy

For every scored criterion:
- criterion and weight if provided
- evaluator question it implies
- evidence needed
- response location
- proof status: verified / pending / unavailable
- consequence if weak

When weights are absent, do not invent them. Use mandatory requirements, repetition, buyer emphasis, clarification questions, and source structure only as labeled signals.

### 3. Proof plan

Precedent signals may shape structure and proof discovery only within their reuse constraints. A prior-proposal claim becomes bidder proof only after fresh bidder-owned verification.

Separate:
- buyer requirements
- bidder facts
- public authoritative facts
- benchmark patterns
- assumptions

A differentiator is usable only if it is:
- relevant to a buyer risk or score
- demonstrably different
- supported by evidence
- operationally true in the proposed model

### 4. Response strategy

Define:
- 3 to 5 response themes
- executive-summary proof points
- sections requiring disproportionate depth because of score or risk
- where case evidence should appear
- evaluator navigation aids such as cross-reference tables
- what must not be claimed

## Failure taxonomy

- **Vanity differentiation**: claims such as "leading", "best", or "unique" with no proof
- **Score blindness**: equal space given to high- and low-value criteria
- **Evidence laundering**: old proposal language presented as current bidder evidence
- **Buyer mind-reading**: invented motives treated as facts
- **Commercial blindness**: strategy promises a capability not supportable by resources or price
- **Qualification blindness**: response effort continues despite an unresolved pass/fail eligibility gap

## Handoff contract

Append to `bid_state`:
- bid posture and reasons
- evaluation strategy
- proof plan
- response themes
- evidence gaps
- human decisions still required

Continue to `technical-architect`.
