---
name: precedent-miner
description: "Mine prior Saudi proposal libraries and benchmark material for reusable structure, operating patterns, units, risks, and verified bidder-owned proof without carrying client-specific facts forward. Use when prior bids, pitch decks, financial offers, case materials, or benchmark corpora are available. Do NOT use as authority for current buyer requirements, current regulation, or final market pricing."
version: 0.4.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs: [source_inventory, requirement_ledger, situation_classification]
requires: [source_grounding]
produces: [precedent_ledger, benchmark_signals, reuse_constraints]
gates: [provenance_preserved, confidentiality, no_claim_laundering]
neural_links:
  precursors: [rfp-forensics]
  continuations: [bid-strategist]
  lateral_peers: [service-router]
  recovery: precedent-miner
---
# Precedent Miner

Extract decision patterns from prior work without turning old client material into current truth.

Classify each signal as BIDDER_OWNED_VERIFIED, STRUCTURAL_ONLY, PUBLIC_BENCHMARK, or DO_NOT_REUSE. Similarity selects what to inspect, not what to copy.

Prefer operating similarity: buyer type, service family, operating shape, scale, duration, languages, live operations, and submission type.

Every signal records source, locator, pattern, relevance, reuse status, caveat, and linked requirement where applicable. If no precedent library is available, emit an explicit empty result and continue.

Never use an old price as current market authority, reuse an old client result without fresh bidder evidence, expose private client material to an external reviewer without authorization, or treat old regulatory wording as current law.

Read references/precedent-retrieval-and-learning.md and references/benchmark-provenance.md.
