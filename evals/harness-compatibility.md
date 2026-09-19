# Runtime Harness Compatibility

The skill pack is provider-neutral at the behavior layer. A host maps canonical capabilities to its own tools.

## Compatibility principle

A runtime is compatible when it can satisfy the capability contract needed for the requested operating mode. Tool brand names are not part of the canonical skill contract.

## Capability matrix

| Capability | Full bid | Technical only | Financial only | Review only | Discovery draft |
| --- | --- | --- | --- | --- | --- |
| connected source read/search | required when evidence is not supplied inline | required when evidence is not supplied inline | required when pricing evidence is not supplied inline | required when target/source files are external | optional |
| public web search/fetch | required for current regulatory claims | required when current compliance matters | required when current tax/compliance matters | required to verify freshness claims | optional |
| spreadsheet compute | required | optional | required | required when financial files are reviewed | optional |
| document/presentation artifact | required only for finished artifact generation | required only for finished artifact generation | optional | optional | optional |
| deterministic validator | required for release | required for release | required for release | required for release decision | recommended |
| independent reviewer | optional | optional | optional | optional | optional |

## Degraded behavior

A missing capability changes what the pack may claim.

### No private-source connector

If the user supplied the full source inline, work may continue.

If a referenced private RFP, rate card, or prior file is not available:
- record SOURCE_GROUNDING_REQUIRED
- do not invent its contents
- do not replace private evidence with public web search

### No public web

Work may continue on stable non-regulatory content.

When current Saudi regulatory, tax, permit, or authority naming materially affects the bid:
- record REGULATORY_FRESHNESS_BLOCKED
- do not claim current compliance
- keep dependent scope or price provisional

### No spreadsheet compute

Technical work may continue.

Final financial modeling is blocked when arithmetic, quantity reconciliation, tax, or milestone calculations are required.

### No artifact renderer

The pack may produce approved content structure and artifact instructions.

It may not claim final render validation or submission-file readiness.

### No independent external reviewer

Core execution continues using deterministic validation plus the internal independent QC skill.

An external reviewer is additional evidence, not a correctness dependency.

## State transport

A host must preserve:
- bid-state revision
- evidence/source IDs
- gate status
- blockers
- invalidated artifacts
- handoff receipts

A host that cannot persist state across node calls should execute the pack in one bounded session or serialize the bid state between calls.

## Compatibility assertions

A compatible adapter must not:
- change source precedence
- bypass exit guards
- convert missing capability into simulated success
- expose private source content to an unrelated external reviewer
- make external-review availability a prerequisite for core correctness
- mark a stale reconciliation or QC receipt as current

See evals/fixtures/runtime-adapter-cases.json for executable static cases.
