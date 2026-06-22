---
domain: documentation-strategy
last-reviewed: 2026-03-30
---

## Stance
Broad and shallow, not deep and prescriptive. Over-specification kills agent exploration — Anthropic research shows agents explore more thoroughly with a broad map than turn-by-turn directions. Prescriptive docs go stale fast, create false confidence, and agents follow them literally.

## What to Look For
- If a project maintains separate `docs/development/` and `docs/stable/` trees, only edit `docs/development/` — stable docs are published artifacts and must never be updated directly; they are promoted from development docs through a release process
- Docs are entry points with progressive disclosure — overview first, details available when needed; a README answers "what is this, how do I run it, where do I find things" in under a page
- CLAUDE.md and AGENTS.md stay under ~50 lines — pointers to deeper docs, not the docs themselves. Use a single source of truth across AI tools (e.g., CLAUDE.md symlinked to AGENTS.md) rather than maintaining duplicate instructions
- A `docs/` directory organized by concern with an `index.md` hub — architecture, data model, domain patterns, testing, tooling as separate files. An index page serves as the navigation entry point with links and one-line descriptions
- Docs describe architecture, boundaries, and decisions — never step-by-step implementation that goes stale the moment code changes. Include a conventions section for mandated choices (e.g., "always use date-fns for date operations") that would otherwise scatter across code comments
- Public interfaces have docstrings — functions, classes, and modules document their purpose, parameters, and return values inline; this is the documentation that actually stays in sync with the code

## Red Flags
- Documentation that duplicates what's already in the code
- Exhaustive API docs that are always stale
- No documentation at all
- Agent instructions maintained in multiple files that can drift out of sync
- Architecture docs that describe implementation details instead of patterns and decisions

## See Also
- **specification-first** — specs define what to build; docs help navigate what was built
- **agent-testability** — for how to structure agent-facing files (AGENTS.md, rules, skills) so agents actually follow them

## Known Gaps
- Right balance between too little and too much documentation.
- Documentation strategy for rapidly evolving codebases.
- When exhaustive docs are justified (public APIs, compliance).
