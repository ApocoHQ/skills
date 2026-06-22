---
domain: testing-strategy
last-reviewed: 2026-03-26
---

## Stance
E2E/integration over unit tests. Fewer, longer tests that verify core use cases end-to-end. Test real behavior, not current behavior. Playwright for frontend testing despite complexity. Hooks are more reliable than instructions for enforcing test checks. Heavily mocked unit tests gave false confidence in a prior incident where mock/prod divergence masked a broken migration. Design the test strategy before writing the test — understand what you control, what you observe, and whether that's enough to verify the feature.

## What to Look For
- Integration and E2E tests outnumber unit tests — unit tests are the exception for isolated pure logic, not the default
- Tests assert expected behavior against a spec, not snapshot current output — a test that passes when the feature is broken is worse than no test
- Test setup uses real infrastructure (real database, real services) — mocks only at true system boundaries (third-party APIs), never for internal components
- Test names describe the scenario and expected outcome — `it("returns 401 when token is expired")` not `it("tests auth")`
- Fewer, longer tests that walk through real user flows — prefer one test that creates, reads, updates, and deletes over four isolated CRUD tests
- Test isolation via separate database schemas and/or separate service instances per test suite — enables parallel execution without shared state interference
- A reusable test harness bootstraps the full environment in one call — database, queues, workers, mocks, cleanup. Individual tests don't wire their own infrastructure
- Mock implementations live alongside real implementations, implementing the same interface — controlled via config flags (e.g., `APIFY_MOCK=true`), not test-specific code paths. Mock objects track calls and data for assertions
- Async/event-driven behavior tested via polling utilities (`waitFor`) with configurable timeout, delay, and diagnostic labels — not arbitrary sleeps
- Unit tests are appropriate for pure domain logic with no I/O — scoring algorithms, state machines, and aggregate behavior benefit from exhaustive unit test coverage that would be impractical as E2E tests
- Test strategy is designed before writing the test — map the feature to testable boundaries (what do we control, what do we observe, are there gaps?) then write the plan, then the code

## Red Flags
- Tests that mirror implementation rather than behavior
- Extensive mocking of internals
- Agents marking test failures as "expected" rather than diagnosing root cause
- Test files longer than the code they test
- Tests that use arbitrary `sleep()` instead of polling for conditions
- Test suites that can't run in parallel due to shared database or shared state

## See Also
- **developer-experience** — single-command test runs, parseable output, flaky test quarantine
- **agent-testability** — can an agent go from clone to green tests without human help

## Known Gaps
- Optimal testing strategy for logic-heavy frontends
- Property-based testing guidance
