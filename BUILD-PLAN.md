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
- [x] 16 city-specific event security pages (plus 2 additional via 3C = 18 total)

## Phase 2K — Blog Factory
- [x] **Batch 1 (27 May 2026):** how to vet CP company, EP cost factors, UAE licensing, Dubai airport transfer, Nairobi risk
- [x] **Batch 2 (27 May 2026):** SA licensing, Mexico City risk, Lagos driver vs taxi, Saudi EP, JHB airport transfer
- [x] **Batch 3 (27 May 2026):** Sao Paulo risk, Bogota driver, Turkey regulation, Nairobi drivers, Manila safety
- [x] **Batch 4 (27 May 2026):** SIA CP licence, EP Johannesburg, Dubai 2026 tensions, Lagos airport transfer, female EP
- [x] **Batch 5 (27 May 2026):** Riyadh safety, Istanbul CP, Dubai residential security, Hong Kong bodyguard, Mumbai EP
- [x] **Batch 6 (28 May 2026):** Mexico City cartels EP guide, PSARA India bodyguard licence, Bangkok safety, Cairo security driver, Mumbai women travellers
- [x] **Batches 7–8:** Additional articles including Beijing safety, Karachi safety, Singapore CP, Tel Aviv EP, Jakarta regulations, Egypt/Cairo, Latin America vetting, government officials CP, eastern Europe, financial services security, kidnap prevention, Indonesia regulations, JHB residential, JHB cost EP, provider selection criteria, female executives ME, can bodyguards carry guns Mexico
- [ ] **Batches 9–19:** continuing through keyword matrix (next: is-lagos-safe-for-business-travel, close-protection-female-executives-middle-east, private-security-regulations-brazil, security-driver-nairobi-vs-taxi, executive-protection-bogota)

**46 blog articles live.**

## Phase 3A — P3 City Expansion Batch 1 (23 cities)
- [x] Deployed 27 May 2026: Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B — P3 City Expansion Batch 2 (5 cities)
- [x] Deployed 27 May 2026: Madrid, Amsterdam, Ankara, Kigali, Yangon

## P3 City Expansion — Additional cities (unlogged)
- [x] Baghdad, Beirut, Caracas, Kabul, Kampala, Kathmandu, Kyiv, Auckland, Melbourne (found in repo, not previously logged)

**~83 city files present (including test pages). ~80 real city pages live.**

## Phase 3C — Service x City Combinatorial Matrix

5 services x 10 priority cities. Priority cities: Johannesburg, Lagos, Dubai, Nairobi, Mexico City, Bogota, Riyadh, Mumbai, Sao Paulo, Istanbul.

- [x] **Block 1 (28 May 2026): `bodyguard-hire/{city}` — 10 cities.**
- [x] **Block 2 (28 May 2026): `security-drivers/{city}` — 10 cities.**
- [x] **Block 3 (28 May 2026): `executive-protection/{city}` — 10 cities.**
- [x] **Block 4 (28 May 2026): `residential-security/{city}` — 10 cities.**
- [x] **Block 5 (28 May 2026): event-security gaps filled — all 10 priority cities now covered.**

**Engine 1 (combinatorial generators) complete for priority cities.**

---

## Remaining Stages

### Stage 2H — Travel Safety Guides Batch 1
- [ ] 15 travel safety guide pages for P1 cities

### Stage 2J — Internal Link Graph
- [ ] Run `scripts/rebuild_link_graph.py` diagnostic
- [ ] Resolve under-linked pages, orphans, top-inbound rebalancing

### Stage 2L — QA + Full Site Audit
- [ ] Run `scripts/qa_audit.py` across all silos
- [ ] Run `scripts/check_titles.py` + `scripts/check_descriptions.py`
- [ ] Fix any YMYL safety-guarantee patterns, banned words, or em dashes found
- [ ] Schema markup verification

### Phase 3D — P3 City Expansion Batch 3
- [ ] Next cities: Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica)

### Blog Factory continuation
- [ ] Blog Batches 9–19 (currently 8 of 19 target batches done — 46 articles live)

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
| 29 May 2026 | 2K B7-B8 | ~16 | ~273 | Additional blog articles (Beijing, Karachi, Singapore, Tel Aviv, Jakarta, others) |
| 01 Jun 2026 | Audit | 0 | ~280 | Repo audit — found additional city pages (Baghdad, Beirut, Caracas, Kabul, Kampala, Kathmandu, Kyiv, Auckland, Melbourne) not previously logged. Docs synced. |
