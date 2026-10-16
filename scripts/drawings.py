#!/usr/bin/env python3
"""Render patent drawing sheets from a JSON spec to an A4 PDF (Indian Patents Rules, rule 15 style).

Usage: python3 drawings.py SPEC.json OUTPUT.pdf

Each sheet: A4, drawable area x 40..180 mm, y 40..267 mm (margins 4 cm top and left, 3 cm bottom and right),
applicant's name top left, "Sheet N of M" top right, "FIG. N" and a signature line with the name at the bottom.
Black lines only; text at least 4.4 mm font size (about 3.2 mm capitals).

Spec:
{
  "applicant": "FULL NAME AS ON THE SIGNING ID",
  "figures": [
    {"elements": [ ... ]},          # one sheet per figure, numbered in order
    ...
  ]
}

Coordinates are millimetres on the page. Keep elements inside x 40..180 and y 52..245
(the header sits at y 40..50 and the figure label and signature at y 247..267). Elements:

  {"type": "box", "x", "y", "w", "h", "lines": ["112 Input module"], "dashed": false, "thick": 0.4,
   "r": 0, "fill": "none" | "hatch" | "dots"}
  {"type": "text", "x", "y", "text", "anchor": "start" | "middle" | "end", "size": 4.4, "bold": false}
  {"type": "line", "points": [[x, y], [x, y], ...], "arrow": true, "dashed": false, "width": 0.35}
  {"type": "diamond", "cx", "cy", "w", "h", "lines": ["Battery low?"]}
  {"type": "hatch" | "dots", "x", "y", "w", "h"}             # shading for a part (solid, magnet, textile) without an outline
  {"type": "ellipse", "cx", "cy", "rx", "ry"}
  {"type": "flow", "x", "y", "w", "h", "gap", "steps": ["702 Read position", "704 ..."], "loop": false}
      A vertical flowchart: boxes of size w x h, gap mm apart, joined by arrows; "loop" adds a return arrow.

The script warns about anything outside the drawable area and text smaller than the minimum.
"""
import html, json, pathlib, sys, tempfile
from chrome import find_chrome, print_pdf

X0, X1, Y0, Y1 = 40, 180, 40, 267
TOP, BOTTOM = 52, 245
FS = 4.4
warnings = []


def esc(t):
    return html.escape(str(t))


def check(fig, what, x0, y0, x1, y1):
    if x0 < X0 - 0.01 or x1 > X1 + 0.01 or y0 < TOP - 0.01 or y1 > BOTTOM + 0.01:
        warnings.append(f"FIG. {fig}: {what} is outside the drawable area ({x0:.0f},{y0:.0f})-({x1:.0f},{y1:.0f})")


def text(x, y, t, size=FS, anchor="middle", bold=False):
    w = ' font-weight="bold"' if bold else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}"{w}>{esc(t)}</text>'


def lines_in(x, y, w, h, lines, size=FS):
    lh = size * 1.25
    top = y + h / 2 - (len(lines) - 1) * lh / 2 + size * 0.35
    return "".join(text(x + w / 2, top + i * lh, l, size) for i, l in enumerate(lines))


def dash(d):
    return ' stroke-dasharray="2,1.5"' if d else ""


def el_box(e, fig):
    x, y, w, h = e["x"], e["y"], e["w"], e["h"]
    check(fig, "box " + " ".join(e.get("lines", [])), x, y, x + w, y + h)
    fill = {"hatch": "url(#hatch)", "dots": "url(#dots)"}.get(e.get("fill", "none"), "none")
    out = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{e.get("r", 0)}" fill="{fill}" '
           f'stroke="black" stroke-width="{e.get("thick", 0.4)}"{dash(e.get("dashed"))}/>')
    return out + lines_in(x, y, w, h, e.get("lines", []))


def el_text(e, fig):
    size = e.get("size", FS)
    if size < FS:
        warnings.append(f"FIG. {fig}: text '{e['text']}' is smaller than {FS} mm")
    check(fig, f"text '{e['text']}'", e["x"], e["y"] - size, e["x"], e["y"])
    return text(e["x"], e["y"], e["text"], size, e.get("anchor", "middle"), e.get("bold", False))


def el_line(e, fig):
    pts = e["points"]
    for x, y in pts:
        check(fig, "line point", x, y, x, y)
    p = " ".join(f"{x},{y}" for x, y in pts)
    m = ' marker-end="url(#ah)"' if e.get("arrow", True) else ""
    return (f'<polyline points="{p}" fill="none" stroke="black" stroke-width="{e.get("width", 0.35)}"'
            f'{dash(e.get("dashed"))}{m}/>')


