---
name: saudi-marcom-proposal
description: "Agentic operating system for tailored Saudi technical and financial proposals across corporate communications, media, marketing, promotion, events, crisis and reputation, digital products, AI, monitoring, production, and adjacent MarCom services. Use for Saudi RFP responses, tenders, pitches, retainers, proposal reviews, and bid package assembly. Do NOT use for civil/MEP/construction engineering tenders, legal opinions, generic sales decks, or bare price formatting."
version: 0.3.0
pack: proposal
inputs:
  - rfp_documents
  - organization_context
  - bidder_evidence
  - reference_work
  - pricing_inputs
requires:
  - source_grounding
produces:
  - bid_state
  - requirement_ledger
  - compliance_matrix
  - bid_strategy
  - technical_proposal
  - financial_proposal
  - reconciliation_certificate
  - qc_report
gates:
  - evidence_before_claims
  - no_unsourced_pricing
  - regulatory_effective_state
  - technical_financial_reconciliation
  - mandatory_form_preservation
  - confidentiality
fallback: source-intake
mutatesWorkspace: false
parallelSafe: false
neural_links:
  architecture: guarded-state-dag
  graph: neural-links/graph.yaml
  state_contract: schemas/bid-state.schema.json
  orchestrator: master-bid-engine
  nodes:
    - source-intake
    - rfp-forensics
    - regulatory-scout
    - service-router
    - bid-strategist
    - technical-architect
    - commercial-modeler
    - scope-reconciliation
    - proposal-qc
    - artifact-assembler
  recovery: source-intake
---

# Saudi MarCom Proposal Operating System

Build evidence-backed Saudi proposals that are tailored to the buyer, executable by the delivery team, commercially supportable, and safe to submit.

## Core idea

Do not start with slides. Start with a bid state.

The pack converts raw sources into one shared model:

```text
sources -> requirements -> buyer/evaluation strategy -> solution -> commercial model
        -> semantic reconciliation -> adversarial QC -> client package
```

The technical and financial offers are two views of the same scope model, not two independent documents.

## Runtime state

Create and maintain one `bid_state` that conforms to `schemas/bid-state.schema.json`.

Every atomic skill reads the current state, appends evidence or decisions, and returns a handoff receipt. No skill may silently overwrite a higher-precedence fact.

Required state sections:
- source receipts and effective versions
- buyer and submission classification
- requirement ledger and evaluation map
- active regulatory checks with effective-state evidence
- active service modules and cross-cutting lenses
- bidder evidence and claim status
- deliverable map and acceptance proof
- capacity and pricing basis
- assumptions, exclusions, risks, clarifications
- reconciliation findings
- QC blockers and release status

Read `references/state-and-handoff-protocol.md` before multi-node execution.

## Non-negotiable invariants

1. **Source before prose**: current RFP, addenda, buyer forms, official authority sources, and verified bidder facts outrank memory.
2. **Evidence before claims**: no credentials, performance results, case metrics, permits, certifications, or commitments without traceable evidence.
3. **No silent contradiction resolution**: conflicting quantities, dates, forms, or clauses must be surfaced with source references and an interim assumption if execution must continue.
4. **No unsourced final pricing**: final unit rates require an approved rate card, bidder cost basis, supplier quote, contractual schedule, or explicitly authorized commercial assumption.
5. **Technical-financial parity**: reconcile not only quantities but SLA, geography, languages, formats, revision rounds, operating hours, rights, licenses, dependencies, and capacity.
6. **Mandatory form fidelity**: prescribed BOQs and declarations are immutable structures unless the buyer explicitly allows alteration.
7. **Regulatory effective-state proof**: a law or policy that is announced is not automatically treated as effective. Capture publication, effective date, status, and checked date.
8. **Private benchmark isolation**: prior bids are pattern evidence only unless the user explicitly authorizes reuse of a factual bidder-owned item.
9. **Internal commercial isolation**: internal costs, buy rates, salaries, margins, and bank details never enter client artifacts unless the RFP requires them.
10. **Human-owned bid decision**: the pack can recommend `BID`, `NO_BID`, or `CONDITIONAL` with reasons, but does not silently make the commercial commitment for the organization.

## Execution model

### Stage 0: classify the request

