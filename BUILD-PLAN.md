# CloseProtectionHire.com — Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every session.
> **NOTE: This BUILD-PLAN is on `master`. All commits go to `master` only.**

## Status Legend
- `[x]` Completed
- `[ ]` Remaining
- `[~]` In Progress

---

## Phase 0 -- Research
- [x] City risk profiles, security regulations, FCDO/State Dept advisories, keyword matrix (75 clusters), database schema, tech stack, competitor analysis

## Phase 1 -- Foundation
- [x] 15 P1 city pages, 15 P1 country hub pages, 5 service silo pages, core pages (about/contact/FAQ/network/privacy/terms), 18 risk assessment pages

## Phase 2A-2F -- P2 City and Country Expansion
- [x] 25 P2 city pages, 19 P2 country hub pages

## Phase 2G -- Event Security Silo
- [x] 16 city-specific event security pages

## Phase 2H -- Travel Safety Guides (P1 cities)
- [x] **Deployed 02 Jun 2026:** 15 travel safety guides for all P1 cities: Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Riyadh, Dubai, Mumbai, Moscow, Sao Paulo, Manila, Karachi, Bangkok, Jakarta

## Phase 2K -- Blog Factory
- [x] Batches 1-8+ (100+ articles live across operational batches)
- [ ] Continuing through keyword matrix

## Phase 3A -- P3 City Expansion Batch 1 (23 cities)
- [x] Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B -- P3 City Expansion Batch 2 (5 cities)
- [x] Madrid, Amsterdam, Ankara, Kigali, Yangon

## Phase 3C -- Service x City Combinatorial Matrix
- [x] Block 1: bodyguard-hire x 10 priority cities
- [x] Block 2: security-drivers x 10 priority cities
- [x] Block 3: executive-protection x 10 priority cities
- [x] Block 4: residential-security x 10 priority cities
- [x] Block 5: event-security gap fill -- all 10 priority cities covered

## Phase 3D -- P3 City Expansion Batch 3 (6 cities)
- [x] Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica)

## Phase 3E -- P3 City Expansion Batch 4 (6 cities)
- [x] **Deployed 02 Jun 2026:** Medellin, Guadalajara, Accra, Maputo, Lusaka, Abidjan

## Phase 3F -- P3 City Expansion Batch 5 (5 cities)
- [x] **Deployed 02 Jun 2026:** Almaty, Tashkent, Islamabad, Conakry, Harare
- [x] Deleted test stubs (auto-deploy-test.md, test-deploy.md) from cities

**93 city pages live (true tree count). ~350 non-index content pages (304 audited by qa_audit.py). 108 blog, 38 countries, 24 guides, 18 risk-assessments, 18 event-security, 5 service overview pages + 5 service x city silos.**

---

## Remaining Stages

### Stage 2J -- Internal Link Graph
- [x] Run `scripts/rebuild_link_graph.py` diagnostic
- [x] **Country-hub block done 04 Jun 2026:** all 38 country pages given descriptive-anchor prose links down to their city pages and across to the executive-protection and security-drivers service silos. Total internal links 281 to 395; avg per page 0.92 to 1.30; 38 country link-floor warnings cleared. (Note: the link/QA scripts count only prose body links, not the city/service links templates render from front matter, so on-page hubs were never true orphans.)
- [x] **Floor complete 04 Jun 2026:** prose-link pass extended across event-security, risk-assessments, guides, services, all remaining cities, and 54 thematic blog articles. All 161 internal-link-floor warnings cleared; every audited page now carries >=2 prose links.
- [ ] Remaining (refinement): top-inbound link rebalancing and a backlink strategy document

