# CI Failure Modes

Use this document to interpret repository validation failures.

## security_gate.py fails

Likely causes:
- credential-like token committed to agent/config surfaces
- Saudi IBAN copied from a benchmark
- private key material
- remote pipe-to-shell instruction
- destructive root delete
- forced push to default branch
- world-writable chmod instruction

Action:
- remove the secret or dangerous instruction
- rotate/revoke a real exposed credential outside this repository if applicable
- rerun the gate

Do not weaken the regex merely to make a real finding disappear.

## validate_pack.py fails

Common causes:
- graph and manifest membership drift
- node path missing
- unknown neural link target
- skill frontmatter contract missing
- orchestrator or atomic skill reaches 500+ lines
- state router missing required states
- eval corpus breadth drops
- required reference/template missing

Fix the contract mismatch, not the validator expectation, unless the product contract itself intentionally changed.

## run_static_evals.py fails

This validates eval corpus shape, not model behavior.

Common causes:
- missing scenario fields
- duplicate IDs
- insufficient semantic family breadth
- malformed JSON

Do not interpret PASS as behavioral maturity.

## unit tests fail

Run the failing test in isolation first. Negative tests intentionally mutate temporary copies to ensure the validator fails closed.

## GitHub Actions environment failure

Distinguish:
- repository defect
- dependency installation/network defect
- GitHub runner incident

A runner/environment failure should not be converted into a product pass. Rerun only after the external failure is identified.
