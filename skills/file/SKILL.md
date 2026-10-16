---
name: file
description: Walk the inventor through filing the provisional application on the IP India portal, field by field, from account and eSign to upload, signing and payment, including the portal's known problems. Use when the PDFs are ready, or when the inventor is on a portal screen and asks what to fill.
---

# patent-kit: file

The plugin root is two folders above this skill's folder. The step-by-step guide is `<root>/jurisdictions/india/portal-guide.md`: read it first and follow it.

## First: a filing sheet

Before the inventor opens the portal, write `filing-sheet.md` in the workspace with every value already filled: the phase 4 account steps with their name and address; the Form 1 table (jurisdiction from the state, page counts from `pagecount.py`, the title copied from `form2.md`, address, text-box files, claims line, declarations, no bundled forms); the upload table with the exact file paths; the pre-sign checklist; and the payment steps. During filing the inventor copies from it and you only need to handle surprises.

## How to help

- The inventor fills the portal; you never log in or enter their personal details. Ask for screenshots with ID numbers hidden.
- For each screen, give the exact value per field as a short table, with copy-ready text for the title, address and claims box.
- Never let them sign before checking: after eSign, nothing can be edited.
- Name and address must match across Form 1, Form 2, drawings, Form 3 and the signing ID. If the portal shows a different name (for example the longer Aadhaar name), regenerate the PDFs with it before uploading.
- If the applicant address cannot be edited and has a typo, note it in `tracker.md` for correction after filing; the address for service is what the office uses.
- Keep `tracker.md` updated with the temporary application number, uploads, signing and each payment attempt (transaction ID, time, debited or not).

## Payment problems

Follow the guide: never pay twice in a hurry; check Pending CBR after 60 minutes; retry only if nothing was debited and the status says failed; write to ipo-helpdesk@nic.in with all IDs if money left the account and the status stays failed.

## When the receipt arrives

Ask for the receipt PDF and continue with `/patent-kit:track`.

## Before you stop

Update `tracker.md`: the status of this phase in "Status at a glance", a line in the log, and the "Resume here" line (what was done, and the next step with its command). The inventor may pause here and come back any time.
