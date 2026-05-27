#!/usr/bin/env python3
"""
generate_blog_batch5.py
Stage 2K Batch 5 -- Blog articles 21-25.
"""
import os
BLOG_DIR = os.path.join("site", "content", "blog")
ARTICLES = [
    {"slug": "is-riyadh-safe-for-business-travel", "author": "James Calloway, Senior Security Consultant",
     "sources": "FCDO Saudi Arabia advisory, US State Dept, ARAMCO incident reports, Houthi conflict data"},
    {"slug": "close-protection-istanbul", "author": "Marcus Webb, Security Operations Adviser",
     "sources": "FCDO Turkey advisory, Law 5188, MIT counter-terrorism data, IST airport security post-2016"},
    {"slug": "residential-security-expats-dubai", "author": "James Calloway, Senior Security Consultant",
     "sources": "FCDO UAE advisory, 2022 Abu Dhabi attack reports, UAE SIRA residential security standards"},
    {"slug": "bodyguard-hire-hong-kong", "author": "James Calloway, Senior Security Consultant",
     "sources": "Security and Guarding Services Ordinance Cap 460, NSL June 2020, HK Police SPP registry"},
    {"slug": "executive-protection-mumbai", "author": "Marcus Webb, Security Operations Adviser",
     "sources": "PSARA 2005, FCDO India advisory, 2008 Mumbai attacks after-action, BOM airport protocols"},
]
if __name__ == "__main__":
    for a in ARTICLES:
        exists = os.path.exists(os.path.join(BLOG_DIR, f"{a['slug']}.md"))
        print(f"  [{'EXISTS' if exists else 'MISSING'}] {a['slug']}")
