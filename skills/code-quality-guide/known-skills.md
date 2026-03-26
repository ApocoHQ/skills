# Known Skills Index

This file is an index of skills that serve as knowledge sources for the code-quality-guide skill. The code-quality-guide reads these skills to absorb their methodology — it does not invoke them. Each entry describes what extractable knowledge the skill contains, what it only touches superficially, and when it should or should not be loaded.

---

## design-first-engineering
**Path:** ../design-first-engineering/SKILL.md
**Core knowledge:** Extractable 4-step design framework (capabilities -> components -> interactions -> contracts). A concrete, structured methodology.
**Touches but doesn't own:** architecture principles (surface-level, within design context)
**Load when:** user needs to think through design structure, wants a systematic approach to decomposing a system
**Do NOT load for:** codebase assessment, testing discussion, code review

## grill-me
**Path:** ../grill-me/SKILL.md
**Core knowledge:** Relentless questioning disposition and decision tree resolution. This is a style/disposition to absorb, not a step-by-step framework.
**Touches but doesn't own:** design validation (through questioning, not assessment)
**Load when:** user is ideating, defending a design, or needs their assumptions challenged
**Do NOT load for:** codebase analysis, testing, implementation guidance

## write-a-prd
**Path:** ../write-a-prd/SKILL.md
**Core knowledge:** User-centric specification methodology, user stories, problem framing. An extractable framework for turning ideas into specs.
**Touches but doesn't own:** requirements gathering process
**Load when:** user is defining requirements, needs to frame a problem before solving it
**Do NOT load for:** code assessment, architecture review, testing

## align-repo
**Path:** ../align-repo/SKILL.md
**Core knowledge:** Claude Code project setup conventions — settings.json structure, CLAUDE.md conventions, commit format, skill recommendations.
**Touches but doesn't own:** architecture principles (surface-level — just checks CLAUDE.md has them)
**Load when:** user asks about repo setup, Claude configuration, project bootstrapping
**Do NOT load for:** deep architectural discussion, testing strategy, design patterns
