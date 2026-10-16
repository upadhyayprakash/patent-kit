# patent-kit

**File a provisional patent for your own invention, yourself, in an evening.**

patent-kit is a Claude Code plugin for inventors, engineers and builders who have a new technical idea and want a priority date on it. It interviews you, keeps everything private, searches prior art only with your approval, writes the provisional specification and the drawings as compliant PDFs, walks you through the patent office portal field by field, and tracks every deadline after filing.

India first: a provisional application there costs **Rs 1,600** for an individual filing online, and the whole flow in this kit was tested on a real filing in October 2026.

## What you get

| Step | Command | You end up with |
|---|---|---|
| 1. Start | `/patent-kit:start` | A private workspace, an encrypted backup plan, and your **invention disclosure** written from an interview |
| 2. Prior art | `/patent-kit:prior-art` | Searches run in batches **you approve**, and a record of what exists and how yours differs |
| 3. Draft | `/patent-kit:draft` | **Form 2** (provisional specification) and **Form 3** as A4 PDFs with the official margins and page numbers |
| 4. Drawings | `/patent-kit:drawings` | Drawing sheets in the rule 15 layout (name, sheet numbers, margins, black lines), checked sheet by sheet |
| 5. File | `/patent-kit:file` | Exact values for every portal field, the upload types, signing and payment, including what to do when the payment page fails |
| 6. Track | `/patent-kit:track` | Application number and filing date recorded, every deadline computed, and what you may now publish |

New to patents? Read the [glossary](GLOSSARY.md) (who is involved and the terms you will meet) and the [websites you will use](jurisdictions/india/websites.md). The [journey](JOURNEY.md) shows every phase with its time and cost; you can pause after any phase and resume later with `/patent-kit:start`.

See [`examples/sync-window/`](examples/sync-window/) for a fictional invention taken through every step, with the resulting PDFs.

## Your idea stays yours

- **Nothing leaves your machine without you.** Inside a patent workspace, a hook asks you before every web search, page fetch, `git push`, upload or publishing action. A search query can reveal an idea; you decide each one.
- **The workspace lives outside git**, and the kit suggests an encrypted backup on your own drive.
- **You are the inventor.** Claude asks, organises and writes up what you tell it. It never adds inventive content of its own, and it never names itself, Anthropic or anyone else as inventor or contributor in your filing.

## Install

In Claude Code:

```
/plugin marketplace add upadhyayprakash/patent-kit
/plugin install patent-kit@patent-kit
```

Then open a new session and type `/patent-kit:start`.

Requirements: Python 3 and Google Chrome (or Chromium) for the PDFs. Nothing else to install.

## How the PDFs are made

- `scripts/spec_to_pdf.py`: a form in simple Markdown to an A4 PDF (margins 4 cm top and left, 3 cm bottom and right, "Page X of Y").
- `scripts/drawings.py`: a JSON drawing spec to rule-15-style sheets, with warnings for anything outside the margins or too small.
- `scripts/check_spec.py`: checks the title (15 words, no promotional words), the abstract (150 words), paragraph numbering, placeholders, and that the drawings' reference numerals appear in the text.
- `scripts/portal_text.py`: the plain text for the Form 1 boxes.
- `scripts/pagecount.py`: the page counts Form 1 asks for.
- `scripts/deadlines.py`: every deadline from the filing date, including your eSign expiry.

All use Chrome's headless print, so the output is the same on macOS, Windows and Linux.

## What a provisional does, in brief

It fixes your priority date for everything it describes, needs no claims, and gives you 12 months to file the complete specification with claims. After filing you can say "patent pending" and publish what the provisional describes. Read [`jurisdictions/india/rules.md`](jurisdictions/india/rules.md) for the details that matter: format, the 15-word title, the 150-word abstract, software inventions under sections 3(k) and 3(n), fees and deadlines.

## Scope

patent-kit helps inventors file **their own** applications. Acting for someone else before the Indian Patent Office is reserved for registered patent agents, and similar rules exist elsewhere. It is not legal advice. For the complete specification, where the claims decide what you own, a patent professional's review is worth considering.

## Contributing

Other countries are welcome as `jurisdictions/<country>/` with the same files: `rules.md`, `portal-guide.md` and the form templates. Corrections to the India portal guide (screens change) are especially useful.

## License

MIT. See [LICENSE](LICENSE).
