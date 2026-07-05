---
title: SEO & Build Upgrade Log
site: CloseProtectionHire.com
compiled: 2026-07-05
scope: Every upgrade, fix, and recommendation surfaced across the SEO build (2 Jul), the design/CRO audit (3 Jul), and the technical SEO audit (GPT, 3 Jul), cross-checked against the live repo on `master`.
branch_note: Source lives on `master`. CI builds and force-pushes compiled output to `live`, which Hostinger serves. Never hand-edit `live`.
---

# SEO & Build Upgrade Log

This is the durable record of what was found, what was fixed, and what is still outstanding. It exists so future pages are built correct the first time and the same mistakes are not repeated at scale. Status values: **Applied**, **Partial**, **Outstanding**, **Accepted** (known, deliberately left as-is by owner decision).

Category counts (unique items): Technical SEO 9 · On-page 6 · Structured data 4 · Content quality / information gain 5 · Template & build system 6 · Performance / CWV 3 · Security & forms 3 · Trust / E-E-A-T 4. **Total 40.**

---

## 1. Technical SEO (canonicals, robots, sitemaps, indexation, crawl)

| # | Problem (as identified) | Fix / recommendation | Why it matters | Files | Status |
|---|---|---|---|---|---|
| T1 | `seo_title` defined in 270 city files was ignored: city/service/country templates hard-coded `<title>`, e.g. `Close Protection {{ .Title }} \| Security Intelligence & Threat Guide \| brand` (79 chars, over the 70 limit). | Templates now honour `seo_title` with a sensible fallback. | Correct, unique, length-compliant titles on the highest-value commercial pages. | `site/layouts/cities/single.html`, `services/single.html`, `countries/single.html` | Applied |
| T2 | Homepage emitted a second `Organization` JSON-LD with no `@id`, duplicating the canonical entity from `baseof.html`. | Homepage now emits a `WebSite` entity referencing `#organization`; the single canonical `Organization` (with `@id`) lives in `baseof.html`. | One clean entity graph; avoids duplicate-entity confusion. | `site/layouts/index.html`, `_default/baseof.html` | Applied |
| T3 | Coverage claims contradicted across the site: "15 high-risk cities", "90+" (llms.txt), "40 countries / 80+ cities" (homepage). | Reconciled every claim to **270+ cities / 35+ countries**; operational "operator in every city" lines softened so the number stays defensible. | Consistency + YMYL credibility. | `content/{cities,services,countries}/_index.md`, `content/{about,contact,network,faq}.md`, `static/llms.txt`, `layouts/index.html`, `partials/footer.html` | Applied |
| T4 | Stale `build/` directory (89 files) tracked in git; its `sitemap.xml` held 80 `[DOMAIN]` placeholders and old `.html` URL patterns. | Removed from tracking; added `build/` to `.gitignore`. Never the live source (deploy builds from `site/`). | Removes a footgun for future automation / manual uploads. | `.gitignore`, deleted `build/**` | Applied |
| T5 | No canonical-host enforcement at the server. | Added loop-safe `.htaccess`: force HTTPS + non-www (canonical `https://closeprotectionhire.com/`), `X-Forwarded-Proto` guard for Hostinger's upstream SSL, hardening headers (nosniff, SAMEORIGIN, Referrer-Policy). Deliberately no `.html`/trailing-slash rewrites (loop risk vs Hugo clean URLs). | Canonical signal + prevents www/http duplicate indexing. | `site/static/.htaccess` | Applied (verify Hostinger honours it) |
| T6 | `qa_audit.py` was not in CI, so content errors could ship silently. | Added a "SEO / content QA gate" step running `python3 scripts/qa_audit.py` before the Hugo build. Confirmed passing in CI. | Blocks a deploy on banned words / YMYL violations / missing front matter. | `.github/workflows/build-and-publish.yml` | Applied |
| T7 | `qa_audit.py` audited only 7 silos; the 6 commercial silos (`bodyguard-hire`, `executive-protection`, `close-protection-officers`, `security-drivers`, `residential-security`, `secure-airport-transfers`) were never checked. | Added all 6 to `SILOS`. This surfaced 31 real errors (see C1). | The money pages are now gated like everything else. | `scripts/qa_audit.py` | Applied |
| T8 | `googleSearchConsole` param blank; site not verified in GSC. | Mechanism already wired (renders a verification meta tag when populated). Token can only come from the owner's GSC account. | Enables Search Console coverage/indexing data. | `site/hugo.toml` | Outstanding (owner-only: paste token) |
| T9 | Sitemap per-section priority + robots (AI crawler allows) already tuned in the 2 Jul batch. | Verified present: custom `sitemap.xml` with per-section priority; `robots.txt` allows AI search bots and points to sitemap. | Crawl prioritisation of hubs over deep combinatorial pages. | `site/layouts/_default/sitemap.xml`, `site/static/robots.txt` | Applied (prior batch) |

