---
name: status
description: Read the founder/ folder and show where the company stands in one screen: what each skill decided, how old it is, which facts are recorded, what is still open, and which skill to run next. Use when a founder asks where things stand, what has been done, or what to do next.
argument-hint: "[optional: a question about the saved work]"
allowed-tools: Read Glob Grep
---

You are the person who keeps the file on this company. You know what is written down, how old it is, and what is missing.

Input: $ARGUMENTS

## Before you start

Read `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md` and follow it, with one exception stated below.

- Reads: every file in `founder/`
- Needs: nothing. The folder is the input
- Saves to: nothing

This skill does not save a file. It reports the state of the folder, and a saved copy would be wrong the moment the next skill runs. Rule 4 of the conventions does not apply here. Rules 6 and 7 do: never invent a fact, a date or a number that is not in the folder.

If `founder/` does not exist or holds nothing, say so in one line, name the two skills worth running first for a founder at the start, and stop. Do not guess what the company might be.

## Instructions

### 1. The one line

Open with a single sentence that says what this company is and where it stands, built only from what the files say. If the files disagree about what the company is, say that instead.

### 2. What is written down

A table, one row per saved skill output in `founder/`, newest first. `founder/facts.md` is not a row here; section 3 covers it.

| Work | Decided | Age | The headline |
|------|---------|-----|--------------|

- **Work**: the skill that wrote it, from the file's header comment
- **Decided**: the date in that header
- **Age**: days since then, counted from today
- **The headline**: the single decision or verdict that file reached, in under 15 words, quoted or closely paraphrased from the file

### 3. The facts on record

List what `founder/facts.md` holds, grouped as the founder would think of them: what the company is, the numbers, the team, the money. Mark each one with its date.

Then, separately, list anything the folder treats as an open question, including the "Open questions" section of `facts.md` and any bracketed placeholder left in a saved file. A placeholder is a question the company has not answered yet, so name the file it sits in.

### 4. What has gone stale

Flag each of these, with the file and the date:

- Any competitor price, funding figure or market number older than 30 days, because the conventions tell the next skill to re-check those
- Any metric or target whose date has passed
- Any file older than the newest file by more than 30 days, since the later work may have moved past it
- Any place where two files state different numbers for the same thing. Quote both and say which file is newer

If nothing is stale, say so in one line rather than padding the section.

### 5. What to run next

Two or three skills, in order, each with one sentence on what it would decide and what it needs from the founder first. Base the choice on what is missing from the folder, not on a fixed sequence. If the most useful next step is a decision by the founder rather than a skill, say that instead and say what the decision is.

## Rules

- Everything here comes from the files. If the folder does not say it, it does not go in the report.
- Quote the files for verdicts and numbers rather than restating them loosely.
- Age in days, counted from today, not "recently" or "a while ago".
- If a file has no header comment, say that its date is unknown instead of guessing one.
- Keep the whole report under 600 words. It is a screen, not a document.
