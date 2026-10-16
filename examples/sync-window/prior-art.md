# Prior-art search record: Sync Window

> Example only. The rows below are illustrative, to show the format; they are not the result of a real search.

## Batch 1 (approved 21 Oct 2026)

Queries: `mobile background job scheduler deferred network`; `radio tail energy batching mobile`

| Item | What it does | How the invention differs | Weight |
|---|---|---|---|
| Operating-system job schedulers | Defer jobs until charging or unmetered network | Do not align jobs of different apps to a radio window opened by another transfer | high |
| Research on radio tail energy | Measures and models tail energy; batches one app's requests | One app, not a cross-app scheduler with deadlines | medium |

## What the search means for the application

- Known on their own: deferral, single-app batching, tail energy models.
- Not found: starting pending syncs of many apps in a radio window opened by any transfer, chosen by deadline and expected window length.
- Drafting consequence: every claim keeps the radio-window trigger and the cross-app selection.
