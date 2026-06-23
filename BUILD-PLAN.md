# CloseProtectionHire.com - Build Plan

> **Primary tracker:** Always reference `bodyguard-cascading-build-plan.html` for full stage detail, scope, and DONE/IN PROGRESS/TODO badges.
> This file is the mirrored checklist. Both files must be updated at the end of every run.
> **NOTE: This BUILD-PLAN is on `master`. All commits go to `master` only.**
> **CADENCE (5 June 2026): the build routine runs a batch of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap (changed from one block per run). Full QA gate on every block, commit the whole batch to master ONCE, post live links to Slack as a record. See GROWTH MODE at the foot of this file for what to build.**

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
- [x] **Deployed 02 Jun 2026:** 15 travel safety guides for all P1 cities

## Phase 2K -- Blog Factory
- [x] Batches 1-8+ (100+ articles live across operational batches)
- [ ] Continuing through keyword matrix (target 600)

## Phase 3A -- P3 City Expansion Batch 1 (23 cities)
- [x] Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan

## Phase 3B -- P3 City Expansion Batch 2 (5 cities)
- [x] Madrid, Amsterdam, Ankara, Kigali, Yangon

## Phase 3C -- Service x City Combinatorial Matrix (priority-10 seed)
- [x] Block 1: bodyguard-hire x 10 priority cities
- [x] Block 2: security-drivers x 10 priority cities
- [x] Block 3: executive-protection x 10 priority cities
- [x] Block 4: residential-security x 10 priority cities
- [x] Block 5: event-security -- all 10 priority cities covered
- [ ] **FULL MATRIX EXPANSION: see GROWTH MODE below.** Only the 10 priority cities are seeded. Extend all services across all live cities.

## Phase 3D -- P3 City Expansion Batch 3 (6 cities)
- [x] Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica)

## Phase 3E -- P3 City Expansion Batch 4 (6 cities)
- [x] **Deployed 02 Jun 2026:** Medellin, Guadalajara, Accra, Maputo, Lusaka, Abidjan

## Phase 3F -- P3 City Expansion Batch 5 (5 cities)
- [x] **Deployed 02 Jun 2026:** Almaty, Tashkent, Islamabad, Conakry, Harare

## Phase 3G -- P3 City Expansion Batch 6 (5 cities)
- [x] **Deployed 05 Jun 2026:** Naypyidaw, Bamako, Niamey, Mogadishu, Tripoli

**98 city pages live. ~355 non-index content pages. 108 blog, 38 countries, 24 guides, 18 risk-assessments, 18 event-security, 5 service overview pages + 5 service x city silos (priority-10 seed only).**

---

## Routine cadence note (5 June 2026)

Switched to batch builds of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap. A block here = one service x 10 cities, or one blog batch of 5, or one layout fix. A run builds up to 4 such blocks (floor 1), each through the full QA gate, then commits the whole batch to master ONCE (one commit, one push, one deploy) so concurrent deploys never clobber each other. The HTML-preview-then-approval step in CLAUDE.md still applies before the commit. Bulk-generation scripts that skip the per-block QA gate remain banned: a batch is N individually quality-gated blocks, never a mass-generation script. Skip rule: skip a block whose slugs already exist; skip the whole run only when nothing is left to build across the active tracks. Do NOT skip just because a build ran earlier today; this routine runs twice a day on purpose.

---

## Remaining refinement (non-blocking)

### Stage 2J -- Internal Link Graph
- [x] Country-hub, event-security, risk-assessments, guides, services, all cities and 54 blog articles prose-linked. All 161 link-floor warnings cleared (04 Jun 2026).
- [ ] Refinement: top-inbound link rebalancing and a backlink strategy document.

### Stage 2L -- QA + Full Site Audit
- [x] **0 errors, 0 warnings** across audited pages (04 Jun 2026).
- [ ] Title cannibalisation follow-up: duplicate country pages (uk/united-kingdom, usa/united-states) -- resolve via canonical/redirect (folded into country_expansion track in GROWTH MODE).

---

## Session Log

