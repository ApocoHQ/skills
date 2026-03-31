---
domain: security
last-reviewed: 2026-03-26
---

## Stance
Security fundamentals are table stakes, not exotic practices. Auth patterns follow least-privilege principle. Getting them wrong has outsized consequences compared to other quality issues — non-negotiable regardless of who writes the code.

## What to Look For
- Secrets live in environment variables or a secret manager — never in code, config files, or git history; `.env` is in `.gitignore` without exception
- Environment configuration is validated at startup with schema validation (Zod or equivalent) — missing or malformed config fails fast with a clear error listing all problems, not a cryptic runtime crash later. Use conditional validation to require secrets only when mock mode is disabled (e.g., require API key only when `SERVICE_MOCK=false`)
- `.env.example` defaults to mock/safe mode for all external services — a developer who copies `.env.example` to `.env` and runs the app should never accidentally call production APIs or send real notifications
- Input is validated at every system boundary — user input, API payloads, webhook data, file uploads; trust nothing from outside the process
- Auth is on every endpoint by default — public access is the exception that requires explicit opt-out, not something you add later
- Database queries use parameterized statements — string concatenation for SQL is never acceptable, regardless of how "internal" the endpoint is. ORM query builders (Drizzle, Prisma) handle this automatically
- Dependencies are scanned for known vulnerabilities in CI — no merge without a clean security scan
- CORS policies are restrictive and explicit — no wildcard origins in production
- Passwords are hashed with a modern algorithm (bcrypt, argon2) — never plaintext, never reversible encryption
- Agent permissions are conservative — auto-allow only read-only operations; destructive commands require explicit approval

## Red Flags
- Hardcoded secrets or API keys
- `.env` files committed to git
- SQL built with string concatenation
- Missing auth on endpoints that need it
- Disabled CSRF protection
- `eval()` with user input
- `.env.example` containing real API keys or defaulting to production service endpoints
- Reading `process.env` directly in application code instead of through a validated config layer

## See Also
- **api-design** — auth on every endpoint by default, auth/authz separation
- **error-handling** — error messages and stack traces can leak sensitive information
- **dependency-management** — every dependency is an attack surface

## Known Gaps
- Team-specific security review process
- Threat modeling practices
- Specific compliance requirements (SOC2, GDPR)
- Secrets rotation strategy
