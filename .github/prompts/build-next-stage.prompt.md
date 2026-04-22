---
description: "Execute the next stage of the security-bodyguard website build. Reads the build plan, identifies the next TODO stage, loads relevant worker souls and research data, generates all deliverables, and marks the stage DONE. Use when: building the next chunk, executing next stage, continuing the build, 'go', 'next'."
agent: "agent"
---

# Build Next Stage — CloseProtectionHire.com

You are executing the next build stage for a programmatic SEO website targeting security services in high-risk cities globally.

## Step 1: Read the Build Plan

Open `bodyguard-cascading-build-plan.html` and find the stage tables. Identify the first stage with a `TODO` badge. That is the stage you will execute.

If a stage is already `IN PROGRESS`, resume that stage instead.

Record:
- Stage ID (e.g. 2H, 2I)
- Task numbers it covers
- Description and expected outputs
- Which workers are active for this stage

Also read `BUILD-PLAN.md` for the current session log and remaining checklist.

## Step 2: Load Worker Souls

Read the soul files for workers relevant to this stage. Only load what you need — not all 14 every time.

| Worker | Path | Load for stages involving... |
|--------|------|------|
| The Builder | `workforce/development/the-builder.md` | Templates, Hugo generation, deployment |
| The Wordsmith | `workforce/content/the-wordsmith.md` | Any content writing |
| The Chameleon | `workforce/content/the-chameleon.md` | ALL content stages (humaniser pass is always required) |
| The Interrogator | `workforce/content/the-interrogator.md` | FAQ generation |
| The Geographer | `workforce/intelligence/the-geographer.md` | Risk data, city profiles, geographic context |
| The Optimiser | `workforce/seo/the-optimiser.md` | SEO metadata, schema markup, E-E-A-T |
| The Connector | `workforce/seo/the-connector.md` | Internal linking, link graphs |
| The Auditor | `workforce/leadership/the-auditor.md` | QA, legal review, regulatory accuracy |
| The Architect | `workforce/leadership/the-architect.md` | Planning, orchestration, phase gates |
| The Librarian | `workforce/development/the-librarian.md` | Data management, schema |
| The Scout | `workforce/intelligence/the-scout.md` | Keyword research |
| The Spider | `workforce/intelligence/the-spider.md` | Web scraping, data extraction |
| The Analyst | `workforce/monitoring/the-analyst.md` | Analytics, performance tracking |
| The Watchdog | `workforce/monitoring/the-watchdog.md` | Security monitoring |

## Step 3: Load Research Data

For any content or template stage, read the relevant data files.

| Data | Path | Use for |
|------|------|---------|
| P1 city risk profiles | `data/city_risk_profiles.json` | Risk scores, crime, terrorism, kidnapping, safe/unsafe zones, emergency contacts |
| P2 city risk profiles | `data/city_risk_profiles_p2.json` | P2 city risk data |
| Security regulations | `data/security_regulations_v1_backup.json` | Firearms laws, licensing, foreign operator rules — BACKUP IS SOURCE OF TRUTH |
| Keyword matrix | `data/keyword_matrix.json` | Target keywords per city x silo, search volumes, SERP context |
| FCDO advisories | `data/fcdo_advisories.json` | UK government travel advisory levels |
| State Dept data | `data/state_dept_data.json` | US government travel advisory levels |
| Database schema | `data/database_schema.json` | Schema for city profiles, operators, regulations |
| Tech stack | `data/tech_stack.md` | Hugo architecture, template patterns |
| Competitor analysis | `data/competitors/competitor_analysis.html` | Competitor page structures to differentiate from |
| Vetting framework | `workforce/vetting_framework.md` | Bronze/Silver/Gold operator vetting criteria |

## Step 4: Mark IN PROGRESS

Update `bodyguard-cascading-build-plan.html`: change the current stage badge from `TODO` to `IN PROGRESS` (change `b-cyan` to `b-blue`, text to "IN PROGRESS").

## Step 5: Execute

Build all deliverables for the stage. Follow these rules:

### Content Rules
- No banned vocabulary: delve, tapestry, vibrant, crucial, comprehensive, meticulous, embark, robust, seamless, groundbreaking, leverage, synergy, transformative, paramount, multifaceted, myriad, cornerstone, reimagine, empower, catalyst, invaluable, bustling, nestled, realm
- No em dashes (zero tolerance)
- No safety guarantees or promises of guaranteed protection
- Authority voice: senior security consultant, not travel blog or military briefing
- Every factual claim needs a named, dated source or it gets cut
- Vary sentence rhythm. Short. Then longer ones. High burstiness.
- British English throughout

### Design Rules
- Dark professional palette: charcoal (#0d1117, #161b22), navy, slate. Not black-and-red.
- Clean sans-serif typography. White space. Clear hierarchy.
- Mobile-first.
- Confidence without aggression. Competence, discretion, professionalism.

### SEO Rules
- Unique title tag and meta description per page (rotate formulas, don't just swap city names)
- JSON-LD ProfessionalService schema on service pages
- Target keyword in: title, H1, first 100 words, one H2, meta description
- E-E-A-T signals: `[Author Name]` attribution, trust badges, source citations
- Front matter: TOML format between `+++` delimiters
- Internal links: minimum 2 per new page with descriptive anchor text

### File Output
- Hugo content goes into `site/content/[section]/` as markdown files
- Build command: `hugo --gc --minify` from `site/`
- Deploy command: `surge public closeprotectionhire.surge.sh` from `site/`
- Scripts that generate content live in `scripts/` — all must use skip-if-exists logic

### Business Logic Rules
- White-label model. Never expose subcontracted operator names.
- Quote-only pricing. Every pricing mention points to the enquiry form.
- Placeholders: `[Brand]` for business name, `[Author Name]` for expert author.

## Step 6: Mark DONE

After all deliverables are complete:
1. Update `bodyguard-cascading-build-plan.html`: change the stage badge from `IN PROGRESS` to `DONE` (change `b-blue` to `b-green`, text to "DONE").
2. Update `BUILD-PLAN.md`: tick off the completed stage, add a session log entry.
3. Run `hugo --gc --minify` from `site/` to confirm 0 errors.
4. Report what was built and any issues found.

## Important Notes

- **15 P1 cities:** Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Riyadh, Dubai, Mumbai, Moscow, Sao Paulo, Manila, Karachi, Bangkok, Jakarta.
- **25 P2 cities:** London, New York, Paris, Berlin, Tokyo, Hong Kong, Singapore, Sydney, Doha, Kuwait City, Abu Dhabi, Cape Town, Accra, Dar es Salaam, Addis Ababa, Lima, Buenos Aires, Santiago, Beijing, Shanghai, Delhi, Bangalore, Tel Aviv, Cairo, Casablanca.
- **5 service silos:** bodyguard-hire, executive-protection, security-drivers, event-security, residential-security.
- **Strategic decisions locked.** See `.github/agents/bodyguard.agent.md` for the full decision table. Do not re-ask.
- **Operator data is internal.** Never expose operator names, contacts, or pricing in public-facing HTML.
- **Surge deploy:** The bodyguard subagent cannot handle interactive Surge login. Deploy from the main terminal only.
