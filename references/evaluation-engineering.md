# Evaluation Engineering

This reference converts an RFP scoring model into an internal response-control system.

## Criterion record

For every scored criterion create:

| Field | Meaning |
| --- | --- |
| criterion_id | stable key |
| buyer_text | exact buyer wording |
| weight | stated percentage or points |
| pass_fail | yes/no |
| evidence_required | attachments, cases, CVs, certifications, method |
| response_owner | skill/workstream |
| section_target | proposal location |
| proof_source | source ID |
| risk | missing / weak / strong |
| qc_test | how final review falsifies coverage |

## Coverage states

- COMPLETE: requirement answered and required evidence attached
- PARTIAL: answer exists but evidence, quantity, or ownership is incomplete
- ASSUMPTION: answer depends on an explicit unresolved assumption
- BLOCKED: cannot answer without clarification or missing source
- NOT_APPLICABLE: only when source logic supports exclusion

## Weight discipline

Do not manufacture a "recommended weight." Use buyer weights where supplied.

When no weights exist, classify importance as:
- pass/fail
- decision-critical
- supporting
- optional

Record this as internal prioritization, not buyer scoring.

## Evidence strength scale

- E0: unsupported statement
- E1: plausible operating statement with no proof
- E2: verified internal fact or named mechanism
- E3: verified case/credential/source directly relevant
- E4: multiple independent proof types for a critical criterion

No client-facing claim should depend on E0.

## Falsification tests

Before release, ask:
- Can a reviewer find the answer without guessing?
- Does the answer match the exact quantity and unit?
- Is the required proof attached?
- Is the proof relevant to the criterion?
- Does the methodology show who, when, and how?
- Is the commercial model capable of funding the promise?

## Executive-summary alignment

Every claim in the executive summary must point to at least one detailed section or verified evidence item. The summary may compress the proposal, not introduce new promises.
