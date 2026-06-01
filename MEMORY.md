# CloseProtectionHire.com — Project Memory

Generated: April 2026 — migrated from Research monorepo to standalone VS Code instance. Last updated: June 2026.

---

## 1. Site Overview

**Site:** CloseProtectionHire.com
**Niche:** Security services — bodyguard hire, executive protection, security drivers, event security, residential security
**Target audience:** Corporate travellers, executives, event organisers, and HNWIs operating in or travelling to high-risk cities globally
**Primary goal:** Lead generation via organic SEO. Capture enquiries for vetted security service bookings.
**Tech stack:** Hugo v0.160.1 extended (Windows/AMD64), Go HTML templates, Markdown content, YAML front matter
**Build command:** `hugo --gc --minify` from within `site/`
**Deployment:** Hostinger via GitHub Actions OAuth (push to `main` triggers build-and-publish workflow; deploys `live` branch to `public_html/` automatically within ~3 minutes)
**Live URL:** closeprotectionhire.com
**Pages live:** ~280 (June 2026 estimate)

---

## 2. Build Decisions

- **Hugo over Next.js** — chosen for pure content-at-scale, zero JS complexity, fast builds.
- **GitHub Actions + Hostinger OAuth for deployment** — replaced legacy FTP workflow (May 2026) due to FTPS data-channel silent failure on Hostinger shared hosting. See ERRORS.md.
- **YAML front matter** (`---` delimiters) — consistent across all content files. TOML was used early; all new files use YAML.
- **Page bundle structure** — city and country pages use flat `.md` files under section directories (e.g. `cities/dubai.md`). Service x city pages similarly flat within their silo directories.
- **5 service silos** as primary content taxonomy: bodyguard-hire, executive-protection, security-drivers, event-security, residential-security.
- **Priority city set** for combinatorial matrix: Johannesburg, Lagos, Dubai, Nairobi, Mexico City, Bogota, Riyadh, Mumbai, Sao Paulo, Istanbul.
- **P1/P2/P3 city split** — 15 P1 cities first, then 25 P2, then P3 batches. ~80 city pages now live.
- **Risk data approach** — city risk profiles (JSON files in `data/`) drive location-specific content.
- **Blog author personas** — James Calloway (regulation, licensing, risk frameworks) and Marcus Webb (operational CP, secure transport, city safety). All blog articles carry one persona byline.
- **Cannibalisation rule** — blog articles must not duplicate topics already covered by Phase 3C service x city deep pages. Blog covers angles those pages do not: cost breakdowns, regulatory explainers, comparison pieces.

---

## 3. Content Completed (June 2026)

### Phase 1 — P1 Foundation (COMPLETE)
**P1 city pages (15):** Bangkok, Bogota, Dubai, Istanbul, Jakarta, Johannesburg, Karachi, Lagos, Manila, Mexico City, Moscow, Mumbai, Nairobi, Riyadh, Sao Paulo

**P1 country hub pages (15):** Brazil, Colombia, India, Indonesia, Kenya, Mexico, Nigeria, Pakistan, Philippines, Russia, Saudi Arabia, South Africa, Thailand, Turkey, UAE

**Service silo pages (5):** bodyguard-hire, executive-protection, security-drivers, event-security, residential-security

**Core pages:** about, contact, FAQ, network, privacy, terms, vetting-standards

**Risk assessments (18):** 15 city-specific + pre-travel, residential, venue-security

### Phase 2A-2F — P2 Expansion (COMPLETE)
**P2 city pages (25):** London, New York, Paris, Berlin, Tokyo, Hong Kong, Singapore, Sydney, Doha, Kuwait City, Abu Dhabi, Cape Town, Accra, Dar es Salaam, Addis Ababa, Lima, Buenos Aires, Santiago, Beijing, Shanghai, Delhi, Bangalore, Tel Aviv, Cairo, Casablanca

**P2 country hub pages (19):** United Kingdom, United States, France, Germany, Japan, China, Singapore, Australia, Qatar, Kuwait, Ghana, Tanzania, Ethiopia, Peru, Argentina, Chile, Israel, Egypt, Morocco

