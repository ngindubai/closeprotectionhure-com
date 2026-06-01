# CloseProtectionHire.com — Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every session.
> **NOTE: This BUILD-PLAN is on `master`. All commits go to `master` only.**

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

## Phase 2H — Travel Safety Guides (P1 cities)
- [x] **Deployed 02 Jun 2026:** 15 travel safety guides for all P1 cities: Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Riyadh, Dubai, Mumbai, Moscow, Sao Paulo, Manila, Karachi, Bangkok, Jakarta

## Phase 2K — Blog Factory
- [x] Batches 1–8+ (100+ articles live across operational batches)
- [ ] Continuing through keyword matrix

## Phase 3A — P3 City Expansion Batch 1 (23 cities)
- [x] Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B — P3 City Expansion Batch 2 (5 cities)
- [x] Madrid, Amsterdam, Ankara, Kigali, Yangon

## Phase 3C — Service x City Combinatorial Matrix
- [x] Block 1: bodyguard-hire x 10 priority cities
- [x] Block 2: security-drivers x 10 priority cities
- [x] Block 3: executive-protection x 10 priority cities
- [x] Block 4: residential-security x 10 priority cities
- [x] Block 5: event-security gap fill — all 10 priority cities covered

## Phase 3D — P3 City Expansion Batch 3 (6 cities)
- [x] Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica)

## Phase 3E — P3 City Expansion Batch 4 (6 cities)
- [x] **Deployed 02 Jun 2026:** Medellin, Guadalajara, Accra, Maputo, Lusaka, Abidjan

**~92 city pages live. ~320+ total pages.**

---

## Remaining Stages

### Stage 2J — Internal Link Graph
- [ ] Run `scripts/rebuild_link_graph.py` diagnostic
- [ ] Resolve under-linked pages, orphans, top-inbound rebalancing

### Stage 2L — QA + Full Site Audit
- [ ] Run `scripts/qa_audit.py` across all silos
- [ ] Run `scripts/check_titles.py` + `scripts/check_descriptions.py`
- [ ] Fix any YMYL safety-guarantee patterns, banned words, or em dashes found

### Phase 3F — P3 City Expansion Batch 5
- [ ] Candidates: Baku expansion, Almaty, Tashkent, Colombo expansion, Santiago expansion

### Blog Factory continuation
- [ ] Continue through keyword matrix targeting angles not covered by Phase 3C service x city deep pages

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
| 02 Jun 2026 | 2H | 15 | Travel safety guides for all 15 P1 cities (date fix: buildFuture=true added to hugo.toml) |
| 02 Jun 2026 | 3E | 6 | Medellin, Guadalajara, Accra, Maputo, Lusaka, Abidjan |
