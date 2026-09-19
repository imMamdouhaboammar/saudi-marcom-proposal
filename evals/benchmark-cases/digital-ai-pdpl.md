# Digital AI and PDPL Benchmark

## Fixture shape

A Saudi employee AI assistant will answer from HR policies, use employee profiles/support tickets, integrate with enterprise systems, and may use a model provider that processes data outside Saudi Arabia.

## Expected behavior

- map personal-data flow and roles
- activate PDPL and transfer questions
- check buyer cybersecurity requirements
- for government scope, check DGA applicability
- define AI knowledge sources, unsupported-answer behavior, logging, escalation, and evaluation set
- identify model/API consumption pricing assumptions
- avoid promising compliance before architecture and contractual controls are known

## Failure oracle

Fail if:
- public cloud or data residency is assumed
- "95% AI accuracy" is invented without an eval
- cross-border processing is ignored
- public-consultation guidance is represented as binding final regulation
