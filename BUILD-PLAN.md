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
- [x] 18 city-specific event security pages

## Phase 2K — Blog Factory
- [x] Batches 1–8 complete (46 articles live)
- [ ] Batches 9–19 continuing through keyword matrix

## Phase 3A — P3 City Expansion Batch 1 (23 cities)
- [x] Deployed 27 May 2026: Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B — P3 City Expansion Batch 2 (5 cities)
- [x] Deployed 27 May 2026: Madrid, Amsterdam, Ankara, Kigali, Yangon

## P3 City Expansion — Unlogged additions (found in audit)
- [x] Baghdad, Beirut, Caracas, Kabul, Kampala, Kathmandu, Kyiv, Auckland, Melbourne

## Phase 3C — Service x City Combinatorial Matrix
- [x] Block 1 (28 May 2026): bodyguard-hire x 10 priority cities
- [x] Block 2 (28 May 2026): security-drivers x 10 priority cities
- [x] Block 3 (28 May 2026): executive-protection x 10 priority cities
- [x] Block 4 (28 May 2026): residential-security x 10 priority cities
- [x] Block 5 (28 May 2026): event-security gap fill — all 10 priority cities covered

## Phase 3D — P3 City Expansion Batch 3 (6 cities)
- [x] **Deployed 02 Jun 2026:** Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica)

**~86 city pages live. ~284 total pages.**

---

## Remaining Stages

### Stage 2H — Travel Safety Guides Batch 1
- [ ] 15 travel safety guide pages for P1 cities

### Stage 2J — Internal Link Graph
- [ ] Run `scripts/rebuild_link_graph.py` diagnostic
- [ ] Resolve under-linked pages, orphans, top-inbound rebalancing

### Phase 3E — P3 City Expansion Batch 4
- [ ] Candidates: Accra expansion, Medellin, Guadalajara, Cape Verde (Praia), Maputo, Lusaka

### Blog Factory continuation
- [ ] Blog Batch 9: is-lagos-safe, female-executives-ME, brazil-regulations, nairobi-driver, bogota-EP
- [ ] Batches 10–19 continuing

---

## Session Log

| Date | Stage | Pages Added | Total Pages | Notes |
|------|-------|-------------|-------------|-------|
| Pre-migration | 2A-2F | 121 | 121 | |
| 22 Apr 2026 | 2G | 16 | 143 | Event security silo: 16 cities |
| 27 May 2026 | 2K B1-B2 | 10 | 153 | Blog factory launched |
| 27 May 2026 | 3A B1 | 23 | 178 | P3 cities Batch 1 |
| 27 May 2026 | 3B | 5 | 183 | Madrid, Amsterdam, Ankara, Kigali, Yangon |
| 27 May 2026 | 2K B3-B4 | 10 | 193 | Blog batches 3 and 4 |
| 27 May 2026 | Deploy fix | 0 | 193 | Migrated from FTP to build-and-publish + Hostinger OAuth |
| 27 May 2026 | 2K B5 | 5 | 198 | Riyadh, Istanbul, Dubai residential, HK, Mumbai EP |
| 28 May 2026 | 2K B6 | 5 | 203 | Mexico cartels, PSARA India, Bangkok, Cairo driver, Mumbai women |
| 28 May 2026 | Engine 4+5 | 4 scripts | 203 | qa_audit.py, check_titles.py, check_descriptions.py, rebuild_link_graph.py |
| 28 May 2026 | CLAUDE.md harden | 0 | 203 | Seven Engines, mandatory workflow, forbidden moves locked in |
| 28 May 2026 | 3C B1 | 11 | 214 | bodyguard-hire/{city} x 10 + _index.md |
| 28 May 2026 | 3C B2 | 11 | 225 | security-drivers/{city} x 10 + _index.md |
| 28 May 2026 | 3C B3 | 11 | 236 | executive-protection/{city} x 10 + _index.md |
| 28 May 2026 | 3C B4 | 11 | 247 | residential-security/{city} x 10 + _index.md |
| 28 May 2026 | 3C B5 | ~8 | ~257 | event-security gap fill for priority cities |
| 29 May 2026 | 2K B7-B8 | ~16 | ~273 | Additional blog articles |
| 01 Jun 2026 | Audit + sync | -2 | ~271 | Docs synced, test stubs deleted, Stage 2L QA passed |
| 02 Jun 2026 | 3D | 6 | ~284 | Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose |
