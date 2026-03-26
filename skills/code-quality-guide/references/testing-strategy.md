---
domain: testing-strategy
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, linkedin-manager e2e patterns]
---

## Stance
E2E/integration over unit tests. Fewer, longer tests that verify core use cases end-to-end. Test real behavior, not current behavior. Playwright for frontend testing despite complexity. Hooks are more reliable than instructions for enforcing test checks. Heavily mocked unit tests gave false confidence in a prior incident where mock/prod divergence masked a broken migration.

## What to Look For
- Integration and E2E tests outnumber unit tests — unit tests are the exception for isolated pure logic, not the default
- Tests assert expected behavior against a spec, not snapshot current output — a test that passes when the feature is broken is worse than no test
- Test setup uses real infrastructure (real database, real services) — mocks only at true system boundaries (third-party APIs), never for internal components
- Test names describe the scenario and expected outcome — `it("returns 401 when token is expired")` not `it("tests auth")`
- Fewer, longer tests that walk through real user flows — prefer one test that creates, reads, updates, and deletes over four isolated CRUD tests

## Red Flags
- Tests that mirror implementation rather than behavior
- Extensive mocking of internals
- Agents marking test failures as "expected" rather than diagnosing root cause
- Test files longer than the code they test

## See Also
- **developer-experience** — single-command test runs, parseable output, flaky test quarantine

## Known Gaps
- Optimal testing strategy for logic-heavy frontends
- When unit tests ARE appropriate in agent workflows
- Property-based testing guidance
