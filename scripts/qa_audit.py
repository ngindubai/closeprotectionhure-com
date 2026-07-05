#!/usr/bin/env python3
"""
qa_audit.py — Engine 5 (QA + SEO quality gate)
Ported from pet-transport pattern, adapted for closeprotectionhire.com.

Checks all content files in site/content/ for:
- YMYL compliance (no safety guarantees in a security context)
- Banned AI-tell vocabulary
- Banned phrases
- Em dashes (must use periods/commas/colons instead)
- Required front-matter fields
- FAQ count floor
- Internal-link count floor (2+ per page)
- Title length
- Description length

Usage:
    python scripts/qa_audit.py

Exit code 0 on pass, non-zero on errors found.
"""
import os
import re
import sys
from collections import defaultdict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT_ROOT = os.path.join(REPO_ROOT, "site", "content")

# Silos to walk
SILOS = [
    "cities",
    "countries",
    "services",
    "blog",
    "event-security",
    "risk-assessments",
    "guides",
    "bodyguard-hire",
    "executive-protection",
    "close-protection-officers",
    "security-drivers",
    "residential-security",
    "secure-airport-transfers",
]

# Banned AI-tell vocabulary (universal across pet-transport and security domains)
BANNED_WORDS = {
    "delve", "tapestry", "vibrant", "crucial", "meticulous",
    "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy",
    "transformative", "paramount", "multifaceted", "myriad", "cornerstone",
    "reimagine", "empower", "catalyst", "invaluable", "bustling", "nestled", "realm",
    "furthermore", "moreover", "paradigm", "holistic", "utilize", "facilitate",
    "nuanced", "illuminate", "encompasses", "catalyze", "proactive",
    "ubiquitous", "quintessential", "plethora",
}

# YMYL safety-guarantee patterns specific to the security industry
SAFETY_GUARANTEE_PATTERNS = [
    r"guarantee[ds]?\s+(safety|protection|safe)",
    r"100%\s+safe",
    r"completely\s+safe",
    r"absolutely\s+safe",
    r"guaranteed\s+protection",
    r"ensure[ds]?\s+(safety|your\s+safety)",
    r"risk[- ]free",
    r"eliminate[ds]?\s+(all\s+)?risk",
    r"will\s+keep\s+you\s+safe",
    r"will\s+protect\s+you\s+from",
    r"foolproof",
    r"bulletproof\s+security",  # metaphor abuse
]

BANNED_PHRASES = [
    "in today's digital age",
    "it is worth noting",
    "it is important to note",
    "plays a crucial role",
    "plays a vital role",
    "serves as a testament",
    "a testament to",
    "in the realm of",
    "harness the power of",
    "embark on a journey",
    "without further ado",
    "ever-changing landscape",
    "ever-evolving",
    "in this day and age",
    "in today's fast-paced world",
    "when it comes to",
    "navigate the complexities",
    "at the end of the day",
    "rest assured",
    "look no further",
    "dive into",
    "cutting-edge",
    "game-changer",
    "in conclusion",
    "whether you are a",
]

# Required YAML front-matter fields (varies by silo, checked per-page)
REQUIRED_FIELDS_ALL = ["title", "description"]
REQUIRED_FIELDS_BY_SILO = {
    "cities": ["title", "description", "country"],
    "blog": ["title", "description", "author", "slug"],
    "event-security": ["title", "description"],
    "countries": ["title", "description"],
    "services": ["title", "description"],
    "risk-assessments": ["title", "description"],
}

# Length limits
TITLE_MAX = 70
DESC_MIN = 120
DESC_MAX = 175

# Floors
FAQ_MIN_BLOG = 5
FAQ_MIN_CITY = 4
INTERNAL_LINK_MIN = 2


# Negation tokens that, when they immediately precede a safety phrase, flip it from
# a banned guarantee into a legitimate disclaimer (e.g. "does not eliminate risk",
# "not risk-free"). These must NOT trip the YMYL gate.
NEGATION_RE = re.compile(
    r"(?:\bnot\b|\bnever\b|\bcannot\b|\bcan't\b|\bwon't\b|\bno\b|\bwithout\b|"
    r"\bdoes\s+not\b|\bdo\s+not\b|\bdoesn't\b|\bdon't\b|\bisn't\b|n't)\s*$"
)


def parse_front_matter(text):
    """Extract YAML front matter as a dict (shallow, regex-based; good enough for QA)."""
    fm = {}
    # Tolerate a leading UTF-8 BOM so a stray byte-order mark before '---' does not
    # silently blank the front matter (real incident: bangalore/delhi/lima).
    text = text.lstrip("﻿")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return fm, text
    fm_text = m.group(1)
    body = text[m.end():]
    for line in fm_text.splitlines():
        if ":" not in line or line.startswith((" ", "-", "\t")):
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def count_faqs(text):
    """Count FAQ entries in front matter (rough — counts '- question:' occurrences)."""
    return len(re.findall(r"^\s*-\s*question\s*:", text, re.MULTILINE))


def count_internal_links(body):
    """Count internal markdown links (starting with /)."""
    return len(re.findall(r"\]\(/[^)]+\)", body))


