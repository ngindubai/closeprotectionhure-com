#!/usr/bin/env python3
"""
rebuild_link_graph.py — Engine 4 (internal link graph rebuild)
Ported from pet-transport pattern, adapted to closeprotectionhire.com.

For a security site the link relationships are:
  city  --downstream--> service (city x service deep pages)
  city  --sibling-----> other cities in same country
  city  --upward------> country hub
  blog  --reference---> cities and services it covers
  service --sideways--> cities where service is offered

This script reports the CURRENT link graph state across all silos so we know
where we are before Phase 3C and the Stage 2J link audit. It does not rewrite
files (the pet-transport rewriting logic depends on a route-based schema
closephire does not have). Use this as the diagnostic for Stage 2J.

Usage:
    python scripts/rebuild_link_graph.py
"""
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(REPO_ROOT, "site", "content")

SILOS = ["cities", "countries", "services", "blog", "event-security", "risk-assessments", "guides"]

LINK_RE = re.compile(r"\[([^\]]+)\]\((/[^\s\)]+)\)")


def walk(silo):
    silo_path = os.path.join(CONTENT_ROOT, silo)
    if not os.path.isdir(silo_path):
        return
    for entry in sorted(os.listdir(silo_path)):
        if entry.endswith(".md") and entry != "_index.md":
            yield os.path.join(silo_path, entry), entry[:-3]


def extract_outgoing_links(filepath):
    with open(filepath, encoding="utf-8") as f:
        text = f.read()
    return [m.group(2) for m in LINK_RE.finditer(text)]


def main():
    print("=" * 72)
    print("closeprotectionhire.com — Engine 4 internal link graph audit")
    print("=" * 72)

    # outgoing[page_slug_full] = list of /target/ paths
    outgoing = {}
    # incoming[target_path] = list of source page slugs
    incoming = defaultdict(list)
    # silo counts
    per_silo = defaultdict(int)

    for silo in SILOS:
        for filepath, slug in walk(silo):
            page_id = f"/{silo}/{slug}/"
            per_silo[silo] += 1
            links = extract_outgoing_links(filepath)
            outgoing[page_id] = links
            for target in links:
                # normalise trailing slash
                if not target.endswith("/") and "." not in target.split("/")[-1]:
                    target = target + "/"
                incoming[target].append(page_id)

    total_pages = sum(per_silo.values())
    total_links = sum(len(v) for v in outgoing.values())

    print(f"\nIndexed {total_pages} content pages across {len([s for s in per_silo if per_silo[s]])} silos")
    print(f"Total outgoing internal links: {total_links}")
    print(f"Average outgoing per page:     {total_links / total_pages:.2f}" if total_pages else "")

    # Pages with too few outgoing links
    print("\n--- Pages with < 2 outgoing internal links ---")
    underlinked = [(p, links) for p, links in outgoing.items() if len(links) < 2]
    if not underlinked:
        print("  none")
    for p, links in sorted(underlinked):
        print(f"  [{len(links)}] {p}")

    # Orphan pages (no incoming links)
    print("\n--- Orphan pages (no incoming internal links) ---")
    orphans = [p for p in outgoing if p not in incoming]
    if not orphans:
        print("  none")
    for p in sorted(orphans):
        print(f"  {p}")

    # Top inbound targets
    print("\n--- Top 15 most-linked-to targets ---")
    by_inbound = sorted(incoming.items(), key=lambda kv: -len(kv[1]))[:15]
    for target, sources in by_inbound:
        print(f"  [{len(sources):3d}] {target}")

    # Per-silo summary
    print("\n--- Per-silo page counts ---")
    for silo in SILOS:
        if per_silo[silo]:
            print(f"  {silo}: {per_silo[silo]}")

    print("\n" + "=" * 72)
    print("Diagnostic complete. Use this output to plan Stage 2J link rebuild.")
    print("=" * 72)

    return 0


if __name__ == "__main__":
    sys.exit(main())
