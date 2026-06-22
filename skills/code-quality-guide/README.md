# code-quality-guide

A conversational code quality advisor that draws on bundled skills and reference documents to provide engineering guidance.

## Contributing

### Bundled Skills

The `bundled-skills/` folder contains copies of other skills from this repo, used as knowledge sources (not invoked as workflows). These copies are kept in sync automatically by a GitHub Actions workflow (`.github/workflows/sync-bundled-skills.yml`).

**When adding a new bundled skill:**
1. Add the source skill path to the workflow's `paths` trigger
2. Add a `cp` line in the workflow's copy step
3. Add an entry in `known-skills.md` describing what knowledge the skill provides and when to load it

**When removing a bundled skill:**
1. Remove the source skill path from the workflow's `paths` trigger
2. Remove the `cp` line from the workflow's copy step
3. Remove the entry from `known-skills.md`
4. Delete the subfolder from `bundled-skills/`
