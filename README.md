# Practical Skills

Practical skills that teach AI agents to get things done for you.

## Installation

### Claude Code Plugin (recommended)

Install via the Apoco marketplace:

```sh
claude plugin install practical-skills@apoco
```

Or search for "practical-skills" in the `/plugin` UI.

Skills are invoked as `/practical-skills:<skill-name>` (e.g. `/practical-skills:gmail-multi-inbox`).

### Agent Skills format

Also works with [Agent Skills](https://github.com/vercel-labs/agent-skills)-compatible tools:

```sh
npx skills add apocohq/skills
```

Works in [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [OpenCode](https://opencode.ai), and other AI tools that support the format.

## Skills

### 🔧 align-repo

New repo? Inherited a project? This skill audits your `.claude/settings.json` and `CLAUDE.md` against team conventions and walks you through each gap one by one — attribution config, allowed tools, architecture principles, commit conventions, and recommended skills. It only applies changes you approve, so nothing gets overwritten by surprise.

**Use when:** bootstrapping Claude Code config in a new project, standardizing conventions across repos, or checking if a repo is aligned with team standards.

### 🧹 cleanup-commits

Messy branch history? This skill rebases and reorganizes your commits into clean, meaningful units for easy PR review. Automatically restructures branch history to make code review smoother and clearer.

**Use when:** preparing a branch for PR review, cleaning up WIP commits, reorganizing commit history.

### 🏗️ design-first-engineering

Guide software design iteration before writing any code. Walks you through 4 sequential steps — capabilities, interactions, contracts, and components — to produce a clear, iterated design that prevents costly rework later.

**Use when:** designing a system, planning architecture, thinking through a feature's structure before implementing.

### 🗂️ dir-tree-index

Working in a large repo and losing track of where things live? This skill generates or updates distributed `STRUCTURE.md` files across directories, each with concise one-line summaries of folders and files. It helps LLMs orient quickly in unfamiliar codebases and is especially useful for knowledge repositories where discoverability and navigation matter.

**Use when:** mapping project structure, improving LLM repo orientation, indexing documentation-heavy repos, and keeping folder-level overviews up to date.

### 📬 gmail-multi-inbox

Tired of a messy inbox? This skill scans your Gmail, figures out who's emailing you, and organizes everything into clean Multiple Inbox sections. It generates a Google Apps Script that sets up labels and filters automatically. It can also help you find noisy senders worth unsubscribing from. It keeps a local config, so you can run it again to add new senders or tweak categories over time.

**Use when:** organizing Gmail, setting up multiple inboxes, managing labels and filters, cleaning up subscriptions.

### 🔥 grill-me

Have a plan or design you're not sure about? This skill interviews you relentlessly until reaching shared understanding. It stress-tests your decisions by walking down each branch of the design tree and resolving dependencies one by one.

**Use when:** stress-testing a plan, validating design decisions, preparing for a design review.

### 📝 meeting-minutes

Got a meeting recording or transcript? This skill turns it into a clean, structured set of meeting minutes — decisions, action items, and key discussion points preserved verbatim. Works with `.vtt` files from Zoom, Teams, or any WebVTT-compatible recorder. Handles multilingual transcripts by translating to English automatically.

**Requires:** [uv](https://docs.astral.sh/uv/) installed on your machine (used to run the VTT stripping script).

**Use when:** processing a meeting transcript, extracting action items, creating meeting notes, summarizing a recorded call.

### 🎙️ process-transcript

Have a pile of meeting recordings sitting in a folder? This skill watches `meetings/incoming/` (and `~/Downloads/`) for `.vtt` transcript files, parses them into clean Markdown with frontmatter, adds a title and summary, and files them into `meetings/` with a date-slug filename. No manual reformatting needed.

**Requires:** [uv](https://docs.astral.sh/uv/) installed on your machine (used to run the VTT parsing script).

**Use when:** processing meeting transcripts, converting VTT files to markdown, organizing meeting notes.

### 🚀 ralph-it

Pick and implement the next user story from a PRD GitHub issue. Analyzes merged PRs for prior work and findings, proposes a plan, implements it, and creates a PR linking back to the original PRD.

**Use when:** working through PRD user stories, implementing the next feature from a spec.

### 👀 review-work

Dispatch a code-reviewer subagent to catch issues before they cascade. Provides focused context for evaluation without cluttering your session history, keeping the reviewer focused on the work product.

**Use when:** reviewing code before merging, getting a second opinion on changes, catching issues early.

### ✅ things-morning-organizer

Never sure what to focus on in the morning? Born out of spending 15–25 minutes every Monday manually sorting through 40+ todos ([full story](https://www.havlena.com/p/i-automated-monday-morning-triage)), this skill reviews your [Things 3](https://culturedcode.com/things/) todos, moves them into the right areas, tags what needs attention, and gives you a prioritized 30-second briefing so you know exactly where to start.

Features:
- **Auto-generated config** - On first run, scans your existing todos, areas, and tags to build a config with descriptions and examples. No manual setup needed.
- **Smart categorization** - Moves uncategorized items into the right area and applies tags conservatively using example-based matching.
- **Daily routines** - Automatically creates recurring weekday todos (e.g. "Check email") if they're missing from Today.
- **Drucker-style briefing** - Prioritizes your day into Must do / Should do / Could do using Peter Drucker's "Effective Executive" lens, with a motivational quote.
- **Todo creation** - Add todos by describing them naturally; the skill rephrases, assigns an area, and schedules them.
- **Silent mode** - Run with `[silent]` for automated/headless execution via `-p` mode. Skips all prompts, requires existing config, and outputs only the final briefing.
- **Learning mode** - Run with `[learning]` to compare your todos against the config and refine area/tag descriptions and examples over time.
- **Idempotent** - Safe to run multiple times a day. Skips items that already have areas and tags, and won't duplicate daily routine todos.

**Use when:** starting your day, triaging todos, organizing tasks by area and priority, adding new todos.

### 📋 write-a-prd

Create a PRD through user interview, codebase exploration, and module design, then submit it as a GitHub issue. Systematically defines requirements, validates against the codebase, and designs the implementation approach.

**Use when:** starting a new feature, defining requirements, creating a spec before implementation.

## License

[MIT](LICENSE)
