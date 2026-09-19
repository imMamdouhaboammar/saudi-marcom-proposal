# Tool Capability Contract

The canonical Skill is provider-neutral. Hosts can map these capability families to available tools.

## Required capability families

### File/source discovery

- list/search connected files
- read documents, presentations, spreadsheets, PDFs, and text
- preserve source identifiers and page/section references

### Current web research

- search official Saudi domains
- fetch current pages
- capture URL and check date

### Spreadsheet production

- create/edit formulas, formatting, validations, and separate internal/client sheets
- inspect formulas and scan for spreadsheet errors

### Document/presentation production

- create/edit Arabic and English documents and decks
- support native RTL
- export to client-required formats

### Validation

- search all artifacts for stale client identifiers or confidential patterns
- validate numeric reconciliation
- run pack/eval scripts when filesystem execution exists

## Capability degradation

If a required capability is missing:

- no live web: mark regulatory proof stale and do not claim current compliance
- no spreadsheet engine: produce a structured financial schema but do not claim formula verification
- no document renderer: produce content structure but mark visual QA incomplete
- no source access: ask for or clearly list the missing source instead of reconstructing it from memory

## Secret handling

Never copy credentials, bank details, API keys, private contact information, or unrelated sensitive identifiers from a benchmark source into a new proposal.
