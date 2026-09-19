---
name: saudi-marcom-proposal
description: "Create, audit, or improve Saudi technical and financial proposals for media, corporate communications, marketing, promotion, events, crisis and reputation, digital and AI, monitoring, and related services. Use for Saudi RFP, tender, pitch, retainer, or commercial proposal work that needs requirement traceability, Saudi-context grounding, technical-to-financial alignment, or bid quality control. Do NOT use for unrelated construction or engineering tenders, legal opinions, generic sales decks, or bare price quotes with no service scope."
version: 0.1.0
pack: proposal
inputs:
  - rfp_documents
  - organization_context
  - reference_work
  - pricing_inputs
requires:
  - source_grounding
produces:
  - requirement_ledger
  - compliance_matrix
  - technical_proposal
  - financial_proposal
  - assumptions_register
  - risk_register
  - source_ledger
  - qc_report
gates:
  - evidence_before_claims
  - no_unsourced_pricing
  - regulatory_freshness
  - technical_financial_reconciliation
  - confidentiality
fallback: proposal-intake
mutatesWorkspace: false
parallelSafe: false
neural_links:
  precursors:
    - source-intake
    - rfp-forensics
  continuations:
    - technical-architect
    - commercial-modeler
    - proposal-qc
  lateral_peers:
    - regulatory-scout
    - artifact-assembler
  recovery: proposal-recovery
---

# Saudi MarCom Proposal

## Mission

Turn an RFP, tender pack, meeting brief, or partially defined opportunity into a decision-ready Saudi technical proposal and a financially reconciled commercial offer for media, communications, marketing, events, crisis and reputation, digital and AI, monitoring, and adjacent services.

The skill is an orchestrator plus domain expert. It does not merely write slides. It builds an evidence model first, routes to the right service logic, then creates and audits the final artifacts.

## Activation contract

Use when the requested job includes one or more of these:

- build or review an عرض فني, عرض مالي, technical proposal, financial proposal, RFP response, tender response, retainer proposal, or event proposal for Saudi Arabia
- extract requirements, evaluation criteria, quantities, deliverables, SLAs, assumptions, or commercial dependencies from a Saudi brief or RFP
- tailor a communications, PR, marketing, digital, AI, monitoring, crisis, content, production, or event offer to a Saudi entity
- reconcile a technical scope with a BOQ, pricing model, payment milestones, options, exclusions, or VAT treatment
- audit a proposal before submission for compliance, evidence, arithmetic, client leakage, or scope gaps

Do not activate for:

- civil, MEP, architectural, construction, legal, medical, or engineering bids unless the communications or event work is the actual scoped service
- a generic company profile, credentials deck, case study deck, or sales presentation with no bid or proposal decision
- legal advice or a claim that a tender is legally compliant without an authoritative current source
- a one-line price quote where the user explicitly does not need a scoped proposal

## Non-negotiable invariants

1. Source before prose. Never write a material requirement from memory when the supplied RFP or official source can answer it.
2. Evidence before claims. Never invent credentials, case-study results, audience statistics, client facts, certifications, permit status, or KPIs.
3. Financials mirror the technical scope. Every client-facing price line must map to a deliverable, resource, service unit, option, or explicit commercial allowance.
4. Do not fabricate a price. Missing costs stay marked as `PRICING INPUT REQUIRED` unless the user explicitly authorizes an assumption or scenario band.
5. Separate technical and financial offers by default. Combine them only when the brief, platform, or user explicitly requires a combined submission.
6. Preserve prescribed forms and tables. Never redesign a mandatory government BOQ, declaration, or submission form in a way that changes its structure or meaning.
7. Treat regulations as live facts. Re-check current Saudi rules whenever they can change bid eligibility, tax treatment, data handling, media activity, permits, or submission procedure.
8. No client leakage. Never copy a past client name, number, internal assumption, price, account detail, confidential case fact, or proprietary phrase into another proposal without explicit authorization.
9. State uncertainty. Missing or contradictory inputs belong in a clarification log, assumptions register, or gap report, not in confident prose.
10. The proposal must remain executable. A promise that cannot be staffed, scheduled, measured, permitted, priced, or accepted is not ready for submission.

