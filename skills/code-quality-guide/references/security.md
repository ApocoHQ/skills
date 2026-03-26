---
domain: security
last-reviewed: 2026-03-26
status: draft
sources: [OWASP, industry standard practices]
---

## Stance
Security fundamentals are table stakes, not exotic practices. Auth patterns follow least-privilege principle. Be aware of OWASP top 10. Getting them wrong has outsized consequences compared to other quality issues — non-negotiable regardless of who writes the code.

## What to Look For
- Secrets live in environment variables or a secret manager — never in code, config files, or git history; `.env` is in `.gitignore` without exception
- Input is validated at every system boundary — user input, API payloads, webhook data, file uploads; trust nothing from outside the process
- Auth is on every endpoint by default — public access is the exception that requires explicit opt-out, not something you add later
- Database queries use parameterized statements — string concatenation for SQL is never acceptable, regardless of how "internal" the endpoint is
- Dependencies are scanned for known vulnerabilities in CI — no merge without a clean security scan
- CORS policies are restrictive and explicit — no wildcard origins in production
- Passwords are hashed with a modern algorithm (bcrypt, argon2) — never plaintext, never reversible encryption

## Red Flags
- Hardcoded secrets or API keys
- `.env` files committed to git
- SQL built with string concatenation
- Missing auth on endpoints that need it
- Disabled CSRF protection
- `eval()` with user input

## See Also
- **api-design** — auth on every endpoint by default, auth/authz separation
- **error-handling** — error messages and stack traces can leak sensitive information
- **dependency-management** — every dependency is an attack surface

## Known Gaps
- Team-specific security review process
- Threat modeling practices
- Specific compliance requirements (SOC2, GDPR)
- Secrets rotation strategy
