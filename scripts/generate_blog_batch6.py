#!/usr/bin/env python3
"""
generate_blog_batch6.py
Stage 2K Batch 6 -- Blog articles 26-30.
Mirror tracker for batch 6 articles, generated through the workforce loop:
  the-wordsmith -> the-chameleon -> the-optimiser -> the-auditor.
Sources cited inline within each article (FCDO, US State Dept, PSARA, NCRB,
Egyptian MoI, Royal Thai Police, Mumbai Police).
"""
import os
BLOG_DIR = os.path.join("site", "content", "blog")
ARTICLES = [
    {"slug": "is-mexico-city-safe-from-cartels-executive-guide",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "US State Dept Mexico advisory, FCDO Mexico, CDMX police homicide data, NCRB-equivalent crime data"},
    {"slug": "bodyguard-licence-india-psara",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "Private Security Agencies (Regulation) Act 2005, MHA guidelines, Maharashtra Controlling Authority registry"},
    {"slug": "is-bangkok-safe-for-business-travel",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "FCDO Thailand advisory, US State Dept Thailand, Royal Thai Police data, 2015 Erawan incident review"},
    {"slug": "security-driver-cairo",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "FCDO Egypt advisory, US State Dept Egypt, Egyptian Ministry of Interior licensing framework, CAI airport security review"},
    {"slug": "women-business-travellers-mumbai-safety",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "NCRB crimes-against-women statistics, FCDO India advisory, Mumbai Police data, post-2008 hotel security protocols"},
]
if __name__ == "__main__":
    for a in ARTICLES:
        exists = os.path.exists(os.path.join(BLOG_DIR, f"{a['slug']}.md"))
        print(f"  [{'EXISTS' if exists else 'MISSING'}] {a['slug']}")
