# Monitoring and Intelligence Module

## Owns

- media monitoring
- social listening
- source tracking
- sentiment and topic analysis
- issue detection and early warning
- executive intelligence reports
- dashboards
- competitor/category intelligence when requested
- alert routing into crisis or communications teams

## Discovery questions

- Which sources are in scope: social, news, broadcast, print, forums, creators?
- Which geographies and languages?
- What query taxonomy/keywords/entities?
- Is historical data required?
- What does "real time" mean operationally?
- What alerts are urgent and to whom?
- Is sentiment machine-only, human-reviewed, or hybrid?
- How many reports and what cadence?
- What source licensing/tooling is available?
- How should false positives be handled?
- Does personal data or profiling create PDPL relevance?

## Operating architecture

1. source universe
2. query/topic taxonomy
3. ingestion/tool layer
4. classification and analyst QA
5. alert severity
6. escalation
7. dashboard/reporting
8. insight/recommendation
9. query tuning and learning

Tool output is not automatically intelligence. Human interpretation may be required.

## Deliverable units

- source/query setup
- dashboard
- daily brief
- weekly report
- monthly report
- alert
- analyst shift
- monitoring month
- issue deep-dive
- competitor report
- crisis surge
- executive briefing

## SLA contract

Define:
- monitored window
- source refresh reality
- alert threshold
- detection-to-alert clock
- analyst validation
- recipient
- escalation path
- false-positive handling
- outage/fallback

Avoid the term "real time" unless the tool/source and operations can support the exact latency claimed.

## Capacity and pricing drivers

- languages
- source breadth
- keyword/topic complexity
- history depth
- dashboard seats/licenses
- operating hours
- alert volume
- analyst QA
- report frequency
- crisis surge
- API/data export

## Sentiment discipline

Document:
- model/tool used if relevant
- language limitations
- human review policy
- confidence handling
- sampling/QA method

Do not present sentiment as objective truth without method limitations.

## Failure modes

- 24/7 monitoring funded as one business-hours analyst
- source universe not defined
- reports count does not match contract duration
- dashboard license omitted
- alert SLA ignores tool refresh interval
- machine sentiment treated as definitive
- monitoring recommendations drift into unpriced crisis consulting
- personal data/profiling implications ignored
