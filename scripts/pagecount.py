#!/usr/bin/env python3
"""Page counts to enter on Form 1, from the specification and drawings PDFs.

Usage: python3 pagecount.py SPECIFICATION.pdf [DRAWINGS.pdf]

Assumes the abstract is the last page of the specification PDF (as spec_to_pdf.py lays it out)
and that a provisional has no claims.
"""
import sys
from chrome import count_pages


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    spec = count_pages(sys.argv[1])
    draw = count_pages(sys.argv[2]) if len(sys.argv) > 2 else 0
    print(f"Description, no. of pages:  {spec - 1}")
    print("Claims, no. of pages:       0")
    print("Claims, no. of claims:      0")
    print("Abstract, no. of pages:     1")
    print(f"Drawings, no. of pages:     {draw}")
    print(f"Drawings, no. of drawings:  {draw}  (one figure per sheet)")
    print(f"Total pages for the fee:    {spec + draw}  (the base fee covers 30; verify on ipindia.gov.in)")


if __name__ == "__main__":
    main()