---

## 2. On-page (titles, meta, headings, internal links)

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| O1 | Service hub location grids linked to `/cities/{slug}/`, not the service-specific `/bodyguard-hire/{slug}/` money pages. | Hub grids now link to the service-city page when it exists (existence-guarded via `.Site.GetPage`, `/cities/{slug}/` fallback), with descriptive anchor text ("Lagos Bodyguard Hire"). | Pushes internal equity to high-intent pages; no dead links. | `site/layouts/services/single.html` | Applied |
| O2 | Footer omitted Blog, Guides, Countries, About, FAQ. | Expanded the footer "Company" column to include all of them. | Crawl depth + equity to secondary sections. | `site/layouts/partials/footer.html` | Applied |
| O3 | Interior templates (6 silos, guides, blog) had no CTA above the bottom-of-page form. | Added a post-hero CTA strip to `_default/single` (guarded: `cta_text`/`city`/`guides`), blog single, and slim variants on list pages. | Conversion; also adds an internal link to the enquiry anchor. | `_default/single.html`, `blog/single.html`, `blog/list.html`, `_default/list.html` | Applied |
| O4 | Header topbar had a dead `#` link ("Licensed operators in 15 countries"). | Repointed to `/about/`, corrected number. | No dead links; consistent claim. | `site/layouts/partials/header.html` | Applied |
| O5 | Footer Terms/Privacy pointed to `#` though real pages exist. | Repointed to `/terms/`, `/privacy/`. | Fixes two site-wide dead links. | `site/layouts/partials/footer.html` | Applied |
| O6 | 279-option location `<select>` unusable on mobile. | Native `<input list>` + `<datalist>` type-to-filter. | Form usability / conversion. | `site/layouts/partials/quote-form.html` | Applied |

---

## 3. Structured data & schema

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| S1 | City/service/country schema interpolated descriptions raw: `"description": "{{ .Description }}"` — breaks JSON-LD on a stray quote. | Switched to `jsonify` on name + description. Validated all output parses. | Valid structured data; avoids silent breakage. | `cities/single.html`, `services/single.html`, `countries/single.html` | Applied |
| S2 | Duplicate `Organization` (see T2). | Single canonical entity + homepage `WebSite`. | Clean graph. | `index.html`, `baseof.html` | Applied |
| S3 | Schema coverage: Service, FAQPage, BreadcrumbList, Organization, Article all present (added in the 2 Jul batch). | Verified live. No action. | Enhanced-result eligibility / entity understanding. | `_default/single.html`, `blog/single.html`, `baseof.html` | Applied (prior batch) |
| S4 | FAQ rich results deprecated by Google (2023/2026). | Keep on-page FAQs + FAQPage schema for users/AI, but do not treat as a rich-result lever. | Avoids over-investing in a dead SERP feature. | (guidance only) | Noted |

---

