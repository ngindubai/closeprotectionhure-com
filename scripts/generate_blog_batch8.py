#!/usr/bin/env python3
"""
generate_blog_batch8.py
Stage 2K Batch 8 -- Blog articles 36-40.
Mirror tracker for batch 8 articles.
"""
import os
BLOG_DIR = os.path.join("site", "content", "blog")
ARTICLES = [
    {"slug": "private-security-regulations-indonesia",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "Government Regulation No. 60/2016 (BUJP), POLRI KTA Satpam framework, FCDO Indonesia advisory"},
    {"slug": "is-karachi-safe-for-business-travel",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "FCDO Pakistan advisory, US State Dept Pakistan, Pakistan Rangers Operation Cleanup reporting, Sindh Police crime data"},
    {"slug": "bodyguard-hire-johannesburg-cost",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "PSIRA grade and fee structure, Firearms Control Act 2000, SARS VAT Act, South African security industry pricing surveys"},
    {"slug": "executive-protection-cairo",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "FCDO Egypt advisory, US State Dept Egypt, Egyptian Ministry of Interior private security licensing, OSAC Egypt reports"},
]
if __name__ == "__main__":
    for a in ARTICLES:
        exists = os.path.exists(os.path.join(BLOG_DIR, f"{a['slug']}.md"))
        print(f"  [{('EXISTS' if exists else 'MISSING')}] {a['slug']}")
