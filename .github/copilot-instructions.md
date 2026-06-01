# CloseProtectionHire.com — Copilot Instructions

## Site Identity
- This is a programmatic SEO lead generation website for security services: bodyguard hire, executive protection, security drivers, event security, and residential security in high-risk cities globally.
- Primary goal: capture enquiries from corporate travellers, executives, event organisers, and HNWIs via organic search.
- Domain: https://closeprotectionhire.com (live)
- Repository: https://github.com/ngindubai/closeprotectionhure-com
- Tech stack: Hugo v0.160.1 extended (Windows/AMD64), Go HTML templates, Markdown content, TOML front matter
- Deployment: Push to `master` triggers `.github/workflows/build-and-publish.yml`, which builds Hugo and force-pushes `site/public/` to the `live` branch. Hostinger's GitHub OAuth integration (Advanced → GIT) watches `live` and deploys via webhook. No manual deploy step required.
- Build command: `hugo --gc --minify` run from within `site/`

## Project Status
- 200+ pages live. Phase 0 (research), Phase 1 (P1 cities/countries/services/core), Phase 2A-2F (P2 cities/countries), blog (80+ posts), and guides (9 posts) are all COMPLETE.
- Do NOT restructure existing files, change naming conventions, or alter existing content unless explicitly asked.
- The primary build tracker is `bodyguard-cascading-build-plan.html`. Always check it before starting any build task.
- `BUILD-PLAN.md` mirrors remaining tasks. Both files must be updated at the end of every session.
- Next stage: 2G — Event Security Silo pages for all 15 P1 cities.

## Directory Structure
- Site Hugo root: `site/`
- Content files: `site/content/` (subdirs: cities/, countries/, services/, risk-assessments/, guides/, blog/)
- Templates: `site/layouts/`
- Static assets: `site/static/`
- Research data (JSON): `data/`
- Worker soul files: `workforce/`
- Build plan: `bodyguard-cascading-build-plan.html`

## Content Rules (Non-Negotiable)
1. **YMYL compliance.** This is a Your Money or Your Life site. Author attribution, trust signals, and source citations are mandatory. Google holds security content to higher E-E-A-T standards.
2. **No safety guarantees.** Never imply guaranteed safety or zero risk. "Reduce risk" and "trained professionals" are acceptable. "Stay safe" and "guaranteed protection" are not. This is a legal liability issue.
3. **Humaniser rules active.** Apply the 24 anti-AI patterns from `workforce/content/the-chameleon.md`. No banned vocabulary (delve, tapestry, robust, seamless, leverage, synergy, transformative, paramount, etc.). No em dashes or en dashes. Vary sentence rhythm. High burstiness.
4. **Building names redacted.** Use "Unit 1", "Unit 2" etc. for any specific property references.
5. **Authority voice.** Every page sounds like a senior security consultant wrote it. Not a travel blog, not a military briefing, not a marketing brochure.
6. **Source attribution.** Every factual claim has a named, dated source, or it gets cut.

## SEO Requirements (Non-Negotiable)
- Every page must have a unique `title` and `description` in TOML front matter.
- Title format: `[Primary Keyword] in [City] | CloseProtectionHire` — 50-60 characters.
- Meta description: 140-160 characters, includes a call to action.
- H1: exactly one per page, contains primary keyword and city/location name where applicable.
- Primary keyword must appear in the first 100 words of body copy.
- Internal links: minimum 2 per new page, descriptive anchor text only (never "click here").
- FAQ schema JSON-LD required on all service and informational pages.
- No duplicate content across city/service combinations.

## Code and Template Conventions
- Front matter: TOML format between `+++` delimiters. Never YAML.
- City pages: `site/content/cities/[city-name]/_index.md`
- Country hub pages: `site/content/countries/[country-name]/_index.md`
- Service pages: `site/content/services/[silo-name]/_index.md`
- All slugs: lowercase, hyphen-separated, no underscores.
- Extend existing layouts in `site/layouts/` — do not rewrite base templates.
- No inline CSS — use existing CSS classes from `site/static/css/`.
- Do not create new top-level directories without asking first.

## Worker Souls
14 specialist workers are defined in `workforce/`. Reference them for their domain:
- The Architect (`workforce/leadership/`): orchestration and planning
- The Auditor (`workforce/leadership/`): legal/regulatory accuracy and QA
- The Wordsmith (`workforce/content/`): copywriting and authority voice
- The Chameleon (`workforce/content/`): anti-AI humanisation — reference for banned vocabulary
- The Interrogator (`workforce/content/`): FAQ generation
- The Geographer (`workforce/intelligence/`): risk analysis
- The Scout (`workforce/intelligence/`): keyword research
- The Builder (`workforce/development/`): templates and page generation
- The Librarian (`workforce/development/`): data management
- The Optimiser (`workforce/seo/`): on-page SEO and schema markup
- The Connector (`workforce/seo/`): internal linking
- The Analyst (`workforce/monitoring/`): performance tracking
- The Watchdog (`workforce/monitoring/`): security monitoring

## 15 P1 Cities
Lagos, Nairobi, Johannesburg, Bogota, Mexico City, Istanbul, Riyadh, Dubai, Mumbai, Moscow, Sao Paulo, Manila, Karachi, Bangkok, Jakarta

## 25 P2 Cities
London, New York, Paris, Berlin, Tokyo, Hong Kong, Singapore, Sydney, Doha, Kuwait City, Abu Dhabi, Cape Town, Accra, Dar es Salaam, Addis Ababa, Lima, Buenos Aires, Santiago, Beijing, Shanghai, Delhi, Bangalore, Tel Aviv, Cairo, Casablanca

## 5 Service Silos
bodyguard-hire, executive-protection, security-drivers, event-security, residential-security

## Deployment
- Push to `master` → GitHub Actions builds Hugo → force-pushes `site/public/` to `live` branch → Hostinger webhook deploys to `public_html`.
- No manual deploy step. No FTP. No CLI commands needed.
- To verify a deploy, check the Actions tab on GitHub, then visit the live URL.

## Communication Rules
- Always state what you are about to do before doing it.
- If a task is ambiguous, ask one clarifying question before proceeding.
- When you complete a task, summarise: what was done, what files were changed, and what comes next.
- Flag any decisions that deviate from these instructions.
- **End of every session:** update `BUILD-PLAN.md` AND `bodyguard-cascading-build-plan.html` to reflect what was completed. Add a session log entry to `BUILD-PLAN.md`.