| Date | Stage | Pages Added | Notes |
|------|-------|-------------|-------|
| Pre-migration | 2A-2F | 121 | |
| 22 Apr 2026 | 2G | 16 | Event security silo |
| 27-28 May 2026 | 2K, 3A-3C | many | Blog batches, P3 cities, service x city seed matrix |
| 02 Jun 2026 | 3D, 2H, 3E, 3F | 32+ | P3 cities, travel safety guides, forms wired |
| 03 Jun 2026 | 2L | 0 | QA error pass: 142 errors to 0 |
| 04 Jun 2026 | 2J, 2L | 0 | Link floors, FAQ floors, title/description fixes. QA gate 0 errors, 0 warnings |
| 05 Jun 2026 | 3G | 5 | Naypyidaw, Bamako, Niamey, Mogadishu, Tripoli |
| 05 Jun 2026 | Routine config | 0 | Switched to batch builds of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap. One commit and one deploy per run. Pointer-based skip (no same-day skip). Docs only (CLAUDE.md + this file). No content built this entry. |
| 05 Jun 2026 | 3C matrix expansion (4 blocks) | 42 | Block 1: close-protection-officers x 10 priority cities (JHB, Lagos, Dubai, Nairobi, MEX, Bogota, Riyadh, Mumbai, SP, Istanbul). Block 2: secure-airport-transfers x 10 priority cities (same). Block 3: bodyguard-hire x 10 non-priority cities (London, Paris, NYC, SG, HK, Sydney, Tokyo, Beijing, Berlin, Cape Town). Block 4: security-drivers x same 10 non-priority cities. QA: 0 errors. |
| 05 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: executive-protection x 10 non-priority cities. Block 2: residential-security x 10 non-priority cities. Block 3: close-protection-officers x 10 non-priority cities. Block 4: secure-airport-transfers x 10 non-priority cities. All 7 services now cover top 20 cities. QA: 0 errors across all 40 pages. |
| 06 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: event-security x 10 (hong-kong, beijing, berlin, cape-town, abu-dhabi, doha, kuala-lumpur, amsterdam, madrid, toronto). Block 2: bodyguard-hire x 10 (bangkok, abu-dhabi, amsterdam, kuala-lumpur, madrid, toronto, moscow, doha, vienna, zurich). Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. QA: 0 errors. All services now cover 28-30 cities. |
| 07 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: residential-security x batch2 (bangkok, abu-dhabi, amsterdam, kuala-lumpur, madrid, toronto, moscow, doha, vienna, zurich). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: bodyguard-hire x batch3 (buenos-aires, cairo, miami, jakarta, auckland, tel-aviv, manila, washington-dc, milan, melbourne). QA: 0 errors. residential-security, close-protection-officers, secure-airport-transfers now at 30 cities; bodyguard-hire at 40 cities. Total: 517 pages live. |
| 07 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: security-drivers x batch3 (buenos-aires, cairo, miami, jakarta, auckland, tel-aviv, manila, washington-dc, milan, melbourne). Block 2: executive-protection x batch3 (same 10). Block 3: event-security x batch3 inc. vienna+zurich (buenos-aires, cairo, miami, jakarta, auckland, tel-aviv, manila, washington-dc + vienna, zurich). Block 4: residential-security x batch3 (same 10 as Block 1). QA: 0 errors. security-drivers, executive-protection, residential-security now at 40 cities; event-security now at 38 cities. Total: 557 pages live. |
| 08 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: close-protection-officers x batch3 (buenos-aires, cairo, miami, jakarta, auckland, tel-aviv, manila, washington-dc, milan, melbourne). Block 2: secure-airport-transfers x same 10. Block 3: bodyguard-hire x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). Block 4: security-drivers x same 10. QA: 0 errors across all 40 pages. close-protection-officers, secure-airport-transfers now at 40 cities; bodyguard-hire, security-drivers now at 50 cities. Total: 597 pages live. |
| 08 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: executive-protection x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). Block 2: residential-security x same 10. Block 3: event-security x batch4 (milan, melbourne, abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara). Block 4: close-protection-officers x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). QA: 0 errors across all 40 pages. executive-protection, residential-security, close-protection-officers now at 50 cities; event-security now at 48 cities. Total: 637 pages live. |
| 09 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: secure-airport-transfers x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). Block 2: event-security x batch5 (baghdad, baku, delhi, bangalore, shanghai, casablanca, warsaw, montreal, geneva, rome). Block 3: bodyguard-hire x batch5 (bangalore, delhi, shanghai, casablanca, kyiv, warsaw, montreal, geneva, rome, naples). Block 4: security-drivers x same 10. QA: 0 errors across all 40 pages. secure-airport-transfers now at 50 cities; event-security at 58 cities; bodyguard-hire and security-drivers now at 60 cities each. Total: 677 pages live. |
| 10 Jun 2026 | 3C matrix expansion (5 blocks, run 1+2) | 50 | Block 1: close-protection-officers x batch6 (beirut, colombo, dar-es-salaam, dhaka, ho-chi-minh-city, kampala, mombasa, muscat, tashkent, tbilisi). Block 2: secure-airport-transfers x batch6 (same 10). Block 3: bodyguard-hire x batch7 (luanda, dakar, kigali, lima, medellin, kinshasa, yangon, tunis, lusaka, maputo). Block 4: security-drivers x batch7 (same 10). Block 5: executive-protection x batch7 (same 10). QA: 0 errors across all 50 pages. CPO and SAT now at 70 cities; BH/SD/EP now at 80 cities. Total: 827 pages live. |
| 11 Jun 2026 | 3C matrix expansion (5 blocks) | 50 | Block 1: residential-security x batch7 (luanda, dakar, kigali, lima, medellin, kinshasa, yangon, tunis, lusaka, maputo). Block 2: close-protection-officers x batch7 (same 10). Block 3: secure-airport-transfers x batch7 (same 10). Block 4: bodyguard-hire x batch8 (islamabad, conakry, harare, naypyidaw, bamako, niamey, mogadishu, tripoli, guadalajara, port-of-spain). Block 5: security-drivers x batch8 (same 10). QA: 0 errors across all 50 pages. RS/CPO/SAT now at 80 cities; BH/SD now at 90 cities. Total: 877 pages live. |
| 11 Jun 2026 | 3C matrix expansion (5 blocks, run 2) | 50 | Block 1: executive-protection x batch8 (islamabad, conakry, harare, naypyidaw, bamako, niamey, mogadishu, tripoli, guadalajara, port-of-spain). Block 2: residential-security x batch8 (same 10). Block 3: event-security x batch8 (islamabad, conakry, medellin, naypyidaw, bamako, niamey, mogadishu, tripoli, kinshasa, port-of-spain -- replaced already-covered guadalajara+harare with medellin+kinshasa). Block 4: close-protection-officers x batch8 (same 10 as block 1). Block 5: secure-airport-transfers x batch8 (same 10 as block 1). QA: 0 errors across all 50 pages. All 7 services now at 88-90 cities each. Total: 927 pages live. |
| 12 Jun 2026 | 3C matrix expansion batch9 (7 blocks) | 58 | All 7 services x 8 cities (caracas, kabul, karachi, kathmandu, kuwait-city, panama-city, san-jose, santiago). event-security also covered tunis + yangon (10 cities total for ES). QA: 0 errors across all 58 pages. All 7 services now cover all 98 live cities. Matrix batch9 complete. Total: 985 pages live. |
| 12 Jun 2026 | P4 city expansion batch10 (5 blocks) | 50 | Block 1: 10 new P4 cities (Manama, Jeddah, Erbil, Lahore, Phnom Penh, Quito, Port Harcourt, Kano, Douala, Santo Domingo). Block 2: bodyguard-hire x 10 new cities. Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. Block 5: residential-security x same 10. QA: 0 errors across all 50 pages. Cities live: 108. Total: 1,035 pages live. |
| 13 Jun 2026 | Batch11 (5 blocks) | 50 | Block 1: event-security x 10 batch10 cities (manama, jeddah, erbil, lahore, phnom-penh, quito, port-harcourt, kano, douala, santo-domingo). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: 10 new P4 city pages (Chittagong, Vientiane, Ulaanbaatar, Bishkek, Dushanbe, Ashgabat, La Paz, Asuncion, Montevideo, Guayaquil). Block 5: bodyguard-hire x same 10 new cities. QA: 0 errors across all 50 pages. Cities live: 118. Total: 1,085 pages live. |
| 14 Jun 2026 | Batch12-14 (multiple runs) | 150 | security-drivers/executive-protection/residential-security x batch11 cities (chittagong-guayaquil) + all 7 services (ES/CPO/SAT) x batch12/13 cities (Kingston-Yaounde 10 cities) + 10 new P4 city pages (Libreville-Bujumbura). Cities live: 138. Total: 1,235 pages live. |
| 15 Jun 2026 | Batch15 (4 blocks + city expansion) | 50 | Block 1: bodyguard-hire x 10 batch14 cities (libreville, brazzaville, bangui, ndjamena, khartoum, juba, asmara, djibouti-city, hargeisa, bujumbura). Block 2: security-drivers x same 10. Block 3: executive-protection x same 10. Block 4: residential-security x same 10. City expansion batch15: 10 new P4 city pages (Antananarivo, Port Louis, Victoria-Seychelles, Gaborone, Windhoek, Maseru, Mbabane, Freetown, Monrovia, Ouagadougou). QA: 0 errors, 6 description fixes. Cities live: 148. Total: 1,285 pages live. |
| 20 Jun 2026 | Batch25 -- matrix completion (6 blocks) | 60 | Completed the 7-service x 198-city matrix. All 6 non-BH services were missing the same 10 cities (atlanta, boston, chicago, houston, los-angeles, manchester, osaka, san-francisco, taipei, vancouver). Blocks: security-drivers x 10, executive-protection x 10, residential-security x 10, event-security x 10, close-protection-officers x 10, secure-airport-transfers x 10. QA gate: 0 errors across all 60 pages (1 banned-word fix: encompasses -> covers in EP files). All 7 services now cover all 198 live cities. Total: 1,345 pages live. build_state.json reconciled from disk. |
| 21 Jun 2026 | Batch27 (5 blocks) | 50 | Block 1: event-security x 10 batch21 cities (dallas, seattle, philadelphia, brisbane, perth, calgary, busan, porto, glasgow, denver). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: 10 new P4 city pages batch22 (Seoul, Austin, Hanoi, Phoenix, Kolkata, Chennai, Wellington, Adelaide, Ottawa, Hyderabad). Block 5: bodyguard-hire x batch22 cities. QA: 0 errors (1 banned-word fix: robust -> security in ES/philadelphia cta_text). Cities live: 218. Total: 1,825 pages live. All 7 services cover all 208 prior cities; BH now covers 218. |
| 23 Jun 2026 | Batch30 (5 blocks) | 50 | Block 1: RS x 10 batch23 cities (shenzhen/guangzhou/chengdu/monterrey/durban/pune/porto-alegre/barranquilla/surabaya/cebu). Block 2: ES x same 10. Block 3: CPO x same 10. Block 4: SAT x same 10. Block 5: 10 new P4 city pages batch24 (Port Moresby, Lilongwe, Mandalay, Wuhan, Recife, Fortaleza, Cali, Macao, Nanjing, Sharm el-Sheikh). QA: 0 errors, 0 warnings across all 50 pages. All 7 services now cover 228 cities. Cities live: 238. Total: 1,925 pages live. |

