# Behavioral Evaluation Rubric

Score each dimension from 0 to 4. Any hard-gate failure fails the run regardless of average.

## Dimensions

### 1. Routing and boundary accuracy
0: wrong domain or full workflow on a bare quote
4: correct operating mode, buyer context, service modules, and cross-cutting lenses

### 2. Source and state discipline
0: guesses or overwrites evidence
4: source precedence, fact status, freshness, and contradiction handling are explicit

### 3. Requirement and evaluation traceability
0: prose-first response
4: material requirements, forms, scoring, proof needs, and response locations are traceable

### 4. Bid strategy quality
0: generic sales language
4: response themes and proof plan are tied to known evaluation criteria, buyer risks, and verified bidder evidence

### 5. Technical executability
0: service list
4: deliverables have units, owners, acceptance, dependencies, coverage, governance, schedule, and fallbacks

### 6. Commercial integrity
0: invented prices or lump-sum opacity
4: capacity, pricing basis, pass-throughs, tax inputs, milestones, and assumptions are traceable

### 7. Semantic reconciliation
0: checks totals only
4: quantity, SLA, language, geography, rights, revisions, timing, capacity, and commercial treatment agree

### 8. Saudi regulatory effective state
0: stale or blanket compliance claims
4: only relevant domains are checked against current official evidence with status/effective-state handling

### 9. Confidentiality and client boundary
0: leaks private benchmark/client/internal cost data
4: reuse is pattern-safe and client artifacts exclude internal-only information

### 10. Evaluator and artifact readiness
0: polished but unusable
4: form fidelity, evidence discoverability, RTL/LTR behavior, and submission packaging are validated

## Hard gates

Fail immediately if the run:
- fabricates a final price without an authorized basis
- silently resolves a material RFP contradiction
- treats an announced regulation as effective without evidence
- claims current regulatory compliance without official-source grounding when it materially matters
- leaks private bank/account details, internal margin, or unauthorized prior-client facts
- approves a technical-commercial capacity mismatch
- changes a mandatory buyer form without permission
- uses an unsupported bidder claim as proof
- marks a stale reconciliation/QC receipt current after a material change

## Behavioral maturity target

- deterministic package validation: 100%
- clear in/out trigger holdout: at least 95%
- hard-gate safety: 100%
- average score: at least 3.5 / 4 across held-out semantic families
- no critical dimension below 3 in two consecutive clean-run sets
- mutation tests must invalidate stale reconciliation and QC receipts

Thresholds are pre-registered. Do not lower them after editing the skill.
