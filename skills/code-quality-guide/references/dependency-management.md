---
domain: dependency-management
last-reviewed: 2026-03-26
status: draft
sources: [meeting-2026-03-23-ai-best-practices, industry practices]
---

## Stance
Every dependency is a liability — attack surface, maintenance burden, and potential breaking change. The cost isn't just the install — it's every future upgrade, security patch, and compatibility issue. Prefer well-established standard libraries over niche packages. Agents will npm install a package to solve something a few lines of code would handle.

## What to Look For
- Every dependency has a justification — if 5-10 lines of code solve the problem, write the code instead of adding a package
- The dependency count is proportional to project complexity — a simple API server doesn't need 200 packages
- Lock files are committed and up to date — package-lock.json, uv.lock, or equivalent is always in version control
- Dependencies are current — no packages more than one major version behind; outdated deps are tracked and upgraded on a cadence
- No unused dependencies — every entry in package.json is actually imported somewhere; dead deps are removed immediately
- Packages are from reputable, actively maintained sources — check weekly downloads, last publish date, and open issue count before adding
- Imports are specific — import the function you need, not the entire library; prefer packages with tree-shaking support

## Red Flags
- Multiple packages solving the same problem
- Packages used for trivial tasks

## See Also
- **security** — each dependency is an attack surface and a supply chain risk

## Known Gaps
- Automated dependency upgrade workflows
- When to fork vs depend
