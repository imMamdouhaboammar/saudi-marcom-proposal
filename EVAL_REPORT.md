# Evaluation Report

Date: 2026-09-19
Target: v0.3.0 branch

## Deterministic package validation

Status: PASS in GitHub Actions PR run.

Current CI executes:
- focused agent/config security gate
- pack structural validation
- static eval schema validation
- Python unit-test discovery

The v0.3 validator checks:
- 10 atomic skills
- graph/manifest parity
- state-router presence
- required progressive references
- secret patterns
- minimum 12 scenarios and 8 semantic families

## Static eval corpus

Status: PASS.

Current corpus:
- 16 behavioral scenario definitions
- 16 named scenario families
- 8 compact golden decision cases
- adversarial pricing, contradiction, SLA/staffing drift, event permit category, AI/data, weighted-evidence, multilingual and non-trigger coverage

Static validation proves corpus structure, not model behavior.

## Security-focused regression

Status: PASS in GitHub Actions.

The focused gate scans agent, skill, router, neural-link and CI configuration surfaces for:
- common credential/private-key patterns
- Saudi IBAN patterns
- a small set of dangerous executable instruction patterns

This is repository-focused evidence, not a replacement for organization-level secret scanning or platform security controls.

## Spreadsheet baseline

The repository includes a pricing workbook with separated internal/client views and formula-based totals. Prior blank-model formula inspection found no standard spreadsheet error tokens.

A real proposal still requires proposal-specific recalculation and inspection.

## Behavioral model evaluation

Status: NOT EXECUTED.

A valid behavioral maturity claim requires:
- host adapter
- current skill/build hash
- public prompts only to tested model
- private oracle
- tool traces and artifact metadata
- held-out scenarios
- repeated comparable runs where retuning claims are made

See:
- evals/behavior-harness-contract.md
- harness/adapter-contract.yaml
- harness/compatibility-matrix.md

Do not label v0.3 behaviorally mature until this evidence exists.
