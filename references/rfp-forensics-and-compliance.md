# RFP Forensics and Compliance

## Objective

Convert an unstructured RFP pack into an executable bid model before anyone writes a persuasive paragraph.

## Source inventory

Create one row per file or source:

- source ID
- title
- type
- owner or issuing party
- version/date
- language
- authority class
- supersedes / superseded by
- confidentiality
- notes

When documents have appendices or official clarification answers, treat them as separate sources with explicit precedence.

## Requirement extraction

Each requirement row should answer:

1. What exactly is required?
2. Is it mandatory, scored, informational, ambiguous, or optional?
3. Where was it stated?
4. What artifact or evidence proves coverage?
5. Which workstream owns it?
6. Does it affect price, schedule, staffing, permit, data, or risk?
7. Where will it appear in the response?
8. What is its current coverage state?

Recommended fields are included in `templates/requirement-ledger.csv`.

## Requirement types

- eligibility
- submission
- scope
- quantity
- service level
- technical specification
- quality / acceptance
- governance
- staffing / CV
- experience / case study
- timeline
- reporting
- data / security
- IP / licensing
- permit / access
- commercial / BOQ
- tax
- guarantee / insurance
- local content
- contractual
- evaluation criterion

## Scoring map

If the RFP exposes evaluation criteria, create an evaluator map:

- criterion
- weight or priority
- exact evidence requested
- proposal section
- proof artifact
- confidence
- missing evidence

Do not respond to a 30% methodology criterion with five pages of company history.

## Quantity reconciliation

Quantities are high-risk. Extract into one canonical table with:

- requirement ID
- item
- unit
- quantity
- duration or frequency
- source
- source location
- ambiguity note

If the main scope says 12 reports and an appendix says 24, do not average or choose silently. Flag the contradiction and record the commercial effect.

## Mandatory form preservation

When the buyer provides a template, capture:

- fields that must remain unchanged
- fields to populate
- signatures / stamps
- date format
- currency
- tax presentation
- attachment reference
- portal upload requirement

The internal pricing workbook can be richer than the client BOQ. The client BOQ must still follow the buyer's structure.

## Clarification log

Create a clarification item when a missing or conflicting fact changes:

- eligibility
- price
- deliverable volume
- staffing
- response time
- implementation schedule
- permit responsibility
- data access or security
- acceptance criteria

Each item includes impact and interim assumption, if drafting must continue.

## Government and semi-government mode

Increase rigor for:

- mandatory attachment completeness
- exact prescribed forms
- evaluation criterion traceability
- source freshness
- arithmetic
- local content requirements where the RFP activates them
- validity and guarantee requirements
- platform instructions

Do not import a generic government checklist blindly. The current RFP remains the primary source.

## Coverage states

- `COVERED`: requirement has a section and evidence
- `PARTIAL`: section exists but proof or detail is insufficient
- `GAP`: no adequate response
- `CLARIFICATION`: cannot be resolved responsibly from current evidence
- `N/A`: explicitly not applicable with rationale

A final proposal should have zero hidden mandatory `GAP` rows.
