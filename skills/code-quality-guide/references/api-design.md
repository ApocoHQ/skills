---
domain: api-design
last-reviewed: 2026-03-26
---

## Stance
APIs are promises to consumers. A broken contract breaks everyone downstream. Agents will modify an endpoint's contract without considering who depends on it, and tightly couple response shapes to database schemas.

The choice between REST and RPC-style (tRPC, gRPC) depends on context. REST with OpenAPI suits public APIs with diverse consumers. Type-safe RPC (tRPC) suits full-stack TypeScript projects where client and server share a codebase — the contract is the TypeScript type, not a separate spec document.

## What to Look For
- Contracts defined before implementation — OpenAPI spec for REST, TypeScript types + Zod schemas for tRPC, not reverse-engineered from code
- New fields are additive; removed fields go through deprecation, never just deleted
- Auth on every endpoint by default — public endpoints are the explicit exception, not the other way around. The exception: single-user internal tools where auth adds complexity without security value
- Authentication (who are you) and authorization (what can you do) are separate concerns, not tangled in one middleware
- One response envelope, one error shape, one pagination style — across the entire API
- API models are their own layer — not database rows with fields removed. Leaking DAO types to the API is a conscious trade-off for internal tools, never for public APIs
- Mutation endpoints accept an idempotency key or are naturally idempotent — duplicate checks in application logic (e.g., "author already exists") are a pragmatic alternative for internal endpoints
- Validation at the API boundary with structured schemas — Zod inline with tRPC procedures or equivalent. Validation errors should identify which fields failed and why, in a consistent structure
- List endpoints include pagination — at minimum limit/offset as input parameters; public APIs should return page metadata (total count, next cursor) in the response

## Red Flags
- Breaking changes without versioning
- Inconsistent response formats across endpoints
- Endpoints that return different shapes depending on state
- No API documentation and no type-safe client — at least one must exist
- API responses that are just raw database rows with no transformation layer
- Mixing concerns in endpoints (one endpoint that creates, updates, and deletes)
- Mutation endpoints that aren't safe to retry
- List endpoints without pagination or with inconsistent pagination
- Validation errors in different formats across endpoints
- Auth applied inconsistently across similar endpoints
- Reading `process.env` directly in route handlers instead of through a validated config layer

## See Also
- **data-modeling** — "don't leak internal data models" means API shape decisions depend on schema design
- **error-handling** — consistent error response formats are an API contract concern

## Known Gaps
- GraphQL vs REST decision framework
- API gateway patterns
- Rate limiting and throttling strategy
