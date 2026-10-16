---
name: prior-art
description: Run a confidential prior-art search for the inventor's patent workspace in approved batches, and record what each result does and how the invention differs. Use after /patent-kit:start, or when the inventor asks whether their idea already exists.
---

# patent-kit: prior-art

A search query is sent to a third party. Treat every query as something that could reveal the idea.

## Rules

1. **The inventor approves every batch before it runs.** Show the exact queries; run only what is approved, word for word. The plugin's hook asks again for each search; that is expected.
2. **Generic terms only.** Search for the known building blocks (for example "magnetic detent position sensor"), never for the new combination itself. Do not put the invention's distinctive phrasing, names or the combination of its key steps into a query, a URL or a fetch prompt.
3. Batches of 3 to 7 queries. Usually 3 or 4 batches are enough: the core mechanism, each major variation, the newest technology era (recent patent applications), and anything the earlier batches pointed to.
4. Remind the inventor once that applications stay unpublished for 18 months, so no search can be complete; filing soon matters more than searching forever.

## Each batch

1. Read `disclosure.md` and propose the queries, each with one line on what it checks.
2. Wait for approval or edits.
3. Run the approved queries (web search). For a batch aimed at patents, restrict the search to `patents.google.com` (the search tool's allowed domains) so results are patent documents, not shops and blogs. Fetch a page only if the snippet is not enough, and only with a neutral prompt.
4. Append to `prior-art.md`: the queries, then a row per relevant item: what it does, how the invention differs, and a weight (low, medium, high). Link each item.
5. Tell the inventor in a few lines: what is close, what is not, and whether anything describes the core combination.

## Conclusion

After the last batch, fill "What the search means for the application" in `prior-art.md`:
- the building blocks that are known on their own,
- the combination that no item describes,
- **inventive step**: whether an examiner could call the invention an obvious combination of the items found, and which technical effect or variation best answers that,
- what every claim must keep in it so it is not anticipated.

Then fill the "Known approaches" list in section 2 of `disclosure.md` from the record, so the draft's background is ready.

If something describes the core combination, say so plainly and stop: the inventor must rethink the claims before filing.

Also suggest free databases the inventor can search directly: InPASS (India), Google Patents, Espacenet.

Update `tracker.md` (prior-art boxes and the log).

## Before you stop

Update `tracker.md`: the status of this phase in "Status at a glance", a line in the log, and the "Resume here" line (what was done, and the next step with its command). The inventor may pause here and come back any time.
