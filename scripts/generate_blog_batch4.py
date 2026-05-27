#!/usr/bin/env python3
"""
generate_blog_batch4.py
Stage 2K Batch 4 -- Blog articles 16-20.

Workforce pipeline: Wordsmith -> Interrogator -> Chameleon -> Optimiser -> Auditor
All: British English, no em dashes, no safety guarantees, 6 FAQs, 2+ internal links.
"""

import os

BLOG_DIR = os.path.join("site", "content", "blog")

ARTICLES = [
    {
        "slug": "sia-close-protection-licence-explained",
        "title": "The SIA Close Protection Licence: What It Is, What It Proves, and How to Verify It",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["uk", "regulation", "licensing", "sia"],
        "internal_links": [
            "/blog/how-to-vet-a-close-protection-company/",
            "/cities/london/",
            "/services/executive-protection/",
        ],
        "keywords": "SIA close protection licence, UK bodyguard licensing, SIA ACS, verify SIA licence",
        "sources": "Private Security Industry Act 2001, SIA licence verification portal, SIA ACS register",
    },
    {
        "slug": "executive-protection-johannesburg",
        "title": "Executive Protection in Johannesburg: What a Professional Detail Actually Involves",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["johannesburg", "south-africa", "executive-protection", "close-protection"],
        "internal_links": [
            "/cities/johannesburg/",
            "/blog/bodyguard-licensing-south-africa/",
        ],
        "keywords": "executive protection Johannesburg, close protection South Africa, PSIRA Grade A, armoured vehicle Johannesburg",
        "sources": "SAPS crime statistics Gauteng, PSIRA Act 56 of 2001, Firearms Control Act 60 of 2000",
    },
    {
        "slug": "is-dubai-safe-2026",
        "title": "Is Dubai Safe in 2026? The Regional Tension Picture for Business Travellers",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["dubai", "uae", "risk-assessment", "middle-east"],
        "internal_links": [
            "/cities/dubai/",
            "/blog/bodyguard-licence-uae/",
        ],
        "keywords": "is Dubai safe 2026, Dubai regional tensions, Houthi UAE, Dubai business travel security",
        "sources": "FCDO UAE advisory, US State Dept UAE alerts, UAE SIRA regulatory framework",
    },
    {
        "slug": "secure-airport-transfer-lagos",
        "title": "Secure Airport Transfer from Lagos Airport: The MMIA Arrival Guide for Business Travellers",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["lagos", "nigeria", "airport-transfer", "security-driver"],
        "internal_links": [
            "/cities/lagos/",
            "/services/security-drivers/",
        ],
        "keywords": "secure airport transfer Lagos, MMIA to Victoria Island, Lagos airport safety, Nigeria airport transport",
        "sources": "FCDO Nigeria advisory, OSAC Lagos Crime and Safety Report, UK Government travel alerts",
    },
    {
        "slug": "close-protection-female-executives",
        "title": "Close Protection for Female Executives: What Works, What to Ask, and Where the Gaps Are",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["executive-protection", "female-security", "business-travel", "vetting"],
        "internal_links": [
            "/services/executive-protection/",
            "/blog/how-to-vet-a-close-protection-company/",
        ],
        "keywords": "close protection female executives, women business travel security, female bodyguard, security for women",
        "sources": "Google autocomplete intelligence from keyword_matrix.json, FCDO women travel advisories",
    },
]


def slug_exists(slug):
    return os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md"))


if __name__ == "__main__":
    print(f"Blog Batch 4 -- {len(ARTICLES)} articles")
    for a in ARTICLES:
        status = "EXISTS" if slug_exists(a["slug"]) else "MISSING"
        print(f"  [{status}] {a['slug']}")
        print(f"         Author: {a['author']}")
        print(f"         Sources: {a['sources']}")
    print()
    print("Content committed directly via GitHub MCP.")
    print("Workforce: Wordsmith -> Interrogator -> Chameleon -> Optimiser -> Auditor")
