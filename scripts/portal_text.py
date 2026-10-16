#!/usr/bin/env python3
"""Write the plain-text files to paste into the Form 1 text boxes on the IP India portal.

Usage: python3 portal_text.py form2.md OUTPUT_DIR

Writes portal-description.txt (FIELD to the last numbered paragraph), portal-abstract.txt (title and abstract)
and portal-claims.txt (the "Nil" line for a provisional).
"""
import pathlib, re, sys


def plain(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    return re.sub(r"^#{2,3} (.*)$", lambda m: m.group(1).upper(), t, flags=re.M).strip() + "\n"


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    s = re.sub(r"<!--.*?-->", "", pathlib.Path(sys.argv[1]).read_text(), flags=re.S)
    out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    desc = s[s.index("## FIELD OF THE INVENTION"):s.index("Dated this")].rstrip().rstrip("-").rstrip()
    (out / "portal-description.txt").write_text(plain(desc))
    if "## ABSTRACT" in s:
        (out / "portal-abstract.txt").write_text(plain(s.split("## ABSTRACT", 1)[1]))
    (out / "portal-claims.txt").write_text(
        "Nil. This is a provisional specification; claims will be filed with the complete specification.\n")
    print(f"wrote portal-description.txt, portal-abstract.txt, portal-claims.txt in {out}")


if __name__ == "__main__":
    main()
