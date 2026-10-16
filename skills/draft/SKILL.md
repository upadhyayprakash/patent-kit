---
name: draft
description: Draft the provisional specification (Indian Form 2) and Form 3 from the inventor's disclosure and prior-art record, and render them to compliant A4 PDFs. Use when the disclosure is ready and the inventor wants the filing text.
---

# patent-kit: draft

The plugin root is two folders above this skill's folder. Work inside the patent workspace.

## Inputs

Read `disclosure.md`, `prior-art.md`, `tracker.md` and `<root>/jurisdictions/india/rules.md`. If the disclosure has open points that affect what must be described, ask before drafting.

## Write `form2.md`

Copy `<root>/jurisdictions/india/form2-provisional.md` into the workspace as `form2.md` and fill it:

- **Title:** at most 15 words, plain, describing the mechanism. Offer two or three options; the inventor chooses.
- **Applicant:** the name exactly as on the signing ID, nationality, address.
- **Background:** the problem, then the known approaches from `prior-art.md`, described fairly with numbers and papers, then the technical problem none of them solves.
- **Summary:** the core mechanism in technical terms.
- **Drawings:** one "Figure N shows ..." line per figure planned in the disclosure.
- **Detailed description:** definitions, the architecture with reference numerals (100, 110, 112, ...; 200 for figure 2, and so on), the flow step by step, the embodiment as built, then **every variation** from the disclosure, each with enough detail to build it. Anything not described here gets no date from this filing.
- **Technical effects:** one numbered paragraph per effect, compared with the known approaches.
- **Industrial applicability**, the closing paragraph, the dated signature block and the abstract (at most 150 words, starting with the title).
- Number every paragraph [0001], [0002], ... in order.
- No claims. No benefit claims for groups of people without data. No trade marks as names. No credit to anyone but the inventor.

Write in plain, confident technical English. Describe what the system does; do not apologise or hedge.

Check, then fix:
- run `python3 <root>/scripts/check_spec.py form2.md` (title of at most 15 words with no promotional words such as premium, ergonomic or smart; abstract of at most 150 words; consecutive paragraph numbers; no placeholders). After the drawings exist, run it again with `drawings.json` to match the reference numerals,
- every variation in the disclosure appears in the description,
- what is protected is how it works: appearance (materials for looks, colours, styling) stays out unless it serves a function.

## Form 3 (optional now, due within 6 months)

Copy `<root>/jurisdictions/india/form3.md` to `form3.md` and fill it (sole applicant, no foreign filings). Filing it with the application removes a deadline.

## Render

```
python3 <root>/scripts/spec_to_pdf.py form2.md filed/Form2-Provisional-Specification-<Name>.pdf
python3 <root>/scripts/spec_to_pdf.py form3.md filed/Form3-Statement-and-Undertaking-<Name>.pdf
```

The script warns about unfilled `{{placeholders}}`. Look at the first, a middle and the last page of each PDF (render them to PNG with `pdftoppm` or open them) before calling it done. File names must not contain "draft".

## For the portal text boxes

Run `python3 <root>/scripts/portal_text.py form2.md filed` to write `portal-description.txt`, `portal-abstract.txt` and `portal-claims.txt` for the Form 1 text boxes.

Ask the inventor to read `form2.md` as a stranger: could an engineer build it from this text alone? Then update `tracker.md` and suggest `/patent-kit:drawings`.

## Before you stop

Update `tracker.md`: the status of this phase in "Status at a glance", a line in the log, and the "Resume here" line (what was done, and the next step with its command). The inventor may pause here and come back any time.
