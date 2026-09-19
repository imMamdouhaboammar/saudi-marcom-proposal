# Saudi Regulatory Freshness Gate

Baseline research date: 2026-09-19

This file is a routing guide, not a substitute for a fresh official-source check. Rules, forms, thresholds, services, and implementation dates can change.

## 1. Government procurement and Etimad

Activate when the buyer is a Saudi government entity or the RFP routes submission through Etimad.

Baseline facts:

- The Saudi Ministry of Finance describes Etimad as the government platform for tender offering, bid submission, bid examination, technical evaluation, and awarding.
- On 2026-08-05, the Ministry of Finance announced Cabinet approval of a new Government Tenders and Procurement Law.

Because that approval is recent relative to this pack, never hardcode old-law thresholds or procedures as current. Before making a compliance statement, verify:

- current effective law text and implementation date
- current executive regulations
- current Etimad submission instructions
- the specific RFP and issued addenda
- any buyer-specific forms

Official starting points:

- https://www.mof.gov.sa/en/eservices/Pages/Etimad.aspx
- https://www.mof.gov.sa/en/MediaCenter/news/Pages/News_05082026.aspx
- https://mof.gov.sa/en/tenders/Pages/default.aspx

## 2. Local content

Activate only when the RFP, procurement mechanism, or buyer requires it.

Check the current Local Content and Government Procurement Authority material and the exact RFP mechanism. Do not assume every service bid uses the same local-content method.

Record whether the requirement affects:

- eligibility
- evaluation
- mandatory certificate or form
- price preference or calculation
- supplier selection
- reporting during delivery

## 3. VAT and tax presentation

Activate for every financial offer, but keep the check proportional.

Baseline: ZATCA states the standard VAT rate is 15% as of the baseline date.

Official starting points:

- https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/default.aspx
- https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/VATImplementingRegulations.aspx

Verify:

- rate and applicable treatment
- whether the buyer requires inclusive or exclusive prices
- whether the mandatory BOQ has a specific VAT row or tax presentation
- any relevant invoice or pass-through treatment

Do not provide tax advice beyond the source-supported bid implication.

## 4. Personal data and AI

Activate when the service touches personal data, CRM/contact lists, audience research, social listening tied to identifiable persons, employee data, event registration, biometrics, recordings, AI systems using personal data, or cross-border processing.

Official SDAIA starting points:

- https://dgp.sdaia.gov.sa/
- https://sdaia.gov.sa/en/SDAIA/about/Pages/RegulationsAndPolicies.aspx

Baseline: the Saudi Personal Data Protection Law is supervised by SDAIA, with current guidance and regulations available through the National Data Governance Platform.

Proposal questions may include:

- controller / processor roles
- lawful basis and notices
- data minimization
- retention and deletion
- access control
- sub-processors
- data transfer outside the Kingdom
- incident handling
- AI vendor data use
- whether a privacy impact assessment is required

Do not promise a data architecture that has not been verified with the buyer's IT/security requirements.

## 5. Social media advertising and influencers

Activate when the scope includes paid or sponsored creator content, influencer activations, or regulated media activity.

Official starting point:

- https://my.gov.sa/en/services/21449

The National Platform lists the General Authority of Media Regulation service for the social media advertising content provider license commonly known as "Trusted". Verify current applicability, eligibility, and who is responsible for compliance for the exact campaign.

Never assume an influencer is licensed because they appeared in a prior campaign.

## 6. Events and entertainment

Activate when the scope includes public or private entertainment shows, performers, live acts, or activities that require authority approval.

Official GEA starting point:

- https://www.gea.gov.sa/en/services/entertainment-show-permit

The baseline service page states that certain entertainment show permit requests should be submitted at least 10 working days before the show and lists requirements including site approval and show-content details. Verify the current service and whether it applies to the exact event category.

Also identify other responsibility areas when relevant:

- venue and municipality requirements
- Civil Defense or safety requirements
- filming and drone permissions
- talent / performer approvals
- customs for imported event equipment
- access badges and security

Do not state that a permit is secured until there is evidence.

## Freshness record format

Every material regulatory check should generate:

| Field | Value |
| --- | --- |
| Domain | procurement / VAT / PDPL / media / event / other |
| Authority | official authority name |
| URL | source |
| Checked | ISO date-time |
| Applies? | yes / no / uncertain |
| Bid implication | exact requirement or risk |
| Owner | party responsible for confirmation/action |
| Status | verified / clarification / legal confirmation needed |

## Stop rule

If an uncertain rule can disqualify the bid, materially alter price, or make the proposed service unlawful or infeasible, the proposal cannot be marked final until the uncertainty is resolved or explicitly assigned to qualified legal/compliance confirmation.