Use `routers/intent-router.yaml` and `routers/buyer-context-router.yaml`.

Possible operating modes:
- `FULL_BID`: technical + financial
- `TECHNICAL_ONLY`
- `FINANCIAL_ONLY`
- `REVIEW_ONLY`
- `DISCOVERY_DRAFT`: brief is incomplete, outputs are assumptions-led and non-final
- `BARE_QUOTE`: do not activate the full pack
- `OUT_OF_DOMAIN`: decline ownership and route elsewhere

### Stage 1: source intake and RFP forensics

Run `source-intake`, then `rfp-forensics`.

Exit only when:
- every material source has a receipt
- addenda precedence is resolved
- mandatory requirements and forms are cataloged
- scoring criteria are extracted when available
- unresolved contradictions are visible

### Stage 2: parallel context resolution

After forensics, three nodes may run in parallel:
- `regulatory-scout`
- `service-router`
- `bid-strategist`

Their outputs converge before solution drafting.

### Stage 3: technical architecture

Run `technical-architect`.

The proposal must answer:
- why this buyer needs this outcome now
- what will be delivered
- how work will operate
- who owns each decision
- what proof of acceptance exists
- what can fail and what happens then
- what is explicitly outside scope

No generic methodology may survive if it cannot map to a requirement, evaluation criterion, buyer risk, or delivery necessity.

### Stage 4: commercial architecture

Run `commercial-modeler`.

Pricing is driven by:
- deliverable units
- effort and capacity
- direct suppliers and pass-throughs
- licensing and permit assumptions
- operating coverage
- risk explicitly approved for pricing
- tax treatment from current regulatory evidence

A missing price basis stays missing. The workbook can be structurally complete while the offer remains commercially non-final.

### Stage 5: semantic reconciliation

Run `scope-reconciliation`.

A passing reconciliation proves:
- every technical commitment has a commercial treatment
- every commercial line has a technical purpose
- quantity, unit, timing, SLA, language, geography, acceptance, rights, and capacity are consistent
- changes propagate to dependent artifacts

### Stage 6: independent proposal QC

Run `proposal-qc`.

Release states:
- `READY`
- `REVISIONS_REQUIRED`
- `BLOCKED`

Only `READY` may proceed to final client packaging.

### Stage 7: artifact assembly

Run `artifact-assembler` after QC.

The assembler preserves:
- mandatory buyer formats
- technical/financial separation
- Arabic RTL and English LTR behavior
- client-safe content boundaries
- internal evidence ledgers outside the client package unless requested

## Saudi regulatory routing

Canonical behavior is defined in:
- `references/regulatory-state-resolver.md`
- `references/saudi-regulatory-freshness.md`

Triggered domains may include procurement/Etimad, local content, VAT and tax, personal data, media/advertising, event permits, cybersecurity, telecom/digital services, or sector-specific controls.

Never research all domains by default. Relevance gates decide.

## Benchmarks

Use benchmarks to improve structure, delivery logic, units, risks, and evaluation coverage.

Do not use benchmark client names, rates, confidential claims, bank data, or private commercial terms.

Read:
- `references/benchmark-corpus-anonymized.md`
- `references/evaluation-and-win-strategy.md`
- `references/commercial-unit-library.md`

## Tool policy

Use capabilities, not provider names, inside canonical skill behavior.

`tools/tool-registry.yaml` defines tool families for:
- connected-source retrieval
- web research
- spreadsheet calculation
- document/deck generation
- deterministic validation
- external review adapters

External reviewers such as CodeRabbit-style or plugin-eval systems are optional independent reviewers. They never replace the pack's deterministic gates and cannot self-certify their own fixes.

## Accelerated bid mode

For deadlines under four days, reduce optional ideation, not control quality.

Still mandatory:
- requirement extraction
- form preservation
- material contradiction logging
- pricing basis labeling
- semantic reconciliation
- confidentiality scan
- final package checklist

## Completion contract

Do not call a bid package complete unless:
- mandatory requirements have traceable coverage
- current regulatory claims have effective-state receipts when relevant
- bidder claims are verified or downgraded
- financial formulas and commercial bases are valid
- semantic reconciliation passes
- no unresolved blocker remains
- client artifacts exclude internal-only data
- final files match required submission formats
