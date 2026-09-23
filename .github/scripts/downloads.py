#!/usr/bin/env python3
"""Record how many times each release has been downloaded, and draw it.

GitHub counts downloads but keeps no history: the API returns how many times
an asset has been fetched *so far*, and nothing about when. There is no
endpoint, no export and no backfill — a chart of the past can only be built
by someone who started writing the numbers down. This is that someone.

Run daily. Appends one row to docs/downloads.csv and redraws
assets/downloads.svg from the whole file.

Two things the numbers do that a reader would otherwise call a bug:

  * **The total can go down.** A count belongs to an asset, not a release, so
    replacing a release's files — which happened to v0.2.1 — takes their
    downloads with them. The file records what GitHub said on the day; it is
    a log, not a ledger.
  * **Source archives are not counted.** GitHub's own "Source code (zip)"
    links have no counter, so a chart drawn from this is downloads of the
    binaries we published, which is the number worth having anyway.

Standard library only, on purpose: this runs unattended for years, and every
dependency is something that can break while nobody is looking.
"""

import csv
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone

REPO = os.environ.get("DOWNLOADS_REPO", "cubepy/CubePilot")
CSV_PATH = os.environ.get("DOWNLOADS_CSV", "docs/downloads.csv")
SVG_PATH = os.environ.get("DOWNLOADS_SVG", "assets/downloads.svg")

FIELDS = ["date", "total", "android", "windows", "releases"]


def fetch_releases():
    """Every release and its assets, following pagination."""
    releases = []
    page = 1
    token = os.environ.get("GITHUB_TOKEN")
    while True:
        url = (f"https://api.github.com/repos/{REPO}/releases"
               f"?per_page=100&page={page}")
        headers = {
            "User-Agent": "cubepilot-downloads",
            "Accept": "application/vnd.github+json",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=60) as response:
            batch = json.load(response)
        if not batch:
            break
        releases.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return releases


def tally(releases):
    """Totals, split by what a reader would actually ask for."""
    total = android = windows = 0
    for release in releases:
        for asset in release.get("assets", []):
            count = asset.get("download_count", 0)
            name = asset.get("name", "").lower()
            total += count
            if name.endswith(".apk"):
                android += count
            elif "windows" in name:
                windows += count
    return {
        "total": total,
        "android": android,
        "windows": windows,
        "releases": len(releases),
    }


def read_rows(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row.get("date")]


