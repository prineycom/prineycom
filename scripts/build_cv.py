# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown>=3.6"]
# ///
"""Build CV.pdf from README.md and CV_RU.pdf from README.ru.md: Markdown -> HTML (styles/cv.css) -> headless Chrome PDF.

Run: uv run scripts/build_cv.py
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
BUILDS = [("README.md", "CV.pdf", "en"), ("README.ru.md", "CV_RU.pdf", "ru")]
CSS = ROOT / "styles" / "cv.css"

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome",
    "chromium",
    "chromium-browser",
]


def find_chrome() -> str:
    for c in CHROME_CANDIDATES:
        if c and (Path(c).exists() or shutil.which(c)):
            return c
    sys.exit("Chrome not found; set CHROME=/path/to/chrome")


def build(src: str, out: str, lang: str) -> None:
    text = (ROOT / src).read_text(encoding="utf-8")
    # The PDFs do not link to themselves.
    text = re.sub(r" • \[CV\.pdf\]\([^)]*\)( · \[CV_RU\.pdf\]\([^)]*\))?", "", text)
    text = text.replace("](assets/", f"]({(ROOT / 'assets').as_uri()}/")
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    html = ROOT / "build" / f"{Path(out).stem}.html"
    html.parent.mkdir(exist_ok=True)
    html.write_text(
        f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'>"
        "<title>Pavel Donin — CV</title>"
        f"<style>{CSS.read_text(encoding='utf-8')}</style></head>"
        f"<body>{body}</body></html>",
        encoding="utf-8",
    )
    subprocess.run(
        [find_chrome(), "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={ROOT / out}", html.as_uri()],
        check=True,
        capture_output=True,
    )
    print(f"wrote {out}")


def main() -> None:
    for src, out, lang in BUILDS:
        build(src, out, lang)


if __name__ == "__main__":
    main()
