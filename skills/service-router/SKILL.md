---
name: service-router
description: "Classify Saudi MarCom bid scope into specialist service families and cross-cutting operational lenses, then define ownership and interfaces between them. Use after requirement extraction for multi-service or ambiguous communications, marketing, event, crisis, digital/AI, or monitoring scopes. Do NOT use to draft final narrative, create prices, or add unsolicited workstreams."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs:
  - requirement_ledger
requires:
  - source_grounding
produces:
  - active_service_modules
  - cross_cutting_lenses
  - service_boundaries
gates:
  - boundary_isolation
  - material_scope_owned
  - no_phantom_workstreams
neural_links:
  precursors: [rfp-forensics]
  continuations: [technical-architect]
  lateral_peers: [regulatory-scout, bid-strategist]
  recovery: rfp-forensics
---

# Service Architecture Router

Route requirements to domain guidance without duplicating scope.

## Primary service families

Activate only when supported by requirements:
- media and corporate communications
- marketing and promotion
- events and experiences
- crisis and reputation
- digital and AI
- monitoring and intelligence

Load the corresponding file under references/service-modules/.

## Cross-cutting lenses

Also inspect for concerns that span families:
- creative/production
- measurement/analytics
- multilingual operations
- onsite/live operations
- data/security
- third-party/vendor dependencies

Use routers/service-router.yaml as the canonical routing map.

## Boundary contract

For each active module define:
- owned requirements
- inputs received
- outputs produced
- shared resources
- downstream consumers
- handoff timing
- exclusions
- duplicate-risk notes

Monitoring may detect a reputation incident while crisis owns the response protocol. Do not price two separate war rooms unless the architecture actually requires them.

## Optional enhancements

A useful but unrequested idea may be proposed only as:
- clearly optional
- operationally defined
- commercially treated
- excluded from mandatory compliance coverage unless adopted

Do not smuggle value-add into base scope.

## Failure taxonomy

- one requirement owned by nobody
- same deliverable duplicated across modules
- digital/AI used as a catch-all for analytics or monitoring
- monitoring and crisis responsibilities blurred
- event production separated from required content/PR handoffs
- multilingual work treated as formatting only
- optional enhancement becomes an unpriced commitment

## Handoff

Append active modules, cross-cutting lenses, and boundary matrix to bid_state.

Continue to technical-architect.
