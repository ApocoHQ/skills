# Skills Repo

This repo contains practical AI agent skills. Each skill lives in its own folder under `skills/`.

The repo is distributed in two formats:
- **Claude Code plugin** (`practical-skills`) via the Apoco marketplace — see [Plugin Manifest](#plugin-manifest)
- **[Agent Skills](https://github.com/vercel-labs/agent-skills) format** — compatible with Claude Code, OpenCode, and other tools that support the format

## Skill Structure

Each skill folder must contain:

- **`SKILL.md`** — The skill definition. Has YAML frontmatter with `name` and `description` (used for trigger matching), followed by the full instructions Claude follows when the skill is invoked.

Optional folders:

- **`scripts/`** — Executable scripts or templates the skill uses to produce output.
- **`references/`** — Detailed reference docs loaded into context when needed (API docs, workflow guides, etc.). Keep SKILL.md concise and put lengthy reference material here.
- **`assets/`** — Static files used in skill output (templates, images, fonts, boilerplate). These are NOT loaded into context — they are used within the output Claude produces.

## What a Skill Delivers

A skill is a set of instructions that teach Claude how to perform a specific task. When triggered, Claude receives the SKILL.md as context and follows its workflow. A good skill:

- Has clear trigger phrases in the frontmatter `description` so it activates reliably
- Defines a step-by-step workflow with decision points
- Uses templates/scripts in `scripts/` to generate consistent output
- Keeps reference material in `references/` to avoid bloating SKILL.md
- Produces a concrete deliverable (generated code, config files, reports, etc.)

## Plugin Manifest

This repo is distributed as a Claude Code plugin (`practical-skills`) via the Apoco marketplace. The manifest lives at `.claude-plugin/plugin.json`.

- All skill folders under `skills/` are auto-discovered by the plugin — no need to register them individually.
- Internal or company-specific skills should not be in this repo.
- After adding, removing, or updating skills, bump the `version` in `.claude-plugin/plugin.json` using semver: **minor** for new/removed skills, **patch** for skill updates.
