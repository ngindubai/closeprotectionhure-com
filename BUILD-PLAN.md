# CloseProtectionHire.com — Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every session.

## Status Legend
- `[x]` Completed
- `[ ]` Remaining
- `[~]` In Progress

---

## Phase 0 — Research
- [x] City risk profiles (15 P1 cities) — `data/city_risk_profiles.json`
- [x] Security regulations (15 P1 countries) — `data/security_regulations_v1_backup.json`
- [x] FCDO advisories — `data/fcdo_advisories.json`
- [x] US State Dept advisories — `data/state_dept_data.json`
- [x] Keyword matrix (75 clusters) — `data/keyword_matrix.json`
- [x] Database schema — `data/database_schema.json`
- [x] Tech stack decision — `data/tech_stack.md`
- [x] Competitor analysis — `data/competitors/competitor_analysis.html`

## Phase 1 — Foundation
- [x] 15 P1 city pages
- [x] 15 P1 country hub pages
- [x] 5 service silo pages
- [x] Core pages (about, contact, FAQ, network, privacy, terms)
- [x] 18 risk assessment pages

## Phase 2A — P2 Cities: London, New York, Paris, Berlin, Tokyo
- [x] All 5 city pages created and deployed

## Phase 2B — P2 Cities: Hong Kong, Singapore, Sydney, Doha, Kuwait City
- [x] All 5 city pages created and deployed

## Phase 2C — P2 Cities: Abu Dhabi, Cape Town, Accra, Dar es Salaam, Addis Ababa
- [x] All 5 city pages created and deployed

## Phase 2D/2E — P2 Cities: Lima, Buenos Aires, Santiago, Beijing, Shanghai, Delhi, Bangalore, Tel Aviv, Cairo, Casablanca
- [x] All 10 city pages created and deployed

## Phase 2F — P2 Country Hub Pages (19 countries)
- [x] UK, US, France, Germany, Japan, China, Singapore, Australia, Qatar, Kuwait
- [x] Ghana, Tanzania, Ethiopia, Peru, Argentina, Chile, Israel, Egypt, Morocco

---

## Remaining Stages

### Stage 2G — Event Security Silo (16 conference cities)
- [x] Event security pages built: Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Dubai, Mumbai, Moscow, Bangkok, London, New York, Paris, Singapore, Sydney, Tokyo
- **NOTE:** 5 P1 cities NOT covered: Riyadh, Sao Paulo, Manila, Karachi, Jakarta. Previous session chose 16 major conference cities over strict P1 list. To be addressed in a supplementary pass if required.

### Stage 2H — Travel Safety Guides Batch 1
- [ ] 15 travel safety guide pages for P1 cities

### Stage 2I — Travel Safety Guides Batch 2 + Regulation Guides
- [ ] Remaining travel safety guides
- [ ] Country-specific security regulation guides

### Stage 2J — Internal Link Graph + Backlink Strategy
- [ ] Internal linking audit across all 121+ pages
- [ ] Backlink outreach strategy document

### Stage 2K — Blog Factory (target: 100+ articles across 19+ batches)
- [~] **Batch 1 LIVE — 5 articles deployed (27 May 2026)**
  - `how-to-vet-a-close-protection-company`
  - `executive-protection-cost-factors`
  - `bodyguard-licence-uae`
  - `secure-airport-transfer-dubai`
  - `is-nairobi-safe-for-business-travel`
- [x] Blog infrastructure created:
  - `site/layouts/blog/single.html` — Article schema, author bar, FAQ accordion, quote form
  - `site/layouts/blog/list.html` — Blog index listing
  - `site/content/blog/_index.md` — Section index
  - `scripts/generate_blog_batch1.py` — Generator script and workforce pipeline documentation
- [ ] Batch 2 (articles 6-10) — targets: regulation guides, city-specific security questions
- [ ] Batch 3+ — continuing through keyword matrix informational clusters

**Blog factory workforce pipeline (per CLAUDE.md):**
1. The Wordsmith — authority voice, British English, sourced facts, no filler
2. The Interrogator — city/service-specific FAQs, no safety guarantees
3. The Chameleon — humaniser: no em dashes, no banned vocab, high burstiness
4. The Optimiser — SEO metadata, FAQ schema via `faq-accordion.html` partial
5. The Auditor — QA gate: YMYL compliance, legal accuracy, named sources

**Author personas in use:**
- James Calloway, Senior Security Consultant (regulation, risk assessment, vetting content)
- Marcus Webb, Security Operations Adviser (operational, logistics, transport content)

### Stage 2L — QA + Security Audit
- [ ] Full site QA pass
- [ ] YMYL compliance check
- [ ] Security audit
- [ ] Schema markup verification

---

## Session Log

| Date | Stage | Pages Added | Total Pages | Notes |
|------|-------|-------------|-------------|-------|
| Pre-migration | 2A-2F | 121 | 121 | Migrated to standalone VS Code instance |
| 22 Apr 2026 | 2G | 16 | 143 | Event security silo: 16 conference cities via generate_event_security_pages.py. Hugo: 143 pages, 0 errors. Deployed. |
| 22 Apr 2026 | Setup | 0 | 143 | New chat session initiated. Build plan synced. BUILD-PLAN.md updated. Next: Stage 2H. |
| 27 May 2026 | 2K Batch 1 | 5 blog articles + 3 infrastructure files | 148 | Blog factory launched. Infrastructure: blog/single.html, blog/list.html, blog/_index.md. 5 articles: vetting a CP company, EP cost factors, UAE licensing, Dubai airport transfer, Nairobi risk assessment. Generator script: scripts/generate_blog_batch1.py. Both author personas established. Workforce pipeline documented. Auto-deployed to Hostinger via GitHub Actions. |
