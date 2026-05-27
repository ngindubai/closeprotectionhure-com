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

## Phase 2G — Event Security Silo (16 conference cities)
- [x] Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Dubai, Mumbai, Moscow, Bangkok, London, New York, Paris, Singapore, Sydney, Tokyo

## Phase 2K — Blog Factory
- [x] **Batch 1 LIVE — 5 articles (27 May 2026)**
- [x] **Batch 2 LIVE — 5 articles (27 May 2026)**
- [ ] Batch 3 (articles 11-15): Sao Paulo risk, Bogota transport, Istanbul regulation, Nairobi drivers, Manila safety
- [ ] Batches 4-19+: continuing through keyword matrix

## Phase 3A — P3 City Expansion (25 new city hub pages)
- [x] **Batch 1 LIVE (27 May 2026) — 25 cities deployed:**
  - Amman (Jordan) — medium risk, diplomatic/transit hub
  - Abuja (Nigeria) — high risk, federal capital
  - Kuala Lumpur (Malaysia) — low risk, SE Asia hub
  - Dhaka (Bangladesh) — high risk, NGO/garment sector
  - Muscat (Oman) — low risk, Gulf energy hub
  - Ho Chi Minh City (Vietnam) — low risk, SE Asia commercial
  - Luanda (Angola) — high risk, oil and gas sector
  - Tbilisi (Georgia) — medium risk, South Caucasus emerging hub
  - Naples (Italy) — low risk, HNWI/Campania
  - Rome (Italy) — low risk, diplomatic/corporate
  - Miami (USA) — low risk, HNWI/Latin America gateway
  - Toronto (Canada) — low risk, financial/HNWI
  - Vienna (Austria) — low risk, UN/OSCE diplomatic
  - Warsaw (Poland) — low risk, NATO Eastern Europe
  - Colombo (Sri Lanka) — medium risk, infrastructure/port
  - Baku (Azerbaijan) — medium risk, energy sector
  - Kinshasa (DRC) — high risk, mining sector
  - Mombasa (Kenya) — high risk, port/logistics
  - Geneva (Switzerland) — low risk, UN/HNWI banking
  - Washington DC (USA) — low risk, government/diplomatic
  - Montreal (Canada) — low risk, events/HNWI
  - Zurich (Switzerland) — low risk, private banking/HNWI
  - Milan (Italy) — low risk, fashion/financial
  - **NOTE:** 25 of target batch committed. 2 additional pages (Madrid, Amsterdam) queued for Phase 3A Batch 2.

---

## Remaining Stages

### Stage 2H — Travel Safety Guides Batch 1
- [ ] 15 travel safety guide pages for P1 cities

### Stage 2I — Travel Safety Guides Batch 2 + Regulation Guides
- [ ] Remaining travel safety guides
- [ ] Country-specific security regulation guides

### Stage 2J — Internal Link Graph + Backlink Strategy
- [ ] Internal linking audit
- [ ] Backlink outreach strategy document

### Phase 3B — P3 City Expansion Batch 2
- [ ] Madrid, Amsterdam + next priority cities from combinatorial gap analysis
- [ ] Priority candidates: Ankara, Lagos-Ikeja, Kigali, Maputo, Yangon, Colombo EP pages

### Phase 3C — Service x City Deep Expansion
- [ ] Bodyguard-hire city-specific pages (modelled on event-security/{city}.md pattern)
- [ ] Security-drivers city-specific pages
- [ ] Executive-protection city-specific pages
- [ ] Residential-security city-specific pages
- Target: 5 services x 10 priority cities = 50 additional pages per pass

### Stage 2L — QA + Security Audit
- [ ] Full site QA pass
- [ ] YMYL compliance check
- [ ] Schema markup verification

---

## Session Log

| Date | Stage | Pages Added | Total Pages | Notes |
|------|-------|-------------|-------------|-------|
| Pre-migration | 2A-2F | 121 | 121 | Migrated to standalone VS Code instance |
| 22 Apr 2026 | 2G | 16 | 143 | Event security silo: 16 conference cities. Hugo: 143 pages, 0 errors. Deployed. |
| 22 Apr 2026 | Setup | 0 | 143 | New chat session. BUILD-PLAN.md synced. |
| 27 May 2026 | 2K Batch 1 | 5 blog + 3 infra | 148 | Blog factory launched: 5 articles, layouts, generator script. |
| 27 May 2026 | 2K Batch 2 | 5 blog | 153 | 5 articles: SA licensing, Mexico City risk, Lagos driver, Saudi Arabia EP, OR Tambo transfer. |
| 27 May 2026 | 3A Batch 1 | 25 cities | 178 | P3 city expansion: Amman, Abuja, Kuala Lumpur, Dhaka, Muscat, Ho Chi Minh City, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan + 2 queued. Full city template: threats, services, regulations, zones, FAQs, warnings, related cities. FCDO/OSAC sources cited. No safety guarantees. British English. Auto-deployed via GitHub Actions. |
