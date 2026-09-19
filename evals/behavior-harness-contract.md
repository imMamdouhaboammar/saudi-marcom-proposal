# Behavioral Harness Contract

Static schema checks are necessary but not evidence that an agent behaves correctly.

## Required run record

A behavioral run should capture:
- skill/build revision
- fixture-set revision or cryptographic hash
- run date/time in UTC
- model/harness identity
- scenario ID
- operating mode selected
- route decisions
- source/evidence receipts
- state mutations
- tools called and outcomes
- gate transitions
- blockers
- final artifacts or response
- terminal status
- token/cost metadata when available

## Evaluation isolation

Provider-visible prompts receive only the public scenario and normal runtime context.

Expected routes, must-do, must-not-do, hidden assertions, and scoring keys remain evaluator-side.

## Test families

Run:
- positive activation
- negative boundary
- ambiguous brief
- adversarial shortcut pressure
- contradictory evidence
- stale/current regulatory conflict
- commercial missing-data pressure
- capacity mismatch
- confidentiality/proof laundering
- mandatory-form fidelity
- mutation/invalidation
- constrained tool availability

## Mutation tests

At minimum:
1. run a case to passing reconciliation
2. mutate a material deliverable field such as quantity, SLA, language, or operating window
3. assert prior reconciliation and QC receipts become stale
4. invalidate evaluator-simulation and QC receipts that depend on the changed state
5. require re-reconciliation and fresh evaluator simulation before READY

## Baseline and noise

For model or prompt retuning:
- run identical-build repeats first
- establish normal variance
- register success threshold before edits
- use held-out scenarios for final claims

## Release claim

A repo can say static validation passes without a live behavior harness.

It may only claim behavioral maturity when the current corpus revision has fresh held-out evidence meeting evals/rubric.md.
