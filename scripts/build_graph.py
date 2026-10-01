"""Render data/commit-days.json as a GitHub-style contribution heatmap: assets/contributions.svg.

The GitHub graph of one account misses commits made under the work identity, so the
heatmap is drawn from local git counts across both identities.

Run: python3 scripts/build_graph.py
"""

import json
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "commit-days.json"
OUT = ROOT / "assets" / "contributions.svg"

CELL, GAP, LEFT, TOP = 11, 3, 30, 18
PALETTE = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
THRESHOLDS = [1, 4, 9, 16]  # commits per day for levels 1..4


def level(n: int) -> int:
    return sum(n >= t for t in THRESHOLDS)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    days = data["days"]
    start, end = (date.fromisoformat(d) for d in data["window"])
    first = start - timedelta(days=start.weekday())  # Monday of the first week
    weeks = (end - first).days // 7 + 1
    width = LEFT + weeks * (CELL + GAP)
    height = TOP + 7 * (CELL + GAP) + 16

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif" font-size="9" fill="#57606a">'
    ]
    for row, label in ((0, "Mon"), (2, "Wed"), (4, "Fri")):
        parts.append(f'<text x="0" y="{TOP + row * (CELL + GAP) + CELL - 2}">{label}</text>')

    last_month = None
    total = 0
    d = first
    while d <= end:
        week = (d - first).days // 7
        x = LEFT + week * (CELL + GAP)
        if d.day <= 7 and d.weekday() == 0 and d.month != last_month and d >= start:
            parts.append(f'<text x="{x}" y="{TOP - 6}">{d.strftime("%b")}</text>')
            last_month = d.month
        if d >= start:
            n = days.get(d.isoformat(), 0)
            total += n
            y = TOP + d.weekday() * (CELL + GAP)
            parts.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" fill="{PALETTE[level(n)]}">'
                f"<title>{d.isoformat()}: {n} commits</title></rect>"
            )
        d += timedelta(days=1)

    legend_y = TOP + 7 * (CELL + GAP) + 10
    parts.append(f'<text x="{LEFT}" y="{legend_y}">{total:,} commits, {start:%b %Y} — {end:%b %Y}</text>')
    lx = width - 5 * (CELL + GAP) - 60
    parts.append(f'<text x="{lx}" y="{legend_y}">Less</text>')
    for i, color in enumerate(PALETTE):
        parts.append(
            f'<rect x="{lx + 26 + i * (CELL + GAP)}" y="{legend_y - 9}" width="{CELL}" height="{CELL}" rx="2" fill="{color}"/>'
        )
    parts.append(f'<text x="{lx + 30 + 5 * (CELL + GAP)}" y="{legend_y}">More</text>')
    parts.append("</svg>")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {total} commits")


if __name__ == "__main__":
    main()
