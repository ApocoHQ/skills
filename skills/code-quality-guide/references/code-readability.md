---
domain: code-readability
last-reviewed: 2026-03-26
---

## Stance
Code is read 10x more than it's written — optimize for the reader. Over multiple agent sessions naming and structural clarity degrade because each session lacks the context of the original naming decisions. If an agent can't understand a function from its name and signature, it will misuse it.

## What to Look For
- Names convey intent — function names describe what they do, variable names describe what they hold; no abbreviations that require domain knowledge to decode
- Naming is consistent project-wide — one convention for each concept (e.g., always `userId` never sometimes `user_id`, `uid`, or `id`). Consistent file naming conventions too: `*-service.ts`, `*-aggregate.ts`, `*.worker.ts`, `*.test.ts`
- Factory functions follow `create*()` convention — `createDatabase()`, `createTestHarness()`, `createMockTelegramBot()`. Predictable naming makes the codebase searchable
- Comments explain why, never what — if code needs a comment to explain what it does, the code should be rewritten to be clearer
- Functions are short enough to understand at a glance — if you can't hold the function's logic in your head, it needs to be split; each function operates at one abstraction level
- Guard clauses and early returns handle edge cases first — the happy path flows straight down with minimal nesting
- Magic numbers and strings are named constants — `MAX_RETRIES = 3` not `3`; `VIRALITY_ENGAGEMENT_WEIGHT = 0.6` not `0.6` scattered through scoring logic
- No dead code — commented-out blocks, unused imports, and unreachable branches are removed, not left "just in case"
- Discriminated union types over enums — `type Priority = "ignore" | "normal" | "strategic" | "vip"` is more composable, works better with pattern matching, and doesn't create a runtime object. Use exhaustive pattern matching (e.g., ts-pattern `.exhaustive()`) to get compile-time safety when handling all variants
- Conventional commit prefixes — `feat:`, `fix:`, `refactor:`, `test:`, `docs:`, `chore:` make git history scannable and support automated changelog generation

## Red Flags
- Single-letter variables outside trivial loops
- Deeply nested conditionals (3+ levels)
- Boolean parameters without context — `doThing(true, false, true)`
- More than ~3 positional parameters — use keyword arguments, named parameters, or a structured input
- Negative or double-negative conditionals — `if (!isNotValid)`
- Switch/match on a union type without exhaustiveness — a new variant added later will silently fall through

## See Also
- **architecture** — readability at the structural level; clear module boundaries make code navigable

## Known Gaps
- Language-specific idiom guidance
- When to optimize for brevity vs. explicitness
- Naming conventions for domain-specific concepts
