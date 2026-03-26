---
domain: error-handling
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, industry practices]
---

## Stance
Fail explicitly and early. Agents silently catch and ignore errors by default — silent failures are the hardest bugs to track down and cascade into something catastrophic.

## What to Look For
- Errors propagate upward with context — each layer adds what it knows (what was being attempted, with which input) rather than swallowing or re-wrapping with less information
- Errors are logged as structured data — not bare strings; include operation, input identifiers, error type, and stack trace as separate fields
- Failure modes are explicit — each component's possible failure states are obvious from its interface, not discovered at runtime
- Retry logic uses exponential backoff with a maximum attempt count and a circuit breaker — never an unbounded retry loop
- Expected errors (validation, auth, timeouts) and unexpected errors (bugs, invariant violations) follow different paths — expected errors produce user-facing messages, unexpected errors alert the team
- Catch blocks are narrow and specific — catch the specific error type at the specific failure point, not a try/catch around an entire function

## Red Flags
- Empty catch blocks
- Catch-all handlers that swallow context
- Error messages that say "something went wrong" with no diagnostic detail
- `try/catch` around entire functions rather than specific failure points

## See Also
- **security** — error messages and stack traces can leak sensitive information in production
- **api-design** — consistent error response formats are part of the API contract

## Known Gaps
- Team-specific error reporting and monitoring setup
- Error rate alerting thresholds
- Structured error taxonomy
