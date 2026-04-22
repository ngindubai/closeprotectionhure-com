# CloseProtectionHire.com — Project Memory

Generated: April 2026 — migrated from Research monorepo to standalone VS Code instance.

---

## 1. Site Overview

**Site:** CloseProtectionHire.com
**Niche:** Security services — bodyguard hire, executive protection, security drivers, event security, residential security
**Target audience:** Corporate travellers, executives, event organisers, and HNWIs operating in or travelling to high-risk cities globally
**Primary goal:** Lead generation via organic SEO. Capture enquiries for vetted security service bookings.
**Tech stack:** Hugo v0.160.1 extended (Windows/AMD64), Go HTML templates, Markdown content, TOML front matter
**Build command:** `hugo --gc --minify` from within `site/`
**Deployment:** Surge.sh — `surge public closeprotectionhire.surge.sh` from within `site/`
**Live URL:** closeprotectionhire.surge.sh
**Surge account:** garethdeansomers@gmail.com (Student plan)
**Pages live at last deploy:** 121 pages, 1039 files, 392.6 MB

---

## 2. Build Decisions

- **Hugo over Next.js** — chosen for pure content-at-scale, zero JS complexity, fast builds (~1800-1900ms for 121 pages), and ease of programmatic page generation at volume.
- **Surge.sh for deployment** — fast, CLI-driven, no build pipeline required.
- **TOML front matter** (not YAML) — consistent across all content files. `+++` delimiters.
- **Page bundle structure** — city and country pages use `_index.md` inside named folders (e.g. `cities/dubai/_index.md`).
- **5 service silos** as primary content taxonomy: bodyguard-hire, executive-protection, security-drivers, event-security, residential-security.
- **P1/P2 city split** — 15 high-risk P1 cities built first, then 25 P2 cities in a second phase. All 40 now complete.
- **Risk data approach** — city risk profiles (JSON files in `data/`) drive location-specific content. Each city page references real crime indices, FCDO and US State Dept advisory levels.
- **bodyguard subagent** — a VS Code Copilot subagent was used for all build execution in the prior workspace. It must be manually recreated in the new standalone VS Code instance. See AGENTS.md.
- **Surge deploy workaround** — the bodyguard subagent cannot handle interactive Surge login prompts. Deploy is always run from the main terminal with an active Surge session, not via the subagent.

---

## 3. Pages Completed (121 pages)

### Phase 1 — P1 Foundation (COMPLETE)

**P1 city pages (15):** Bangkok, Bogota, Dubai, Istanbul, Jakarta, Johannesburg, Karachi, Lagos, Manila, Mexico City, Moscow, Mumbai, Nairobi, Riyadh, Sao Paulo

**P1 country hub pages (15):** Brazil, Colombia, India, Indonesia, Kenya, Mexico, Nigeria, Pakistan, Philippines, Russia, Saudi Arabia, South Africa, Thailand, Turkey, UAE

**Service silo pages (5):** bodyguard-hire, executive-protection, security-drivers, event-security, residential-security

**Core pages:** about, contact, FAQ, network, privacy, terms

**Risk assessments (18):** 15 city-specific + pre-travel, residential, venue-security

### Phase 2A-2F — P2 Expansion (COMPLETE)

**P2 city pages (25):** London, New York, Paris, Berlin, Tokyo, Hong Kong, Singapore, Sydney, Doha, Kuwait City, Abu Dhabi, Cape Town, Accra, Dar es Salaam, Addis Ababa, Lima, Buenos Aires, Santiago, Beijing, Shanghai, Delhi, Bangalore, Tel Aviv, Cairo, Casablanca

**P2 country hub pages (19):** United Kingdom, United States, France, Germany, Japan, China, Singapore, Australia, Qatar, Kuwait, Ghana, Tanzania, Ethiopia, Peru, Argentina, Chile, Israel, Egypt, Morocco

---

## 4. Pages Remaining (Priority Order)

See `bodyguard-cascading-build-plan.html` for full detail and `BUILD-PLAN.md` for checklist.

1. **Stage 2G** — Event security silo: city-specific event-security pages for all 15 P1 cities
2. **Stage 2H** — Travel safety guides batch 1: 15 pages for P1 cities
3. **Stage 2I** — Travel safety guides batch 2 + country-specific regulation guides
4. **Stage 2J** — Internal link graph audit + backlink outreach strategy
5. **Stage 2K** — Blog launch: 8 cornerstone articles targeting informational keywords
6. **Stage 2L** — Full QA + security audit + YMYL compliance check

---

## 5. Patterns to Follow

### Content Structure — City Page
- **H1:** "[Service Type] in [City] | Hire Vetted [Security Role]"
- **Opening (2-3 sentences):** city risk context, no safety guarantees
- **Risk overview section:** crime index, FCDO advisory level, US State Dept level, key risk factors
- **Service description:** what the service covers, what a vetted operator provides
- **Why use a local specialist:** city-specific operational reasoning
- **Our network:** brief operator quality statement
- **FAQ:** 4-5 questions with FAQ schema JSON-LD
- **CTA:** enquiry prompt or contact link

### Front Matter Pattern (TOML)
```toml
+++
title = "Bodyguard Hire in Dubai | Hire Vetted Security Professionals"
description = "Planning travel or business in Dubai? Our vetted security professionals reduce risk in UAE's most complex environments. Get a free quote today."
date = 2024-01-01
draft = false
city = "Dubai"
country = "UAE"
+++
```

### Internal Linking Pattern
- City pages link to: their country hub + at least one service silo page
- Service silo pages link to: top 3-5 most relevant city pages
- Risk assessments link to: related city pages + related service pages

### Risk Data Sources
- P1 city profiles: `data/city_risk_profiles.json`
- P2 city profiles: `data/city_risk_profiles_p2.json`
- FCDO advisories: `data/fcdo_advisories.json`
- US State Dept: `data/state_dept_data.json`
- Security regulations: `data/security_regulations_v1_backup.json`
- Keyword matrix: `data/keyword_matrix.json`

---

## 6. Mistakes Avoided

- **Surge deploy in subagent** — the subagent cannot complete the interactive email/password login. Always deploy from the main terminal.
- **Rate limit crashes** — rapid sequential subagent calls hit rate limits. Batch city page creation in groups of 5-10 maximum, not 15+ at once.
- **Hugo public/ in git** — do not commit the `public/` output directory. It regenerates from every build.
- **YAML front matter** — use TOML (`+++`) not YAML (`---`) for all content files.
- **Safety guarantees in copy** — phrases like "ensure your safety", "stay safe", "guaranteed protection" must be removed. They create legal liability and YMYL compliance issues.
- **Unattributed statistics** — every crime index figure, advisory level, or risk statistic needs a named, dated source.

---

## 7. Open Questions / Pending Decisions

- **Custom domain** — closeprotectionhire.com not yet pointed to Surge. DNS change pending.
- **Operator vetting data** — `workforce/vetting_framework.md` defines Bronze/Silver/Gold tiers but no real operator data exists yet. Placeholder network content in use.
- **Blog author attribution** — YMYL requires named authors. Author persona or byline strategy not yet decided. Needed before Stage 2K (blog launch).
- **LocalBusiness schema** — not yet confirmed as implemented on homepage.
- **bodyguard subagent** — must be manually recreated in the new standalone VS Code instance (see AGENTS.md for configuration).
