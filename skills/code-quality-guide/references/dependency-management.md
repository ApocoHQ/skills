---
domain: dependency-management
last-reviewed: 2026-03-26
---

## Stance
Every dependency is a liability — attack surface, maintenance burden, and potential breaking change. The cost isn't just the install — it's every future upgrade, security patch, and compatibility issue. Prefer well-established standard libraries over niche packages. Agents will npm install a package to solve something a few lines of code would handle.

## What to Look For
- Every dependency has a justification — if 5-10 lines of code solve the problem, write the code instead of adding a package
- The dependency count is proportional to project complexity — a simple API server doesn't need 200 packages. The gold standard: a domain/core package with zero external dependencies
- Lock files are committed and up to date — package-lock.json, pnpm-lock.yaml, uv.lock, or equivalent is always in version control. CI enforces frozen lockfile (`--frozen-lockfile`) to prevent drift between what's committed and what's installed
- Dependencies are current — no packages more than one major version behind; outdated deps are tracked and upgraded on a cadence
- No unused dependencies — every entry in package.json is actually imported somewhere; dead deps are removed immediately
- Packages are from reputable, actively maintained sources — check weekly downloads, last publish date, and open issue count before adding
- Imports are specific — import the function you need, not the entire library; prefer packages with tree-shaking support
- Standard library choices are documented as conventions — when a library is chosen for a domain (e.g., `date-fns` for all date operations), document it in architecture docs so agents and developers don't introduce alternatives. "Always use X for Y" prevents drift
- In monorepos, each package owns its own dependencies — use workspace protocol (`workspace:*`) for internal packages. Keep each package's dependency surface minimal by splitting concerns (separate packages for logger, config, domain)

## Red Flags
- Multiple packages solving the same problem
- Packages used for trivial tasks
- Monorepo packages with access to dependencies they don't declare (phantom dependencies)

## See Also
- **security** — each dependency is an attack surface and a supply chain risk

## Known Gaps
- Automated dependency upgrade workflows
- When to fork vs depend
