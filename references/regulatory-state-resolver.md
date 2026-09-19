# Saudi Regulatory State Resolver

Checked baseline: 2026-09-19. This file is a routing guide, not a frozen legal summary.

## Why state matters

Saudi regulatory material can exist in different states:
- public announcement
- approved/enacted text
- implementing regulation
- effective obligation
- superseded rule
- buyer-specific instruction

Do not collapse these states.

## Procurement transition

In August 2026, official Saudi government reporting announced Cabinet approval of a new Government Tenders and Procurement Law. That fact alone does not tell an agent which text governs a specific September 2026 bid.

For each government bid, verify:
- applicable law/version
- publication in the official channel if needed
- effective date
- implementing regulation status
- transition provisions
- buyer/Etimad submission instructions

Useful official starting points:
- Ministry of Finance / Etimad information: https://www.mof.gov.sa/en/eservices/Pages/Etimad.aspx
- Saudi Press Agency procurement-law announcement: https://www.spa.gov.sa/en/N2647942
- buyer-specific Etimad guidance where available

Never cite a secondary law-firm note as the final authority.

## Local content

LCGPA obligations can vary by procurement, category, mandatory list, certificate, and current mechanism.

Start at:
https://lcgpa.gov.sa/en/LocalContent/Pages/default.aspx

Record whether the current bid actually invokes a local-content mechanism.

## VAT and tax

Current official starting points:
- VAT law: https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/VATLaw.aspx
- VAT implementing regulations: https://zatca.gov.sa/en/RulesRegulations/Taxes/Pages/VATImplementingRegulations.aspx

The standard VAT rate is currently 15%, but the proposal engine must still store the rate as sourced, checked input rather than timeless code.

If foreign suppliers, withholding, or cross-border services matter, open a separate tax applicability question. Do not infer treatment from VAT alone.

## Personal data and AI

Official starting points:
- SDAIA / DGP PDPL guide:
  https://dgp.sdaia.gov.sa/wps/portal/pdp/knowledgecenter/details/PDPLCP/
- Personal data transfer regulation:
  https://dgp.sdaia.gov.sa/wps/wcm/connect/e5bbede0-1119-4f70-b4ef-f043ce58d780/Regulation%2Bon%2BPersonal%2BData%2BTransfer%2BOutside%2Bthe%2BKingdom..pdf?MOD=AJPERES

For AI/digital proposals, map actual data flow before writing compliance language.

## Media and advertising

Use the current official authority identity shown on:
- General Authority for Media Regulation: https://gmedia.gov.sa/en/overview
- current laws/regulations: https://gmedia.gov.sa/en/executive-regulations

Do not preserve old authority names or acronyms from legacy proposals.

Specific advertising/influencer licensing must be verified against the current official service, activity type, and actor.

## Events and entertainment

Official starting points:
- GEA services: https://www.gea.gov.sa/en
- Entertainment Event Permit: https://www.gea.gov.sa/en/services/entertainment-event-permit-new-request
- Entertainment Show Permit: https://www.gea.gov.sa/en/services/entertainment-show-permit

Permit lead time depends on the classified activity. Record the live requirement in the bid schedule rather than using a generic event-permit assumption.

## Resolver output

For each triggered rule produce:
```yaml
reg_id:
domain:
authority:
instrument:
status:
publication_date:
effective_date:
checked_at:
official_url:
technical_implication:
commercial_implication:
open_question:
```
