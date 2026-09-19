# Source and Evidence Policy

## Why this exists

Proposal agents fail in two opposite ways: they either write from memory, or they research everything and lose the actual bid. This policy makes evidence proportional to the decision.

## Evidence classes

### Class A: bid-authoritative

Examples:

- current RFP and appendices
- issued addenda and official clarification responses
- mandatory BOQ and submission forms
- portal notice or official buyer instruction

Use for requirement, quantity, due date, submission method, mandatory evidence, scoring, contractual deliverables, and prescribed commercial structure.

### Class B: regulatory-authoritative

Current official Saudi government or regulator source. Use only where it can alter eligibility, scope, risk, tax, data handling, permit sequence, or submission procedure.

Record:

- authority
- URL
- page or provision when possible
- date checked
- applicability
- exact implication for the bid

Do not write "compliant with all Saudi regulations". Name what was checked and what remains subject to legal, buyer, or permit confirmation.

### Class C: bidder-authoritative

Approved bidder facts such as:

- legal entity name
- commercial registration and certificates
- approved team CVs
- verified case studies
- verified portfolio
- approved rate cards and commercial policies

Never infer these from a past deck if a current approved source exists.

### Class D: private benchmark pattern

Prior proposals, internal playbooks, past project files, delivery plans, and historical commercial models.

Allowed uses:

- section architecture
- unit taxonomy
- workflow patterns
- common risks
- typical dependencies
- review heuristics

Forbidden without explicit authorization:

- client names
- private prices
- bank or account details
- tax identifiers
- private contacts
- proprietary client strategy
- unapproved performance results
- contractual terms copied as defaults

A private benchmark is a pattern source, not a fact source for a new bid.

### Class E: public benchmark

Credible industry or market references. Use when they help justify a design decision, estimate a range, or contextualize a market fact. Prefer primary or first-party sources.

### Class F: assumption

An assumption is allowed only when:

- the missing fact is not mandatory to verify before drafting, and
- the assumption is labeled, and
- the downstream effect is visible.

Every commercial assumption that changes price belongs in the financial assumptions register.

## Claim ledger

Material claims should be classifiable as one of:

- `VERIFIED`
- `BUYER_STATED`
- `BIDDER_STATED`
- `REGULATORY_VERIFIED`
- `BENCHMARK`
- `ASSUMPTION`
- `UNKNOWN`

`UNKNOWN` claims cannot survive into a final submission if they affect eligibility, scope, price, results, or risk.

## Research relevance test

Before opening a source, ask which bid decision it can change:

- requirement coverage
- solution choice
- deliverable or acceptance criterion
- schedule or staffing
- risk and mitigation
- compliance or permit
- commercial model
- evaluator proof

If none, skip it.

## Citation behavior inside artifacts

Public-facing proposals should use client-appropriate citations only where useful. Internal source ledgers should be more complete than the visible deck.

For a client deck, a source may appear as a footnote, appendix, or source note. For a compliance workbook, use explicit URLs and source references. Never expose private connected-drive URLs to a third party unless the user explicitly intends to share those files.
