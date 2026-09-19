# Validation Failure Modes

Use this reference when repository CI or local deterministic checks fail.

## Package validator failures

### Manifest and graph mismatch

Signal:
- a skill exists in manifest but not neural graph, or vice versa

Likely cause:
- a new atomic skill was added to only one registry

Fix:
- reconcile manifest.json, neural-links/graph.yaml, and the skill path
- do not delete a node merely to make validation green if the capability is required

### Missing exit guard

Signal:
- graph node has no exit_guard

Risk:
- downstream work can proceed without explicit evidence that the node is complete

Fix:
- define a state condition that is falsifiable and owned by the node

### Missing progressive reference

Signal:
- service route points to a nonexistent reference

Fix:
- repair the route or add the actual domain reference
- do not redirect unrelated services to a generic file

## Static eval failures

### Unknown route

Signal:
- eval expected_route contains an unregistered node/service/lens

Likely causes:
- typo
- new route not registered
- scenario is relying on implementation detail rather than public routing contract

Fix:
- register the real route or correct the fixture

### Missing semantic family

Signal:
- semantic family threshold fails

Fix:
- add a genuinely different decision problem
- do not duplicate an existing prompt with new wording

## Security regression failures

### Secret pattern found

Signal:
- private key, token-like string, Saudi IBAN, or similar pattern detected

Fix:
- remove the secret from history/current change
- rotate a real exposed credential
- replace examples with clearly fake placeholders that do not match live-secret formats

### Workflow permission failure

Signal:
- CI requests write/admin permissions without a justified need

Fix:
- narrow GitHub Actions permissions to read-only where possible

### Dangerous workflow pattern

Signal:
- pull_request_target or remote script piped to a shell

Fix:
- use safer pull_request execution and pinned/known build steps
- do not silence the check without reviewing the trust boundary

## Runtime adapter failures

### Registry/adapter drift

Signal:
- canonical capability exists but the example adapter map omits it

Fix:
- add a host mapping or explicitly document that the host cannot support that operating mode

### Missing capability fixture

Signal:
- required degraded-mode case is absent

Fix:
- add a case proving how the skill behaves when that capability is unavailable

## Regulatory validation failures

### Stale authority identifier

Signal:
- an outdated authority acronym appears in an active regulatory file

Fix:
- verify the current official authority identity
- preserve historical names only in clearly historical context

## CI execution failures

### Dependency install fails

Check:
- requirements.txt remains minimal
- dependency versions are compatible with supported Python
- no unnecessary dependency was added for a standard-library task

### Unit tests fail after schema/graph change

Treat this as contract drift first, not test brittleness.

Do not weaken the test until the intended contract is explicit.

## Principle

A validator failure is evidence that two parts of the pack disagree. Repair the disagreement. Do not edit thresholds or tests merely to restore a green badge.
