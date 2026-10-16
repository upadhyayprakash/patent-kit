# Example: Sync Window (fictional)

A made-up invention taken through patent-kit end to end, so you can see every artefact before starting your own. The inventor, address and invention are invented for this example; the idea is not claimed to be new and must not be filed.

| File | Made by | What it is |
|---|---|---|
| `disclosure.md` | `/patent-kit:start` | The interview written up |
| `prior-art.md` | `/patent-kit:prior-art` | Illustrative search record (not a real search) |
| `form2.md` | `/patent-kit:draft` | Provisional specification source |
| `form3.md` | `/patent-kit:draft` | Statement and undertaking source |
| `drawings.json` | `/patent-kit:drawings` | Drawing spec |
| `filed/*.pdf` | the scripts | The PDFs you would upload |
| `tracker.md` | all steps | Status, deadlines and log |

Rebuild the PDFs from the plugin root:

```
python3 scripts/spec_to_pdf.py examples/sync-window/form2.md examples/sync-window/filed/Form2-Provisional-Specification-Asha-Example.pdf
python3 scripts/spec_to_pdf.py examples/sync-window/form3.md examples/sync-window/filed/Form3-Statement-and-Undertaking-Asha-Example.pdf
python3 scripts/drawings.py examples/sync-window/drawings.json examples/sync-window/filed/Drawings-Asha-Example.pdf
python3 scripts/pagecount.py examples/sync-window/filed/Form2-*.pdf examples/sync-window/filed/Drawings-*.pdf
python3 scripts/deadlines.py 2026-11-02 --esign-expiry 2027-10-20
```
