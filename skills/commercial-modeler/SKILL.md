---
name: commercial-modeler
description: "Engineer commercial models, client BOQs, financial proposals (العرض المالي), and payment schedules for Saudi MarCom bids from grounded deliverables and authorized price inputs. Use for labor/vendor costing, VAT presentation, options, milestones, and commercial assumptions. Do NOT invent rates, redesign mandatory BOQs, or write the technical narrative."
version: 0.3.0
pack: saudi-marcom-proposal
role: atomic-skill
inputs: [deliverable_map, boq_templates, pricing_inputs, regulatory_source_ledger, response_strategy]
requires: [source_grounding]
produces: [pricing_engine, client_boq, payment_milestones, commercial_assumptions]
gates: [zero_unsourced_pricing, mandatory_boq_preservation, internal_cost_isolation, value_add_commercial_treatment]
neural_links:
  precursors: [technical-architect, regulatory-scout, bid-strategist]
  continuations: [scope-reconciliation]
  lateral_peers: [technical-architect]
  recovery: commercial-modeler
---

# Commercial Modeler

Translate technical scope into a defensible commercial model without inventing prices.

## Pricing source order

1. approved company rate card
2. current vendor quote
3. approved internal cost basis
4. authorized normalized historical basis
5. user-approved planning scenario

No source means `PRICING INPUT REQUIRED`.

Market research may inform an internal sensitivity check, but must not silently become a final bid price.

## Model layers

Keep separate:
- labor
- supplier/direct costs
- licenses/technology
- media spend
- creator/talent fees
- logistics/travel
- contingency/risk only when authorized
- overhead/margin internal only
- VAT/tax presentation

## Unit selection

Use the unit that reflects the cost driver:
- person-day/month
- item/output
- finished minute
- production day
- event/day
- attendee
- report
- platform/license
- campaign
- creator deliverable
- supplier package

Do not convert a buyer-prescribed unit merely to fit the internal model. Build a mapping layer instead.

## Mandatory BOQ

If buyer supplies a BOQ:
- preserve row order, wording, columns, formulas/form constraints where required
- map internal cost model behind it
- log impossible/ambiguous units as clarification risks
- never add internal margin columns to the client file

## Value-add and options

Every strategy-level value-add must be:
- priced
- included with an explicit funded basis
- optional
- client-supplied
- excluded

No "free dashboard/workshop/support" can enter technical prose without commercial treatment.

## Payment milestones

Tie payment to measurable acceptance where allowed.

Do not invent advance-payment percentages or validity periods. Examples in old proposals are not policy.

## VAT

Use Regulatory Scout evidence for current rate/treatment and buyer format.

Keep VAT as configurable input. Verify inclusive/exclusive presentation.

## Vendor-dependent scope

For events, creators, production, licenses, travel:
- quote source
- quote date
- validity
- quantity basis
- substitution assumptions
- FX if applicable
- cancellation/change exposure where material

## Handoff

Output:
- internal pricing engine
- client BOQ
- payment milestones
- commercial assumptions/exclusions
- price-source ledger or receipts

Then route to scope-reconciliation.

## Resources

- references/financial-modeling.md
- references/service-modules/*.md
- tools/reconciliation-schema.json
- templates/pricing-model.xlsx
- templates/boq.csv
