# CLAUDE.md — Master Entry Point

> **Read this file first every session.** It is the index to the four planning documents that govern this build. Do not pull the whole repo into context — use this file map.

---

## Site Overview
**CloseProtectionHire.com** — a UK-English, programmatic SEO lead-generation site for security services (bodyguard hire, executive protection, security drivers, event security, residential security) across 70 cities globally. Audience: corporate travellers, executives, event organisers, HNWIs. Goal: capture enquiries via organic search. This is a **YMYL** site — Google holds it to higher E-E-A-T standards. ~203 pages currently live.

---

## File Map — Read These In Order at the Start of Every Task

### Planning system (the four authoritative documents)
| File | Read for |
|---|---|
| [bodyguard-cascading-build-plan.html](bodyguard-cascading-build-plan.html) | **WHAT to build and in what order.** Master roadmap. Stages, scope, capability assessment, gantt. This is the source of truth. |
| [BUILD-PLAN.md](BUILD-PLAN.md) | Mirrored checklist of stages with `[x]` / `[ ]` status. Quick view of next stage. |
| [DESIGN-PLAN.md](DESIGN-PLAN.md) | **HOW every page must look.** Design system, components, locked fixes, pre-publish checklist. |
| [AGENTS.md](AGENTS.md) | Full workforce-soul index and routing rules. |
| [ERRORS.md](ERRORS.md) | Running log of bugs, gotchas, and resolutions (consult before re-debugging anything). |
| [MEMORY.md](MEMORY.md) | Architectural decisions, migrations, locked technical context. |

### Key live site files
| File | Purpose |
|---|---|
| `site/hugo.toml` | Hugo config (baseURL, permalinks — touch with care) |
| `site/layouts/index.html` | Homepage template (`.hero-fb`, `.service-card-tall`, `.hiw-step`) |
| `site/layouts/services/single.html` | Service silo template (`.incl-card`, `.loc-city-card`) |
| `site/layouts/cities/single.html` | City page template |
| `site/layouts/countries/single.html` | Country hub template |
| `site/layouts/risk-assessments/single.html` | Risk assessment template |
| `site/layouts/event-security/single.html` | Event security silo template (combinatorial city x event) |
| `site/layouts/blog/single.html` | Blog article template |
| `site/layouts/partials/` | Header, footer, FAQ, schema partials |
| `site/static/css/style.css` | Base CyberGuard theme — **DO NOT EDIT** |
| `site/static/css/custom.css` | All overrides — append-only |
| `site/assets/js/main.js` | Form handler (`.de_form`, `.quote-success`) |
| `site/content/` | All Markdown content (cities/, countries/, services/, blog/, event-security/, guides/, risk-assessments/) |

### Research data (Engine 2 — structured data layer)
| File | Purpose |
|---|---|
| `data/city_risk_profiles.json` | 15 P1 city risk profiles |
| `data/city_risk_profiles_p2.json` | 25 P2 city risk profiles |
| `data/security_regulations.json` | Country-level regulatory data |
| `data/fcdo_advisories.json` | UK FCDO travel advisories |
| `data/state_dept_data.json` | US State Dept advisories |
| `data/keyword_matrix.json` | 75 keyword clusters + Google Autocomplete intelligence |

### Workforce (specialist souls — Engine 7, load only when relevant)
14 worker souls in `workforce/`. Load the one whose domain matches the task:
- `workforce/content/the-chameleon.md` — anti-AI humaniser, banned vocabulary
- `workforce/content/the-wordsmith.md` — copywriting voice
- `workforce/seo/the-optimiser.md` — on-page SEO, schema
- `workforce/seo/the-auditor.md` — QA gate, audit logic
- `workforce/intelligence/the-geographer.md` — risk analysis
- (full list in `AGENTS.md`)

### Engine scripts (Engines 3, 4, 5 — see `BUILD-PLAN.md` for status)
| File | Engine | Purpose |
|---|---|---|
| `scripts/generate_blog_batch*.py` | Engine 3 | Bulk blog factory tracker manifests |
| `scripts/qa_audit.py` | Engine 5 | QA + SEO quality gate (to port from pet-transport) |
| `scripts/check_schema.py` | Engine 5 | FAQ schema verification (to port) |
| `scripts/check_titles.py` | Engine 5 | Title length and uniqueness (to port) |
| `scripts/rebuild_link_graph.py` | Engine 4 | Internal link graph rebuilder (to port) |
| `scripts/diagnose_links.py` | Engine 4 | Broken-link diagnosis (to port) |

---

## Session Workflow (mandatory — Engine 7 discipline)

1. **Read** `bodyguard-cascading-build-plan.html` → identify the next IN-PROGRESS / TODO stage.
2. **Read** `BUILD-PLAN.md` → confirm the mirrored checklist matches.
3. **Read** `DESIGN-PLAN.md` → confirm the design tokens and components you'll reuse.
4. **Read** `ERRORS.md` → confirm you are not about to re-debug something already solved.
5. **Build** the next deliverable, generating new pages from the existing Hugo templates only.
6. **Run quality gate** (Engine 5 scripts once ported; until then mirror the audit logic inline).
7. **HTML preview, await approval** — never commit before approval per the cascading plan.
8. **Update** `BUILD-PLAN.md`, `build_state.json`, and `bodyguard-cascading-build-plan.html` to reflect what was completed. Add a session log entry to `BUILD-PLAN.md`.
9. **Commit** with a descriptive message and push to `master`.
10. **Stop.** One block per session. Do not start the next block.

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
- **No em dashes anywhere in content.** British English throughout.

---

## Deploy (current architecture, 2026-05-28 onwards)

Push to `master` → `.github/workflows/build-and-publish.yml` runs Hugo build → force-pushes `site/public/` to the `live` branch → Hostinger's GitHub OAuth integration receives a webhook → auto-deploys `live` branch contents to `public_html/`.

The entire pipeline is automated. Every push to `master` is live on `closeprotectionhire.com` within ~3 minutes.

**Never edit `.github/workflows/build-and-publish.yml` without explicit approval.** If you do need to change it, give Gareth the full file to paste (the MCP token is blocked from writing workflow files).

Manual build (local sanity check, run from `site/`):
```
hugo --gc --minify
```
Expected: 200+ pages, 0 errors.

### Legacy notes (do not use)
The old FTP-based `.github/workflows/deploy.yml` is disabled in the Actions tab and superseded. It reported success while silently failing to transfer files (FTPS data-channel issue on Hostinger). Do not re-enable it. If the build-and-publish pipeline ever stops working, see `ERRORS.md` for the full deploy-migration history rather than reverting.

---

## Current Status (28 May 2026)
- **Pages live:** ~203
- **Blog articles live:** 30 (Batches 1-6)
- **Cities live:** 70 (P1 + P2 + P3 batches 1+2)
- **Completed:** Phase 0 (research), Phase 1 (P1), Phase 2A-2G (P2 + event security), Phase 3A-3B (P3), Blog 2K Batches 1-6, deploy migration to build-and-publish
- **Next stage candidates:** Turn C (Phase 3C combinatorial service x city), Blog Batch 7, Stage 2L QA audit, port pet-transport Engine 4 + Engine 5 scripts