### Phase 2G — Event Security Silo (COMPLETE)
18 city-specific event-security pages total (16 original + 2 from Phase 3C gap fill)

### Phase 3A-3B — P3 Cities (COMPLETE, logged)
Amman, Abuja, KL, Dhaka, Muscat, HCMC, Luanda, Tbilisi, Naples, Rome, Miami, Toronto, Vienna, Warsaw, Colombo, Baku, Kinshasa, Mombasa, Geneva, Washington DC, Montreal, Zurich, Milan, Madrid, Amsterdam, Ankara, Kigali, Yangon

### P3 Cities — Additional (found in repo, unlogged)
Baghdad, Beirut, Caracas, Kabul, Kampala, Kathmandu, Kyiv, Auckland, Melbourne

### Phase 3C — Service x City Matrix (COMPLETE)
5 silos x 10 priority cities = 50 deep service pages + index files

### Phase 2K — Blog Factory (IN PROGRESS)
46 articles live across 8 batches

---

## 4. Remaining Work (Priority Order)

See `bodyguard-cascading-build-plan.html` for full detail and `BUILD-PLAN.md` for checklist.

1. **Stage 2L** — Full QA pass: run qa_audit.py, check_titles.py, check_descriptions.py across all ~280 pages. Fix any YMYL, em-dash, or cannibalisation issues found.
2. **Blog Batch 9** — 5 articles on: Lagos safety, female executives ME, Brazil regulations, Nairobi driver comparison, Bogota EP.
3. **Stage 2H** — Travel safety guides: 15 pages for P1 cities.
4. **Stage 2J** — Internal link graph: run rebuild_link_graph.py, resolve orphans and under-linked pages.
5. **Phase 3D** — P3 city expansion Batch 3: Dakar, Tunis, Algiers, Port of Spain, Panama City, San Jose (Costa Rica).
6. **Blog Batches 10-19** — Continue through keyword matrix.

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

### Front Matter Pattern (YAML)
```yaml
---
title: "Bodyguard Hire in Dubai | Hire Vetted Security Professionals"
description: "Planning travel or business in Dubai? Our vetted security professionals reduce risk in UAE's most complex environments. Get a free quote today."
date: 2024-01-01
draft: false
city: "Dubai"
country: "UAE"
---
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

- **Legacy FTP deploy** — FTPS data-channel silent failure on Hostinger shared host. Replaced with GitHub Actions OAuth. Do not re-enable. See ERRORS.md.
- **Rate limit crashes** — Rapid sequential API calls hit limits. Batch page creation in groups of 5-10 maximum.
- **Hugo public/ in git** — Do not commit the `public/` output directory.
- **TOML front matter** — Use YAML (`---`) not TOML (`+++`) for all new content files.
- **Safety guarantees in copy** — Phrases like "ensure your safety", "stay safe", "guaranteed protection" create legal liability and YMYL compliance issues.
- **Unattributed statistics** — Every crime index figure needs a named, dated source.
- **Cannibalisation** — Do not blog topics that duplicate service x city deep pages.
- **Test stubs left live** — Two test files (`auto-deploy-test.md`, `test-deploy.md`) exist in `site/content/cities/`. These should be cleaned up.

---

## 7. Open Questions / Pending Decisions

- **Test stub cleanup** — `site/content/cities/auto-deploy-test.md` and `site/content/cities/test-deploy.md` are live but serve no purpose. Delete or convert.
- **Unlogged city pages** — Baghdad, Beirut, Caracas, Kabul, Kampala, Kathmandu, Kyiv, Auckland, Melbourne are live but their quality has not been formally QA'd under the current standards. Flag for Stage 2L review.
- **Custom domain** — closeprotectionhire.com — confirm DNS and SSL are correctly pointed to Hostinger.
- **Operator vetting data** — `workforce/vetting_framework.md` defines Bronze/Silver/Gold tiers but no real operator data exists. Placeholder network content in use.
- **Blog author attribution** — Two author personas in use (Calloway, Webb). Confirm all 46 live articles carry correct byline and are not missing author front-matter field.
