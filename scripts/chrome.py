"""Find a local Chrome or Chromium and print an HTML file to PDF with it."""
import os, pathlib, shutil, subprocess, sys

CANDIDATES = [
    os.environ.get("CHROME_PATH", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
NAMES = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"]


def find_chrome():
    for c in CANDIDATES:
        if c and pathlib.Path(c).exists():
            return c
    for n in NAMES:
        p = shutil.which(n)
        if p:
            return p
    sys.exit("Chrome or Chromium not found. Install it, or set CHROME_PATH to its executable.")


def print_pdf(chrome, html_path, pdf_path):
    cmd = [chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           f"--print-to-pdf={pathlib.Path(pdf_path).resolve()}", pathlib.Path(html_path).resolve().as_uri()]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if not pathlib.Path(pdf_path).exists():
        sys.exit("Chrome did not produce a PDF:\n" + r.stderr[-2000:])


def count_pages(pdf_path):
    """Page count without extra tools: count page objects in the PDF."""
    import re
    data = pathlib.Path(pdf_path).read_bytes()
    return len(re.findall(rb"/Type\s*/Page[^s]", data))
