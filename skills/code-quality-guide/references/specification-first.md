---
domain: specification-first
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, write-a-prd skill principles]
---

## Stance
Business spec before technical plan. Use interview-based requirements gathering. Without a spec there's no accountability — no way to know if the code is wrong or the requirements were never defined. Agents jump to implementation and lose sight of the goal. Humans without specs build the wrong thing too, just slower. The team uses a "grill me" approach to pressure-test requirements before committing.

## What to Look For
- A spec or PRD exists before any code is written — no exceptions for "small" features; scope creep starts with "it's just a quick change"
- Success criteria are concrete and measurable — "users can do X" with acceptance conditions, not vague outcomes like "improve the experience"
- User stories drive scope decisions — if a feature can't be tied to a user story, question why it exists
- Specs describe what and why, never how — implementation details in a spec constrain solutions and go stale immediately
- Requirements have been pressure-tested before committing — someone has asked "what about edge case X?" and there's an answer

## Red Flags
- Requirements discovered during code review — the spec process failed

## See Also
- **documentation-strategy** — specs define what to build; docs help navigate what was built

## Known Gaps
- Right level of spec detail for small tasks vs. large features.
- When it's okay to skip formal spec (hotfixes, trivial changes).
