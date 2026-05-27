#!/usr/bin/env python3
"""
generate_blog_batch1.py
Stage 2K Batch 1 — Blog articles 1-5.

Worforce pipeline applied (per CLAUDE.md):
  The Wordsmith (voice: senior security consultant) ->
  The Interrogator (FAQ generation) ->
  The Chameleon (humaniser pass: no em dashes, no banned vocab, high burstiness) ->
  The Optimiser (SEO metadata, FAQ schema) ->
  The Auditor (QA gate: no safety guarantees, YMYL compliance, sourced facts)

All articles:
  - British English
  - YAML front matter (--- delimiters)
  - FAQPage schema via faq-accordion.html partial
  - 2+ internal links per article
  - No em dashes
  - No safety guarantees ("reduces risk" / "trained professionals" only)
  - Named author personas (not corporate voice — E-E-A-T signal)
  - Source attribution on all factual claims
"""

import os

BLOG_DIR = os.path.join("site", "content", "blog")

ARTICLES = [
    {
        "slug": "how-to-vet-a-close-protection-company",
        "title": "How to Vet a Close Protection Company: A Corporate Buyer's Checklist",
        "description": "What to ask before hiring a close protection company. Licensing, vetting standards, insurance, and the red flags that separate credible operators from marketing exercises.",
        "date": "2026-05-27",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["executive-protection", "vetting", "corporate-security"],
        "internal_links": ["/services/executive-protection/", "/about/"],
    },
    {
        "slug": "executive-protection-cost-factors",
        "title": "Executive Protection Cost Factors: What Determines the Day Rate?",
        "description": "Why EP costs vary so widely, and what actually drives the price. Threat level, location, team size, armoured vehicles, and advance work.",
        "date": "2026-05-27",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["executive-protection", "cost", "planning"],
        "internal_links": ["/services/executive-protection/", "/services/bodyguard-hire/"],
    },
    {
        "slug": "bodyguard-licence-uae",
        "title": "Do Bodyguards Need a Licence in the UAE? SIRA Rules Explained",
        "description": "Private security licensing in the UAE. What SIRA certification means, which bodyguards can legally operate in Dubai and Abu Dhabi.",
        "date": "2026-05-27",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["uae", "dubai", "regulations", "licensing"],
        "internal_links": ["/cities/dubai/", "/countries/united-arab-emirates/"],
    },
    {
        "slug": "secure-airport-transfer-dubai",
        "title": "Secure Airport Transfer Dubai: What to Expect and How to Book",
        "description": "What a professional secure airport transfer in Dubai involves, how it differs from a standard taxi, and what to look for when booking.",
        "date": "2026-05-27",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["dubai", "security-drivers", "airport"],
        "internal_links": ["/cities/dubai/", "/services/security-drivers/"],
    },
    {
        "slug": "is-nairobi-safe-for-business-travel",
        "title": "Is Nairobi Safe for Business Travel? A Security Consultant's Assessment",
        "description": "Nairobi's security environment for corporate travellers. Crime data, terrorism risk, safe districts, airport transfer risks, and a realistic security plan.",
        "date": "2026-05-27",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["nairobi", "kenya", "risk-assessment", "africa"],
        "internal_links": ["/cities/nairobi/", "/risk-assessments/"],
    },
]


def slug_exists(slug: str) -> bool:
    return os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md"))


def write_article(article: dict) -> bool:
    slug = article["slug"]
    if slug_exists(slug):
        print(f"  SKIP (exists): {slug}.md")
        return False

    print(f"  WOULD WRITE: {slug}.md")
    print(f"    Title: {article['title']}")
    print(f"    Author: {article['author']}")
    print(f"    Internal links: {', '.join(article['internal_links'])}")
    return True


if __name__ == "__main__":
    print("Blog Batch 1 — Article inventory:")
    print(f"Articles defined: {len(ARTICLES)}")
    print()
    for article in ARTICLES:
        write_article(article)
    print()
    print("Content files committed directly via GitHub MCP in this batch.")
    print("To add Batch 2, copy this script as generate_blog_batch2.py and define new ARTICLES.")
    print()
    print("Workforce loop for each batch:")
    print("  1. The Wordsmith  — authority voice, British English, sourced facts")
    print("  2. The Interrogator — FAQs, city/service-specific, no safety guarantees")
    print("  3. The Chameleon  — humaniser: no em dashes, no banned vocab, high burstiness")
    print("  4. The Optimiser  — SEO metadata, FAQ schema, internal links")
    print("  5. The Auditor    — QA gate: YMYL compliance, legal accuracy, no safety guarantees")
