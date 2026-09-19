# Tool Capability Contract

Canonical skills depend on capabilities, not specific plugin brands.

The machine-readable registry is tools/tool-registry.yaml.

## Selection rule

For each task:
1. identify required capability
2. prefer the connected/private source provider for user-owned evidence
3. prefer official public sources for current Saudi rules
4. use deterministic compute for money and reconciliation
5. use artifact-specific tools for final files
6. verify writes/readback
7. return a blocker if no compatible capability exists

## Evidence rule

Every material tool-derived fact should leave a receipt appropriate to the capability.

Examples:
- connected file: source ID, title, locator, fetched time
- web rule: authority, official URL, checked time
- spreadsheet: formula/model revision and validation result
- artifact: output ID/path and render-validation result
- external review: reviewer, target revision, finding IDs

## Failure behavior

Never simulate:
- file reads
- live regulatory checks
- spreadsheet calculations
- reviewer runs
- artifact writes

A missing provider is a named runtime limitation, not permission to invent evidence.