## Situation classification

Classify before drafting. The classification changes the workflow.

| Dimension | Classes | Consequence |
| --- | --- | --- |
| Buyer | Government / semi-government / private | Government work gets strict form preservation, evaluation mapping, and live procurement checks |
| Input | Full RFP / partial RFP / meeting brief / verbal brief | Missing formal inputs require an assumptions-led draft and a clarification log |
| Output | Technical only / financial only / both / combined | Both are generated from one scope model, but normally delivered separately |
| Deadline | Standard / accelerated / critical | Accelerated mode reduces optional research, never mandatory compliance and arithmetic checks |
| Scope | Single service / multi-service / event / retainer / campaign / managed service | Route to the relevant service modules |
| Evidence | Sufficient / partial / contradictory | Partial evidence becomes gaps; contradictions become clarification items |
| Data sensitivity | None / personal data / confidential / regulated | Activate data, access, retention, and vendor checks when relevant |
| Commercial state | Rates known / vendor quotes pending / cost model missing | Never disguise missing commercial inputs as a final price |

## Source precedence

Use this order when sources disagree:

1. Current user instruction and signed clarifications
2. Current RFP, appendices, BOQ, official Q&A, platform notices, and issued addenda
3. Current official Saudi regulatory or authority source when the rule is relevant
4. Verified organization-owned facts and approved case studies
5. Approved internal templates and prior proposals as patterns only
6. Credible current public benchmarks
7. Heuristics, clearly labeled as assumptions

A past proposal is never authority over a current RFP.

Read `references/source-and-evidence-policy.md` before using prior proposals or connected drives as evidence.

## Router

Use `routers/intent-router.yaml` and `routers/service-router.yaml`.

Primary routes:

- `rfp-forensics`: extract requirements, scoring, forms, deadlines, quantities, dependencies, and ambiguities
- `technical-architect`: design the technical response and evidence-backed proposal narrative
- `commercial-modeler`: build the unit model, BOQ, pricing dependencies, taxes, options, and payment logic
- `regulatory-scout`: verify only rules relevant to the scope
- `artifact-assembler`: produce the requested DOCX, PPTX, XLSX, PDF, Google Workspace, or structured Markdown artifacts using available host tools
- `proposal-qc`: independently falsify compliance, arithmetic, scope reconciliation, claims, and confidentiality

## Protocol

### Stage 0: Preflight

Objective: know what kind of bid this is before touching the prose.

Required evidence:

- buyer and project name or a clear placeholder
- deadline and submission method if available
- files received and their version dates
- output language and format
- whether prices, vendor quotes, or rate cards exist
- confidentiality constraints

Actions:

1. Inventory every source.
2. Classify the situation using the table above.
3. Identify missing critical inputs.
4. Decide whether the proposal can be final, draft-for-validation, or structure-only.

Exit when the source inventory and status are explicit.

Stop or escalate when the user asks for a final compliant bid but a mandatory RFP, form, or pricing input is unavailable.

### Stage 1: RFP forensics and requirement ledger

Read `references/rfp-forensics-and-compliance.md`.

Build a requirement ledger before the proposal outline. Each material requirement gets:

- requirement ID
- exact or faithful source reference
- mandatory / scored / informational / ambiguous
- responsible workstream
- deliverable or evidence needed
- proposal section
- financial dependency
- status: covered / gap / clarification / not applicable

Also extract:

- evaluation criteria and weights
- eligibility and mandatory attachments
- requested qualifications or case evidence
- exact quantities and units
- service levels and response times
- project duration and key dates
- approval model and dependencies
- exclusions and client responsibilities if stated
- required templates, portal fields, guarantees, declarations, and signatures

