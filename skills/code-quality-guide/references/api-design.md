---
domain: api-design
last-reviewed: 2026-03-26
status: draft
sources: [industry practices, linkedin-manager patterns]
---

## Stance
APIs are promises to consumers. RESTful conventions unless there's a strong reason otherwise. Agents will modify an endpoint's contract without considering who depends on it, and tightly couple response shapes to database schemas. A broken contract breaks everyone downstream.

## What to Look For
- Contracts defined before implementation — OpenAPI spec or equivalent, not reverse-engineered from code
- New fields are additive; removed fields go through deprecation, never just deleted
- Auth on every endpoint by default — public endpoints are the explicit exception, not the other way around
- Authentication (who are you) and authorization (what can you do) are separate concerns, not tangled in one middleware
- One response envelope, one error shape, one pagination style — across the entire API
- API models are their own layer — not database rows with fields removed
- Mutation endpoints accept an idempotency key or are naturally idempotent
- Validation errors identify which fields failed and why, in a consistent structure

## Red Flags
- Breaking changes without versioning
- Inconsistent response formats across endpoints
- Endpoints that return different shapes depending on state
- No API documentation
- API responses that are just raw database rows
- Mixing concerns in endpoints (one endpoint that creates, updates, and deletes)
- Mutation endpoints that aren't safe to retry
- List endpoints without pagination or with inconsistent pagination
- Validation errors in different formats across endpoints
- Auth applied inconsistently across similar endpoints

## See Also
- **data-modeling** — "don't leak internal data models" means API shape decisions depend on schema design
- **error-handling** — consistent error response formats are an API contract concern

## Known Gaps
- GraphQL vs REST decision framework
- API gateway patterns
- Rate limiting and throttling strategy
- HTTP status code conventions
