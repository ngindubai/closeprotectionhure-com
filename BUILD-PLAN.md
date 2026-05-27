# CloseProtectionHire.com — Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every session.

## Status Legend
- `[x]` Completed
- `[ ]` Remaining
- `[~]` In Progress

---

## Phase 0 — Research
- [x] City risk profiles, security regulations, FCDO/State Dept advisories, keyword matrix (75 clusters), database schema, tech stack, competitor analysis

## Phase 1 — Foundation
- [x] 15 P1 city pages, 15 P1 country hub pages, 5 service silo pages, core pages (about/contact/FAQ/network/privacy/terms), 18 risk assessment pages

## Phase 2A–2F — P2 City and Country Expansion
- [x] 25 P2 city pages, 19 P2 country hub pages

## Phase 2G — Event Security Silo
- [x] 16 city-specific event security pages

## Phase 2K — Blog Factory
- [x] **Batch 1 (27 May 2026):** how to vet CP company, EP cost factors, UAE licensing, Dubai airport transfer, Nairobi risk
- [x] **Batch 2 (27 May 2026):** SA licensing, Mexico City risk, Lagos driver vs taxi, Saudi EP, JHB airport transfer
- [x] **Batch 3 (27 May 2026):** Sao Paulo risk, Bogota driver, Turkey regulation, Nairobi drivers, Manila safety
- [x] **Batch 4 (27 May 2026):** SIA CP licence, EP Johannesburg, Dubai 2026 tensions, Lagos airport transfer, female EP
- [x] **Batch 5 (27 May 2026):** Riyadh safety, Istanbul CP, Dubai residential security, Hong Kong bodyguard, Mumbai EP
- [x] **Batch 6 (28 May 2026):** Mexico City cartels EP guide, PSARA India bodyguard licence, Bangkok safety, Cairo security driver, Mumbai women travellers
- [ ] **Batches 7-19+:** continuing through keyword matrix

**30 blog articles live. Scripts: generate_blog_batch1.py through generate_blog_batch6.py**

## Phase 3A — P3 City Expansion Batch 1 (23 cities)
- [x] Deployed 27 May 2026: Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B — P3 City Expansion Batch 2 (5 cities)
- [x] Deployed 27 May 2026: Madrid, Amsterdam, Ankara, Kigali, Yangon

**70 city pages live.**

## Phase 3C — Service x City Combinatorial Matrix (Engine 1 widening)

Mirrors the pet-transport `generate_p2_routes.py` engine pattern. Five service silos x ten priority cities = 50 deep service x city pages. Each block is one service x ten cities. Built one block per session per Engine 7 discipline.

Priority cities: Johannesburg, Lagos, Dubai, Nairobi, Mexico City, Bogota, Riyadh, Mumbai, Sao Paulo, Istanbul.

- [x] **Block 1 (28 May 2026): `bodyguard-hire/{city}` for 10 priority cities.** Section _index.md plus 10 deep pages. Each page: regulator-named (PSIRA, NSCDC, SIRA, PSRA, DGSP, SuperVigilancia, MoI, PSARA, DPF, OGG), city-specific operational detail, 4 FAQ schema entries, 3 internal links, no safety guarantees, no em dashes, British English.
- [ ] **Block 2: `security-drivers/{city}` for 10 priority cities.**
- [ ] **Block 3: `executive-protection/{city}` for 10 priority cities.**
- [ ] **Block 4: `residential-security/{city}` for 10 priority cities.**
- [ ] **Block 5: `event-security/{city}` extension to non-overlap priority cities** (note: event-security/{city} silo already exists for 16 cities from Phase 2G; this block fills the priority-city gaps not yet covered).

**80 city + service-city pages live (70 + 10). ~214 total pages.**

---

## Remaining Stages

### Stage 2H — Travel Safety Guides Batch 1
- [ ] 15 travel safety guide pages for P1 cities

### Stage 2J — Internal Link Graph
- [ ] Run `scripts/rebuild_link_graph.py` diagnostic
- [ ] Resolve under-linked pages, orphans, top-inbound rebalancing
- [ ] Backlink outreach strategy

