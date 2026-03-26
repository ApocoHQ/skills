---
domain: developer-experience
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, linkedin-manager patterns]
---

## Stance
A project that's hard to set up is a project that's hard to contribute to. Fast feedback loops — developers (and agents) should know within seconds if something is broken. Support running a subset of tests relevant to what changed. Agents can't distinguish real failures from environment issues — humans benefit from the same clarity.

## What to Look For
- One command runs everything — `npm test`, `make test`, or equivalent works out of the box with zero manual setup steps
- Setup is self-contained — all dependencies are containerized or scripted; no "install Postgres locally and configure it" instructions
- Test output is structured and parseable — agents and CI can distinguish pass/fail/skip programmatically; no wall of unstructured text
- Flaky tests are quarantined — they're marked, tracked, and excluded from the main suite so they don't block real work
- A new contributor (human or agent) is productive within minutes — clone, install, run; if it takes longer, the setup is broken
- `.env.example` exists and stays in sync with actual environment requirements — every env var the app needs is documented there

## Red Flags
- Undocumented dependencies on system-level tools
- Setup instructions that say "ask someone" for credentials

## See Also
- **documentation-strategy** — README structure and progressive disclosure
- **testing-strategy** — test ergonomics overlap with developer experience

## Known Gaps
- CI/CD pipeline design best practices
- Deployment workflow patterns
- Staging environment conventions
- How to handle environment-specific configuration cleanly