def el_diamond(e, fig):
    cx, cy, w, h = e["cx"], e["cy"], e["w"], e["h"]
    check(fig, "diamond", cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    p = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    return (f'<polygon points="{p}" fill="none" stroke="black" stroke-width="0.4"/>'
            + lines_in(cx - w / 2, cy - h / 2, w, h, e.get("lines", [])))


def el_shade(e, fig):
    check(fig, e["type"], e["x"], e["y"], e["x"] + e["w"], e["y"] + e["h"])
    pat = "hatch" if e["type"] == "hatch" else "dots"
    return f'<rect x="{e["x"]}" y="{e["y"]}" width="{e["w"]}" height="{e["h"]}" fill="url(#{pat})" stroke="none"/>'


def el_ellipse(e, fig):
    check(fig, "ellipse", e["cx"] - e["rx"], e["cy"] - e["ry"], e["cx"] + e["rx"], e["cy"] + e["ry"])
    return f'<ellipse cx="{e["cx"]}" cy="{e["cy"]}" rx="{e["rx"]}" ry="{e["ry"]}" fill="none" stroke="black" stroke-width="0.4"/>'


def el_flow(e, fig):
    x, y, w, h, gap = e["x"], e["y"], e["w"], e["h"], e.get("gap", 8)
    out, cx = [], x + w / 2
    for i, s in enumerate(e["steps"]):
        by = y + i * (h + gap)
        out.append(el_box({"x": x, "y": by, "w": w, "h": h, "lines": [s], "r": 1}, fig))
        if i:
            out.append(el_line({"points": [[cx, by - gap], [cx, by]]}, fig))
    if e.get("loop") and len(e["steps"]) > 1:
        last = y + (len(e["steps"]) - 1) * (h + gap) + h / 2
        out.append(el_line({"points": [[x, last], [x - 8, last], [x - 8, y + h / 2], [x, y + h / 2]]}, fig))
    return "".join(out)


RENDER = {"box": el_box, "text": el_text, "line": el_line, "diamond": el_diamond, "hatch": el_shade,
          "dots": el_shade, "ellipse": el_ellipse, "flow": el_flow}

DEFS = """<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="2.2" markerHeight="2.2" markerUnits="userSpaceOnUse" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="black"/></marker>
<pattern id="hatch" width="1.6" height="1.6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="1.6" stroke="black" stroke-width="0.35"/></pattern>
<pattern id="dots" width="1.6" height="1.6" patternUnits="userSpaceOnUse"><circle cx="0.8" cy="0.8" r="0.22" fill="black"/></pattern>
</defs>"""


def sheet(n, total, name, body):
    head = text(X0, Y0 + 5, name, anchor="start") + text(X1, Y0 + 5, f"Sheet {n} of {total}", anchor="end")
    label = text((X0 + X1) / 2, Y1 - 13, f"FIG. {n}", size=5.2, bold=True)
    foot = (f'<line x1="{X1-60}" y1="{Y1-7}" x2="{X1}" y2="{Y1-7}" stroke="black" stroke-width="0.25"/>'
            + text(X1, Y1 - 2, f"{name}, Applicant", anchor="end"))
    return (f'<svg class="page" xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297" '
            f'font-family="Arial, Helvetica, sans-serif">{DEFS}{head}{body}{label}{foot}</svg>')


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
    name, figs = spec["applicant"], spec["figures"]
    pages = []
    for i, f in enumerate(figs, 1):
        body = []
        for e in f["elements"]:
            if e["type"] not in RENDER:
                sys.exit(f"FIG. {i}: unknown element type '{e['type']}'")
            body.append(RENDER[e["type"]](e, i))
        pages.append(sheet(i, len(figs), name, "".join(body)))
    doc = ('<!doctype html><html><head><meta charset="utf-8"><title>Drawings</title><style>'
           '@page { size: A4; margin: 0 } html, body { margin: 0; background: white } '
           'svg.page { display: block; page-break-after: always }</style></head><body>' + "".join(pages) + "</body></html>")
    dst = pathlib.Path(sys.argv[2]).resolve()
    with tempfile.TemporaryDirectory() as d:
        page = pathlib.Path(d, "drawings.html")
        page.write_text(doc)
        print_pdf(find_chrome(), page, dst)
    for w in warnings:
        print("warning: " + w, file=sys.stderr)
    print(f"wrote {dst} ({len(figs)} sheets)")


if __name__ == "__main__":
    main()