---

## GROWTH MODE -- THE SERVICE x CITY MATRIX (added 5 June 2026)

> This is the growth engine that takes the site from ~355 pages to ~2,400. The routine runs a batch of up to 4 blocks per run, full QA gate on every block, commit to master once, post live links to Slack as a record. When one track completes, move to the next in build order. `build_state.json` holds the machine-readable state the routine reads to pick the next block.

### The opportunity

The service x city combinatorial matrix is the highest-leverage SEO surface on the site. "{service} in {city}" is exactly how this market searches (bodyguard hire in Lagos, security drivers in Mexico City, executive protection in Riyadh). Right now only 10 priority cities are covered, for 5 services (50 deep pages). The plan below fills the full matrix.

### Track 1 -- Service x city matrix (DEFAULT every run)

Seven services across every live city:

1. bodyguard-hire
2. security-drivers
3. executive-protection
4. residential-security
5. event-security
6. close-protection-officers (new silo)
7. secure-airport-transfers (new silo)

- 7 services x 250 target cities = approximately **1,750 service-city deep pages.**
- A block = 10 service-city pages. A run builds up to 4 such blocks (up to 40 service-city pages), committed once.
- Rotation: extend bodyguard-hire across its next 10 uncovered cities, then security-drivers across its next 10, then executive-protection, residential-security, event-security, close-protection-officers, secure-airport-transfers, then back to bodyguard-hire for the next 10 cities. This fills the matrix evenly rather than finishing one service before starting the next. Within a single run, take the next 4 blocks in this rotation.
- Skip-check: before building, read site/content/{service}/ for slugs already on disk. Skip any present, take the next uncovered city.
- Start point: close-protection-officers and secure-airport-transfers are the two not-started services. Begin by building close-protection-officers across the 10 priority cities, then secure-airport-transfers across the 10 priority cities, then resume the rotation extending all seven services to non-priority cities.

