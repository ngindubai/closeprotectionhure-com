#!/usr/bin/env python3
"""
check_titles.py — Engine 5 (QA quality gate)
Ported from pet-transport pattern.

Checks all page titles for:
- Length over 70 chars (display truncation in SERPs)
- Duplicate titles across the site (cannibalisation risk)
- Missing titles (front-matter incomplete)

Reads site/content/**/*.md and reports per-silo.

Usage:
    python scripts/check_titles.py
"""
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(REPO_ROOT, "site", "content")
TITLE_MAX = 70

SILOS = ["cities", "countries", "services", "blog", "event-security", "risk-assessments", "guides"]


def extract_title_pair(filepath):
    """Return (title, seo_title) from front matter."""
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return ("", "")
    fm = m.group(1)
    title = ""
    seo_title = ""
    for line in fm.splitlines():
        if line.startswith("title:"):
            title = line.split(":", 1)[1].strip().strip('"').strip("'")
        elif line.startswith("seo_title:"):
            seo_title = line.split(":", 1)[1].strip().strip('"').strip("'")
    return title, seo_title


def main():
    print("=" * 72)
    print("closeprotectionhire.com — Title length + uniqueness check")
    print("=" * 72)

    long_titles = []
    missing_titles = []
    title_to_files = defaultdict(list)

    for silo in SILOS:
        silo_path = os.path.join(CONTENT_ROOT, silo)
        if not os.path.isdir(silo_path):
            continue
        for entry in sorted(os.listdir(silo_path)):
            if not entry.endswith(".md") or entry == "_index.md":
                continue
            filepath = os.path.join(silo_path, entry)
            title, seo_title = extract_title_pair(filepath)
            effective = seo_title or title
            rel = os.path.relpath(filepath, REPO_ROOT)

            if not effective:
                missing_titles.append(rel)
                continue
            if len(effective) > TITLE_MAX:
                long_titles.append((rel, effective, len(effective)))
            title_to_files[effective.lower()].append(rel)

    print("\n--- Titles over %d chars ---" % TITLE_MAX)
    if not long_titles:
        print("  none")
    for path, title, n in long_titles:
        print(f"  [{n}] {path}")
        print(f"       {title}")

    print("\n--- Missing titles ---")
    if not missing_titles:
        print("  none")
    for path in missing_titles:
        print(f"  {path}")

    print("\n--- Duplicate titles (cannibalisation risk) ---")
    dupes = {t: paths for t, paths in title_to_files.items() if len(paths) > 1}
    if not dupes:
        print("  none")
    for title, paths in sorted(dupes.items()):
        print(f"  {title}")
        for p in paths:
            print(f"    — {p}")

    n_long = len(long_titles)
    n_missing = len(missing_titles)
    n_dupes = len(dupes)
    print("\n" + "=" * 72)
    print(f"  Long titles:      {n_long}")
    print(f"  Missing titles:   {n_missing}")
    print(f"  Duplicate titles: {n_dupes}")
    print("=" * 72)

    return 1 if (n_missing or n_dupes) else 0


if __name__ == "__main__":
    sys.exit(main())
