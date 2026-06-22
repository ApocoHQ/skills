---
domain: specification-first
last-reviewed: 2026-03-26
---

## Stance
Define requirements through conversation before writing code. The conversation itself is the spec process — no document or ticket is needed upfront. Use interview-based requirements gathering and a "grill me" approach to pressure-test requirements before committing. Without clear requirements there's no accountability — no way to know if the code is wrong or the requirements were never defined. Agents jump to implementation and lose sight of the goal. Humans without clear requirements build the wrong thing too, just slower. Once the conversation converges, the result can optionally be captured as an issue, PRD, or other artifact.

## What to Look For
- Requirements are defined before implementation starts — through conversation, not necessarily a document
- Success criteria are concrete and measurable — "users can do X" with acceptance conditions, not vague outcomes like "improve the experience"
- User stories drive scope decisions — if a feature can't be tied to a user story, question why it exists
- Requirements describe what and why, never how — implementation details constrain solutions and go stale immediately
- Requirements have been pressure-tested before committing — someone has asked "what about edge case X?" and there's an answer
- When the conversation converges, the result is captured somewhere durable — an issue, a PRD, or at minimum acceptance criteria on the task
- Spec-first applies to testing too — before writing a test, map the feature to testable boundaries: what do we control (mocks, DI), what do we observe (DB state, API responses, queue counts), are there gaps? Design the test plan, then write the code
- Structured issue creation from vague problems — explore the codebase for context, ask clarifying questions, synthesize into a structured issue with acceptance criteria, check for duplicates before creating

## Red Flags
- Requirements discovered during code review — the definition process failed
- Jumping straight to implementation without discussing what "done" looks like
- Writing tests without first understanding what the test can actually control and observe given the project's infrastructure

## See Also
- **documentation-strategy** — requirements define what to build; docs help navigate what was built
- **testing-strategy** — test strategy design is a form of specification

## Known Gaps
- Right level of conversation depth for small tasks vs. large features
- When it's okay to skip requirements conversation entirely (hotfixes, trivial changes)
