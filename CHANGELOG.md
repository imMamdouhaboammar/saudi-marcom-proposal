# Changelog

## 0.4.1 - 2026-09-19

### Fixed
- security scan now inspects UTF-8 extensionless files and dotfiles instead of relying only on filename suffixes
- GitHub Actions permission audit now checks workflow-level and job-level permission grants
- CI now runs the full test discovery set and validates fix branches
- GitHub Actions checkout and Python setup dependencies upgraded to Node 24 based v7 releases
- README, evaluation report, review report, manifest, and master Skill version are synchronized
- README architecture now reflects all 12 atomic skills
- validation now detects release-document version drift

### Added
- CodeRabbit path-specific review guidance for executable skill, router, state, regulatory, evaluation, and validation surfaces
- compact golden decision cases for critical bid behaviors
- deeper benchmark fixtures for public-sector MarCom, private event, crisis-monitoring, and digital-AI cases

## 0.4.0 - 2026-09-19

### Added
- guarded shared bid-state architecture and JSON state contract
- buyer-context router
- bid-strategist atomic skill
- precedent-miner and evaluator-simulator atomic skills
- cross-cutting service lenses for multilingual, onsite, measurement, data/security, production, and vendor dependencies
- regulatory effective-state resolver for announced, enacted, effective, superseded, and unknown rules
- capacity and pricing-basis commercial model
- semantic scope-price reconciliation and change invalidation
- specialist agent contract
- provider-neutral tool registry and independent reviewer adapter
- capacity, evidence, change-impact, precedent, and evaluator templates
- expanded semantic eval suite including procurement transition, form fidelity, claim laundering, capacity stress, value-add scope, foreign-supplier tax ambiguity, precedent contamination, and evaluation mutation

### Changed
- all core atomic skills operate through the shared bid state
- media regulation guidance uses the current authority identity from official sources
- VAT is treated as a sourced input rather than immutable configuration
- artifact assembly requires render validation and stricter client/internal boundaries
- QC evaluates evaluator usability as well as compliance

### Evaluation status
- deterministic and static validation are required before merge
- behavioral maturity still requires a fresh external agent harness run against the current corpus
