---
domain: agent-testability
last-reviewed: 2026-03-30
---

## Stance
A repository is agent-ready when an agent can *find and follow instructions* (navigability) and *run and interpret tests* (testability) — going from `git clone` to green tests without human intervention. Both are empirical — the only way to know is to try.

## Assessment Process

1. **Try it** — run the test command and observe. The failure mode is the diagnostic.
2. **Classify blockers** — missing instructions, missing environment, missing dependency, configuration issue, or actual test bug. Prioritize instructions and environment.
3. **Fix navigability first** — if the agent can't find its instructions, nothing else matters.
4. **Fix bootstrapping second** — nothing else matters until tests run.
5. **Then address output and discoverability** — once tests run, can an agent act on the results?

## What to Look For

### Agent-facing file design

- **Directives are reachable from the auto-loaded file** — each AI tool auto-loads specific files (Claude Code: `CLAUDE.md`; others: `AGENTS.md`). Directives not in these files or imported by them are invisible. Files that are neither auto-loaded nor imported only work if something explicitly routes the agent to them.
- **CONTRIBUTING.md as a navigability source** — many repos have a `CONTRIBUTING.md` with setup, testing, and contribution conventions. It's not auto-loaded by AI tools, but it's often the most complete human-facing onboarding doc. If it exists, the auto-loaded file should reference or import relevant sections rather than duplicating them.
- **Architecture reading is mandated from the auto-loaded file** — agents that don't understand the system's design will violate its conventions. The mandate must be in the auto-loaded file, not in a file the agent has to discover.
- **Directives before reference material** — agents that encounter reference (architecture, design context) before directives (commands, decision tables, safety rules) get primed into exploration mode. Observed: an agent reading 60 lines of architecture before a decision table ignored the table entirely.
- **Routing instructions at the top** — "when asked to do X, use the table in Section N." Without explicit routing, the agent defaults to exploring the codebase regardless of what the file contains further down.
- **Decision tables over prose** — "if working on X, run Y" as a lookup table works; the same information in paragraph form gets lost.

### Agent guardrails

- Test strategy design enforced before implementation — agents map features to testable boundaries before writing tests or code
- Conservative permissions by default — settings.json auto-allows only read-only operations

### Environment bootstrapping

- Zero-to-green path — clone, install, test succeeds with no manual steps, no secrets to fetch, no services to start manually
- Test infrastructure is codified — databases, queues, external services started by the test runner or a single setup command
- Secrets are absent or have committed test-only defaults — agents cannot retrieve secrets from vaults or ask someone
- `.env.example` covers every variable the test suite needs, with working defaults. External services default to mock mode
- Mock flag pattern — real and mock implementations share the same interface, selected via config flags (e.g., `APIFY_MOCK=true`). No test-specific code paths in production code

### Test discoverability

- Agent can determine which tests to run after changing a file — colocated test files, consistent naming (`foo.ts` → `foo.test.ts`), or a test manifest
- Test command is documented and obvious — `npm test`, `make test`, or clearly stated in CLAUDE.md / README
- Test suites can run selectively — by file, directory, or pattern

### Failure actionability

- Infrastructure failures distinguishable from test failures — "connection refused" should not send agents chasing phantom code bugs
- Flaky tests are quarantined — agents waste entire cycles diagnosing flaky failures or introducing unnecessary "fixes"
- Test failures include enough context to locate the problem — the operation and inputs, not just an assertion diff

### Output interpretability

- Test runner output is structured — agents can programmatically distinguish pass, fail, skip, and error
- Failed test output includes test name, file location, and failure reason in a parseable format
- Application logs don't drown out test results — route them separately or suppress them

### Agent access beyond testing

- MCP server as interaction surface — exposing system capabilities as MCP tools lets agents query, inspect, and operate on the system directly, not just run tests

## Red Flags
- Setup instructions that include "ask X for the credentials" or "copy from the staging server"
- Tests that require machine state not codified anywhere (running database, populated cache, specific OS tooling)
- Tests that fail on first run after clone but pass on subsequent runs (hidden state dependency)
- Test output that requires human interpretation to determine pass/fail

## See Also
- **testing-strategy** — what good tests look like (behavior over implementation, E2E over unit, test isolation)
- **developer-experience** — one-command setup, fast feedback loops, parseable output

## Known Gaps
- Repos that depend on external paid services for testing (Stripe, Twilio, etc.)
- CI-specific agent-testability (agents running in CI vs locally)
- Test data management strategies for agent workflows
- Monorepo test orchestration for agents
