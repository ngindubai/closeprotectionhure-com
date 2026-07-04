---
title: Design & Conversion Build Plan — CloseProtectionHire.com
date: 2026-07-03
source_audit: Browser UI/UX & CRO audit (Sonnet 4.6), 3 July 2026 — 26 findings (F01–F26)
execution_model: Sonnet (every step is Sonnet-safe once the DECISIONS block is answered)
branch: master   # master is the ONLY deploy branch. Never main, never live. See guardrails.
companion_docs: closeprotectionhire-seo-audit-2026-07-02.html, closeprotectionhire-seo-build-plan-2026-07-02.md
---

# Design & Conversion Build Plan

> This plan turns the 3 July browser design/CRO audit into executable work. **Every finding below was re-verified against the actual repo** before being written up. Where the audit was wrong, this plan says so and gives the corrected instruction — follow this plan, not the raw audit, when they disagree.

---

## How to use this plan
1. **Answer the DECISIONS block first.** Several fixes need real business facts (a professional email, a phone number, accurate coverage numbers, legal/registration details). Sonnet must NOT invent these. Where a safe default exists, it is stated; use it only if the user has approved it.
2. Work the batches in order (A → D). A and B are the high-leverage, low-risk template fixes. C and D depend on decisions/assets.
3. One batch per run. Build-check, QA-gate, preview, get approval, commit once, push to `master`.

