# State and Handoff Protocol

## Purpose

The pack operates on one evolving bid state. Atomic skills do not communicate through prose alone.

## Bid-state rules

Every node:
1. reads the current state
2. reads only sources needed for its decision
3. appends evidence, decisions, or artifacts it owns
4. records blockers and freshness
5. emits a handoff receipt

A lower-precedence source cannot overwrite a higher-precedence fact.

## Fact statuses

Use:
- `VERIFIED`
- `ASSUMED`
- `CONTRADICTED`
- `PENDING`
- `SUPERSEDED`
- `NOT_APPLICABLE`

## Evidence receipt

Each material fact should carry:
- fact ID
- value or assertion
- source ID
- source locator
- effective/issued date when relevant
- checked timestamp
- confidence
- owner node

## Handoff receipt

Each node returns:
- node ID and version
- inputs consumed
- outputs created/changed
- evidence IDs added
- decisions made
- blockers
- unresolved questions
- invalidated downstream artifacts
- next eligible nodes

## Mutation invalidation

Any change to:
- requirement quantity
- deliverable SLA
- service window
- language
- geography
- buyer form
- regulatory effective state
- price basis

must invalidate dependent reconciliation/QC receipts.

## No phantom completion

A node may complete with unresolved items only if:
- they are explicitly recorded
- the downstream node can legally operate with them
- final release remains blocked where required
