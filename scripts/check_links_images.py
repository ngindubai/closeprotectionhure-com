#!/usr/bin/env python3
"""
Engine 5 link/image integrity gate.

Catches the two failure modes that produced Semrush 4xx errors and broken
internal images in July 2026:

  1. Internal markdown/HTML links that point to a URL no content page builds
     (the "dead-link incident").
  2. hero_image / og_image front-matter values that name a file which does
     not exist in site/static/images (the broken-hero-image incident).

Both are existence checks, not style checks. Run from the repo root:

    python3 scripts/check_links_images.py

Exit status is non-zero if any broken link or image is found, so it can be
wired into the QA gate alongside qa_audit.py.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "site", "content")
IMAGES = os.path.join(ROOT, "site", "static", "images")
STATIC = os.path.join(ROOT, "site", "static")

# Internal link prefixes that are static assets or known non-page files.
# Links beginning with these are not expected to resolve to a content page.
STATIC_PREFIXES = ("/images/", "/css/", "/js/", "/fonts/", "/api/")
STATIC_FILES = {"/sitemap.xml", "/llms.txt", "/robots.txt", "/favicon.ico"}

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.DOTALL)
MD_LINK_RE = re.compile(r"\]\((/[^)\s]*)\)")
HREF_RE = re.compile(r'href=["\'](/[^"\']*)["\']')
SLUG_RE = re.compile(r'^slug:\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)
IMG_FIELD_RE = re.compile(r'^(hero_image|og_image):\s*"?([^"\n]+?)"?\s*$', re.MULTILINE)


def split_front_matter(text):
    m = FRONT_MATTER_RE.match(text)
    if m:
        return m.group(1), m.group(2)
    return "", text


def url_for(path):
    """Compute the built URL for a content .md file."""
    rel = os.path.relpath(path, CONTENT)
    parts = rel.split(os.sep)
    name = parts[-1]
    directory = parts[:-1]
    with open(path, encoding="utf-8") as fh:
        fm, _ = split_front_matter(fh.read())
    if name == "_index.md":
        if not directory:
            return "/"
        return "/" + "/".join(directory) + "/"
    slug_m = SLUG_RE.search(fm)
    slug = slug_m.group(1).strip() if slug_m else name[:-3]
    return "/" + "/".join(directory + [slug]) + "/"


def normalise(link):
    link = link.split("#", 1)[0].split("?", 1)[0]
    if not link:
        return ""
    if not link.endswith("/") and "." not in link.rsplit("/", 1)[-1]:
        link += "/"
    return link


def main():
    md_files = []
    for dirpath, _dirs, files in os.walk(CONTENT):
        for f in files:
            if f.endswith(".md"):
                md_files.append(os.path.join(dirpath, f))

    valid_urls = {"/"}
    for path in md_files:
        valid_urls.add(url_for(path))

    link_errors = []
    image_errors = []

    for path in sorted(md_files):
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        fm, body = split_front_matter(text)

        # hero_image / og_image existence
        for field, value in IMG_FIELD_RE.findall(fm):
            value = value.strip()
            if not value:
                continue
            if not os.path.isfile(os.path.join(IMAGES, value)):
                image_errors.append((rel, field, value))

        # internal link existence
        links = set(MD_LINK_RE.findall(body)) | set(HREF_RE.findall(body))
        for raw in links:
            if raw.startswith(STATIC_PREFIXES):
                continue
            norm = normalise(raw)
            if not norm or norm in STATIC_FILES:
                continue
            # allow links to real static files
            if "." in norm.rsplit("/", 1)[-1]:
                if os.path.isfile(os.path.join(STATIC, norm.lstrip("/"))):
                    continue
            if norm not in valid_urls:
                link_errors.append((rel, raw))

    if image_errors:
        print(f"\nBROKEN IMAGES ({len(image_errors)}):")
        for rel, field, value in image_errors:
            print(f"  {rel}: {field} -> {value} (missing in static/images/)")

    if link_errors:
        print(f"\nBROKEN INTERNAL LINKS ({len(link_errors)}):")
        for rel, raw in link_errors:
            print(f"  {rel}: {raw}")

    total = len(image_errors) + len(link_errors)
    if total == 0:
        print(f"OK: {len(md_files)} pages checked, no broken internal links or images.")
        return 0
    print(f"\nFAIL: {total} issue(s) across {len(md_files)} pages.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
