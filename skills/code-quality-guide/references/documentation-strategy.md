---
domain: documentation-strategy
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, Anthropic research on agent exploration]
---

## Stance
Broad and shallow, not deep and prescriptive. Over-specification kills agent exploration — Anthropic research shows agents explore more thoroughly with a broad map than turn-by-turn directions. Prescriptive docs go stale fast, create false confidence, and agents follow them literally.

## What to Look For
- Docs are entry points with progressive disclosure — overview first, details available when needed; a README answers "what is this, how do I run it, where do I find things" in under a page
- CLAUDE.md and AGENTS.md stay under ~50 lines — pointers to deeper docs, not the docs themselves
- Docs describe architecture, boundaries, and decisions — never step-by-step implementation that goes stale the moment code changes
- Public interfaces have docstrings — functions, classes, and modules document their purpose, parameters, and return values inline; this is the documentation that actually stays in sync with the code

## Red Flags
- Documentation that duplicates what's already in the code
- Exhaustive API docs that are always stale
- No documentation at all

## See Also
- **specification-first** — specs define what to build; docs help navigate what was built

## Known Gaps
- Right balance between too little and too much documentation.
- Documentation strategy for rapidly evolving codebases.
- When exhaustive docs are justified (public APIs, compliance).