### Stage 2L -- QA + Full Site Audit
- [x] **Error pass complete 03 Jun 2026:** `scripts/qa_audit.py` now PASSES with 0 errors (was 142). Fixed: 469 em dashes converted to colons/commas/parentheses across ~100 files (mostly blog); 37 banned-vocabulary occurrences reworded (leverage, robust, facilitate, nuanced, encompasses, vibrant, ubiquitous, proactive, paradigm); 1 banned phrase ("it is worth noting"); BOM stripped from bangalore/delhi/lima (front matter was unreadable). Auditor hardened: YMYL patterns now skip negated disclaimers ("does not eliminate risk", "not risk-free") and the front-matter parser tolerates a BOM.
- [x] **Thin-city depth expansion done 04 Jun 2026:** all city pages that sat at 3 FAQs brought to full depth (5 FAQs, 4+ body sections, 2+ prose links) across batches 2-10, clearing their FAQ-floor warnings.
- [x] **ALL WARNINGS CLEARED 04 Jun 2026 (was 651):** internal-link floors (161), blog FAQ floor (67 articles, 134 authored FAQs), city FAQ floor (caracas/kabul/kathmandu), title-length (53 seo_titles), and description-length (187 trimmed/rewritten). `qa_audit.py` now reports **0 errors, 0 warnings** across 304 pages.
- [ ] Title cannibalisation follow-up: `countries/uk.md` + `countries/united-kingdom.md` and `countries/usa.md` + `countries/united-states.md` are duplicate country pages sharing titles - resolve (canonical/redirect) in a later stage. (`check_titles.py` still flags these 2.)

### Phase 3G -- P3 City Expansion Batch 6
- [ ] Candidates: Naypyidaw, Bamako, Niamey, Mogadishu (conflict-zone advisory), Tripoli

### Blog Factory continuation
- [ ] Continue through keyword matrix

---

## Session Log

| Date | Stage | Pages Added | Notes |
|------|-------|-------------|-------|
| Pre-migration | 2A-2F | 121 | |
| 22 Apr 2026 | 2G | 16 | Event security silo |
| 27-28 May 2026 | 2K, 3A-3C | many | Blog batches, P3 cities, service x city matrix |
| 01 Jun 2026 | Blog batches | many | Missing posts batch 1-4, guides section |
| 02 Jun 2026 | 3D | 6 | Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose |
| 02 Jun 2026 | Homepage | 0 | Dynamic city dropdown, copy updated to 80+ cities |
| 02 Jun 2026 | 2H | 15 | Travel safety guides all P1 cities (buildFuture=true fix) |
| 02 Jun 2026 | 3E | 6 | Medellin, Guadalajara, Accra, Maputo, Lusaka, Abidjan |
| 02 Jun 2026 | Forms | 0 | FormSubmit wired to garethsomers@outlook.com, both forms fixed |
| 02 Jun 2026 | 3F | 5 | Almaty, Tashkent, Islamabad, Conakry, Harare; deleted 2 test stubs |
| 03 Jun 2026 | 2L | 0 | QA error pass: 142 errors to 0 (em dashes, banned words, BOM fixes, auditor hardening) |
| 04 Jun 2026 | Thin-city expansion | 0 | Batches 2-10: ~45 city pages at 3 FAQs expanded to full depth (5 FAQs, 4+ sections, 2+ prose links). Warnings 651 to 463 |
| 04 Jun 2026 | 2J (country-hub block) | 0 | All 38 country pages prose-linked to their cities + service silos. Internal links 281 to 395; avg 0.92 to 1.30 |
| 04 Jun 2026 | 2J (link floor complete) | 0 | Prose links added to event-security, risk-assessments, guides, services, 46 cities, 54 blog articles. All 161 link-floor warnings cleared |
| 04 Jun 2026 | Title/description fixes | 0 | 53 seo_titles shortened to <=70; 187 descriptions trimmed/rewritten to 120-175 |
| 04 Jun 2026 | FAQ floors | 0 | 3 cities + 67 blog articles brought to >=5 FAQs (134 authored blog FAQs). QA gate now 0 errors, 0 warnings |
| 03 Jun 2026 | 2L | 0 | QA error pass: 142 errors to 0. Em dashes (469), banned words (37), banned phrase (1), BOM fixes (3). Auditor hardened (YMYL negation guard, BOM-tolerant parser). Reconciled stale counts in build_state.json (cities 70->93, blog 39->108, pages 261->350). |
