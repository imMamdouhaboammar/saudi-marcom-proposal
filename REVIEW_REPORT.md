# Independent Review Report

Version: 0.4.1
Audit date: 2026-09-19

## Review status

The repository is suitable for guarded pilot use after current CI passes the v0.4.1 release gates.

Behavioral maturity remains intentionally unproven until held-out live model evaluations run.

## Architecture reviewed

The active architecture contains:
- one guarded shared bid state
- 12 atomic skills
- buyer and intent routing
- sanitized precedent mining
- regulatory effective-state resolution
- service and cross-cutting lens routing
- evaluation-weighted bid strategy
- technical architecture
- capacity-aware commercial modeling
- semantic technical-financial reconciliation
- evaluator traceability simulation
- independent proposal QC
- client artifact assembly

## Post-merge findings addressed

A post-merge automated review of v0.4.0 identified two valid security gaps:

1. the secret scan skipped extensionless and dotfiles such as `.env` and `id_rsa`
2. the workflow permission audit checked top-level permissions but missed job-level write grants

v0.4.1 addresses both with regression tests.

## PR reconciliation

The older open PR #2 was based on the pre-v0.4 merge base and diverged from the newer guarded-state architecture.

Useful non-duplicative ideas from that branch are incorporated selectively:
- CodeRabbit path review guidance
- golden decision cases
- deeper benchmark case fixtures

Its older graph/router architecture should not be merged over v0.4.x.

## Safety and confidentiality

Reviewed controls include:
- no unsourced final pricing
- no invented credentials or case results
- no silent requirement contradiction resolution
- mandatory buyer form fidelity
- prior-client fact isolation
- internal commercial data isolation
- current-source requirements for time-sensitive regulation
- capability degradation without simulated tool success
- revision-bound reconciliation and QC evidence

## Remaining pilot risks

1. Real behavior varies by model and host until a held-out harness run is executed.
2. Regulatory correctness still depends on current official-source access at proposal time.
3. Commercial correctness depends on real bidder rate cards, supplier quotes, tax treatment, and company policy.
4. Final deck/document quality requires artifact generation plus render inspection.
5. Legal, tax, cybersecurity, data-protection, and sector-specific interpretations may require qualified specialist confirmation when material.
6. External reviewers are advisory and may be unavailable, rate limited, or commercially disabled.

## Release decision

Proceed only when the current revision has green deterministic CI and no unresolved blocking review findings.

Do not use this report as a substitute for current CI, current regulatory evidence, or behavioral evaluation.
