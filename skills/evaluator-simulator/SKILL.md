---
name: evaluator-simulator
description: "Simulate evaluator traceability for a reconciled Saudi MarCom proposal using disclosed buyer criteria, mandatory requirements, and clearly labeled readability heuristics. Use before final QC to find hard-to-locate answers, unsupported strengths, ambiguous commitments, and evidence gaps. Do NOT invent hidden evaluation weights, predict award, or replace the buyer's actual evaluation."
version: 0.4.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs: [evaluation_map, requirement_ledger, technical_outline, client_boq, reconciliation_certificate, proof_plan]
requires: [semantic_reconciliation]
produces: [evaluator_readability_report, criterion_coverage_report, ambiguity_questions]
gates: [disclosed_criteria_fidelity, requirement_traceability, no_invented_scoring]
neural_links:
  precursors: [scope-reconciliation]
  continuations: [proposal-qc]
  lateral_peers: []
  recovery: technical-architect
---
# Evaluator Simulator

Review the response as a reader who must evaluate it from the buyer's published material.

Use, in order: disclosed criteria and weights, mandatory requirements and forms, repeated buyer objectives, then labeled readability heuristics when no scoring model exists. Never turn heuristics into fake weights.

For each criterion record its exact text, buyer-stated weight if any, response location, direct answer, proof location, unresolved qualifier, evaluator question, and PASS, QUESTION, or BLOCKER status.

Check findability, evidence proximity, requirement traceability, ambiguity, duplication, contradiction, and prose that hides the answer. These are diagnostics, not a score.

Any material addendum, requirement, scope, price, or evaluation change invalidates the report.

Read references/evaluator-simulation.md.
