---
name: service-router
description: "Route and structure Saudi MarCom tender requirements across the 6 core service modules: Media & Comms, Marketing & Promotion, Events & Experiences, Crisis & Reputation, Digital & AI, and Monitoring & Intelligence. Use when classifying tender scopes, setting up multi-service delivery frameworks, and loading specialized domain guidance. Do NOT use for writing final narrative text, financial calculations, or single-line quotes."
version: 0.1.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
requires:
  - source_grounding
produces:
  - active_service_modules
  - service_boundaries
gates:
  - boundary_isolation
  - reference_module_activation
neural_links:
  precursors:
    - rfp-forensics
  continuations:
    - technical-architect
  lateral_peers:
    - regulatory-scout
  recovery: rfp-forensics
---

# Service Architecture Router

Classify tender requirements into specialized Saudi MarCom service families.

## Mission

Analyze the extracted requirements and route workstreams into the appropriate specialized service architectures, defining clear operational boundaries and loading corresponding technical references.

## Activation Contract

Activate when:
- Determining the technical composition of a Saudi MarCom tender
- Structuring multi-disciplinary proposals spanning media, events, digital, and crisis communications
- Deciding which specialized service reference modules must govern the technical architecture
- Defining cross-stream dependencies (e.g., event PR feeding media monitoring)

Do NOT activate for:
- Writing the comprehensive technical proposal (use `technical-architect`)
- Calculating bill of quantities or staffing rates (use `commercial-modeler`)
- Conducting general RFP clause extraction (use `rfp-forensics`)

## Non-Negotiable Invariants

1. **Explicit Module Activation**: Every active workstream must explicitly load its dedicated service reference file.
2. **Boundary Definition**: In multi-service tenders, define clear interface boundaries to prevent duplicate staffing or unowned deliverables.
3. **No Phantom Workstreams**: Do not propose unsolicited service modules unless presented as clearly labeled optional enhancements.

## Execution Procedure

### Step 1: Scope Family Classification
Map each requirement in the ledger against the 6 core service families:

| Service Family | Scope Indicators | Governing Reference |
|---|---|---|
| **Media & Corporate Comms** | Press releases, media relations, spokesperson prep, executive thought leadership, op-eds, bilingual content | `references/service-modules/media-corporate-comms.md` |
| **Marketing & Promotion** | Multi-channel campaigns, creative concepts, social media management, brand awareness, activation, collateral | `references/service-modules/marketing-promotion.md` |
| **Events & Experiences** | Forums, exhibitions, launch events, VIP hospitality, staging, AV production, permitting, crowd logistics | `references/service-modules/events-experiences.md` |
| **Crisis & Reputation** | Risk audits, crisis manuals, dark site preparation, 24/7 incident response, stakeholder escalation | `references/service-modules/crisis-reputation.md` |
| **Digital & AI** | Web/app development, chatbots, AI content workflows, CRM, performance marketing, social listening | `references/service-modules/digital-ai.md` |
| **Monitoring & Intelligence** | Media tracking, sentiment analysis, daily news clipping, influencer monitoring, competitive intelligence | `references/service-modules/monitoring-intelligence.md` |

### Step 2: Multi-Service Interface Mapping
When a tender spans multiple families:
- Map inputs and outputs between workstreams:
  - *Example*: `Monitoring & Intelligence` provides daily sentiment alerts $\to$ `Crisis & Reputation` triggers response protocols.
  - *Example*: `Creative & Promotion` generates campaign assets $\to$ `Events & Experiences` displays assets on venue LED walls.
- Prevent duplicate resource allocation (e.g., shared creative director across marketing and events).

### Step 3: Architecture Directives Generation
Synthesize specific technical constraints for `technical-architect`:
- List mandatory reference files to load
- Define core vs optional enhancement streams
- Specify bilingual language requirements (e.g., Arabic-first copy for government audiences)

## Neural Handoff Contract

When complete, output:
- `active_service_modules`: List of activated modules and referenced guides
- `service_boundaries`: Matrix of workstream responsibilities and handoffs
- Target Continuation: Hand off directly to **`technical-architect`**

## Progressive Resources
- `routers/service-router.yaml`
- `references/service-modules/*.md`
