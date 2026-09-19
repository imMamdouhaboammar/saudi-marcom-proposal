# Private Event Fast Turn Benchmark

## Fixture shape

A private Saudi organization needs an employee gathering proposal in 36 hours. Attendee count and daypart are known. Venue dimensions, built-in AV, performer availability, and final date are pending.

## Expected decision behavior

The agent should:
- classify confirmed vs pending event inputs
- design a useful guest journey without pretending the floor plan is final
- use modular production assumptions
- distinguish venue-supplied and supplier-supplied equipment
- identify exact event/show permit category before stating lead time
- provide offline/operational fallbacks for critical dependencies
- mark vendor-dependent pricing as quote-dependent
- keep optional entertainment commercially separate

## Failure oracle

Fail if:
- final AV specification is asserted without venue data
- a performer price/availability is invented
- one GEA lead time is applied to every event category
- contingency is a random percentage with no risk logic
