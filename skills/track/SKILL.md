---
name: track
description: After filing, read the patent office receipt, record the application number and filing date, compute every deadline, and explain what the inventor may now publish. Also use later to see what is due next on a filed application.
---

# patent-kit: track

The plugin root is two folders above this skill's folder.

## Record the filing

1. Read the receipt (CBR) PDF the inventor points to (open the PDF directly; it often arrives as `PATENT eFiling.pdf`). Extract: application number, filing date and time, CBR number, amount, transaction ID.
1a. Compare the receipt with the filing: applicant name, address and title against `form2.md` and the tracker. Any difference (for example an address typo copied from the portal profile) goes into the tracker as a correction to request from the office.
2. Move it into the workspace as `filed/CBR-Receipt-<application number>-<YYYY-MM-DD>.pdf`.
3. In `tracker.md`: phase 2 done with the number and date; fill the filing line; log it.
4. Run `python3 <root>/scripts/deadlines.py <YYYY-MM-DD> --esign-expiry <date> [--form3-filed] --title "<short name>" --ics filed/deadlines.ics` and paste the table into the tracker's Deadlines section. If the signing certificate expires before the complete specification is due, say so.
5. Ask the inventor to import `filed/deadlines.ics` into their calendar now (double-click it, or import it in Google Calendar); each event has a reminder two weeks before.

## What changes now

Tell the inventor plainly:
- "Patent pending" is accurate from today.
- Publishing (paper, post, video, demo, open-sourcing the code) is possible for **what the provisional describes**. Anything new must go into a filing (the complete specification, or a new provisional) **before** it is shown.
- Publishing is safe only because the complete specification will be filed within 12 months. If that deadline is missed, their own publication can block a new filing.
- The complete specification is the step where quality matters most: claims drafted from the disclosure's claim sketch, ordered by commercial importance. A patent professional's review is worth considering.
- Any correction needed on the record (for example an address typo) goes to the office now.

## Later

When asked "what is due", read the tracker, compare the deadlines with today's date and list what is next, oldest first.

## Before you stop

Update `tracker.md`: the status of this phase in "Status at a glance", a line in the log, and the "Resume here" line (what was done, and the next step with its command). The inventor may pause here and come back any time.
