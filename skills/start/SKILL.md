---
name: start
description: Start a patent filing for the user's own invention. Sets up a private patent workspace, interviews the inventor and writes the invention disclosure that the provisional specification is drafted from. Use when someone wants to patent an idea, file a provisional, protect an invention, or asks "can I patent this". India first.
---

# patent-kit: start

You help an inventor file **their own** invention. The idea is theirs alone: you ask, organise and write up what they tell you. Never present any part of the invention as your idea, and never add yourself, Claude or Anthropic as inventor, co-author or contributor anywhere in the filing.

The plugin root is two folders above this skill's folder. Paths below are relative to it.

## 0. Resume or begin

Look for an existing workspace: a `.patent-kit` marker in the current folder or a parent, or folders under `~/patents/`. If one exists, read its `tracker.md`, show the "Status at a glance" table and the "Resume here" line, and ask whether to continue from there (then run the step it names). Otherwise begin with orientation.

## 1. Orientation (phase 0)

Keep it short and friendly; the inventor may never have filed anything.

1. Show the journey table from `JOURNEY.md` (phases, commands, time, cost), and say they can stop after any phase and resume later by running `/patent-kit:start` again.
2. Explain only the terms needed right now, one line each: inventor and applicant, prior art, public disclosure, priority date, provisional and complete specification, claims. Point to `GLOSSARY.md` for everything else.
3. Show the websites they will use and what each is for, from `jurisdictions/india/websites.md` (search sites, eSign provider, the IP India portal and its payment gateway). Mention that the eSign and portal account (phase 4) can be done any time, in parallel.
4. Ask, in one line, what kind of invention it is (software, hardware, mechanical, a process, or a mix), and whether its value is in how it **works** or how it **looks**. If appearance is a large part, explain the patent and design difference from the glossary table "Patent, or something else?": the filing will describe the mechanism and function; the look may need a design registration outside this kit.
5. Tell them which patent office branch they will file with, from their state (table in `jurisdictions/india/rules.md`, "Which patent office").
6. Ask whether anything is unclear before going on.

## 1a. Confidentiality

Explain in two or three plain sentences: India (like most countries) is first to file, with no general grace period, so anything made public before the filing date can destroy novelty. That includes posts, videos, demos, talks, pushed repositories, shared documents and published artifacts. Ask whether anything about the idea is already public, and record the answer.

## 2. Create the workspace

- Ask for a short name (for example `smart-sync`). Default location: `~/patents/<short-name>/`. Offer a different one if they prefer.
- Check the folder is **not inside a git repository** (`git -C <dir> rev-parse --is-inside-work-tree` must fail). If it is, pick another place: a pushed repo is a publication.
- Create the folder with `filed/` inside it, and an empty marker file `.patent-kit`. The marker turns on the plugin's guard hook: web searches, fetches, pushes and publishing from this folder will ask the inventor first.
- Copy `templates/disclosure.md`, `templates/tracker.md` and `templates/prior-art.md` into it, and copy `GLOSSARY.md` and `JOURNEY.md` alongside so the inventor can read them offline.
- Work from inside the workspace for the rest of the process (start shell commands there) so the guard applies.

## 3. Backup

Suggest an encrypted backup the inventor controls:
- macOS: Disk Utility > File > New Image > Blank Image, 256-bit AES, size about 500 MB, saved on an external drive. The inventor sets the password; it never passes through you. Copy the workspace in when mounted.
- Windows or Linux: VeraCrypt container, or a 7-Zip archive with AES-256.
A plain cloud folder is not a publication, but sharing mistakes and sync make an encrypted file the safer choice.

## 4. Interview

Ask a few questions at a time, in plain language, and wait for answers. Cover:
1. The problem: who has it, how it shows up, how people deal with it today.
2. The idea in one sentence, then how it works step by step.
3. What exists: code, prototype, tests, measurements, recordings (with paths).
4. What is new compared with what they know of, in their words.
5. Variations: other ways to build it, other devices, other industries, cheaper or more advanced versions. Prompt with categories (input, output, devices, timing, scale, failure handling), but let the inventor decide what belongs; never add inventive content of your own.
6. Which variations matter commercially: "if a competitor copied this, which version would hurt most?"
7. Earlier notes or sketches with dates; anyone who has seen it.
8. Applicant details: full name exactly as on the ID they will sign with (Aadhaar or PAN for eSign), nationality, postal address.

Then check that the description can actually work as stated. Where a step is vague or physically or technically contradictory (for example electrical contacts that must close through a fabric layer), ask how it works; offer the inventor the options you see, and record the answer the inventor chooses. Enablement gaps found now are cheap; after filing they cannot be fixed.

Fill `disclosure.md` as you go. Mark each decision with its date and "(inventor)". Put open questions in its section 10.

## 5. Technical framing

For every invention, help the inventor state the **technical problem** and the **technical effects**, and describe the mechanism, not the business idea or the look.
- Devices and mechanical inventions: parts, materials only where they matter to function, how parts connect, move, lock, sense or are powered; effects such as fewer parts, reliability, energy, safety.
- Software: read `jurisdictions/india/rules.md`, "Software inventions" (sections 3(k) and 3(n)); effects such as computation, latency, bandwidth, errors, guarantees.
- Mixed (hardware with an app): describe both, and make clear which part carries the new technical function.

## 6. Update the tracker and hand over

In `tracker.md`: mark phases 0 and 1, tick the pre-flight items that are done, log the date and write the "Resume here" line. Then tell the inventor the next steps: `/patent-kit:prior-art`, then `/patent-kit:draft`, `/patent-kit:drawings`, `/patent-kit:file`.

## Rules for the whole process

- Nothing from the workspace is published, pushed, uploaded or shared until the receipt exists, unless the inventor says so explicitly for that item.
- Every web search is approved by the inventor first (the hook will also ask).
- Not legal advice: say once, plainly, that a patent professional's review is worth considering for the complete specification; do not repeat it on every step.
- This kit is for inventors filing their own applications.
