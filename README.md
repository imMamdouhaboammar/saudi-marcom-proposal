# Saudi MarCom Proposal Skill Pack

A provider-neutral agentic Skill for building and auditing tailored Saudi technical and financial proposals across media, corporate communications, marketing, promotion, events, crisis and reputation, digital and AI, monitoring, production, and adjacent services.

## What makes this pack different

The pack treats proposal creation as a traceable operating system rather than a writing prompt:

1. source inventory and RFP forensics
2. requirement ledger and compliance matrix
3. Saudi-context relevance checks
4. service-specific solution architecture
5. deliverable and acceptance design
6. financial model tied directly to scope
7. technical-financial reconciliation
8. independent red-team QA
9. artifact assembly

It was designed from anonymized patterns found in real Saudi proposal and pricing work, then separated from client-specific facts so the reusable package does not leak names, prices, bank details, or confidential material.

## Install shape

The canonical entrypoint is `SKILL.md`. Supporting depth sits under `references/`, while `routers/`, `agents/`, `neural-links/`, `templates/`, and `evals/` provide host adapters and evaluation material.

## Minimum inputs for a final bid

- RFP or approved brief
- deadline and submission format
- bidder facts and approved credentials
- commercial inputs or rate cards
- any mandatory templates or BOQ
- clarification responses and issued addenda

If these are incomplete, the Skill should produce a draft-for-validation plus an explicit missing-input list rather than invent facts.

## Included artifacts

- `templates/pricing-model.xlsx`: internal pricing engine + client BOQ
- requirement/compliance/risk/assumption/source templates
- 8 specialist agent profiles
- service routing across six MarCom families
- current-source freshness guide for Saudi procurement, tax, data, media, and event checks
- benchmark scenarios and adversarial eval suite
- static package validator

## Evaluation status

The package includes deterministic static tests and behavioral eval definitions. Static checks can run locally with `python scripts/validate_pack.py`. A true model behavioral evaluation still requires a host harness that can run the Skill against held-out prompts and capture tool traces and outputs.