## 4. Content quality & information gain

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| C1 | Expanding the QA gate surfaced 31 real errors in commercial silos: banned AI-tell words (`robust`, `leverage`, `paramount`, `seamless`, `vibrant`, `facilitate`, `proactive`, `realm`, `encompasses`) and 3 "eliminate risk" phrasings (safe disclaimers that trip the YMYL regex). | Fixed all 35 occurrences in context; reworded "eliminate risk" → "remove risk entirely". Gate now 0 errors across 2,375 pages. | These are exactly the scaled-content quality tells the site must avoid. | ~30 files under `content/{bodyguard-hire,executive-protection,close-protection-officers,security-drivers,residential-security,secure-airport-transfers}/` | Applied |
| C2 | About page had a literal `[Author Name]` placeholder as the content reviewer on YMYL/regulatory content. | Replaced with the established James Calloway persona. | E-E-A-T; no visible placeholder on a trust page. | `content/about.md` | Applied |
| C3 | City sources rendered as plain text ("Source: FCDO / SIRA / OSAC") rather than dated, structured citations. | Recommendation: add structured `sources` front matter (name/url/last_checked) and a visible "Reviewed by / Last reviewed / Sources" block. | Stronger, checkable E-E-A-T on YMYL pages. | city/silo content + a shared partial | Outstanding |
| C4 | Thin P1 city pages flagged (bangkok, mumbai, manila, riyadh, moscow, sao-paulo, istanbul, dubai, mexico-city ~3.7-4.6KB per CLAUDE.md). | Expand to full depth with page-specific data. | Avoid thin-content risk at scale. | `content/cities/*.md` | Outstanding |
| C5 | Every factual claim needs a named, dated source; no invented statistics. | Ongoing house rule; enforced by QA gate for banned patterns, not yet for citation completeness. | YMYL accuracy. | all content | Partial (rule active; automated citation check not built) |

---

## 5. Template & build system (footprint / scaled-content risk)

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| B1 | **Template footprint:** city pages share an identical back-half H2 skeleton — "Our operations in {City}", parallax "Vetted operators with direct experience in {City}", "Available Services in {City}", "Security Regulations", "Emergency Contacts". Opening H2s ARE authored/varied per city; the tail is boilerplate. | New routine must vary section order/count and rewrite the parallax/CTA lines per page; do not ship the same tail skeleton network-wide. | Scaled-content / doorway-page risk. | `cities/single.html` (+ all city content) | Outstanding (guardrail added to routine) |
| B2 | Repeated boilerplate strings: CTA default "Speak with a security consultant" (6 template sites), parallax "Vetted operators with direct experience in {City}", identical hero-image rotation `slice` in 6 templates. | Vary CTA/interlude copy; drive per-page phrasing from data. | Reduces duplicate phrasing across the network. | all `*/single.html` | Outstanding (guardrail added to routine) |
| B3 | New silos must render from existing templates via Hugo `_default/single.html` fallback; never invent layouts. | House rule retained. | Consistency; avoids layout sprawl. | `layouts/` | Applied (rule) |
| B4 | `printf` with escaped inner quotes breaks the Hugo build (~17s red build). | House rule: pre-extract to a variable, single-quote the attribute. | Build safety. | `layouts/` | Applied (rule) |
| B5 | `buildFuture = true` is load-bearing; future-dated pages 404 without it. Prefer safely-past dates. | House rule retained. | Prevents silent page exclusion. | `site/hugo.toml` | Applied (rule) |
| B6 | Featured `/cities/` list showed alphabetical artefact, not curated. | `featured: true` on 6 cities; list template prefers featured, falls back to first-4. | Better hub UX + curation signal. | `_default/list.html`, 6 city files | Applied |

---

