# Financial Modeling for Saudi MarCom Proposals

## Principle

The commercial offer is a model of the technical promise. It is not a separate spreadsheet built at the end by guessing a total.

## Commercial layers

Keep three views separate:

1. `Internal Cost Model`: labor, vendor, production, logistics, overhead, risk, target margin, discounts
2. `Client BOQ`: only the commercial detail the buyer should see
3. `Payment and Validity Terms`: cash-flow triggers, tax treatment, dependencies, validity, and options

Never expose hidden cost or margin logic in a client BOQ unless the user explicitly wants open-book pricing.

## Unit taxonomy

Choose a unit that matches how the work is consumed or accepted.

Common service units include:

- item / design
- post / content piece
- video
- minute of finished motion or film
- production day
- shooting hour
- person-day
- person-month
- month / retainer
- report
- campaign
- event / activation
- venue day
- attendee
- language
- page
- platform
- dashboard / setup
- license / subscription
- integration
- workshop
- training session
- influencer / visit or deliverable
- supplier package

Do not default everything to person-month. A mixed model often gives the buyer and delivery team better control.

## Price input hierarchy

Use, in order:

1. current approved rate card
2. current vendor quote
3. verified internal cost basis and approved commercial policy
4. approved historical normalized cost benchmark
5. explicit user-authorized planning assumption

If none exists, the correct output is a structured blank, not a plausible number.

## Technical link

Every line should carry a mapping key such as `P-001` and point to a deliverable or commercial allowance.

Examples:

- T-014 monthly monitoring report -> P-008 monitoring service per month
- T-021 conference coverage -> P-015 production crew per event day + P-016 editing package
- T-034 AI assistant pilot -> P-025 implementation package + P-026 optional model/API allowance

## Direct cost

A typical internal formula can be:

`Direct Cost = (labor effort x labor unit cost) + vendor cost + pass-through cost`

Use only components supported by the commercial policy.

## Overhead, risk, and margin

These are policy inputs, not universal Saudi market percentages.

If the company has an approved policy, model it transparently in the internal workbook. If not, leave the field blank or require authorization.

Do not hide double-counted risk. For example, a vendor quote already containing contingency should not automatically receive the same contingency again without rationale.

## Optional items

Label optional items clearly and decide whether they are included in the evaluated total based on the RFP.

Examples:

- paid media budget
- influencer fees
- venue rental
- travel and accommodation
- paid stock, music, voice-over, or footage rights
- permits
- third-party AI/API consumption
- cloud hosting
- extra languages
- after-hours coverage

If an item is client-supplied, say so explicitly.

## Tax

The current Saudi standard VAT rate is 15% as of the package baseline date, but the proposal agent must verify current treatment and the buyer's required presentation for each bid. The workbook keeps VAT as an editable sourced input rather than a hardcoded universal constant.

## Payment milestones

Milestones should follow observable acceptance or contractual triggers when possible, such as:

- award / signed purchase order
- approved strategy or design phase
- supplier commitment milestone
- event completion
- monthly service acceptance
- final handover

Do not reuse payment percentages from another client as a default.

## Validity and quote dependencies

State material dependencies:

- vendor price validity
- venue availability
- exchange-rate exposure if any
- performer / talent availability
- travel timing
- production dates
- media budget treatment
- tax presentation

## Financial QA

Check:

- subtotal equals line totals
- VAT base is correct
- VAT arithmetic is correct
- total including VAT is correct
- optional rows are included or excluded as intended
- discounts do not push below authorized commercial floor
- quantity and units match the technical offer
- zero-value included lines are intentionally marked, not accidentally unpriced
- no internal cost or margin columns leak into the client-facing sheet
- no bank, account, or tax identifier is copied from a benchmark file

Use `templates/pricing-model.xlsx` as a starting calculation workbook, then adapt it to the buyer's mandatory BOQ.