### Phase 3D — P3 City Expansion Batch 3
- [ ] Next cities: Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica), Cape Verde

### Stage 2L — QA + Security Audit
- [ ] Full site QA pass via `scripts/qa_audit.py`
- [ ] Title and description audit via `scripts/check_titles.py` + `scripts/check_descriptions.py`
- [ ] YMYL compliance check
- [ ] Schema markup verification

### Engine Alignment (pet-transport replication)
- [x] Engine 1 — Combinatorial page generators (Phase 3C Block 1 done; Blocks 2-5 outstanding)
- [x] Engine 2 — Structured data layer (data/*.json present: city_risk_profiles, security_regulations, fcdo_advisories, state_dept_data, keyword_matrix)
- [~] Engine 3 — Bulk blog factory (6 batches of 5 = 30 articles. Pet-transport has 19 batches / 411 articles)
- [x] Engine 4 — Internal link graph diagnostic (`scripts/rebuild_link_graph.py`); rewriter pending Stage 2J
- [x] Engine 5 — QA + SEO quality gate (`scripts/qa_audit.py`, `check_titles.py`, `check_descriptions.py`)
- [x] Engine 6 — Incremental deploy pipeline (build-and-publish + Hostinger OAuth, 28 May 2026)
- [x] Engine 7 — Operating system (CLAUDE.md hardened with Seven Engines, mandatory workflow, forbidden moves; AGENTS.md / ERRORS.md present)

---

## Session Log

| Date | Stage | Pages Added | Total Pages | Notes |
|------|-------|-------------|-------------|-------|
| Pre-migration | 2A-2F | 121 | 121 | |
| 22 Apr 2026 | 2G | 16 | 143 | Event security silo: 16 cities |
| 22 Apr 2026 | Setup | 0 | 143 | Session sync |
| 27 May 2026 | 2K B1 | 5+3 infra | 148 | Blog factory launched |
| 27 May 2026 | 2K B2 | 5 | 153 | SA, Mexico City, Lagos, Saudi, JHB |
| 27 May 2026 | Method | 3 files | 153 | batch2.py, build_state.json, WORKFLOW.md |
| 27 May 2026 | 3A B1 | 23 | 178 | P3 cities Batch 1 |
| 27 May 2026 | 3B | 5 | 183 | Madrid, Amsterdam, Ankara, Kigali, Yangon |
| 27 May 2026 | 2K B3 | 5 | 188 | Sao Paulo, Bogota, Turkey regs, Nairobi drivers, Manila |
| 27 May 2026 | 2K B4 | 5 | 193 | SIA licensing, EP Johannesburg, Dubai 2026, Lagos airport, female EP. Scripts batch3.py + batch4.py added. 20 blog articles live. |
| 27 May 2026 | 2K B5 | 5 | 198 | Riyadh, Istanbul, Dubai residential, HK, Mumbai EP. 25 blog articles live. |
| 27 May 2026 | Deploy fix | 0 | 198 | Migrated from FTP to build-and-publish + Hostinger OAuth. Permalink and baseURL bugs fixed. |
| 28 May 2026 | 2K B6 | 5 | 203 | Mexico cartels guide, PSARA India, Bangkok safety, Cairo driver, Mumbai women. 30 blog articles live. |
| 28 May 2026 | Engine docs | 0 | 203 | CLAUDE.md updated for new deploy. AGENTS.md / ERRORS.md / engine alignment section added. |
| 28 May 2026 | Engine 5+4 ports | 4 scripts | 203 | qa_audit.py, check_titles.py, check_descriptions.py, rebuild_link_graph.py ported from pet-transport. AGENTS.md + ERRORS.md created. |
| 28 May 2026 | CLAUDE.md harden | 0 | 203 | Locked in Seven Engines table, mandatory session workflow, hard QA gate, forbidden moves. |
| 28 May 2026 | 3C B1 | 11 (1 index + 10 cities) | 214 | bodyguard-hire/{city} for 10 priority cities. First row of service x city matrix. |
