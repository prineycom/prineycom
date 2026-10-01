# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown>=3.6"]
# ///
"""Build CV.pdf from README.md: Markdown -> HTML (styles/cv.css) -> headless Chrome PDF.

Run: uv run scripts/build_cv.py
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "README.md"
CSS = ROOT / "styles" / "cv.css"
HTML = ROOT / "build" / "cv.html"
PDF = ROOT / "CV.pdf"

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


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    # The PDF itself does not link to itself.
    text = text.replace(" • [CV.pdf](https://github.com/prineycom/prineycom/raw/main/CV.pdf)", "")
    text = text.replace("](assets/", f"]({(ROOT / 'assets').as_uri()}/")
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    HTML.parent.mkdir(exist_ok=True)
    HTML.write_text(
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>Pavel Donin — CV</title>"
        f"<style>{CSS.read_text(encoding='utf-8')}</style></head>"
        f"<body>{body}</body></html>",
        encoding="utf-8",
    )
    subprocess.run(
        [
            find_chrome(),
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF}",
            HTML.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    print(f"wrote {PDF.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
