# Specialist Agent Contract

Agents in this pack are bounded workers. The master orchestrator owns routing and release authority.

## Input packet

Every delegated task must contain:
- bid-state revision
- node/agent ID
- bounded objective
- owned state fields
- allowed source IDs or source classes
- invariants that apply
- stop conditions
- expected output schema

## Ownership

An agent may:
- read shared state
- append evidence it verified
- change fields explicitly assigned to it
- report contradictions and blockers

An agent may not:
- overwrite another node's verified fact without a source-precedence reason
- clear its own QC finding without new evidence
- change a mandatory buyer form
- invent bidder evidence or rates
- mark the final bid READY

## Output packet

Return:
- agent ID
- input revision
- state patch/delta
- evidence receipts added
- decisions proposed or made within authority
- blockers
- invalidated artifacts/receipts
- next recommended node
- confidence and coverage limits

## Freshness

A patch against a stale bid-state revision must be reconciled before application.

## Independent review

Reviewer agents are read-only by default. Their findings enter the QC evidence pool and are normalized before action.
