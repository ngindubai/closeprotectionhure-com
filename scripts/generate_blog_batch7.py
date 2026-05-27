#!/usr/bin/env python3
"""
generate_blog_batch7.py
Stage 2K Batch 7 -- Blog articles 31-35.
Mirror tracker for batch 7 articles.
Sources cited inline within each article.
"""
import os
BLOG_DIR = os.path.join("site", "content", "blog")
ARTICLES = [
    {"slug": "is-beijing-safe-for-business-travel",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "FCDO China advisory, US State Dept China, NCSC China threat guidance, FBI economic espionage bulletins, CISA clean-device guidance"},
    {"slug": "close-protection-singapore",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "PLRD PSIA 2007, MHA terrorism threat level, FCDO Singapore advisory, SG Police Force licensing registry"},
    {"slug": "executive-protection-tel-aviv",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "FCDO Israel advisory (post-Oct 2023), US State Dept Israel, Israeli Ministry of National Security PPSS Law 5772-2012, IDF Red Alert protocol"},
    {"slug": "can-bodyguards-carry-guns-in-mexico",
     "author": "James Calloway, Senior Security Consultant",
     "sources": "Ley Federal de Armas de Fuego y Explosivos, SEDENA Licencia Colectiva system, DGSP Ley Federal de Seguridad Privada, FCDO Mexico advisory"},
    {"slug": "residential-security-johannesburg-suburbs",
     "author": "Marcus Webb, Security Operations Adviser",
     "sources": "SAPS quarterly crime statistics (Gauteng), PSIRA regulatory framework, ADT/Fidelity/Chubb armed response data, FCDO South Africa advisory"},
]
if __name__ == "__main__":
    for a in ARTICLES:
        exists = os.path.exists(os.path.join(BLOG_DIR, f"{a['slug']}.md"))
        print(f"  [{'EXISTS' if exists else 'MISSING'}] {a['slug']}")
