---
name: meeting-minutes
description: Extract substantive content from a meeting transcript, preserving important discussions verbatim and filtering out chitchat and inappropriate language
---

Extract substantive content from a meeting transcript, filtering out noise and producing an LLM-context-efficient representation.

## Goal

Produce the most **LLM-context-efficient** representation of the meeting. The output will be used as context in future LLM conversations, so every token must earn its place. Aggressively reduce token count while preserving all substantive content (decisions, reasoning, disagreements, action items). Prefer concise direct quotes over full verbatim exchanges when the meaning is preserved. Remove conversational scaffolding ("So what I'm trying to say is...", "That's a great point, and to add to that...") and keep only the payload.

## Arguments

- `<path>` (optional) — A `.vtt` file or a folder containing `.vtt` files. If omitted, defaults to `~/Downloads/`.
- `--latest` (optional) — Automatically pick the most recent `.vtt` file instead of presenting a choice.

## Context management

Meeting transcripts are large (a 1-hour meeting is ~70K tokens). To avoid accumulating multiple copies of the transcript in the conversation context, this skill uses **temp files and subagents** as a pipeline:

1. The **main agent** handles Steps 0, 1, and 5 (resolve source, strip VTT via Python script, clean up temp files). It never reads the transcript content.
2. A **subagent** handles Step 2 (clean + filter in original language). Reads `meetings/tmp/meeting-stripped.txt`, writes `meetings/tmp/meeting-cleaned.txt`. Context discarded.
3. A **subagent** handles Step 3 (translate to English). Reads `meetings/tmp/meeting-cleaned.txt`, writes `meetings/tmp/meeting-translated.txt`. Context discarded. Skipped if already English.
4. A **subagent** handles Step 4 (extract + structure + save). Reads `meetings/tmp/meeting-translated.txt`, writes final output directly to `meetings/`. Context discarded.

Each subagent starts with a fresh context containing only its task instructions and the current-stage file. No prior transcript versions pollute its context.

## Execution protocol

**You MUST follow these steps strictly in order.** After completing each step, validate that all requirements of that step are met. Only after validation, check off the step and proceed to the next one. Do not skip ahead.

Use the TodoWrite tool to create this checklist at the start of execution:

- [ ] Step 0: Resolve the transcript source
- [ ] Step 1: Strip VTT metadata (Python script)
- [ ] Step 2: Clean and filter (subagent)
- [ ] Step 3: Translate to English (subagent)
- [ ] Step 4: Extract, structure, and save (subagent)
- [ ] Step 5: Clean up

After completing each step, mark it as done in the todo list before moving on.

## Steps

### Step 0: Resolve the transcript source

Determine the target folder and file. Follow the first matching rule:

1. **`<path>` is a `.vtt` file** — Use that file directly. Proceed to Step 1.
2. **`<path>` is a folder + `--latest`** — Run `ls -t <folder>/*.vtt | head -1` via Bash to pick the most recent `.vtt` file. If none exist, stop and tell the user.
3. **`<path>` is a folder (no `--latest`)** — Run `ls -t <folder>/*.vtt | head -3` via Bash. Present the results as a numbered list (newest first) and ask the user to choose. If none exist, stop and tell the user.
4. **No `<path>` + `--latest`** — Same as rule 2, but use `~/Downloads/` as the folder.
5. **No `<path>`, no `--latest`** — Same as rule 3, but use `~/Downloads/` as the folder.
6. **User provided pasted text** — Use that directly.
7. **User provided a URL** — Download the file using `curl -sL <url> -o meetings/tmp/transcript.vtt` via Bash. If the download fails, stop and tell the user.

After resolving, confirm the file name to the user before proceeding.

### Step 1: Strip VTT metadata (Python script)

If the resolved source is a `.vtt` file, run the stripping script via Bash. Use **absolute paths** for both the script and the output to avoid working-directory issues:

```
PROJECT_ROOT="$(pwd)" && SKILL_SCRIPT="$(ls "${PROJECT_ROOT}/.claude/skills/meeting-minutes/scripts/main.py" "${HOME}/.claude/skills/meeting-minutes/scripts/main.py" 2>/dev/null | head -1)" && uv run "$SKILL_SCRIPT" "<input>" "${PROJECT_ROOT}/meetings/tmp/meeting-stripped.txt"
```

Replace `<input>` with the resolved file path. Quote it and use `${HOME}` notation to handle filenames with spaces (e.g. `"${HOME}/Downloads/my meeting.vtt"`).

If the source is pasted text or a non-VTT file, write it directly to `meetings/tmp/meeting-stripped.txt` (under the project root) using the Write tool.

The script removes VTT headers, sequence numbers, timestamps, and HTML tags, keeping only speaker labels and spoken text. Confirm the line count output to the user and proceed.

### Step 2: Clean and filter (subagent)

Launch a subagent using the Agent tool with `model: "sonnet"`. The subagent reads `meetings/tmp/meeting-stripped.txt`, cleans and filters it, and writes the result to `meetings/tmp/meeting-cleaned.txt`. Wait for the subagent to complete before proceeding.

**Subagent prompt (pass this entire block):**

