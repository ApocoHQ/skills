---
domain: developer-experience
last-reviewed: 2026-03-26
---

## Stance
A project that's hard to set up is a project that's hard to contribute to. Fast feedback loops — developers (and agents) should know within seconds if something is broken. Support running a subset of tests relevant to what changed. Agents can't distinguish real failures from environment issues — humans benefit from the same clarity.

## What to Look For
- One command runs everything — `pnpm dev`, `npm test`, `mise run test`, or equivalent works out of the box with absolutely minimal or zero manual setup steps. Integrate infrastructure startup (docker-compose) into the dev command so developers don't need to remember separate steps
- Setup is self-contained — all dependencies are containerized or scripted; no "install Postgres locally and configure it" instructions
- Test output is structured and parseable — agents and CI can distinguish pass/fail/skip programmatically; no wall of unstructured text
- Flaky tests are quarantined — they're marked, tracked, and excluded from the main suite so they don't block real work
- A new contributor (human or agent) is productive within minutes — clone, install, run; if it takes longer, the setup is broken
- `.env.example` exists and stays in sync with actual environment requirements — every env var the app needs is documented there. External services default to mock mode so `cp .env.example .env && pnpm dev` works without any credentials
- Separate test database configuration — test DB variables prevent test runs from corrupting development data
- CI pipeline mirrors local development — service containers with health checks (e.g., `pg_isready`, `redis-cli ping`), frozen lockfile enforcement, same validation sequence (lint → typecheck → test)
- MCP server as a development entry point — exposing the system's capabilities as MCP tools lets LLM agents interact with the application directly, not just run tests

## Red Flags
- Undocumented dependencies on system-level tools
- Development setup instructions that say "ask someone" for credentials
- CI that works differently from local development (different database, different test runner, different env vars)
- `.env.example` that requires editing before the app will start

## See Also
- **documentation-strategy** — README structure and progressive disclosure
- **testing-strategy** — test ergonomics overlap with developer experience
- **agent-testability** — agent-specific DX concerns

## Known Gaps
- Deployment workflow patterns
- Staging environment conventions
- How to handle environment-specific configuration cleanly