def write_rows(path, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def upsert(rows, today, counts):
    """One row per day, whatever happens.

    A workflow can be re-run by hand, and a cron can fire twice across a
    daylight-saving boundary. Appending regardless would put two points on
    the same date and draw a vertical line through the chart.
    """
    row = {"date": today, **{k: str(counts[k]) for k in FIELDS[1:]}}
    for i, existing in enumerate(rows):
        if existing["date"] == today:
            rows[i] = row
            return rows, "updated"
    rows.append(row)
    rows.sort(key=lambda r: r["date"])
    return rows, "added"


# --------------------------------------------------------------------- chart

W, H = 760, 270
# The top padding holds the legend and the bottom holds the dates. They used
# to share the bottom, where the legend's first entry was drawn straight over
# the start date and the two were unreadable on top of each other.
PAD_L, PAD_R, PAD_T, PAD_B = 46, 14, 36, 26

# Colours that read on GitHub's light and dark themes alike. No background is
# painted: a chart with a white panel is a white rectangle on a dark page.
INK = "#8b93a7"
GRID = "#8b93a7"
TOTAL = "#3767E9"
ANDROID = "#22D3EE"
WINDOWS = "#7F50EE"


def esc(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def render(rows, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    if len(rows) < 2:
        # One point is not a line. Saying so beats drawing an empty box and
        # leaving the reader to wonder what broke.
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="90" '
            f'viewBox="0 0 {W} 90" role="img" '
            f'aria-label="Not enough data yet">'
            f'<text x="{W // 2}" y="50" text-anchor="middle" '
            f'font-family="system-ui,sans-serif" font-size="13" fill="{INK}">'
            f'Collecting — a chart needs more than one day of numbers.'
            f'</text></svg>\n'
        )
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(svg)
        return

    series = {
        "total": [int(r["total"]) for r in rows],
        "android": [int(r["android"]) for r in rows],
        "windows": [int(r["windows"]) for r in rows],
    }
    peak = max(max(values) for values in series.values())
    # Never divide by zero, and never draw a line pinned to the axis.
    top = max(peak, 1)
    # A round ceiling, so the gridline labels are numbers a person would say.
    step = 1
    while top / step > 4:
        step *= 2 if str(step)[0] in "125" else 5
    top = step * ((top + step - 1) // step)

    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B

    def x_at(i):
        return PAD_L + (plot_w * i / (len(rows) - 1))

    def y_at(value):
        return PAD_T + plot_h - (plot_h * value / top)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="CubePilot downloads over time. '
        f'Latest total {series["total"][-1]}.">',
        '<style>text{font-family:system-ui,-apple-system,Segoe UI,sans-serif}'
        '</style>',
    ]

    # Horizontal gridlines with their values.
    lines = 4
    for i in range(lines + 1):
        value = top * i / lines
        y = y_at(value)
        parts.append(
            f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W - PAD_R}" y2="{y:.1f}" '
            f'stroke="{GRID}" stroke-opacity="0.18" stroke-width="1"/>')
        parts.append(
            f'<text x="{PAD_L - 8}" y="{y + 4:.1f}" text-anchor="end" '
            f'font-size="11" fill="{INK}" fill-opacity="0.75">'
            f'{int(round(value))}</text>')

    for key, colour, width in (("android", ANDROID, 1.8),
                               ("windows", WINDOWS, 1.8),
                               ("total", TOTAL, 2.6)):
        points = " ".join(
            f"{x_at(i):.1f},{y_at(v):.1f}" for i, v in enumerate(series[key]))
        parts.append(
            f'<polyline points="{points}" fill="none" stroke="{colour}" '
            f'stroke-width="{width}" stroke-linejoin="round" '
            f'stroke-linecap="round"/>')

    # The last value, labelled, because it is the one anyone looks for.
    last_y = y_at(series["total"][-1])
    parts.append(
        f'<circle cx="{x_at(len(rows) - 1):.1f}" cy="{last_y:.1f}" r="3.5" '
        f'fill="{TOTAL}"/>')

    # First and last dates only, on their own line. Every date turns the
    # axis into a smear.
    parts.append(
        f'<text x="{PAD_L}" y="{H - 8}" font-size="11" fill="{INK}" '
        f'fill-opacity="0.75">{esc(rows[0]["date"])}</text>')
    parts.append(
        f'<text x="{W - PAD_R}" y="{H - 8}" text-anchor="end" '
        f'font-size="11" fill="{INK}" fill-opacity="0.75">'
        f'{esc(rows[-1]["date"])}</text>')

    # Legend along the top, with the current numbers in it so the chart is
    # readable as a still image rather than needing the axis decoded.
    legend = [
        ("Total", TOTAL, series["total"][-1]),
        ("Android", ANDROID, series["android"][-1]),
        ("Windows", WINDOWS, series["windows"][-1]),
    ]
    x = PAD_L
    for label, colour, value in legend:
        parts.append(
            f'<rect x="{x}" y="14" width="10" height="3" rx="1.5" '
            f'fill="{colour}"/>')
        parts.append(
            f'<text x="{x + 15}" y="20" font-size="11" fill="{INK}">'
            f'{label} {value}</text>')
        # Advanced by the text's own width rather than a fixed step, or a
        # four-digit total runs the next entry over.
        x += 26 + 6.6 * (len(label) + 1 + len(str(value)))

    parts.append("</svg>")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(parts) + "\n")


def main():
    try:
        releases = fetch_releases()
    except (urllib.error.URLError, TimeoutError) as error:
        # A failed run must not commit anything, and must not look like a
        # day of zero downloads.
        print(f"::error::could not read releases: {error}")
        return 1

    counts = tally(releases)
    today = datetime.now(timezone.utc).date().isoformat()
    rows = read_rows(CSV_PATH)
    rows, what = upsert(rows, today, counts)
    write_rows(CSV_PATH, rows)
    render(rows, SVG_PATH)

    print(f"{what} {today}: total={counts['total']} "
          f"android={counts['android']} windows={counts['windows']} "
          f"over {counts['releases']} releases ({len(rows)} days recorded)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
