#!/usr/bin/env python3
"""Render a patent form written in simple Markdown to an A4 PDF with Indian Patent Office margins.

Usage: python3 spec_to_pdf.py INPUT.md OUTPUT.pdf

Markdown subset:
  - Everything before the first line "---" is the centred front block (form name, Act, title, applicant).
  - "# ", "## ", "### " headings; "**bold**"; blank lines separate paragraphs; single newlines become line breaks.
  - "## ABSTRACT" starts on a new page.
  - A paragraph starting with "Dated this" starts the signature block.
  - HTML comments are dropped (use them for notes to yourself).

Page: A4, margins 4 cm top and left, 3 cm bottom and right, "Page X of Y" at the foot. Needs Google Chrome or Chromium.
"""
import html, pathlib, re, sys, tempfile
from chrome import find_chrome, print_pdf

CSS = """
@page { size: A4; margin: 40mm 30mm 30mm 40mm;
  @bottom-center { content: "Page " counter(page) " of " counter(pages); font: 10pt Arial, Helvetica, sans-serif; } }
body { font-family: Arial, Helvetica, sans-serif; font-size: 12pt; line-height: 1.5; color: #000; margin: 0; }
h1 { font-size: 16pt; text-align: center; margin: 0 0 6pt; }
h2 { font-size: 12.5pt; margin: 16pt 0 6pt; }
h3 { font-size: 12pt; font-style: italic; margin: 12pt 0 4pt; }
p { margin: 0 0 8pt; text-align: justify; }
.c { text-align: center; }
hr.front { border: 0; border-top: 1px solid #000; margin: 14pt 0; }
h2.abstract { page-break-before: always; text-align: center; }
.sig { margin-top: 24pt; text-align: left; }
"""


def inline(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)


def to_html(src):
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S).strip()
    out, front = [], True
    for b in re.split(r"\n\s*\n", src):
        b = b.strip()
        if not b:
            continue
        if b == "---":
            if front:
                out.append('<hr class="front">')
                front = False
            continue
        if b.startswith("## ABSTRACT"):
            out.append('<h2 class="abstract">ABSTRACT</h2>')
            continue
        m = re.match(r"^(#{1,3}) (.*)$", b)
        if m and "\n" not in b:
            lvl = len(m.group(1))
            cls = ' class="c"' if front and lvl == 1 else ""
            out.append(f"<h{lvl}{cls}>{inline(m.group(2))}</h{lvl}>")
            continue
        cls = ' class="c"' if front else ""
        if b.startswith("Dated this"):
            cls = ' class="sig"'
        out.append(f"<p{cls}>" + "<br>".join(inline(l) for l in b.split("\n")) + "</p>")
    return f'<!doctype html><html><head><meta charset="utf-8"><title>Specification</title><style>{CSS}</style></head><body>{"".join(out)}</body></html>'


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]).resolve()
    leftovers = re.findall(r"\{\{[^}]+\}\}", re.sub(r"<!--.*?-->", "", src.read_text(), flags=re.S))
    if leftovers:
        print("warning: unfilled placeholders: " + ", ".join(sorted(set(leftovers))), file=sys.stderr)
    with tempfile.TemporaryDirectory() as d:
        page = pathlib.Path(d, "spec.html")
        page.write_text(to_html(src.read_text()))
        print_pdf(find_chrome(), page, dst)
    print(f"wrote {dst}")


if __name__ == "__main__":
    main()
