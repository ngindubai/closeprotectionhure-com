# CloseProtectionHire.com — Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every session.

## Status Legend
- `[x]` Completed
- `[ ]` Remaining

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

### Stage 2K — Blog Launch (8 articles)
- [ ] 8 cornerstone blog articles targeting informational keywords from `data/keyword_matrix.json`
- [ ] Author attribution strategy decided (required for YMYL compliance)

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
