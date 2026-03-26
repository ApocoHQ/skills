---
domain: agent-testability
last-reviewed: 2026-03-26
status: draft
sources: [team experience with agent-driven development]
---

## Stance
A repository is agent-testable when an agent can go from `git clone` to green tests without human intervention, and when test failures give the agent enough information to diagnose and fix the problem. This is empirical — the only way to know is to try. Agent-testability is a prerequisite for agents contributing meaningful code; without it, agents produce untested changes or get stuck on environment issues that a human would work around by asking someone or googling.

## What to Look For

### Environment bootstrapping
- Zero-to-green path exists — clone, install, test succeeds with no manual steps, no secrets to fetch, no services to start manually
- Test infrastructure is codified — databases, queues, external services are started by the test runner or a single setup command (docker-compose, testcontainers, or equivalent)
- Secrets needed for tests are either absent (test infrastructure doesn't require them) or have committed test-only defaults — agents cannot retrieve secrets from vaults or ask someone
- `.env.example` or equivalent covers every variable the test suite needs, with working defaults for the test environment

### Test discoverability
- An agent can determine which tests to run after changing a file — through colocated test files, consistent naming conventions (`foo.ts` -> `foo.test.ts`), or a test manifest
- The test command is documented and obvious — `npm test`, `make test`, or clearly stated in CLAUDE.md / README
- Test suites can be run selectively — by file, by directory, by pattern — so an agent can validate its change without running the entire suite

### Failure actionability
- Infrastructure failures are distinguishable from test failures — "connection refused" is not a test bug, and the error message should make this obvious so agents don't chase phantom code bugs
- Flaky tests are quarantined — an agent encountering a flaky failure will waste entire cycles diagnosing something that isn't its fault, or worse, introduce unnecessary "fixes"
- Test failures include enough context to locate the problem — not just an assertion diff but the operation and inputs that led to the failure

### Output interpretability
- Test runner output is structured — agents can programmatically distinguish pass, fail, skip, and error
- Failed test output includes the test name, file location, and failure reason in a parseable format
- Application logs during tests don't drown out test results — route them separately or suppress them, so the agent can find the actual failure

## Assessment Process

This domain benefits from a try-diagnose-fix loop rather than pure code review. When assessing a repo's agent-testability:

1. **Try it** — actually run the test command and observe what happens. The failure mode is the diagnostic.
2. **Classify blockers** — each failure is one of: missing environment, missing dependency, configuration issue, or actual test bug. Prioritize environment and configuration — these block everything else.
3. **Fix the bootstrapping first** — nothing else matters until tests run. This often means adding docker-compose for services, committing test-only env defaults, or scripting setup steps.
4. **Then address output and discoverability** — once tests run, evaluate whether an agent could act on the results.

## Red Flags
- Setup instructions that include "ask X for the credentials" or "copy from the staging server"
- Tests that require a specific machine state not codified anywhere (running database, populated cache, specific OS tooling)
- Test output that requires human interpretation to determine pass/fail
- No way to run a single test file — the suite is all-or-nothing
- Tests that fail on first run after clone but pass on subsequent runs (hidden state dependency)

## See Also
- **testing-strategy** — what good tests look like (behavior over implementation, E2E over unit, test isolation)
- **developer-experience** — one-command setup, fast feedback loops, parseable output

## Known Gaps
- Guidance for repos that depend on external paid services for testing (Stripe, Twilio, etc.)
- CI-specific agent-testability (agents running in CI vs locally)
- Test data management strategies for agent workflows
- Monorepo test orchestration for agents
