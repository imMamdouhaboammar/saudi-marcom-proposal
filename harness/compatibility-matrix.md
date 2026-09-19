# Harness Compatibility Matrix

The pack is provider-neutral. Compatibility means a host can map canonical capabilities without changing the decision contract.

## Compatibility levels

- A: full proposal workflow including private sources, live research, spreadsheet verification, artifacts, and render QA
- B: full reasoning workflow with some artifact or render limitations
- C: content/schema workflow only, with explicit missing verification
- Unsupported: host cannot read the required source set

## Capability matrix template

| Host family | Source connectors | Live web | Spreadsheet | Artifact generation | Render QA | Repo/test | Expected level |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ChatGPT-style tool host | map per deployment | map per deployment | map per deployment | map per deployment | map per deployment | map per deployment | A-C |
| Claude-style MCP host | map MCP servers | map MCP/web | map MCP | map MCP/local tools | map browser/doc tools | map shell/GitHub | A-C |
| Codex-style repo agent | limited unless connectors supplied | optional | local file/tool dependent | file generation possible | external check may be needed | strong | B-C |
| OpenCode-style local agent | local/provider plugins | optional | local libraries/tools | local generation | external renderer may be needed | strong | B-C |

These rows describe integration shapes, not guaranteed capabilities of every installation.

## Adapter acceptance tests

A host adapter passes only when it demonstrates:

1. Source provenance
   - read an RFP fixture
   - emit a source receipt
   - preserve source location

2. Current-source research
   - find an official public source
   - fetch it
   - record checked time
   - distinguish source status such as final guidance vs consultation

3. Commercial boundary
   - read a BOQ or price fixture
   - keep internal cost fields out of client output
   - fail cleanly if spreadsheet verification is unavailable

4. Artifact boundary
   - generate or return the requested artifact representation
   - report whether render inspection occurred
   - never claim visual QA when it did not

5. Recovery
   - remove one required capability
   - confirm the workflow degrades to an explicit incomplete/blocking status rather than simulating success

## Cross-harness invariant

Different hosts may call different tools. They must still produce the same logical contracts:
- requirement ledger
- applicability/source ledger
- response strategy for scored bids
- deliverable map
- commercial treatment
- reconciliation result
- QC status

The pack should be retuned only when behavioral evidence shows a model/host-specific regression, not merely because tool names differ.
