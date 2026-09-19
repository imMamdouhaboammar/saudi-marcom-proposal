# Agent Handoff Contract

Every atomic skill should hand downstream work as structured evidence, not prose-only context.

## Required envelope

```yaml
producer: skill-id
status: complete | partial | blocked
source_generation: identifier
inputs_used: []
outputs:
  artifact_name: path-or-object-id
receipts: []
assumptions: []
blockers: []
stale_evidence: []
next_owner: skill-id
acceptance_gate: "condition that makes the next transition valid"
```

## Rules

- A downstream agent may trust an output only if its acceptance gate is satisfied.
- Mutation makes previous verification stale where relevant.
- Partial output must not be silently promoted to complete.
- An unresolved contradiction travels forward as a blocker, not a hidden assumption.
- Tool receipts and source IDs travel with dependent claims.
- Client-facing content does not receive internal cost, confidential source, or reviewer metadata.

## Recovery

Return to the earliest owner capable of resolving the failed invariant:
- source conflict -> source-intake
- requirement conflict -> rfp-forensics
- regulatory freshness -> regulatory-scout
- scoring/evidence weakness -> bid-strategist
- technical feasibility -> technical-architect
- commercial basis -> commercial-modeler
- parity mismatch -> scope-reconciliation
- final defect -> proposal-qc or artifact-assembler by defect class
