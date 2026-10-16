---
name: drawings
description: Produce the patent drawing sheets (Indian rule 15 style) for the inventor's provisional specification from a JSON spec, render them to an A4 PDF and check them visually. Use after the Form 2 text exists or when the inventor asks for patent figures.
---

# patent-kit: drawings

The plugin root is two folders above this skill's folder. The engine is `<root>/scripts/drawings.py`; read its docstring for the element types.

## Plan

From `form2.md` ("Brief description of the drawings" and the reference numerals), list the figures. Typical sets, one figure per sheet:
- Software: architecture, data model, sequence of one run, a timeline or state view, the screen or output at one moment, one flowchart per important process.
- Device or mechanism: top or perspective view, a cross-section through the part that does the work, an exploded view if parts assemble, a block diagram of any electronics, a flowchart of use, and one view per important variation.
For cross-sections, use `"fill": "hatch"` for cut solid parts or magnets and `"dots"` for soft or textile layers, and point to each part with a numbered leader line from outside the object.

## Write `drawings.json`

```json
{"applicant": "FULL NAME AS ON THE SIGNING ID",
 "figures": [{"elements": [
   {"type": "box", "x": 42, "y": 56, "w": 136, "h": 100, "dashed": true},
   {"type": "text", "x": 45, "y": 62, "text": "110 Server", "anchor": "start", "bold": true},
   {"type": "box", "x": 46, "y": 68, "w": 60, "h": 12, "lines": ["112 Input module"]},
   {"type": "line", "points": [[76, 80], [76, 86]]},
   {"type": "flow", "x": 62, "y": 58, "w": 96, "h": 12, "gap": 8, "steps": ["702 Read", "704 Decide"], "loop": true}
 ]}]}
```

Rules the sheets must follow:
- Elements inside x 40 to 180 mm and y 52 to 245 mm. The script adds the name, sheet number, "FIG. N" and signature line.
- Black lines only. Show selected parts or states with `"fill": "hatch"` or `"dots"`, outlines, thick borders or underlines, never colour.
- Labels and flowchart text only; no sentences, no dimensions. Text at least the default size (4.4).
- Every reference numeral in a drawing appears in the description, and the other way round.
- Leave space around labels so nothing overlaps lines or boxes.

## Render and check

```
python3 <root>/scripts/drawings.py drawings.json filed/Drawings-<Name>.pdf
```

Fix every warning. Then **look at every sheet** (for example `pdftoppm -r 80 -png filed/Drawings-<Name>.pdf /tmp/sheet` and view the images): overlapping text, labels crossing lines, arrows pointing at nothing, misaligned brackets. Fix and re-render until each sheet is clean. Show the inventor the sheets and ask for corrections.

Run `python3 <root>/scripts/check_spec.py form2.md drawings.json` (numerals in the drawings must all appear in the description), then `python3 <root>/scripts/pagecount.py filed/Form2-*.pdf filed/Drawings-*.pdf` and record the counts in `tracker.md` for Form 1.

## Before you stop

Update `tracker.md`: the status of this phase in "Status at a glance", a line in the log, and the "Resume here" line (what was done, and the next step with its command). The inventor may pause here and come back any time.