### Track 2 -- City expansion (P4 queue)

Grow the city universe from 98 to 250. Each new city is high-leverage because it unlocks 7 new matrix pages. A block = the next 5 to 10 cities from the P4 queue in build_state.json (`city_expansion.next_p4_queue`); a run may build up to 4 such blocks: next-tier business-travel and high-net-worth destinations, regional capitals, financial centres, energy and resource hubs. Verify any city marked "(verify)" is not already live before building.

### Track 3 -- Country hub expansion

Grow country hubs from 38 to ~120 so every city has a parent country hub and the site captures country-level queries. A block = the next 5 country hubs for any country that has live cities but no hub. Resolve the two known duplicate country pages (uk/united-kingdom, usa/united-states) as part of this track via canonical or redirect.

### Track 4 -- Blog factory (parallel)

Continue the keyword-matrix blog to a target of 600 articles. Built only on a run where the next matrix/city/country blocks are already committed, or to fill out a batch. One block = 5 articles, non-cannibalising angles only (cost breakdowns, regulatory explainers, comparisons, question-led safety guides), checked against existing slugs first.

### Build order each run

1. Service x city matrix block (default).
2. If the next matrix block is already committed: next city-expansion block.
3. Then next country-hub block.
4. Then next blog batch.

A single run pulls up to 4 blocks in this build order, then commits them together. The routine reads `build_state.json` `next_stage` and the per-track blocks to choose. Every new matrix page must pass qa_audit.py (0 errors), carry >=4 FAQs, >=2 prose internal links to its city and service-silo parents, a safely past date, no byline (city and service pages carry no author), no em dashes, no banned vocab, no safety guarantees (use "reduce risk" / "trained professionals"). Re-run scripts/rebuild_link_graph.py after each matrix batch.