> Read the file `meetings/tmp/meeting-stripped.txt`. This is a meeting transcript with speaker-attributed speech (VTT metadata already removed).
>
> Identify the language from the first few exchanges. State it briefly.
>
> Produce a cleaned and filtered version of the transcript **in the same language as the original**. Do NOT translate. Apply all of the following simultaneously in a single output pass. Do NOT output intermediate versions.
>
> **Fix:**
> - Misspelled words and mangled diacritics (e.g., "ceskeho" -> "českého", "nastroj" -> "nástroj", "je to 1" -> "je to jedno")
> - Broken proper nouns garbled by auto-captioning (e.g. VIBMC -> v IBMce -> v IBM)
> - Homophones and misheard words (use surrounding context to pick the correct word)
> - Sentence boundaries (restore natural structure where auto-captions broke it)
> - Speaker attribution (normalize to consistent names throughout)
>
> **Drop entirely:**
> - Greetings, goodbyes, "how was your weekend" chitchat
> - Off-topic tangents unrelated to any work item
> - Filler ("um", "uh", "you know", "like I said", and source-language equivalents)
> - Politically incorrect, offensive, or inappropriate language
> - Personal, sensitive, or political opinions not relevant to the problem at hand
> - Repeated statements that add no new information (keep the clearest version)
> - Conversational scaffolding ("So what I'm trying to say is...", "That's a great point, and to add to that...")
>
> **Keep everything else**, especially: decisions, technical debates, action items, proposals, disagreements, status updates, blockers, reasoning, and any discussion that moves work forward. When in doubt, keep it.
>
> If you are unsure about some corrections, proceed with the most likely interpretation.
>
> Write the result to `meetings/tmp/meeting-cleaned.txt`. Output only the processed transcript, no commentary.

After the subagent completes, confirm success and the detected language to the user and proceed.

### Step 3: Translate to English (subagent)

If the transcript is already in English, copy `meetings/tmp/meeting-cleaned.txt` to `meetings/tmp/meeting-translated.txt` via Bash and skip to Step 4.

Otherwise, launch a subagent using the Agent tool with `model: "sonnet"`. The subagent reads `meetings/tmp/meeting-cleaned.txt` and writes the English translation to `meetings/tmp/meeting-translated.txt`. Wait for the subagent to complete before proceeding.

**Subagent prompt (pass this entire block):**

> Read the file `meetings/tmp/meeting-cleaned.txt`. This is a cleaned, filtered meeting transcript. Translate it to fluent English.
>
> **Preserve:** speaker attribution, tone and register (casual stays casual, technical stays technical), disagreements, hedging, uncertainty ("I'm not sure, but...", "maybe we should..."), technical terms and acronyms standard in English (e.g., "Kubernetes", "API", "SDK").
>
> **Adapt:** idioms and expressions to natural English equivalents. Follow English word order, not source-language syntax.
>
> **Do NOT:** summarize, editorialize, add meaning that wasn't in the original, formalize casual speech, or casualize formal speech. If a term has no clean English equivalent, keep the original in parentheses: "the deployment target (nasazovaci cil)".
>
> Write the result to `meetings/tmp/meeting-translated.txt`. Output only the translated transcript, no commentary.

After the subagent completes, confirm success to the user and proceed.

### Step 4: Extract, structure, and save (subagent)

Launch a subagent using the Agent tool with `model: "sonnet"`. The subagent will read from `meetings/tmp/meeting-translated.txt`, produce the structured extract, and save it directly to `meetings/`. Wait for the subagent to complete before proceeding.

**Subagent prompt (pass this entire block):**

> Read the file `meetings/tmp/meeting-translated.txt`. This is a cleaned, filtered, English-language meeting transcript. Extract and structure it into the following format. Every section is mandatory, but use "None identified." if a section is empty.
>
> ```
> # Meeting Extract
>
> ## Key Decisions
> - [Decision 1]
> - [Decision 2]
>
> ## Action Items
> - [ ] [Owner]: [Action item]
>
> ## Discussion
>
> ### [Topic 1 title]
> [Preserved discussion in the speakers' own words. Use direct quotes attributed to speakers. Keep disagreements, nuance, and reasoning as spoken.]
>
> ### [Topic 2 title]
> [Same approach as for Topic 1]
>
> ## Open Questions
> - [Unresolved question raised during the meeting]
> ```
>
> **Rules:**
> - **Direct quotes for key moments.** Use verbatim quotes for decisions, disagreements, strong opinions, and novel insights. These are the highest-value tokens.
> - **Concise paraphrasing for context.** Background discussion, status updates, and explanations of known concepts can be condensed. Attribute them ("John noted that...") but don't quote word-for-word.
> - **Attribute statements.** Use speaker names/identifiers from the transcript.
> - **Keep disagreements verbatim.** If people disagree, preserve both sides as direct quotes. The exact words matter here.
> - **Preserve reasoning chains.** Keep supporting arguments, objections, counter-arguments, and examples. Condense where possible but don't lose the logic.
> - **No editorializing.** Do not add opinions, assessments, or recommendations. Report what was said.
> - **Collapse repetition.** If the same point is made multiple times, keep the clearest version only.
>
> Write the structured extract to `meetings/YYYY-MM-DD-meeting-<short-slug>.md` where `YYYY-MM-DD` is today's date and `<short-slug>` is a 2-3 word kebab-case summary of the main meeting topic. Do not include any commentary, just the formatted extract.

After the subagent completes, tell the user the output file path and proceed to cleanup.

### Step 5: Clean up

Remove the temp directory by running `rm -rf meetings/tmp/` via Bash.