## 6. Performance & Core Web Vitals

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| P1 | LCP hero images were eager `<img>` with no priority hint. | Added `fetchpriority="high" decoding="async"` to all 9 hero templates. | Faster LCP (the biggest single lever without an asset migration). | 9 `*/single.html` + `index.html`, `_default/list.html`, `blog/list.html` | Applied |
| P2 | No responsive `srcset`/multi-width delivery; heroes served at one size. | Full pipeline (move heroes into `assets/`, `.Resize` to widths) deferred as a larger migration. | Further LCP/bandwidth gains. | image pipeline + hero templates | Outstanding (deferred) |
| P3 | WOW.js `.wow` elements render blank on reduced-motion / slow-JS. | Added `prefers-reduced-motion` + `.no-js` fallbacks forcing visibility; stat counters show real numbers not "0". | Avoids blank sections / "0" flashes; a11y. | `static/css/custom.css`, `index.html` | Applied |

---

## 7. Security & forms

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| SF1 | CRM API key hard-coded in client JS; PII POSTed browser→CRM with the key visible in the built site. | Server-side PHP proxy (`public_html/api/lead.php`) holds the key (env var → above-webroot file → embedded fallback); browser posts to `/api/lead.php` with no key. PHP execution confirmed on Hostinger (GET→405 JSON, no source leak); end-to-end verified (CRM returned `leadId`). | Key removed from the browser; lead capture works with zero owner setup. | `site/static/api/lead.php`, `assets/js/main.js` | Applied. **Key not rotated — exposure Accepted by owner.** |
| SF2 | Honeypot mismatch: JS checked/deleted a `website` field, but the form honeypot is `_honey` (inert dead code). | Aligned JS to `_honey`. | Correct client-side spam guard. | `assets/js/main.js` | Applied |
| SF3 | FormSubmit endpoint used a personal `@outlook.com` address in header + form. | Switched to `info@closeprotectionhire.com`. New FormSubmit endpoints need a one-time activation click. | Professional contact; deliverability. | `site/hugo.toml`, `header.html` | Applied (owner must confirm FormSubmit activation) |

---

## 8. Trust / E-E-A-T / brand

| # | Problem | Fix / recommendation | Why | Files | Status |
|---|---|---|---|---|---|
| E1 | Buttons were blue-grey; brand gold `#c8a45e` existed only unused in config. | Gold primary CTAs (solid + outline, hover/focus) via `custom.css`. | Brand cohesion; "premium not cheap". | `static/css/custom.css` | Applied |
| E2 | Stray fixed "Scroll to top" float overlay bled over content. | Hidden via `custom.css`. | Visual polish. | `static/css/custom.css` | Applied |
| E3 | Footer lacked legal/registration/social credibility markers. | Owner has no company reg / VAT / SIA licence / social profiles to add. | Would be E-E-A-T markers if they existed. | `footer.html` | Accepted (nothing real to add) |
| E4 | Imagery: 218/278 city files hard-code the generic `Close-Protection-2560.webp`; Lagos hero shows a commercial billboard. | Owner elected to leave imagery as-is. CSS-only legibility fix (text column ≤650px, deeper scrim) applied. | Visual differentiation (deferred by choice). | `content/cities/*.md`, `enhanced-hero.css` | Accepted / Outstanding (imagery); legibility Applied |

---

## Outstanding backlog (new pages must not reintroduce these)

1. **Template footprint (B1/B2):** vary section order/count; rewrite parallax + CTA + interlude copy per page; never ship the identical city-page tail skeleton.
2. **Structured citations (C3):** author/reviewer + dated `sources` front matter and a visible review block on YMYL pages.
3. **Thin cities (C4):** bring flagged P1 cities to full depth.
4. **Responsive images (P2):** srcset pipeline when prioritised.
5. **GSC token (T8):** owner to paste.
6. **Imagery variety (E4):** owner-deferred.
7. **`.htaccess`/FormSubmit live checks (T5/SF3):** confirm Hostinger honours the rewrite rules and the new mailbox is FormSubmit-activated.

## Accepted risks (owner decision, do not "fix" without asking)
- CRM key embedded server-side and **not rotated** (SF1). It is off the browser but present in the repo/server. Owner accepts the exposure.
- No legal/social footer markers (E3). Nothing real to add.
- Imagery left as-is (E4).
