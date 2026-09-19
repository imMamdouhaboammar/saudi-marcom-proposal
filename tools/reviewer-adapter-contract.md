# Independent Reviewer Adapter Contract

External reviewers are useful only if their findings can be normalized and traced.

## Supported reviewer classes

Examples include:
- repository/code reviewers
- skill/package evaluators
- prompt/behavior eval systems
- security scanners
- document QA agents

Provider names are optional. The contract is stable.

## Input packet

Send only what the reviewer needs:
- target revision/hash
- target paths/artifacts
- requested review lens
- relevant specification or invariant IDs
- confidentiality-safe context

Do not send unrelated private Drive documents.

## Required output

Normalize each finding to:
- reviewer
- target revision
- finding ID
- severity
- artifact/path
- evidence
- failure mode
- suggested action
- confidence

## Independence rules

- an authoring agent cannot mark its own reviewer finding cleared without fresh verification
- a reviewer cannot change `submission_status` directly
- duplicate findings are merged by failure mode
- disagreement is preserved, not averaged away
- external reviewer failure does not silently become a clean review

## CodeRabbit and Plugin Eval style integrations

When these capabilities are available, connect them here as independent reviewers.

If they are unavailable, do not claim they ran. Continue with local deterministic validation and the pack's own red-team skill.