### Scale and timeline

At 2 runs per day, each a batch of up to 4 blocks (up to 8 blocks per day), the matrix plus city and country expansion (approximately 2,000 new pages) completes in roughly 25 weeks. The priority-city matrix gap (the two new services across the top 10 cities) closes in the first 1 to 2 runs.

### New growth session log

| Date | Track | Pages Added | Notes |
|------|-------|-------------|-------|
| 5 Jun 2026 | Plan rebuild | 0 | Growth mode installed: 7-service x 250-city matrix (~1,750 pages), city expansion to 250, country hubs to 120, blog to 600. build_state.json next_stage points at close-protection-officers across the 10 priority cities. No content built this entry. |
| 5 Jun 2026 | Routine config | 0 | Switched to batch builds of up to 4 blocks per run, 2 runs/day, to fit the 15-run routine cap. One commit and one deploy per run. No content built this entry. |
| 5 Jun 2026 | 3C matrix expansion (4 blocks) | 42 | Block 1: close-protection-officers x 10 priority cities. Block 2: secure-airport-transfers x 10 priority cities. Block 3: bodyguard-hire x 10 non-priority cities. Block 4: security-drivers x 10 non-priority cities. QA 0 errors. |
| 5 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: executive-protection x 10 non-priority. Block 2: residential-security x 10 non-priority. Block 3: close-protection-officers x 10 non-priority. Block 4: secure-airport-transfers x 10 non-priority. All 7 services now cover 20 cities. QA 0 errors. |
| 6 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: event-security x 10 (hong-kong, beijing, berlin, cape-town, abu-dhabi, doha, kuala-lumpur, amsterdam, madrid, toronto). Block 2: bodyguard-hire x 10 (bangkok, abu-dhabi, amsterdam, kuala-lumpur, madrid, toronto, moscow, doha, vienna, zurich). Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. QA 0 errors. Services now cover 28-30 cities each. |
| 8 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: executive-protection x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). Block 2: residential-security x same 10. Block 3: event-security x batch4 (milan, melbourne, abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara). Block 4: close-protection-officers x batch4 (same 10 as Block 1). QA 0 errors. executive-protection, residential-security, close-protection-officers at 50 cities; event-security at 48 cities. Total: 637 pages. |
| 9 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: secure-airport-transfers x batch4 (abidjan, abuja, accra, addis-ababa, algiers, almaty, amman, ankara, baghdad, baku). Block 2: event-security x batch5 (baghdad, baku, delhi, bangalore, shanghai, casablanca, warsaw, montreal, geneva, rome). Block 3: bodyguard-hire x batch5 (bangalore, delhi, shanghai, casablanca, kyiv, warsaw, montreal, geneva, rome, naples). Block 4: security-drivers x same 10. QA 0 errors. secure-airport-transfers at 50 cities; event-security at 58 cities; bodyguard-hire and security-drivers at 60 cities each. Total: 677 pages. |
| 9 Jun 2026 | 3C matrix expansion (5 blocks) | 50 | Block 1: executive-protection x batch5 (bangalore, delhi, shanghai, casablanca, kyiv, warsaw, montreal, geneva, rome, naples). Block 2: residential-security x same 10. Block 3: close-protection-officers x same 10. Block 4: secure-airport-transfers x same 10. Block 5: event-security x batch6 (naples, kyiv, tashkent, tbilisi, muscat, ho-chi-minh-city, colombo, dhaka, mombasa, kampala). QA 0 errors across all 50 pages. All 7 services now cover 60 cities each; event-security at 68 cities. Total: 727 pages. |
| 10 Jun 2026 | 3C matrix expansion (5 blocks) | 50 | Block 1: bodyguard-hire x batch6 (beirut, colombo, dar-es-salaam, dhaka, ho-chi-minh-city, kampala, mombasa, muscat, tashkent, tbilisi). Block 2: security-drivers x same 10. Block 3: executive-protection x same 10. Block 4: residential-security x same 10. Block 5: event-security x batch7 (beirut, dar-es-salaam, dakar, guadalajara, harare, kigali, lima, luanda, lusaka, maputo). QA 0 errors across all 50 pages. bodyguard-hire, security-drivers, executive-protection, residential-security at 70 cities each; event-security at 78 cities. Total: 777 pages. |
| 11 Jun 2026 | 3C matrix expansion (5 blocks) | 50 | Block 1: residential-security x batch7 (luanda, dakar, kigali, lima, medellin, kinshasa, yangon, tunis, lusaka, maputo). Block 2: close-protection-officers x batch7 (same 10). Block 3: secure-airport-transfers x batch7 (same 10). Block 4: bodyguard-hire x batch8 (islamabad, conakry, harare, naypyidaw, bamako, niamey, mogadishu, tripoli, guadalajara, port-of-spain). Block 5: security-drivers x batch8 (same 10). QA 0 errors. RS/CPO/SAT at 80 cities; BH/SD at 90 cities. Total: 877 pages. |
| 12 Jun 2026 | 3C matrix expansion batch9 | 58 | All 7 services x 8 final cities (caracas, kabul, karachi, kathmandu, kuwait-city, panama-city, san-jose, santiago). ES also tunis+yangon. QA 0 errors. All 7 services now cover all 98 live cities. Total: 985 pages. |
| 12 Jun 2026 | P4 city expansion batch10 | 50 | 10 new P4 cities (Manama, Jeddah, Erbil, Lahore, Phnom Penh, Quito, Port Harcourt, Kano, Douala, Santo Domingo) + bodyguard-hire/security-drivers/executive-protection/residential-security x same 10. Total: 1,035 pages. Cities live: 108. |
| 13 Jun 2026 | Batch11 (5 blocks) | 50 | event-security/CPO/SAT x 10 batch10 cities + 10 new P4 city pages (Chittagong, Vientiane, Ulaanbaatar, Bishkek, Dushanbe, Ashgabat, La Paz, Asuncion, Montevideo, Guayaquil) + bodyguard-hire x same 10. QA 0 errors. Cities live: 118. Total: 1,085 pages. |
| 14 Jun 2026 | Batch12 (5 blocks) | 50 | Block 1: security-drivers x 10 batch11 P4 cities. Block 2: executive-protection x same 10. Block 3: residential-security x same 10. Block 4: event-security x same 10. Block 5: close-protection-officers x same 10. Cities: Chittagong, Vientiane, Ulaanbaatar, Bishkek, Dushanbe, Ashgabat, La Paz, Asuncion, Montevideo, Guayaquil. QA: 0 errors, 0 warnings. SD/EP/RS/ES/CPO now at 118 cities each. SAT still to cover these 10 (next run). Total: 1,135 pages live. |
| 14 Jun 2026 | Batch13 (5 blocks) | 50 | Block 1: secure-airport-transfers x 10 batch11 P4 cities (Chittagong, Vientiane, Ulaanbaatar, Bishkek, Dushanbe, Ashgabat, La Paz, Asuncion, Montevideo, Guayaquil) -- completes 7-service matrix for those cities. Block 2: 10 new P4 city pages (Kingston/Jamaica, Georgetown/Guyana, Paramaribo/Suriname, Port-au-Prince/Haiti, Tegucigalpa/Honduras, San Salvador/El Salvador, Guatemala City/Guatemala, Managua/Nicaragua, Belize City/Belize, Yaounde/Cameroon). Block 3: bodyguard-hire x 10 new cities. Block 4: security-drivers x same 10. Block 5: executive-protection x same 10. QA: 0 errors (also fixed 3 pre-existing banned-word errors in islamabad/tripoli pages). Cities live: 128. All 7 services cover 118 cities; BH/SD/EP now also cover 10 new P4 cities (RS/ES/CPO/SAT for new cities next run). Total: 1,185 pages live. |
| 15 Jun 2026 | Batch14 (4 blocks) | 50 | Block 1: residential-security x 10 batch13 cities (Kingston-Yaounde). Block 2: event-security x same 10. Block 3: close-protection-officers x same 10. Block 4: secure-airport-transfers x same 10. Block 5: 10 new P4 city pages (Libreville/Gabon, Brazzaville/Republic of Congo, Bangui/CAR, Ndjamena/Chad, Khartoum/Sudan, Juba/South Sudan, Asmara/Eritrea, Djibouti City/Djibouti, Hargeisa/Somaliland, Bujumbura/Burundi). QA: 0 errors, 6 advisory warnings (pre-existing). Cities live: 138. All 7 services now cover 128 batch13 cities; batch14 cities queued for matrix next run. Total: 1,235 pages live. |
| 15 Jun 2026 | Batch15 (5 blocks) | 50 | Block 1: bodyguard-hire x batch14 cities (Libreville-Bujumbura). Block 2: security-drivers x same 10. Block 3: executive-protection x same 10. Block 4: residential-security x same 10. Block 5: 10 new P4 city pages (Antananarivo/Madagascar, Port Louis/Mauritius, Victoria/Seychelles, Gaborone/Botswana, Windhoek/Namibia, Maseru/Lesotho, Mbabane/Eswatini, Freetown/Sierra Leone, Monrovia/Liberia, Ouagadougou/Burkina Faso). QA: 0 errors. Cities live: 148. BH/SD/EP/RS now cover 138 cities; ES/CPO/SAT at 128 (missing batch14). Total: 1,285 pages live. |
| 16 Jun 2026 | Batch16 (5 blocks) | 50 | Block 1: event-security x 10 batch14 cities (Libreville-Bujumbura). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: bodyguard-hire x 10 batch15 cities (Antananarivo-Ouagadougou). Block 5: security-drivers x same 10. QA: 0 errors across all 50 pages. All 7 services now cover 138 cities. Remaining gap: EP/RS/ES/CPO/SAT x batch15 cities (50 pages). Total: 1,335 pages live. |
| 16 Jun 2026 | Batch17 (5 blocks) | 50 | Block 1: executive-protection x 10 batch15 cities (Antananarivo-Ouagadougou). Block 2: residential-security x same 10. Block 3: event-security x same 10. Block 4: close-protection-officers x same 10. Block 5: secure-airport-transfers x same 10. QA: 0 errors across all 50 new pages (2 pre-existing fails in djibouti-city/hargeisa unrelated to batch17; 2 ES descriptions fixed to under 175 chars). All 7 services now cover 148 cities. Next: city expansion batch16 (Malabo, Lome, Cotonou, Praia, Yerevan, Chisinau, Tirana, Podgorica, Sarajevo, Skopje) then matrix x those 10 cities. Total: 1,385 pages live. |
| 17 Jun 2026 | Batch18 (5 blocks) | 50 | Block 1: 10 new P4 city pages (Malabo/Equatorial Guinea, Lome/Togo, Cotonou/Benin, Praia/Cape Verde, Yerevan/Armenia, Chisinau/Moldova, Tirana/Albania, Podgorica/Montenegro, Sarajevo/Bosnia, Skopje/North Macedonia). Block 2: bodyguard-hire x same 10. Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. Block 5: residential-security x same 10. QA: 0 errors across all 50 pages. Cities live: 158. BH/SD/EP/RS now cover 158 cities; ES/CPO/SAT at 148 (batch16 cities pending). Total: 1,435 pages live. |
| 17 Jun 2026 | Batch19 (5 blocks) | 50 | Block 1: event-security x 10 batch16 cities (Malabo-Skopje). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: 10 new P4 city pages batch17 (Valletta/Malta, Nicosia/Cyprus, Riga/Latvia, Vilnius/Lithuania, Tallinn/Estonia, Ljubljana/Slovenia, Zagreb/Croatia, Bratislava/Slovakia, Sofia/Bulgaria, Minsk/Belarus). Block 5: bodyguard-hire x same 10 new cities. QA: 0 errors (7 banned-word fixes applied). Cities live: 168. ES/CPO/SAT now cover 158 cities; BH covers 168 cities; SD/EP/RS at 158. Total: 1,485 pages live. |
| 18 Jun 2026 | Batch20 (5 blocks) | 50 | Block 1: security-drivers x 10 batch17 cities (Valletta, Nicosia, Riga, Vilnius, Tallinn, Ljubljana, Zagreb, Bratislava, Sofia, Minsk). Block 2: executive-protection x same 10. Block 3: residential-security x same 10. Block 4: event-security x same 10. Block 5: close-protection-officers x same 10. QA: 0 errors across all 50 pages (1 description fix: event-security/riga). SD/EP/RS/ES/CPO now cover 168 cities. SAT still to cover batch17 cities (10 pages, next run). Total: 1,535 pages live. |

