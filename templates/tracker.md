# Filing tracker: {{SHORT NAME}}

> CONFIDENTIAL. Inventor: {{NAME}}. Not legal advice. Check every fee and date on the patent office site on the day you act.

## Resume here

{{ONE LINE: WHAT WAS DONE LAST, AND THE NEXT STEP WITH ITS COMMAND}}

## Status at a glance

| Phase | What | Command | Status |
|---|---|---|---|
| 0 | Orientation | `/patent-kit:start` | not started |
| 1 | Capture: workspace, backup, disclosure | `/patent-kit:start` | not started |
| 2 | Prior art | `/patent-kit:prior-art` | not started |
| 3 | Draft: Form 2, Form 3, drawings | `/patent-kit:draft`, `/patent-kit:drawings` | not started |
| 4 | Accounts: eSign, portal, email | `/patent-kit:file` | not started |
| 5 | File: Form 1, upload, sign, pay | `/patent-kit:file` | not started |
| 6 | After filing: receipt, deadlines | `/patent-kit:track` | not started |
| later | Complete specification with claims (within 12 months of phase 5) | | not started |
| later | Publish (paper, post, video, demo) | | **blocked until phase 5 is done** |

## Pre-flight

- [ ] Applicant: yourself as a natural person (or a company)
- [ ] Patent office branch (by state): ________
- [ ] What this filing protects (how it works); appearance left to a design registration if it matters
- [ ] Nothing about the invention is public: no post, video, page, slide, talk, demo, upload or pushed repository
- [ ] Anyone who has seen it: who, when, in confidence?
- [ ] Workspace backed up privately (encrypted image on a separate drive)
- [ ] Signing: eSign or DSC bought; expiry date: {{DATE}}
- [ ] Patent office portal account created and email verified
- [ ] Earlier notes or sketches, with dates (if any)
- [ ] Variations ranked by commercial importance

## Prior-art search

- [ ] Batches approved and run; record in `prior-art.md`
- [ ] Nothing found describes the core combination (if something does, stop and rethink before filing)

## Provisional

- [ ] `form2.md` drafted from the disclosure; every variation described
- [ ] Title at most 15 words; abstract at most 150 words
- [ ] Drawings rendered; reference numerals match the text
- [ ] Read as a stranger: could an engineer build it from this alone?
- [ ] Name identical on Form 1, Form 2, drawings, Form 3 and the signing ID
- [ ] PDFs in `filed/`; page counts from `pagecount.py`

## Filing

- [ ] Form 1 saved; email verified; documents uploaded (Form 1 PDF, Form 2, drawings, Form 3)
- [ ] Signed; paid; receipt saved in `filed/`
- [ ] Filing date: ________  Application number: ________

## Deadlines

{{PASTE THE TABLE FROM scripts/deadlines.py}}

## After filing

- Publish only what the provisional describes. Anything new: write it into a filing first, then show it.
- Publishing is safe only because the complete specification will be filed in time. Miss it and your own publication can block a re-filing.
- "Patent pending" is accurate from the filing date.

## Log

| Date | What happened |
|---|---|
| {{DATE}} | Workspace created |
