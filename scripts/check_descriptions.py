#!/usr/bin/env python3
"""
check_descriptions.py — Engine 5 (QA quality gate)
Ported from pet-transport pattern.

Checks all meta descriptions for length floor and ceiling.
Google truncates around 155-170 chars; under 120 leaves CTR on the table.

Usage:
    python scripts/check_descriptions.py
"""
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(REPO_ROOT, "site", "content")

DESC_MIN = 120
DESC_MAX = 175

SILOS = ["cities", "countries", "services", "blog", "event-security", "risk-assessments", "guides"]


def extract_description(filepath):
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return ""
    fm = m.group(1)
    for line in fm.splitlines():
        if line.startswith("description:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def main():
    print("=" * 72)
    print("closeprotectionhire.com — Description length check")
    print("=" * 72)
    print(f"  Floor: {DESC_MIN} chars, ceiling: {DESC_MAX} chars")
    print()

    too_short = []
    too_long = []
    missing = []
    n_total = 0

    for silo in SILOS:
        silo_path = os.path.join(CONTENT_ROOT, silo)
        if not os.path.isdir(silo_path):
            continue
        for entry in sorted(os.listdir(silo_path)):
            if not entry.endswith(".md") or entry == "_index.md":
                continue
            filepath = os.path.join(silo_path, entry)
            rel = os.path.relpath(filepath, REPO_ROOT)
            desc = extract_description(filepath)
            n_total += 1
            if not desc:
                missing.append(rel)
            elif len(desc) < DESC_MIN:
                too_short.append((rel, len(desc), desc))
            elif len(desc) > DESC_MAX:
                too_long.append((rel, len(desc), desc))

    print(f"--- Descriptions below {DESC_MIN} chars ---")
    if not too_short:
        print("  none")
    for path, n, desc in too_short:
        print(f"  [{n}] {path}")

    print(f"\n--- Descriptions above {DESC_MAX} chars ---")
    if not too_long:
        print("  none")
    for path, n, desc in too_long:
        print(f"  [{n}] {path}")

    print("\n--- Missing descriptions ---")
    if not missing:
        print("  none")
    for path in missing:
        print(f"  {path}")

    print("\n" + "=" * 72)
    print(f"  Total pages: {n_total}")
    print(f"  Too short:   {len(too_short)}")
    print(f"  Too long:    {len(too_long)}")
    print(f"  Missing:     {len(missing)}")
    print("=" * 72)
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