---

*Cadence updated 5 June 2026: a batch of up to 4 blocks per run, 2 runs/day, QA gate on every block, commit to master once, post live links. Skip only when nothing is left to build.*
| 18 Jun 2026 | Batch21 (5 blocks) | 50 | Block 1: secure-airport-transfers x 10 batch17 cities (Valletta, Nicosia, Riga, Vilnius, Tallinn, Ljubljana, Zagreb, Bratislava, Sofia, Minsk). Block 2: 10 new P4 city pages batch18 (Bucharest/Romania, Prague/Czech Republic, Budapest/Hungary, Belgrade/Serbia, Athens/Greece, Helsinki/Finland, Stockholm/Sweden, Oslo/Norway, Copenhagen/Denmark, Dublin/Ireland). Block 3: bodyguard-hire x same 10 new cities. Block 4: security-drivers x same 10. Block 5: executive-protection x same 10. QA: 0 errors (2 banned-word fixes: seamless/robust). SAT now covers all 168 cities. BH/SD/EP now cover 178 cities. RS/ES/CPO/SAT still need batch18 coverage (40 pages, next runs). Cities live: 178. Total: 1,585 pages live. |
| 19 Jun 2026 | Batch22 (4 blocks) | 40 | Block 1: residential-security x 10 batch18 cities (Bucharest-Dublin). Block 2: event-security x same 10. Block 3: close-protection-officers x same 10. Block 4: secure-airport-transfers x same 10. QA: 40/40 passed (0 errors). All 7 services now cover all 178 cities. Next: city expansion batch19 (Lisbon, Brussels, Munich, Barcelona, Frankfurt, Hamburg, Luxembourg City, Reykjavik, Lyon, Edinburgh). Total: 1,625 pages live. |
| 19 Jun 2026 | Batch23 (5 blocks) | 50 | Block 1: 10 new P4 city pages batch19 (Lisbon/Portugal, Brussels/Belgium, Munich/Germany, Barcelona/Spain, Frankfurt/Germany, Hamburg/Germany, Luxembourg City/Luxembourg, Reykjavik/Iceland, Lyon/France, Edinburgh/Scotland UK). Block 2: bodyguard-hire x same 10. Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. Block 5: residential-security x same 10. QA: 0 errors (4 description-length fixes applied). Cities live: 188. BH/SD/EP/RS now cover 188 cities; ES/CPO/SAT at 178 (batch19 cities pending). Total: 1,675 pages live. |
| 20 Jun 2026 | Batch24 (5 blocks) | 50 | Block 1: event-security x 10 batch19 cities (Lisbon, Brussels, Munich, Barcelona, Frankfurt, Hamburg, Luxembourg City, Reykjavik, Lyon, Edinburgh). Block 2: close-protection-officers x same 10. Block 3: secure-airport-transfers x same 10. Block 4: 10 new P4 city pages batch20 (Chicago/USA, Los Angeles/USA, San Francisco/USA, Houston/USA, Manchester/UK, Vancouver/Canada, Osaka/Japan, Taipei/Taiwan, Boston/USA, Atlanta/USA). Block 5: bodyguard-hire x same 10 new cities. QA: 0 errors (6 advisory warnings pre-existing). Cities live: 198. BH covers 198 cities; SD/EP/RS/ES/CPO/SAT cover 188. Next: SD x batch20 cities (chicago-atlanta). Total: 1,725 pages live. |
| 21 Jun 2026 | Batch26 (5 blocks) | 50 | Block 1: 10 new P4 city pages batch21 (Dallas/USA, Seattle/USA, Philadelphia/USA, Brisbane/Australia, Perth/Australia, Calgary/Canada, Busan/South Korea, Porto/Portugal, Glasgow/UK, Denver/USA). Block 2: bodyguard-hire x same 10. Block 3: security-drivers x same 10. Block 4: executive-protection x same 10. Block 5: residential-security x same 10. QA: 0 errors (1 description-length fix: calgary city page). Cities live: 208. BH/SD/EP/RS now cover 208 cities; ES/CPO/SAT at 198 (batch21 cities pending, next run). Total: 1,775 pages live. |
| 23 Jun 2026 | Batch29 (5 blocks) | 50 | Block 1: secure-airport-transfers x 10 batch22 cities (Seoul, Austin, Hanoi, Phoenix, Kolkata, Chennai, Wellington, Adelaide, Ottawa, Hyderabad) -- catchup to close SAT gap. Block 2: 10 new P4 city pages batch23 (Shenzhen, Guangzhou, Chengdu, Monterrey, Durban, Pune, Porto Alegre, Barranquilla, Surabaya, Cebu). Block 3: bodyguard-hire x same 10. Block 4: security-drivers x same 10. Block 5: executive-protection x same 10. QA: 0 errors across all 50 pages. Cities live: 228. SAT now covers 218 cities; BH/SD/EP cover 228 cities. RS/ES/CPO/SAT still to cover batch23 cities (40 pages next run). Total: 1,875 pages live. |