def check_text_issues(text):
    """Return list of (severity, message) tuples for content violations."""
    issues = []
    text_lower = text.lower()

    for word in BANNED_WORDS:
        if re.search(r"\b" + re.escape(word) + r"\b", text_lower):
            issues.append(("ERROR", f"Banned word: '{word}'"))

    if "\u2014" in text:
        issues.append(("ERROR", "Em dash found (\u2014). Replace with comma, full stop, or colon."))
    if "\u2013" in text:
        issues.append(("WARNING", "En dash found (\u2013)."))

    for pattern in SAFETY_GUARANTEE_PATTERNS:
        for m in re.finditer(pattern, text_lower):
            # Skip negated/disclaimer forms ("does not eliminate risk", "not risk-free").
            preceding = text_lower[max(0, m.start() - 30):m.start()]
            if NEGATION_RE.search(preceding):
                continue
            issues.append(("ERROR", f"YMYL safety-guarantee pattern: '{pattern}'"))
            break

    for phrase in BANNED_PHRASES:
        if phrase in text_lower:
            issues.append(("ERROR", f"Banned phrase: '{phrase}'"))

    return issues


def audit_file(filepath, silo):
    """Audit one Hugo content file. Returns list of (severity, message)."""
    issues = []
    if not os.path.exists(filepath):
        return [("ERROR", "File missing")]

    with open(filepath, encoding="utf-8") as f:
        text = f.read()

    fm, body = parse_front_matter(text)

    # Required front matter
    required = REQUIRED_FIELDS_BY_SILO.get(silo, REQUIRED_FIELDS_ALL)
    for field in required:
        if not fm.get(field):
            issues.append(("ERROR", f"Missing front-matter field: {field}"))

    # Title length
    title = fm.get("title", "")
    seo_title = fm.get("seo_title", "")
    title_to_check = seo_title or title
    if title_to_check and len(title_to_check) > TITLE_MAX:
        issues.append(("WARNING", f"Title too long ({len(title_to_check)} chars; max {TITLE_MAX})"))

    # Description length
    desc = fm.get("description", "")
    if desc:
        if len(desc) < DESC_MIN:
            issues.append(("WARNING", f"Description short ({len(desc)} chars; min {DESC_MIN})"))
        if len(desc) > DESC_MAX:
            issues.append(("WARNING", f"Description long ({len(desc)} chars; max {DESC_MAX})"))

    # FAQ floor
    faq_count = count_faqs(text)
    if silo == "blog" and faq_count < FAQ_MIN_BLOG:
        issues.append(("WARNING", f"Only {faq_count} FAQs (blog min {FAQ_MIN_BLOG})"))
    elif silo == "cities" and faq_count < FAQ_MIN_CITY:
        issues.append(("WARNING", f"Only {faq_count} FAQs (cities min {FAQ_MIN_CITY})"))

    # Internal link floor
    link_count = count_internal_links(body)
    if link_count < INTERNAL_LINK_MIN:
        issues.append(("WARNING", f"Only {link_count} internal links (min {INTERNAL_LINK_MIN})"))

    # Text content checks (body + FAQ answers)
    issues.extend(check_text_issues(text))

    return issues


def walk_silo(silo):
    """Yield (filepath, slug) for every .md file in a silo (excluding _index.md)."""
    silo_path = os.path.join(CONTENT_ROOT, silo)
    if not os.path.isdir(silo_path):
        return
    for entry in sorted(os.listdir(silo_path)):
        if entry.endswith(".md") and entry != "_index.md":
            yield os.path.join(silo_path, entry), entry[:-3]


def main():
    print("=" * 72)
    print("closeprotectionhire.com — Engine 5 QA + SEO Quality Gate")
    print("=" * 72)

    totals = {"pages": 0, "pass": 0, "warn": 0, "fail": 0, "errors": 0, "warnings": 0}

    for silo in SILOS:
        silo_path = os.path.join(CONTENT_ROOT, silo)
        if not os.path.isdir(silo_path):
            print(f"\nSKIP silo {silo}: directory not found")
            continue

        print(f"\n--- {silo.upper()} ---")
        silo_pages = 0
        silo_errors = 0
        silo_warnings = 0

        for filepath, slug in walk_silo(silo):
            silo_pages += 1
            totals["pages"] += 1
            issues = audit_file(filepath, silo)

            errors = [i for i in issues if i[0] == "ERROR"]
            warnings = [i for i in issues if i[0] == "WARNING"]

            silo_errors += len(errors)
            silo_warnings += len(warnings)
            totals["errors"] += len(errors)
            totals["warnings"] += len(warnings)

            if errors:
                status = "FAIL"
                totals["fail"] += 1
            elif warnings:
                status = "WARN"
                totals["warn"] += 1
            else:
                status = "PASS"
                totals["pass"] += 1

            if issues:
                print(f"  [{status}] {slug}")
                for severity, msg in issues:
                    print(f"    {severity}: {msg}")
            else:
                print(f"  [PASS] {slug}")

        print(f"  silo total: {silo_pages} pages, {silo_errors} errors, {silo_warnings} warnings")

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Total pages audited:  {totals['pages']}")
    print(f"  Pass:                 {totals['pass']}")
    print(f"  Warn:                 {totals['warn']}")
    print(f"  Fail (with errors):   {totals['fail']}")
    print(f"  Total errors:         {totals['errors']}")
    print(f"  Total warnings:       {totals['warnings']}")

    if totals["errors"] == 0:
        print("\n  VERDICT: PASS — no blocking errors. Warnings are advisory.")
        return 0
    print(f"\n  VERDICT: FAIL — {totals['errors']} errors must be resolved before ship.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