Never rely on the proposal outline as a substitute for the ledger.

### Stage 2: Saudi relevance and freshness gate

Read `references/saudi-regulatory-freshness.md`.

Only check a regulatory domain if the scope activates it. Typical gates:

- government procurement and Etimad process
- local content or prescribed procurement mechanisms
- VAT and invoice treatment
- personal data, monitoring, CRM, AI, analytics, research, or audience databases
- influencer and social media advertising activity
- events, shows, performers, venue access, filming, drone, or entertainment permits

Record the authority, source URL, checked date, applicability, and exact bid implication in the source ledger.

Do not turn a regulatory check into legal advice. If the applicability is uncertain and material, mark it for client or legal confirmation.

### Stage 3: Solution architecture

Read `references/technical-proposal-anatomy.md` and the relevant service modules.

Build the offer from the problem and requirement model, not from a standard deck.

Minimum technical architecture when relevant:

1. cover and submission identity
2. executive summary
3. our understanding of context, challenge, and desired outcome
4. objectives and success measures
5. solution principles or strategic direction
6. workstreams and methodology
7. deliverables with units, timing, acceptance criteria, and owners
8. operating model, governance, approvals, and escalation
9. implementation schedule or run of show
10. team structure and role responsibilities
11. quality assurance and acceptance process
12. measurement, reporting, and decision cadence
13. risks, mitigations, fallbacks, assumptions, and dependencies
14. relevant case evidence and credentials, only when verified
15. compliance or evaluation-criteria map when required
16. next steps or required client inputs

A section exists only if it helps the evaluator make a decision or proves a requirement.

### Stage 4: Financial architecture

Read `references/financial-modeling.md`.

Create the commercial model from the technical scope.

For each priced item define:

- price line ID
- mapped requirement and deliverable
- pricing basis and unit
- quantity
- internal labor or effort input, when used
- vendor or production cost input, when used
- risk allowance policy, when authorized
- overhead policy, when authorized
- target commercial margin policy, when authorized
- quote unit price
- line total
- tax treatment
- included / optional / excluded status
- quote or cost source
- validity or price-dependency note

Client-facing files must not expose internal cost, margin, or hidden commercial logic unless requested.

If the RFP provides a mandatory BOQ, preserve it and use the internal model only as the calculation layer.

### Stage 5: Technical-financial reconciliation

Run a two-way check:

- every technical deliverable is priced, explicitly included at zero, client-supplied, or clearly excluded
- every client-facing price line has a technical scope reason
- quantities match across technical, financial, and appendices
- schedule matches staffing and supplier lead times
- SLAs match the team coverage actually priced
- options are not silently treated as core scope
- assumptions that change price are visible
- VAT and totals calculate correctly

A mismatch blocks `final` status.

### Stage 6: Red-team and submission QA

Read `references/final-qc.md`.

Run independent checks for:

- uncovered mandatory requirement
- scored criterion with weak or missing evidence
- factual claim with no evidence
- copied client name or stale project fact
- arithmetic or unit error
- inconsistent duration, date, quantity, or SLA
- undocumented assumption
- unpriced promise
- unsupported regulatory claim
- missing mandatory attachment or form
- language, RTL, numbering, table, and visual-readability failure

Produce a QC report with blocking, major, and polish findings. Do not hide blockers because the deadline is close.

### Stage 7: Artifact assembly

Use the host's available document, presentation, spreadsheet, and file tools. Do not assume a specific provider.

Produce only the artifacts requested, plus the internal ledgers needed for integrity.

Default deliverables when the user asks for a complete package:

- technical proposal
- financial proposal / BOQ
- requirement ledger
- compliance matrix
- assumptions and dependencies register
- risk register
- source ledger
- final QC report

## Accelerated mode

For a critical deadline, preserve these gates even if optional work is reduced:

