---
domain: code-readability
last-reviewed: 2026-03-26
status: draft
sources: [industry practices]
---

## Stance
Code is read 10x more than it's written — optimize for the reader. Over multiple agent sessions naming and structural clarity degrade because each session lacks the context of the original naming decisions. If an agent can't understand a function from its name and signature, it will misuse it.

## What to Look For
- Names convey intent — function names describe what they do, variable names describe what they hold; no abbreviations that require domain knowledge to decode
- Naming is consistent project-wide — one convention for each concept (e.g., always `userId` never sometimes `user_id`, `uid`, or `id`)
- Comments explain why, never what — if code needs a comment to explain what it does, the code should be rewritten to be clearer
- Functions are short enough to understand at a glance — if you can't hold the function's logic in your head, it needs to be split; each function operates at one abstraction level
- Guard clauses and early returns handle edge cases first — the happy path flows straight down with minimal nesting
- Magic numbers and strings are named constants — `MAX_RETRIES = 3` not `3`; `STATUS_ACTIVE = "active"` not `"active"` scattered through code
- No dead code — commented-out blocks, unused imports, and unreachable branches are removed, not left "just in case"

## Red Flags
- Single-letter variables outside trivial loops
- Deeply nested conditionals (3+ levels)
- Boolean parameters without context — `doThing(true, false, true)`
- More than ~3 positional parameters — use keyword arguments, named parameters, or a structured input
- Negative or double-negative conditionals — `if (!isNotValid)`

## See Also
- **architecture** — readability at the structural level; clear module boundaries make code navigable

## Known Gaps
- Language-specific idiom guidance
- When to optimize for brevity vs. explicitness
- Naming conventions for domain-specific concepts
- Enum/constant patterns vs scattered string literals
