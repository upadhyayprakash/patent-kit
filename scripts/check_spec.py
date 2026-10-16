#!/usr/bin/env python3
"""Check a provisional specification (form2.md) and its drawing spec before rendering.

Usage: python3 check_spec.py form2.md [drawings.json]

Checks:
  - title: at most 15 words, no promotional or vague words
  - abstract: at most 150 words (excluding the title line and the "(Figure N)" reference)
  - paragraphs numbered [0001], [0002], ... without gaps
  - no unfilled {{placeholders}}
  - reference numerals (3-digit numbers next to a part name) in the text and in the drawings match
Exit code 1 if any check fails.
"""
import json, re, sys

PROMO = ["premium", "ergonomic", "smart", "innovative", "novel", "improved", "revolutionary", "unique", "best",
         "sleek", "stylish", "advanced", "next-generation", "next generation", "cutting-edge", "world-class",
         "intelligent", "magic", "seamless", "ultimate", "efficient"]


def words(t):
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/]*", t)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = re.sub(r"<!--.*?-->", "", open(sys.argv[1]).read(), flags=re.S)
    problems, notes = [], []

    m = re.search(r"TITLE OF THE INVENTION\**\s*\n\s*\n(.+?)\n", src)
    title = m.group(1).strip() if m else ""
    if not title:
        problems.append("title not found after '1. TITLE OF THE INVENTION'")
    else:
        n = len(words(title))
        (problems if n > 15 else notes).append(f"title has {n} words (limit 15): {title}")
        bad = [w for w in PROMO if re.search(rf"\b{re.escape(w)}\b", title, re.I)]
        if bad:
            problems.append("title contains promotional or vague words: " + ", ".join(bad))

    if "## ABSTRACT" in src:
        ab = src.split("## ABSTRACT", 1)[1].strip().split("\n\n", 1)
        body = ab[1] if len(ab) > 1 else ""
        body = re.sub(r"\(Figure \d+\)\s*$", "", body.strip())
        n = len(words(body))
        (problems if n > 150 else notes).append(f"abstract has {n} words (limit 150)")
        if ab[0].strip() != title:
            problems.append("abstract does not start with the exact title")
    else:
        notes.append("no abstract (optional with a provisional, required with the complete specification)")

    nums = [int(x) for x in re.findall(r"^\[(\d{4})\]", src, re.M)]
    if nums != list(range(1, len(nums) + 1)):
        problems.append("paragraph numbers are not consecutive from [0001]")
    else:
        notes.append(f"{len(nums)} numbered paragraphs")

    left = sorted(set(re.findall(r"\{\{[^}]+\}\}", src)))
    if left:
        problems.append("unfilled placeholders: " + ", ".join(left))

    desc = src.split("## DETAILED DESCRIPTION", 1)[-1].split("## ABSTRACT", 1)[0]
    text_refs = set(re.findall(r"(?<![\d\[/])(?<!\d[,.])\b([1-9]\d{2}[a-z]?)\b(?![\d%]|[,.]\d)", desc))
    if len(sys.argv) > 2:
        spec = json.load(open(sys.argv[2]))
        labels = []
        for f in spec["figures"]:
            for e in f["elements"]:
                labels += e.get("lines", []) + [e.get("text", "")] + e.get("steps", [])
        draw_refs = set(re.findall(r"\b([1-9]\d{2}[a-z]?)\b", " ".join(labels)))
        only_text = sorted(text_refs - draw_refs)
        only_draw = sorted(draw_refs - text_refs)
        if only_draw:
            problems.append("numerals in the drawings but not in the description: " + ", ".join(only_draw))
        if only_text:
            notes.append("numerals in the description but in no drawing (fine if intended): " + ", ".join(only_text))

    for n in notes:
        print("ok      " + n)
    for p in problems:
        print("PROBLEM " + p)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