1. requirement extraction
2. mandatory-form preservation
3. assumptions visibility
4. technical-financial reconciliation
5. arithmetic check
6. confidentiality scan
7. submission checklist

What may be reduced: optional market research, decorative sections, broad benchmarks, or extra concept routes.

## Failure taxonomy

### Requirement blindness
Signal: polished proposal but no traceable coverage of RFP clauses.
Recovery: return to requirement ledger and rebuild the outline from uncovered items.

### Template contamination
Signal: wrong client name, old dates, irrelevant KPIs, unexplained inherited scope.
Recovery: quarantine prior proposal content and keep only verified structural patterns.

### Pricing hallucination
Signal: plausible price with no rate, cost, quote, policy, or authorized assumption.
Recovery: replace with `PRICING INPUT REQUIRED` and generate the missing-input list.

### Scope-price drift
Signal: technical promise has no commercial basis or BOQ line has no technical purpose.
Recovery: run bidirectional reconciliation and block final status until resolved.

### Compliance theatre
Signal: claims such as "fully compliant" with no current source or clause mapping.
Recovery: downgrade claim to verified items only and add unresolved checks.

### Over-research
Signal: hours of generic Saudi market research with no effect on a requirement or decision.
Recovery: use the relevance gate. Research must change scope, risk, message, compliance, or price.

### Under-specified proposal
Signal: attractive high-level solution with no deliverable units, acceptance criteria, owners, or schedule.
Recovery: convert every promise into an executable work item.

### False precision
Signal: invented KPI targets, dates, audience numbers, cost estimates, or response times.
Recovery: mark assumptions and request or verify the missing evidence.

## Tempting shortcuts that are invalid

| Shortcut | Binding rule |
| --- | --- |
| "The old proposal already has this section" | Reuse structure only. Re-prove every fact and requirement |
| "The client probably expects 15% VAT" | Verify current tax treatment and whether prices are quoted inclusive or exclusive |
| "Use a single lump sum to keep it clean" | Follow the RFP. Unitize when required or when it materially improves commercial clarity |
| "Put the price in the technical deck too" | Keep it separate unless explicitly required |
| "Add more slides to look substantial" | Every section must prove, explain, de-risk, or price something |
| "Give a KPI so the proposal feels strong" | No KPI target without a baseline, contractual basis, accepted service target, or clearly labeled assumption |
| "Say we are compliant" | Show the clause map and evidence instead |
| "Use the previous client's case study" | Only with approved, verified, confidentiality-safe evidence |

## Handoff packet

A downstream agent receives:

- source inventory with versions and checked dates
- situation classification
- requirement ledger and coverage status
- clarification log
- chosen service routes
- technical outline and deliverable map
- financial mapping and missing pricing inputs
- applicable regulatory checks with URLs and dates
- assumptions, risks, and dependencies
- residual blockers
- artifact paths or file IDs
- QC status and proof freshness

## Progressive resources

- `references/rfp-forensics-and-compliance.md`
- `references/source-and-evidence-policy.md`
- `references/technical-proposal-anatomy.md`
- `references/financial-modeling.md`
- `references/saudi-regulatory-freshness.md`
- `references/risk-assumptions-and-governance.md`
- `references/writing-and-rtl.md`
- `references/final-qc.md`
- `references/benchmark-corpus-anonymized.md`
- `references/service-modules/*.md`

## Completion criteria

Do not call the proposal final until:

- no unresolved mandatory requirement is hidden
- mandatory forms and financial tables are preserved
- technical and financial scope reconcile
- pricing inputs are sourced or explicitly authorized assumptions
- totals and tax formulas pass checks
- material Saudi regulatory statements are current and relevance-gated
- every claim is verified, qualified, or removed
- assumptions, exclusions, dependencies, and options are visible
- confidentiality scan finds no stale client-specific detail
- final artifacts match the requested language, format, and submission structure
- the QC report contains no unresolved blocker
