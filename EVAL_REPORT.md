# Evaluation Report

Version: 0.4.1
Audit date: 2026-09-19

## Current static inventory

- atomic skills: 12
- behavioral scenarios: 23
- named semantic scenario families: 23
- guarded shared state contract: present
- runtime adapter fixture set: present
- end-to-end government and event fixtures: present
- golden decision cases: 8

## Deterministic validation

Repository release gates are:

```bash
python3 scripts/security_scan.py
python3 scripts/validate_pack.py
python3 scripts/run_static_evals.py
python3 scripts/validate_runtime_adapters.py
python3 -m unittest discover -s tests -p "test_*.py"
```

A current revision is considered statically valid only when all five gates pass in CI or an equivalent deterministic environment.

## Security regression scope

The focused security gate now checks UTF-8 text content regardless of normal file suffix, including dotfiles and extensionless files such as environment or key-like filenames. Known binary formats are excluded.

It also checks:
- common credential/private-key patterns
- Saudi IBAN pattern
- dangerous pull-request workflow trigger usage
- pipe-to-shell patterns
- workflow-level write permissions
- job-level write permissions
- required agent/reviewer safety controls

This is repository-focused evidence. It does not replace organization-level secret scanning or platform security controls.

## Static behavior corpus

The scenario bank includes:
- government RFP compliance
- fast-turn private events
- monitoring/crisis SLA capacity
- AI and personal-data processing
- influencer regulatory freshness
- contradictory requirements
- pricing pressure
- scope-price drift
- non-trigger engineering work
- bare-quote boundaries
- multilingual seasonal operations
- vague direct briefs
- procurement-law transition
- mandatory-form fidelity
- proof laundering
- capacity stress
- unfunded value-add pressure
- foreign-supplier tax ambiguity
- precedent contamination
- evaluator traceability
- missing precedent access
- evaluation mutation
- opaque private pitch boundaries

## Behavioral model evaluation

Status: NOT EXECUTED FOR MATURITY CLAIM

Static validation does not prove an agent follows these contracts.

A behavioral maturity claim requires:
- current build/revision identifier
- held-out scenario set
- private evaluator oracle
- model and runtime identity
- tool availability record
- route and state traces
- evidence receipts
- mutation/invalidation evidence
- artifact metadata
- repeated runs sufficient to distinguish improvement from variance

See `evals/behavior-harness-contract.md`.

## Release interpretation

The repository may claim that deterministic checks pass when current CI proves them.

It must not claim behavioral maturity, bid quality superiority, or guaranteed proposal outcomes until fresh behavioral evidence exists.
