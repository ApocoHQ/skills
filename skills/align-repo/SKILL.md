---
name: align-repo
description: |
  Check and align a repo's .claude/settings.json and CLAUDE.md with team conventions. Use when the user wants to standardize a repo, align conventions, check settings, or bootstrap Claude Code config in a new project.
---

# Align Repo Conventions

Audit the current repo's `.claude/settings.json` and `CLAUDE.md` against team standards, then walk the user through each gap one at a time, applying fixes only after confirmation.

## Workflow

### 0. Self-update

Before doing anything else, ensure this skill is up to date:

```bash
npx skills add https://github.com/apocohq/skills --skill align-repo -a claude-code -y
```

If the skill was updated, inform the user and continue with the new version's instructions.

### 1. Gather current state

Read the following files (they may not exist yet — that's fine):

- `.claude/settings.json`
- `CLAUDE.md` (repo root)

Also check for `.claude/settings.local.json` (note its existence but don't modify it).

### 2. Check settings.json

Compare against each expected setting below **one by one**. For each item:

1. Show the **current value** (or "missing" if absent).
2. Show the **expected value**.
3. Ask the user: _"Want me to align this?"_ — wait for their answer before moving on.

If `.claude/settings.json` doesn't exist, ask the user if you should create it before proceeding.

#### Expected settings

**Attribution — commit trailer:**

```json
{
  "attribution": {
    "commit": "Assisted-By: Claude (Anthropic AI) <noreply@anthropic.com>",
    "pr": ""
  }
}
```

**Allowed tools — safe git & GitHub read operations:**

```json
{
  "allowedTools": [
    "Bash(git status*)",
    "Bash(git diff*)",
    "Bash(git log*)",
    "Bash(git fetch*)",
    "Bash(git branch*)",
    "Bash(git checkout -b *)",
    "Bash(git stash*)",
    "Bash(git add *)",
    "Bash(git commit *)",
    "Bash(gh issue view*)",
    "Bash(gh issue list*)",
    "Bash(gh pr view*)",
    "Bash(gh pr list*)",
    "Bash(ls:*)"
  ]
}
```

When comparing `allowedTools`, treat them as a set — order doesn't matter. Report:
- **Missing** entries the repo should have.
- **Extra** entries the repo has but aren't in the standard set (flag but don't remove — these may be intentional project-specific additions).

### 3. Check CLAUDE.md sections

If `CLAUDE.md` doesn't exist, ask the user if you should create it with a minimal scaffold before proceeding.

Check each section below in order. For each item within a section:
1. Show whether it's **present**, **partially covered**, or **missing**.
2. If missing or incomplete, show the suggested text.
3. Ask the user: _"Want me to add/update this?"_ — wait for confirmation.

If an entire section is missing, propose adding it as a whole block and ask for confirmation before moving to the next section.

#### 3a. Architecture Principles

Look for a **Separation of Concerns & DRY Principle** section (or similar heading). If missing or incomplete, propose adding:

```markdown
## Separation of Concerns & DRY Principle

This system is a modular component system following the DRY (Don't Repeat Yourself) principle. Each piece has a single responsibility. You should be able to swap out any component without rewriting others.
```

#### 3b. Commit Conventions

Look for a **Commit Conventions** section (or similar heading). Expected conventions:

1. **Conventional Commits format**: `type(scope): short summary` — types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `revert`, `style`, `perf`, `ci`, `build`.
2. **Scope**: Optional but encouraged (e.g., `feat(ui):`, `fix(hook):`, `docs(design):`).
3. **Body**: Optional concise bullet points for non-trivial changes.
4. **Trailer**: Configured via `.claude/settings.json` `attribution` — do not add manually.
5. **Branch naming**: `type/short-description` (e.g., `feat/session-history`, `fix/stale-timer`). Same type prefixes as commits.

#### 3c. Meeting Format (conditional)

**Skip this if the repo has no `meetings/` directory or doesn't deal with meeting notes.**

Look for a **Meeting Format** section in `CLAUDE.md`. If missing or incomplete, propose adding:

```markdown
## Meeting Format

---
date: "YYYY-MM-DD"
attendees:
  - First Last
  - First Last
---

# Meeting Title

One concise paragraph summarizing the meeting.

## Transcript / Notes / Meeting Minutes
```

### 4. Recommend skills

Review the repo's purpose and tech stack (check README, package.json, or similar) and suggest installing relevant skills from the list below. Only suggest skills that genuinely fit — skip any that don't apply.

Available skills to recommend:

| Skill | What it does | When to suggest |
|---|---|---|
| `process-transcript` | Converts VTT meeting transcripts into structured markdown notes | Repos that track meetings or have a `meetings/` directory |
| `ralph-it` | Picks the next user story from a PRD GitHub issue, implements it, and opens a PR | Repos that use GitHub issues for PRDs or have structured user stories |
| `write-a-prd` | Interviews the user and writes a PRD, then submits it as a GitHub issue | Any repo that plans features via PRDs or GitHub issues |

For each skill you recommend:
1. Explain **why** it fits this repo (one sentence).
2. Show the install command: `npx skills add https://github.com/apocohq/skills --skill <skill-name>`
3. Ask the user: _"Want me to install this?"_ — if yes, run the command.

Skip skills that don't match the repo. If none fit, say so and move on.

### 5. Check for skill updates

Check if any installed skills have updates available:

```bash
npx skills check
```

Show the output to the user. If updates are available, ask: _"Want me to update all skills?"_ — if yes, run:

```bash
npx skills update
```

If no skills are installed yet (no `skills-lock.json` or empty), skip this step.

### 6. Summary

After walking through all checks, print a short summary:

```
## Alignment Summary
- settings.json: X of Y settings aligned (Z changed this session)
- CLAUDE.md architecture principles: present / missing (Z changed this session)
- CLAUDE.md commit conventions: X of Y present (Z added/updated this session)
- Skills installed: [list or "none"]
- Skills updated: [list or "all up to date"]
- Items skipped by user: [list if any]
```

## Important Notes

- **Never auto-apply changes.** Every modification requires explicit user confirmation.
- **Preserve existing content.** When editing CLAUDE.md, don't remove or reorder sections the user already has — only add or update the conventions section.
- **Merge, don't overwrite** settings.json — add missing keys without clobbering existing ones (e.g., project-specific `allowedTools` entries should be kept).
- If the user declines an item, note it in the summary and move on without further persuasion.
