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
| 06 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: event-security x 10 (HK, Beijing, Berlin, Cape Town, Amsterdam, Madrid, Vienna, Doha, KL, Cairo). Blocks 2-4: bodyguard-hire, security-drivers, executive-protection x 10 cities (Amsterdam, Madrid, Vienna, Moscow, Bangkok, Doha, KL, Delhi, Cairo, Ankara). QA: 0 errors, 0 warnings. |

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
| 6 Jun 2026 | 3C matrix expansion (4 blocks) | 40 | Block 1: event-security x 10 cities (hong-kong, beijing, berlin, cape-town + amsterdam, madrid, vienna, doha, kuala-lumpur, cairo). Block 2: bodyguard-hire x 10 cities (amsterdam, madrid, vienna, moscow, bangkok, doha, kuala-lumpur, delhi, cairo, ankara). Block 3: security-drivers x same 10 cities. Block 4: executive-protection x same 10 cities. QA 0 errors, 0 warnings. |

---

*Cadence updated 5 June 2026: a batch of up to 4 blocks per run, 2 runs/day, QA gate on every block, commit to master once, post live links. Skip only when nothing is left to build.*
