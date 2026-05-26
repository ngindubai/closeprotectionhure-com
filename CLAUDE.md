# CLAUDE.md — Master Entry Point

> **Read this file first every session.** It is the index to the three planning documents that govern this build. Do not pull the whole repo into context — use this file map.

---

## Site Overview
**CloseProtectionHire.com** — a UK-English, programmatic SEO lead-generation site for security services (bodyguard hire, executive protection, security drivers, event security, residential security) across 40 high-risk cities globally. Audience: corporate travellers, executives, event organisers, HNWIs. Goal: capture enquiries via organic search. This is a **YMYL** site — Google holds it to higher E-E-A-T standards. 143 pages currently live.

---

## File Map — Read These In Order at the Start of Every Task

### Planning system (the four authoritative documents)
| File | Read for |
|---|---|
| [bodyguard-cascading-build-plan.html](bodyguard-cascading-build-plan.html) | **WHAT to build and in what order.** Master roadmap. Stages, scope, capability assessment, gantt. This is the source of truth. |
| [BUILD-PLAN.md](BUILD-PLAN.md) | Mirrored checklist of stages with `[x]` / `[ ]` status. Quick view of next stage. |
| [DESIGN-PLAN.md](DESIGN-PLAN.md) | **HOW every page must look.** Design system, components, locked fixes, pre-publish checklist. |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Site identity, content rules (YMYL, no safety guarantees, banned vocabulary), SEO requirements. |

### Key live site files
| File | Purpose |
|---|---|
| `site/hugo.toml` | Hugo config |
| `site/layouts/index.html` | Homepage template (`.hero-fb`, `.service-card-tall`, `.hiw-step`) |
| `site/layouts/services/single.html` | Service silo template (`.incl-card`, `.loc-city-card`) |
| `site/layouts/cities/single.html` | City page template |
| `site/layouts/countries/single.html` | Country hub template |
| `site/layouts/risk-assessments/single.html` | Risk assessment template |
| `site/layouts/partials/` | Header, footer, FAQ, schema partials |
| `site/static/css/style.css` | Base CyberGuard theme — **DO NOT EDIT** |
| `site/static/css/custom.css` | All overrides — append-only |
| `site/assets/js/main.js` | Form handler (`.de_form`, `.quote-success`) |
| `site/content/` | All Markdown content (cities/, countries/, services/, guides/, risk-assessments/) |

### Research data
| File | Purpose |
|---|---|
| `data/city_risk_profiles.json` | 15 P1 city risk profiles |
| `data/city_risk_profiles_p2.json` | 25 P2 city risk profiles |
| `data/security_regulations.json` | Country-level regulatory data |
| `data/fcdo_advisories.json` | UK FCDO travel advisories |
| `data/state_dept_data.json` | US State Dept advisories |
| `data/keyword_matrix.json` | 75 keyword clusters |

### Workforce (specialist souls — load only when relevant)
14 worker souls in `workforce/`. Load the one whose domain matches the task:
- `workforce/content/the-chameleon.md` — anti-AI humaniser, banned vocabulary
- `workforce/content/the-wordsmith.md` — copywriting voice
- `workforce/seo/the-optimiser.md` — on-page SEO, schema
- `workforce/intelligence/the-geographer.md` — risk analysis
- (full list in `AGENTS.md`)

---

## Session Workflow (mandatory)

1. **Read** `bodyguard-cascading-build-plan.html` → identify the next IN-PROGRESS / TODO stage.
2. **Read** `BUILD-PLAN.md` → confirm the mirrored checklist matches.
3. **Read** `DESIGN-PLAN.md` → confirm the design tokens and components you'll reuse.
4. **Build** the next deliverable, generating new pages from the existing Hugo templates only.
5. **Update** `BUILD-PLAN.md` AND `bodyguard-cascading-build-plan.html` to reflect what was completed. Add a session log entry to `BUILD-PLAN.md`.
6. **Commit** with a descriptive message and push to `master`.

---

## Working Rules

- Edit only what is asked. Never rewrite whole files unprompted.
- Generate every new page from the existing Hugo template — never invent new layouts without approval.
- All content files: **YAML** front matter (`---` delimiters), never TOML.
- All internal links: relative, descriptive anchor text (never "click here"). Minimum 2 per new page.
- No new colour tokens, fonts, or top-level directories without explicit approval.
- All factual claims need a named, dated source — or they get cut.
- Never imply safety guarantees. "Reduce risk" / "trained professionals" only.
- Building names redacted as "Unit 1", "Unit 2".
- Do not hardcode rates, bank names, or live statistics — source/verify at build time.

---

## Deploy

Push to `master` → GitHub Actions runs `.github/workflows/deploy.yml` → builds Hugo → FTP-syncs `site/public/` to Hostinger (`/home/u356263466/domains/closeprotectionhire.com/public_html/`).

**Never edit `.github/workflows/deploy.yml` or the `FTP_PASSWORD` secret.** If deploy fails, report the error — do not modify the workflow without approval.

Manual build (local sanity check, run from `site/`):
```
hugo --gc --minify
```
Expected: 143+ pages, 0 errors.

---

## Current Status
- **Pages live:** 143
- **Completed:** Phase 0 (research), Phase 1 (P1 cities/countries/services/core), Phase 2A–2F (P2 cities/countries), Phase 2G (Event Security silo — 16 cities)
- **Next stage:** **2H — Travel Safety Guides Batch 1** (15 P1 cities). See `BUILD-PLAN.md` and `bodyguard-cascading-build-plan.html` for full scope.