## Global guardrails (apply to every batch)
1. **Branch:** commit to `master`. Never `main`; never build on/hand-push `live` (it is the compiled output branch — see the SEO build plan's guardrail).
2. **CSS:** never edit `static/css/style.css` (base CyberGuard theme) or `scheme-security.css`. **All overrides go in `static/css/custom.css` (append-only)** and `enhanced-hero.css` for city-hero specifics.
3. **Template `printf`/quotes:** if editing layouts, use backtick `printf` and `| jsonify` on any interpolated JSON — never escaped inner double-quotes (breaks the Hugo build).
4. **Build check before every commit:** from `site/`, run `hugo --gc --minify` → expect ~2,411 pages, 0 errors. Hugo is installed in this environment.
5. **QA gate on any new copy:** British English; **no em dashes anywhere** (content or layout string values); no safety-guarantee language ("guarantee safety", "keep you safe", "100% safe", "risk-free", "foolproof", "bulletproof").
6. **Verify hover/animation states after CSS changes** — several buttons use `fx-slide` (a hover slide effect via pseudo-elements); confirm gold applies on hover, not just at rest.
7. **One commit + one push per batch**; await approval before committing. Output live review URLs after deploy.

---

## CORRECTIONS TO THE AUDIT (verified against the repo — read before doing anything)

The audit is broadly accurate, but these four claims are **wrong** and their fixes are different from what the audit proposed:

- **[C1] "Terms & Privacy pages do not exist — create them" (F03) is WRONG.** `content/terms.md` (67 lines) and `content/privacy.md` (61 lines) **already exist with real content** and build to `/terms/` and `/privacy/`. The only bug is the **footer links point to `#`**. Fix = repoint the two footer links; do NOT create new pages. (Do review the existing pages' content for accuracy once the legal decisions D4 are known.)
- **[C2] "Silo pages have a post-hero CTA strip" is WRONG.** The 6 `_default/single` silos (`bodyguard-hire`, `executive-protection`, `close-protection-officers`, `security-drivers`, `residential-security`, `secure-airport-transfers`), guides, and blog pages have **no CTA strip**. Only `services/single`, `event-security/single`, and `risk-assessments/single` render one (from `cta_text`). Every silo `.md` file already carries an unused `cta_text` front-matter field. **Opportunity:** render it (Batch B1) — this both fixes the conversion gap and uses data that already exists.
- **[C3] "Schema markup is absent from all pages" (audit's out-of-scope note) is WRONG.** Service, FAQPage, BreadcrumbList, Organization and Article JSON-LD were all added last session and are live. No action needed. (The auditor did not view source.)
- **[C4] "F07: make the listing template use `hero_image`" is WRONG about the cause.** The listing template (`_default/list.html`) **already** uses `hero_image` with a fallback. The real cause is the **data**: 218 of 278 city `.md` files hard-code `hero_image: "Close-Protection-2560.webp"`. So F07 is a content/asset task (vary the images), not a one-line template fix. See Batch C.

Other corrections: the "personal email" appears in BOTH the header AND the FormSubmit form endpoint (`hugo.toml`). The repeated header line is "Licensed operators in **15 countries**" with a dead `#` link (the audit called it "15 cities" in the footer — it is the header). Homepage separately claims "80+ cities / 40 countries / 6 continents". These numbers must be reconciled (D3).

---

## DECISIONS NEEDED FROM THE USER (Sonnet: do not invent these)

| # | Decision | Why it is needed | Blocks |
|---|---|---|---|
| **D1** | **Professional contact email** (e.g. `enquiries@closeprotectionhire.com`) AND whether the FormSubmit endpoint should change to it. The mailbox must actually exist and be FormSubmit-activated, or enquiries will silently fail. | Replaces `garethsomers@outlook.com` in the header, footer, and the form action. | F01 (A2), form endpoint |
| **D2** | **Phone number** (UK or international) or explicit "no phone". A `tel:` link and/or WhatsApp. | Add to header + mobile sticky bar; biggest remaining trust/accessibility gap. | F04, F17, mobile CTA |
| **D3** | **Accurate coverage claim.** The repo has ~278 city pages and ~38 country pages. What should the site claim — e.g. "90+ cities across 30+ countries"? Reconcile header ("15 countries"), homepage stats ("40 countries / 80+ cities / 6 continents"), and any others to one true set of numbers. | Fixes a credibility-damaging inconsistency. | F01, F13, copy |
| **D4** | **Legal/registration facts for the footer:** company registration number, VAT number, and/or SIA operator licence number (if held). Any that are real. | Footer credibility markers (F21) and to sanity-check the existing terms/privacy pages. | F21 (D batch) |
| **D5** | **Real social/directory profile URLs** (LinkedIn minimum) — only real ones. | Footer `sameAs`/social links (F21). Omit if none exist (do not fabricate). | F21 |
| **D6** | **Imagery approach.** Either (a) source real per-service and per-city photography (asset cost), or (b) approve a curated re-use of the existing image library with sensible variety and better cropping. Also: confirm replacing the Lagos hero that shows a visible commercial billboard. | Fixes the "same 3 stock photos everywhere" problem (F05, F06, F07, F09, F19, F20, F23, F25). | Batch C |
| **D7** | **Design/CRO direction (recommend "yes" to all):** (i) make primary CTAs gold `#c8a45e`; (ii) reduce the homepage hero form to 3 fields; (iii) add a sticky mobile CTA bar; (iv) add mid-page CTAs on long pages. These are low-risk and reversible; listed here only so the user is not surprised by a visible brand/UX shift. | Governs Batch A2/B. | Batch A, B |

**Safe defaults (only if the user approves them in one go):** D1 = `enquiries@closeprotectionhire.com` and switch the form endpoint to it once the mailbox is live; D2 = no phone until provided (leave the slot ready); D3 = "90+ cities worldwide" + reconcile the numeric stats to match the real page counts; D6 = option (b) curated re-use for now; D7 = yes to all four.

---

# BATCH A — Global trust, correctness & brand (template-level, highest ROI)
*Mostly no-decision. This is the batch that most changes the "cheap vs premium" perception, and it is nearly all CSS + two partials.*

### A1 — Gold primary CTAs (F02) [CSS] — needs D7(i)
- **Verified:** the theme's `scheme-security.css` sets `--primary-color:#6b8299` (grey-blue) and `--secondary-color:#4f6a82` (also blue). `.btn-main` uses `var(--primary-color)`, so **no button is gold anywhere** — the gold `#c8a45e` only lives in `hugo.toml` params, unused by CSS.
- **Change (append to `custom.css`):** override `.btn-main` (solid) to gold background `#c8a45e` with dark navy text `#0a1628`, and handle the `.btn-main.btn-line` (outline) variant to gold border/text with a gold-fill hover. Cover `:hover/:focus/:active`.
- **Watch:** buttons using `fx-slide` animate a pseudo-element on hover — confirm the gold shows both at rest and on hover; if the slide overlay hides it, target `.btn-main.fx-slide span` / the `::before` too.
- **Verify:** homepage, a city page, a silo page, the form submit button, and header button all render gold; hover states correct at desktop + mobile.

### A2 — Header: professional email, phone, dead-link + number fix (F01, F04) [partial] — needs D1, D2, D3
- **File:** `layouts/partials/header.html` (topbar, lines ~9–13).
- **Changes:** (a) swap `contactEmail` value in `hugo.toml` to the professional address (D1) — this fixes header AND the current mailto; (b) the second topbar widget is `<a href="#"><i class="icofont-shield"></i>Licensed operators in 15 countries</a>` — replace the dead `#` with a real destination (e.g. `/about/`) and correct "15 countries" to the D3 number; (c) if D2 provides a phone, add a `tel:` widget in the topbar.
- **Also:** update `hugo.toml` `quoteFormEndpoint` to the professional address if D1 says so (this is the form's delivery target — coordinate with FormSubmit activation).
- **Verify:** no `outlook.com` remains anywhere (`grep -rn outlook site/`), header shows professional email + phone + a working "licensed operators" link.

### A3 — Footer: repoint Terms & Privacy to the existing pages (F03) [partial]
- **File:** `layouts/partials/footer.html` lines 63–64. Change `href="#"` → `/terms/` and `/privacy/` (pages already exist — see C1).
- **Verify:** footer links resolve to the real pages; `grep 'href="#"' layouts/partials/footer.html` returns nothing (also check for any other dead `#` in the footer while there).

### A4 — Hide the stray "Scroll to top" float element (F10) [CSS]
- **Verified:** `.float-text` is `position:fixed; z-index:1002` (style.css:9205) and overlaps content on scroll.
- **Change (custom.css):** `.float-text{display:none;}` (or restrict to `@media(min-width:1600px)` if the user wants to keep it on ultrawide). Confirm the scroll-to-top scrollbar element (`.scrollbar-v`) is unaffected/desired.
- **Verify:** no vertical "Scroll to top" text bleeds over content on any page.

### A5 — Motion-safety + no blank sections (F22) [CSS]
- **Verified:** WOW.js `.wow` elements start hidden and reveal on scroll; on fast scroll / no-JS / prerender they can appear as blank dark blocks.
- **Change (custom.css):** add `@media (prefers-reduced-motion: reduce){ .wow{visibility:visible!important;animation:none!important;opacity:1!important;} }` and a no-JS fallback `.no-js .wow{visibility:visible!important;opacity:1!important;}` (add `no-js`→`js` swap only if not already present; otherwise rely on the reduced-motion rule).
- **Verify:** with "reduce motion" enabled in the browser, all sections are visible immediately.

### A6 — Stat counters show real numbers, not "0" (F13) [index.html] — needs D3
- **Verified:** counters render `<span class="timer" data-to="40">0</span>+` etc.; the `0` is the pre-animation state and shows in screenshots/no-JS.
- **Change:** set the visible text content to the final number (e.g. `>40<`) instead of `0`, keeping `data-to` so the count-up still animates; reconcile the four values (Countries 40, Cities 80, Categories 5, Turnaround 24h) with the D3 truth.
- **Verify:** view-source shows the real numbers; animation still runs on scroll.

---

# BATCH B — Conversion: CTAs everywhere + form friction (template-level)
*This is the CRO core. Interior pages currently bury the only form at the bottom; this batch adds contextual CTAs and reduces form friction.*

### B1 — Post-hero CTA strip on the templates that lack one (F08, F15, F16) [templates]
- **Verified (C2):** `_default/single` (6 silos + guides + utility), `blog/single`, `blog/list`, and `_default/list` have **no** CTA strip; `services/`, `event-security/`, `risk-assessments/` already do (from `cta_text`). Silo `.md` files already contain a `cta_text` field that is currently unused.
- **Reusable pattern (copy from `services/single.html` lines 45–57):**
  ```
  {{/* ===== CTA BAR ===== */}}
  <section class="section-dark bg-color text-light pt-40 pb-30 relative overflow-hidden">
    <div class="container"><div class="row g-4 align-items-center">
      <div class="col-md-9"><h4 class="mb-0 wow fadeInRight">{{ with .Params.cta_text }}{{ . }}{{ else }}Planning travel to {{ .Params.city | default .Title }}? Speak with a security consultant.{{ end }}</h4></div>
      <div class="col-md-3 text-md-end"><a class="btn-main fx-slide btn-line wow fadeInLeft" href="#quote-form"><span>Request Consultation</span></a></div>
    </div></div>
  </section>
  ```
- **Where to add it:** in `_default/single.html` immediately after the subheader/hero (before the direct-answer/content); guides fall through `_default/single` so they get it automatically. For `blog/single.html`, add after the hero (city-agnostic copy: "Travelling somewhere high-risk? Speak with a security consultant."). For `blog/list.html` and `_default/list.html`, add a slim variant near the top ("Can't find what you need? Speak with a security consultant.").
- **Guard:** on `_default/single` only render when `.Params.cta_text` OR `.Params.city` exists, so pure utility pages (about/contact/faq/privacy/terms) don't get an odd strip (or give them a generic one — design call; default: only on city/service pages).
- **Verify:** `/bodyguard-hire/lagos/`, `/guides/travel-safety-guide-lagos/`, a blog article, and `/cities/` all show a CTA strip high on the page; build clean.

### B2 — Trust strip directly above every form submit (F08) [quote-form partial]
- **File:** `layouts/partials/quote-form.html`. Add a compact strip immediately above the submit button: `Confidential · SIA-licensed operators · Response within 24 hours` (adjust to true claims — no safety guarantees). Style `.form-trust-strip` in custom.css (gold accent, small, legible — not the current tiny grey note).
- **Verify:** the strip appears on every page's form; contrast is readable (WCAG AA).

### B3 — City pages: sticky jump-nav with an inline CTA + one mid-page CTA (F09 conv, city recs) [cities/single + enhanced-hero.css]
- **Verified:** `.inner-hero-jumpbar` exists but is **not** sticky. City pages are 7,000–9,700px tall with no persistent CTA after the hero.
- **Changes:** (a) make `.inner-hero-jumpbar` `position:sticky; top:0; z-index:...` in `enhanced-hero.css` and add a right-aligned gold "Request Consultation" button inside it; ensure it doesn't cover content and collapses sensibly on mobile; (b) insert one compact inline CTA card in `cities/single.html` roughly mid-page (e.g. between Zone Intelligence and Emergency Contacts): "Deploying to {{ .Title }}? Get a vetted close protection detail." + gold button.
- **Verify:** on a long city page the CTA stays reachable while scrolling; no overlap; mobile behaves.

### B4 — Location field: replace the 279-option `<select>` with a filterable input (F12) [quote-form partial + tiny JS]
- **Verified:** the location `<select>` renders 279+ options — unusable on mobile.
- **Change:** convert to `<input list="cities-datalist">` + `<datalist id="cities-datalist">…</datalist>` (native, zero-dependency, type-to-filter) — simplest and robust. If richer UX is wanted later, a ~5KB autocomplete (Choices.js) can replace it. Keep the field required on interior pages; keep the `_honey` honeypot.
- **Verify:** typing filters the list on desktop and mobile; form still submits `location`.

### B5 — Homepage hero form: reduce friction (F11) [index.html] — needs D7(ii)
- **Change:** drop the 279-city dropdown from the *hero* form; reduce to Name, Email, and a "Destination & requirements" textarea (+ submit). Keep the full detailed form at the page bottom and on interior pages.
- **Verify:** hero form is 3 fields; still posts to FormSubmit with a sensible `_subject`.

### B6 — Sticky mobile CTA bar (global) [baseof or footer partial + CSS + minimal JS] — needs D7(iii), and D2 for the phone
- **Change:** a slim (~52px) fixed bottom bar shown only `@media(max-width:767px)` with two tap targets: "Request Consultation" (→ `#quote-form`) and, if D2 provides one, a phone icon (`tel:`). Ensure it doesn't cover the footer form's submit (add bottom padding to `body` on mobile).
- **Verify:** on a phone viewport the bar is present on every template, tappable (≥44px), and never obscures content.

---

# BATCH C — Imagery & hero polish (needs D6)
*The "same 3 photos everywhere" problem. All of this is gated on the imagery decision.*

### C1 — Distinct hero per service silo (F06) — [content front matter]
- Give each of the 6 silos (and `services/*`) a distinct default `hero_image` so "Bodyguard Hire in Lagos" and "Executive Protection in Lagos" don't look identical. Existing assets like `service-executive-protection-hero.jpg`, `service-bodyguard-hire-hero.jpg`, `service-security-drivers-hero.jpg` already exist — map one per service via the template's image logic or a per-section default.

### C2 — Vary city-card / city-page images (F07) — [content data, sized]
- **Verified:** 218/278 city `.md` files hard-code `hero_image: "Close-Protection-2560.webp"`. Under option D6(b): batch-replace these with a rotation of the better existing city/architecture images (varied, not one), or per-city where a real image exists. Under D6(a): source real per-city photography (larger effort). Either way this is a **data** change across up to 218 files — stage it, QA each batch, and prefer images without visible third-party branding.

### C3 — Unique heroes for listing / guide / blog / country / FAQ / contact (F05, F20, F23, F25) — [front matter]
- Assign a purpose-fit hero to each non-city template so `hero.jpg` stops appearing on 5+ page types. One image each; use the existing library first.

### C4 — Lagos (and any branded) hero + composition (F09, F19) — [asset + enhanced-hero.css]
- Replace the Lagos hero that shows a visible commercial billboard. Constrain the city-hero text column to ~650px and raise the scrim opacity (~40% → ~55%) in `enhanced-hero.css` for legibility.

---

# BATCH D — Footer credibility & lower-priority polish (needs D4/D5)
- **D1 (F21):** add company registration / VAT / SIA operator-licence line to the footer, and real social links (LinkedIn) — only true facts (D4/D5). Omit any that don't exist.
- **D2 (F14):** proper "Featured" cities on `/cities/` — add `featured: true` to ~6–8 high-demand city files (Lagos, Dubai, Nairobi, Bogota, Mexico City, Istanbul…) and filter the listing template to show those, replacing the current alphabetical B-city artefact.
- **D3 (F26):** FAQ accordion — add a visible open/close chevron (IcoFont is already loaded) and confirm the open state is visually distinct.
- **D4 (F18, services/country recs):** homepage "How It Works" gold CTA at section end; a "Where do you need cover?" city selector on `services/*`; a "Cities in {country}" grid on `countries/*` (also strengthens internal linking).
- **D5 (F23):** optional — blog categories via Hugo taxonomy (larger; defer unless wanted).
- **D6 (F24):** optional — a small shield/monogram logo lockup instead of the bare domain wordmark.

---

## Priority order (from the audit's impact ÷ effort, adjusted for the corrections)
1. **A1** gold CTAs (CSS, template-level) — biggest visual lift.
2. **A2** professional email + phone + dead-link fix (needs D1/D2/D3) — biggest trust lift.
3. **A3** footer Terms/Privacy repoint — trivial, legal/trust (pages already exist).
4. **B4** filterable location field — removes the worst mobile friction.
5. **A4 + A5** hide float-text + motion safety — remove "broken" perception.
6. **B1** CTA strips on silo/guide/blog — closes the biggest conversion gap.
7. **A6** real counter numbers.
8. **B3** sticky city CTA + mid-page CTA.
9. **B2** form trust strip.  10. **B6** mobile sticky CTA bar.
Then C (imagery, on D6) and D (footer/polish, on D4/D5).

## Verification checklist (per batch)
- [ ] `hugo --gc --minify` clean (0 errors, ~2,411 pages).
- [ ] No `outlook.com` anywhere in `site/` after A2.
- [ ] No `href="#"` dead links introduced; footer Terms/Privacy resolve.
- [ ] Gold CTAs render at rest AND on hover, desktop + mobile.
- [ ] New copy passes QA (British English, no em dashes, no safety-guarantee language).
- [ ] Reduced-motion: all sections visible.
- [ ] Mobile: location field filters; sticky CTA reachable and non-obscuring.
- [ ] Docs updated + live review URLs posted after deploy.

## Changes made and why
*(Append-only. Same format as the SEO build plan. Each entry: audit ID(s) · files · what · why · verification.)*

### Batch A — shipped 2026-07-03
DECISIONS answered: D1 = `info@closeprotectionhire.com` (email + FormSubmit endpoint); D2 = no phone (left out); D3 = "the bigger number" → real content counts used (270+ cities / 35+ countries, from actual 278 city / 36 country pages); D4/D5 = skipped (Batch D deferred); D7 = yes to all.

- **A1 (F02)** · `static/css/custom.css` · Overrode `.btn-main` (solid → gold `#c8a45e` bg / navy `#0a1628` text) and `.btn-main.btn-line` (outline → gold border/text, gold fill on hover) with hover/focus states · fixes the "no button anywhere is gold" brand gap · verified via rendered `public/css/custom.css` (8 gold rule matches) and Hugo build.
- **A2 (F01, F04)** · `hugo.toml`, `layouts/partials/header.html` · Replaced `garethsomers@outlook.com` with `info@closeprotectionhire.com` in `contactEmail` and `quoteFormEndpoint`; fixed the dead `href="#"` topbar link (now `/about/`) and corrected "15 countries" → "35+ countries" · removes the personal-email leak and a dead link, aligns the header claim with real coverage · verified zero `outlook.com` matches remain in `layouts/`/`hugo.toml`. **Action required:** `info@closeprotectionhire.com` is a new FormSubmit endpoint — needs a one-time activation click on first submission or enquiries silently fail.
- **A3 (F03)** · `layouts/partials/footer.html` · Repointed Terms & Conditions / Privacy Policy footer links from `href="#"` to `/terms/` and `/privacy/` (pages already existed — audit was wrong to suggest creating new ones) · fixes two dead links site-wide · verified in rendered `public/index.html`.
- **A4 (F10)** · `static/css/custom.css` · `.float-text`/`.float-text-right{display:none}` · removes the stray fixed-position "scroll to top" text overlay that bled over content · verified class present in built CSS.
- **A5 (F22)** · `static/css/custom.css` · Added `prefers-reduced-motion` and `.no-js` fallback rules forcing `.wow` elements visible · prevents blank dark sections for reduced-motion users / slow-JS loads.
- **A6 (F13)** · `layouts/index.html`, `layouts/partials/footer.html` · Stat counters now show real starting numbers (35/270/5/24) instead of "0"; reconciled all homepage + footer coverage copy ("15 high-risk cities", "80+ cities", counter values) to 270+ cities / 35+ countries · fixes a credibility bug where screenshots/no-JS/prerender showed "0+" and inconsistent coverage numbers across the site · verified in rendered `public/index.html`.

Build check: `hugo --gc --minify` → 2,411 pages, 0 errors. QA: no em dashes introduced, no safety-guarantee language, British English maintained.

### Batch B — shipped 2026-07-03
User granted standing approval to ship future batches straight to `master` without a per-batch approval round-trip; build-check + verification gate still runs before every commit.

- **B1 (F08, F15, F16)** · `layouts/_default/single.html`, `layouts/blog/single.html`, `layouts/blog/list.html`, `layouts/_default/list.html` · Added the post-hero CTA strip (copied from `services/single.html`) to the 6 silos + guides via `_default/single.html` (guard: `cta_text` OR `city` OR `Section == "guides"`, so pure utility pages stay clean), to blog articles, and a slim variant to `blog/list.html` and `_default/list.html` · closes the biggest conversion gap identified in the audit — these templates had no CTA above the bottom-of-page form · verified rendered output on a silo page (real `cta_text` renders), a guide (generic fallback renders — guides carry no `city` front-matter field, so the guard was extended to include `Section == "guides"` explicitly), a blog article, and both list pages; confirmed utility pages (`/about/`, `/privacy/`, `/terms/`) render zero CTA strips.
- **B2 (F08)** · `layouts/partials/quote-form.html`, `static/css/custom.css` · Added a gold `.form-trust-strip` ("Confidential · SIA-licensed operators · Response within 24 hours") directly above the submit button · gives the only real trust signal visibility at the point of commitment · verified rendered on a city page form.
- **B3 (F09, city conversion)** · `layouts/cities/single.html`, `static/css/enhanced-hero.css` · Moved the on-page jump-nav out of the `overflow:hidden` 70vh hero into its own standalone `.city-sticky-nav` section with `position:sticky;top:0` and an inline gold "Request Consultation" button; added one always-on mid-page CTA card between Zone Intelligence and Emergency Contacts · the original nested placement could not have stayed visible while scrolling a 7,000-9,700px city page since sticky positioning is bounded by its containing block, so it was restructured rather than just given `position:sticky` as literally described in the plan · verified the sticky nav persists past the hero on Lagos and Dubai city pages and the mid-page CTA renders city-specific copy.
- **B4 (F12)** · `layouts/partials/quote-form.html` · Replaced the 279-option `<select>` location field with a native `<input list>` + `<datalist>` (type-to-filter, zero JS dependency); datalist values switched from city slugs to human-readable titles for a cleaner enquiry email · removes the worst mobile form-friction point · verified the datalist renders and `FormData.get('location')` handling in `main.js` is type-agnostic (no changes needed there).
- **B5 (F11)** · `layouts/index.html` · Reduced the homepage hero form to Name, Email, and a combined "Destination & requirements" textarea (dropped the service-type and 279-city dropdowns from the hero form only; the full form remains at the page bottom and on all interior pages) · verified only 3 named fields (`hf-name`, `hf-email`, `hf-message`) render in the hero form.
- **B6 (global)** · `layouts/_default/baseof.html`, `static/css/custom.css` · Added a slim fixed bottom bar on mobile (`max-width:767px`) with a single "Request Consultation" tap target (no phone widget — D2 was left blank), plus `body{padding-bottom:60px}` on mobile so it never covers the footer form · verified present on both a content page and a utility page, and confirmed the pre-existing `.scrollbar-v` element is already hidden on mobile so there is no positioning conflict.

Build check: `hugo --gc --minify` → 2,411 pages, 0 errors. QA: no em dashes introduced (pre-existing em dashes in two CSS comments predate this session and are not rendered content), no safety-guarantee language, British English maintained. Note: `static/css/custom.css` and `enhanced-hero.css` are copied verbatim into `public/` (not minified) since they're static passthrough files, not Hugo Pipes assets — this is expected Hugo behaviour, not a build issue.

### Batch D (un-gated items only) — shipped 2026-07-03
Skipped per user instruction: D1/legal footer credentials, social links (needs D4/D5 - not provided), imagery (Batch C, needs D6 - not provided), and the two items the plan itself marked optional/defer (blog taxonomy categories, logo lockup).

**Correction to the audit/plan:** the plan's D4 item "add a 'Cities in {country}' grid on countries/*" turned out to already exist and work — `countries/single.html` has a "Key Cities" section driven by `.Params.cities`, and all 36 country content files already populate it. No action needed there.

- **D2 (F14)** · `content/cities/{lagos,dubai,nairobi,bogota,mexico-city,istanbul}.md`, `layouts/_default/list.html` · Added `featured: true` to 6 high-demand cities; changed the list template's "Featured" section to prefer pages with `featured: true` (falling back to the previous first-4 behaviour when a section has none set) · replaces the "current alphabetical B-city artefact" on `/cities/` with a genuinely curated set · verified the Featured section on `/cities/` now shows Bogota, Dubai, Istanbul, Lagos (first 4 of the 6 flagged); confirmed sections with no featured pages (services, risk-assessments) are unaffected since the fallback preserves prior behaviour.
- **D3 (F26)** · `static/css/custom.css` · The FAQ chevron already existed (Bootstrap's default `::after` icon) but was invisible: its SVG fill was near-black (`#212529`) against the dark theme, and the open state used Bootstrap's default light-blue background/text, clashing with the dark theme entirely. Overrode both the chevron icon color (white at rest, gold when open, with the existing 180° rotation) and the open-state colors (gold text on a distinct dark shade `#1e293b`) plus a gold focus ring · gives the accordion a working, visible, on-brand open/close indicator · verified new CSS rules present in built output.
- **D4 (F18, partial)** · `layouts/index.html`, `layouts/services/single.html`, `content/services/{event-security,residential-security,security-drivers}.md` · Added a gold "Start Your Consultation" CTA at the end of the homepage "How It Works" section. Retitled the services template's existing (but under-used) "Available Locations" grid to "Where do you need cover?" to match the plan's framing. Found 3 of 5 service hub pages (`event-security`, `residential-security`, `security-drivers`) had no `locations` front matter at all, so that grid never rendered on them — populated all 3 with the same 8-city set already used by `bodyguard-hire.md`/`executive-protection.md`, so every service hub now shows a working location selector · verified all 5 `/services/*/` hub pages render the "Where do you need cover?" heading and a populated city grid (Lagos link confirmed present on the previously-empty `event-security` page).

Build check: `hugo --gc --minify` → 2,411 pages, 0 errors. QA: no em dashes introduced, British English maintained, no safety-guarantee language.

### C4 legibility fix (CSS-only, decoupled from the imagery decision) — shipped 2026-07-03
User confirmed no legal/registration/social facts exist (D4/D5) and elected to leave imagery alone permanently (D6) — Batch C and the D1 footer-credibility line are now out of scope, not just gated-pending. Pulled the one sub-item from C4 that is pure CSS and independent of which photo is used.

- **C4 legibility half (F09, F19 partial)** · `static/css/enhanced-hero.css` · Constrained the city-hero text column to `max-width:650px` (was full `col-lg-9`, ~75% of the container on large screens) and deepened the hero scrim (vertical gradient mid-stop 0.35→0.55 as specified; other stops raised proportionally, right-hand edge of the horizontal gradient left at 0 so the photo still shows through where there's no text) · improves text legibility over hero photos without touching which image is used, so it doesn't require the imagery decision the user declined · verified both rules present in the built CSS. The other half of C4 (replacing the Lagos hero that shows a visible commercial billboard) remains skipped along with the rest of Batch C.

Build check: `hugo --gc --minify` → 2,411 pages, 0 errors.

---

# SEO / technical batch (from GPT repo audit, 3 July) — shipped 2026-07-03
A second-opinion technical SEO audit (ChatGPT) was run against the repo. I re-verified all 10 findings against `master` (it had audited a different branch and used root-level paths). Most were accurate; several were gaps my earlier SEO pass left in the per-section templates, and the coverage-claim inconsistency was partly introduced by design Batch A. User decisions: CRM key = hide-but-keep-function (see note); coverage = push 270+ everywhere; About reviewer = use James Calloway persona; build items = all.

- **Template `seo_title` + schema (audit #1, #3)** · `layouts/cities/single.html`, `layouts/services/single.html`, `layouts/countries/single.html`, `layouts/index.html` · These three dedicated templates hardcoded their `<title>` (ignoring the `seo_title` 270 city files define) and interpolated `"{{ .Description }}"` raw into JSON-LD (breaks on a quote). Now honour `seo_title` with a sensible fallback, and use `jsonify` on name/description. Also removed the homepage's duplicate Organization node (baseof already emits the canonical one with `@id`); replaced it with a WebSite entity · verified Dubai now renders its `seo_title`, all JSON-LD parses, homepage has one Organization + one WebSite.
- **Coverage claims → 270+ (audit #7)** · `content/{cities,services,countries}/_index.md`, `content/{about,contact,network,faq}.md`, `static/llms.txt` · Reconciled every "15 cities"/"90+" claim to "270+ cities" per user decision. Where a sentence claimed a physical rostered operator per city, softened to "priority cities carry..." so the larger number stays defensible rather than claiming 270+ staffed networks · verified no "15 high-risk/priority/primary" or "90+" strings remain.
- **About reviewer E-E-A-T (audit #9)** · `content/about.md` · Replaced the literal `[Author Name]` placeholder with the site's established James Calloway persona · per user decision to use the existing persona.
- **Internal linking to money pages (audit #8)** · `layouts/services/single.html`, `layouts/partials/footer.html` · Service-hub location grids now link to the service-specific city page (`/bodyguard-hire/lagos/` etc.) with descriptive anchor text ("Lagos Bodyguard Hire"), existence-guarded via `.Site.GetPage` with a `/cities/{slug}/` fallback so no dead links (the exact bug pattern from the SEO session's sub-batch 20). Expanded the footer "Company" column to include About, Guides, Blog, Countries, FAQ (previously unlinked from the footer) · verified service-city links render, fallback works for any missing combination, and all footer targets exist.
- **LCP priority hints (audit #4, partial)** · 9 hero templates · Added `fetchpriority="high" decoding="async"` to every eager LCP hero image · the highest-value LCP lever without a risky asset-pipeline migration. The full responsive `srcset`/multi-width pipeline (moving heroes into Hugo's `assets/` and resizing) is deliberately NOT done here: it would touch every hero across 2,411 pages and the image library, and is better as a dedicated, separately-verified migration. Flagged to the user.
- **Honeypot correctness (audit #6a)** · `assets/js/main.js` · The JS checked/deleted a field named `website`, but the form's honeypot is `_honey`; aligned both. Inert dead code before (FormSubmit's server-side `_honey` still worked), now consistent.
- **Stale `build/` output (audit #2)** · Removed the 89-file legacy `build/` directory from git tracking (its `sitemap.xml` had 80 `[DOMAIN]` placeholders and old `.html` URLs) and added `build/` to `.gitignore`. It was never the live source (deploy builds from `site/`), so this is hygiene against future automation footguns.
- **QA gate silo expansion (audit #5, partial)** · `scripts/qa_audit.py` · Added the 6 commercial silos (`bodyguard-hire`, `executive-protection`, `close-protection-officers`, `security-drivers`, `residential-security`, `secure-airport-transfers`) to the audit's SILOS list. This immediately surfaced **31 real pre-existing errors** in those never-audited pages (banned AI-tell words + 3 "eliminate risk" phrasings). Fixed all 35 occurrences across ~30 content files in context (British English, meaning preserved); the "eliminate risk" cases were all safe disclaimers that tripped the YMYL regex, reworded to "remove risk entirely". Gate now: **2,375 pages, 0 errors.** NOTE: I cannot wire `qa_audit.py` into CI myself — the MCP token 403s on `.github/workflows/`. That step needs a manual workflow edit (see below).

## Still open (need the user)
- **CRM API key exposure (audit #6b) — NOT yet fixed.** `assets/js/main.js` hard-codes an `x-api-key` and POSTs PII from the browser to the Render CRM. User chose "hide the key but keep functionality." **A static site cannot hold a secret and call the API directly from the browser** — any key shipped to the page is public by definition. Genuinely hiding it while keeping lead capture requires a server-side intermediary (a serverless proxy that holds the key; the browser calls the keyless proxy, origin-restricted). I deliberately did NOT ship obfuscation (base64/string-splitting) because that is security theatre, not protection, and would break lead capture if done wrong. Recommended path: a small Cloudflare Worker / Netlify function / a route on the existing Render service that holds the key server-side; then I repoint the JS at it and delete the client key. Needs the user to deploy the proxy (and ideally rotate the leaked key). Functionality left untouched until then.
- **CI QA gate wiring (audit #5)** — needs a manual `.github/workflows/build-and-publish.yml` edit (MCP token cannot write workflows).
- **`.htaccess` redirects + GSC verification (audit #10)** — needs the live www/http behaviour on Hostinger and a GSC token; risky to guess blind.
- **Full responsive-image `srcset` pipeline (audit #4)** — larger migration, available on request.

Build check: `hugo --gc --minify` → 2,411 pages, 0 errors. QA gate: `qa_audit.py` → 2,375 pages, 0 errors (expanded silos). All JSON-LD validated as parseable.
