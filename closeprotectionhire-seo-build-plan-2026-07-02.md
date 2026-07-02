---
title: SEO Build Plan — CloseProtectionHire.com
date: 2026-07-02
companion: seo-audit-2026-07-02.html
execution_model: Sonnet (steps flagged OPUS-REQUIRED must run on Opus)
branch: master   # per CLAUDE.md — master is the ONLY deploy branch. Never main.
---

# SEO Remediation — Execution Build Plan

> Read `seo-audit-2026-07-02.html` first for the *why* and the trade-offs. This file is the *how*.
> Every batch below is a self-contained unit: edit → local `hugo --gc --minify` build check → QA gate → HTML preview → approval → one commit → one push to `master`.
> This obeys the Engine 7 loop in `CLAUDE.md`. Do not merge batches or skip the build check.

## Model legend
- **[SONNET]** — mechanical, fully specified. Safe for Sonnet execution.
- **[OPUS-REQUIRED]** — judgement under ambiguity or non-boilerplate authoring at scale. Must run on Opus. Do not let Sonnet improvise these.

## Global guardrails (apply to every batch)
1. **Branch:** confirm `master` before any edit. Never `main`.
2. **Template quote safety:** in any `printf` inside a layout, use backticks — `printf \`%.1fs\` $x` — never escaped inner double-quotes. A ~17s red build = a template parse error (see CLAUDE.md).
3. **JSON-LD safety:** wrap every interpolated string in schema with `| jsonify` (e.g. `"name": {{ .Title | jsonify }}`). This prevents an unescaped quote in city/description text from breaking the JSON and the build.
4. **Build check before every commit:** from `site/`, run `hugo --gc --minify`. Expect 200+ pages, 0 errors. A failed or ~17s build must be fixed before commit.
5. **QA gate:** no em dashes (anywhere, incl. layout string values), no safety-guarantee language, British English. Run `scripts/qa_audit.py` logic on any content touched.
6. **One commit + one push per batch.** Await explicit approval ("approve" / "ship it") before committing, per CLAUDE.md.
7. **No new colour tokens, fonts, layouts, or top-level dirs** without approval. Template *edits* to existing files are fine; new *layouts* are not.

---

# BATCH 1 — Repair the fallback template (CRITICAL, highest ROI)
**Fixes Findings 1, 3, 4, 11. Model: [SONNET].**
**One file: `site/layouts/_default/single.html`. Repairs 1,638 silo pages in one deploy.**

### 1.1 Render the `components` array
Port the card grid from `site/layouts/event-security/single.html` (lines ~84–110). Insert into `_default/single.html` **after** the `{{ with .Content }}…{{ end }}` section and **before** the FAQ partial:

```go-html-template
{{/* ===== SERVICE COMPONENTS ===== */}}
{{ with .Params.components }}
<section class="section-dark bg-dark-2 text-light">
    <div class="container">
        <div class="row mb-4">
            <div class="col-lg-12">
                <div class="subtitle wow fadeInUp">What this covers</div>
                <h2 class="wow fadeInUp" data-wow-delay=".2s">Operational detail for {{ $.Params.city | default $.Title }}</h2>
            </div>
        </div>
        <div class="row g-4">
            {{ range $i, $comp := . }}
            <div class="col-lg-4 col-md-6 wow fadeInRight" data-wow-delay="{{ printf `%.1fs` (mul (mod $i 3) 0.2) }}">
                <div class="bg-dark rounded-1 p-40 h-100">
                    {{ if reflect.IsMap $comp }}
                    <h3 class="fs-20">{{ $comp.title }}</h3>
                    <p class="mb-0">{{ $comp.description }}</p>
                    {{ else }}
                    <h3 class="fs-20">{{ $comp }}</h3>
                    {{ end }}
                </div>
            </div>
            {{ end }}
        </div>
    </div>
</section>
{{ end }}
```
- Note: `printf \`%.1fs\`` uses backticks (safe). `mod $i 3` keeps the stagger in the 0–0.4s range regardless of component count.
- Use `<h3>` (not `<h4>`) for component titles so the heading outline is H1 → H2 → H3.

### 1.2 Add a schema block (Service + FAQPage + BreadcrumbList)
Add at the **top** of `_default/single.html`, before `{{ define "main" }}`:

```go-html-template
{{ define "schema" }}
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": {{ (printf "%s in %s" (humanize .Section) (.Params.city | default .Title)) | jsonify }},
    "serviceType": {{ (humanize .Section) | jsonify }},
    "description": {{ .Description | default .Title | jsonify }},
    "provider": {
        "@type": "Organization",
        "name": {{ .Site.Params.brand | jsonify }},
        "url": "https://closeprotectionhire.com"
    },
    "areaServed": {
        "@type": "City",
        "name": {{ (.Params.city | default .Title) | jsonify }}
    }
}
</script>
{{ with .Params.faqs }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{ range $i, $f := . }}{{ if $i }},{{ end }}{
      "@type": "Question",
      "name": {{ $f.question | jsonify }},
      "acceptedAnswer": { "@type": "Answer", "text": {{ $f.answer | jsonify }} }
    }{{ end }}
  ]
}
</script>
{{ end }}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://closeprotectionhire.com/" },
    {{ with .Section }}{ "@type": "ListItem", "position": 2, "name": {{ (humanize .) | jsonify }}, "item": {{ (printf "https://closeprotectionhire.com/%s/" .) | jsonify }} },{{ end }}
    { "@type": "ListItem", "position": 3, "name": {{ .Title | jsonify }}, "item": {{ .Permalink | jsonify }} }
  ]
}
</script>
{{ end }}
```
- This gives all six silos Service + FAQ + Breadcrumb structured data they currently lack.
- **Do NOT add `aggregateRating` or review counts.** YMYL structured-data spam risk.
- **CORRECTNESS GUARD (added during execution 2026-07-02):** `_default/single.html` also renders utility pages (about, contact, privacy, terms, faq) and guides that have no `city`. Emitting a `Service`/`areaServed` node on those produces nonsense (e.g. `"About in About"`). The Service node is therefore wrapped in `{{ if .Params.city }}…{{ end }}`; FAQPage stays guarded by `{{ with .Params.faqs }}` and BreadcrumbList emits on every page. Verified: `public/about/index.html` has BreadcrumbList only, no Service.

### 1.3 (Optional, same batch) De-duplicate FAQ markup
The `faq-accordion.html` partial still emits microdata FAQPage. With JSON-LD now present, you may strip the `itemscope`/`itemprop`/`itemtype` attributes from that partial to avoid a double declaration. **Low priority — skip if it risks touching the accordion's behaviour.** The double declaration is not harmful, just redundant.

### 1.4 Verify & ship
- Build: `cd site && hugo --gc --minify` → 0 errors.
- Spot-check rendered HTML for `bodyguard-hire/abidjan/` (or any silo page): the six components must now appear, and three `application/ld+json` scripts must be in `<head>`.
- Validate one page's JSON-LD (Rich Results Test or a JSON linter on the emitted blocks).
- Preview → approve → commit → push `master`.
- **Post-deploy:** verify re-indexing via URL Inspection tool on ~5 sample pages, NOT the GSC bulk report (lagged since 11 June).

**Live review links to output after deploy:** one URL per section sample, e.g.
`/bodyguard-hire/abidjan/`, `/executive-protection/lagos/`, `/close-protection-officers/nairobi/`, `/security-drivers/dubai/`, `/residential-security/mexico-city/`, `/secure-airport-transfers/istanbul/`.

---

# BATCH 1B — llms.txt (DISCOVERABILITY) — **[SONNET]**
**Added 2026-07-02 per session rule 5. This OVERRIDES the audit's Finding 13 note that llms.txt is safe to skip.**
> Rationale: Google does not read `llms.txt`, but other AI systems (some ChatGPT, Perplexity, Claude retrieval paths and a growing set of agents) do, and it drives real referral traffic. The site's `robots.txt` already advertises `# LLM map: https://closeprotectionhire.com/llms.txt` in a comment, so the file is *expected but missing* (currently 404). Treat llms.txt as a live, maintained deliverable, upgraded as later batches land.

### 1B.1 Create `site/static/llms.txt` (Sonnet OK)
- Follow the emerging llms.txt convention: H1 site name, a `>` blockquote one-line summary, then themed `##` sections of Markdown links (`- [Label](https://…): short description`).
- Sections to include: Core Services (the 7 silos' section hubs), Locations (city hub + a curated set of priority cities, not all 278 — link the hub and let it fan out), Guides, Blog hub, Risk Assessments, Company (about/contact/faq).
- Keep it curated and honest — llms.txt is a map, not a dump. Link hubs, not every one of 2,400 pages.
- Absolute URLs. British English. No em dashes. No safety-guarantee language (same QA gate as content).

### 1B.2 Decision questions for this batch
- **Q(1B-a):** Curated hub-level llms.txt (recommended — link section hubs + ~15 priority cities), or an exhaustive variant that also enumerates every city? *Recommendation: curated hub-level; exhaustive lists read as spam to the same systems we want citations from and go stale fast.*
- **Q(1B-b):** Do you want a richer `llms-full.txt` companion (full expanded descriptions) later, or is the single `llms.txt` enough for now? *Recommendation: single file now; revisit after Batch 6 answer-blocks exist, since those make ideal llms.txt descriptions.*

### 1B.3 Upgrade hooks (maintenance)
- After Batch 3 (country dedupe): ensure no retired slug (`/countries/uk/`, `/countries/usa/`) appears in llms.txt.
- After Batch 6 (answer-first): reuse the direct-answer sentences as the llms.txt link descriptions.
- Record every llms.txt change in the changelog like any other fix.

### 1B.4 Verify & ship
- Build check (`llms.txt` is a static file, so confirm it lands at `public/llms.txt`).
- Confirm it is reachable at the URL the `robots.txt` comment advertises.

---

# BATCH 2 — Social cards + Organization entity (HIGH)
**Fixes Findings 5, 6. Model: [SONNET].**
**Files: `site/layouts/_default/baseof.html`, plus a new shared partial `site/layouts/partials/schema-organization.html`.**
> Note: a partial file under `layouts/partials/` is an edit to the template system, not a new *page layout*. Permitted. If in doubt, inline the Organization JSON into `baseof.html` instead of a partial.

### 2.1 og:image fallback + Twitter Card (in `baseof.html`, in the head)
Replace the current single conditional `og:image` line with:
```go-html-template
{{ $ogImg := .Params.og_image | default .Params.hero_image | default "Close-Protection-2560.webp" }}
<meta property="og:image" content="{{ (printf "/images/%s" $ogImg) | absURL }}">
<meta property="og:site_name" content="{{ .Site.Params.brand }}">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ .Title }}">
<meta name="twitter:description" content="{{ with .Description }}{{ . }}{{ else }}{{ .Site.Params.description }}{{ end }}">
<meta name="twitter:image" content="{{ (printf "/images/%s" $ogImg) | absURL }}">
```
- Use `absURL` — relative image URLs break social/AI cards.
- Confirm `Close-Protection-2560.webp` exists in `site/static/images/` (it is used elsewhere, so it should).

### 2.2 Strengthen the Organization entity
Add a sitewide Organization node. Simplest safe route: emit it once in `baseof.html` head (so it appears on every page) with an `@id`, and have Service nodes reference that `@id`.
```go-html-template
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://closeprotectionhire.com/#organization",
  "name": {{ .Site.Params.brand | jsonify }},
  "url": "https://closeprotectionhire.com/",
  "logo": "{{ "/images/Close-Protection-2560.webp" | absURL }}",
  "description": {{ .Site.Params.description | jsonify }},
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "email": {{ .Site.Params.contactEmail | jsonify }}
  }
}
</script>
```
- **`sameAs`:** add ONLY if real social/directory profiles exist. If they do, append `"sameAs": ["<real-url>", …]`. Do not invent profiles (authenticity violation — see brief).
- Optional refinement: change Service nodes' `provider` to `{ "@id": "https://closeprotectionhire.com/#organization" }` to reference rather than re-declare. Safe but not required for this batch.

### 2.3 Verify & ship
- Build check, preview `<head>` on home + one silo + one city page, approve, commit, push.

---

# BATCH 3 — Duplicate country pages (HIGH)
**Fixes Finding 7. Model: [SONNET].**

1. Choose survivors: recommend `united-kingdom` and `united-states` (full-word). If Search Console impression data is available, keep the higher-traffic slug instead.
2. `git rm` (or delete via workflow) `content/countries/uk.md` and `content/countries/usa.md` (the retired pair).
3. Add 301s in `site/static/_redirects` — **match the existing file's syntax exactly** (read it first):
   `/countries/uk/    /countries/united-kingdom/    301`
   `/countries/usa/   /countries/united-states/     301`
4. Repoint internal links: `grep -rn '/countries/uk/\|/countries/usa/' site/content site/layouts` and update any hits to the survivor slug.
5. Build check, preview, approve, commit, push.

---

# BATCH 4 — Cannibalisation decision (CRITICAL) — **[OPUS-REQUIRED]**
**Addresses Finding 2. This step is a DECISION, not an edit. Run on Opus.**

> **Do not start Batch 5 until this is decided and written down.** Sonnet must not pick the option or invent the differentiation model.

Deliverable of this step: a one-page decision memo committed alongside this plan, specifying:
1. **Chosen option** — A (consolidate + canonical), B (differentiate intent), or C (prune + 301). See the audit HTML, Finding 2, for the trade-offs.
2. If **A**: which silo is the canonical target per city, and the exact `canonical` front-matter/template mechanism.
3. If **B**: the explicit, genuinely distinct intent definition for each of the three silos, with an authored example page proving the differentiation is real (not city-name-swapped boilerplate).
4. If **C**: the survivor silo and the full 301 map.
5. The rollout spec precise enough that Sonnet can execute Batch 5 mechanically.

**Why Opus:** ~810 pages are affected; the wrong call (or a lazy "differentiation" that is really duplication) is worse than doing nothing and is hard to reverse once indexed.

---

### BATCH 4 DECISION (2026-07-02) — user chose **Option B: differentiate intent**

**Differentiation model (the three silos each own a distinct intent):**

| Silo | Intent | Buyer | Page leads with | Head keyword |
|---|---|---|---|---|
| `bodyguard-hire` | **Transactional** — hire cover for a specific trip/period | Traveller / EA needing cover now | How hire works, what an officer does day-to-day, speed of engagement, cost | "bodyguard hire {city}", "hire a bodyguard {city}" |
| `executive-protection` | **Programme** — organisational, duty-of-care protection | Corporate security manager / EA | Advance work, written threat assessment, ops controller, layered coverage, corporate duty of care | "executive protection {city}", "corporate close protection {city}" |
| `close-protection-officers` | **Operators** — the people, credentials, standards | Buyer vetting operators | Who the CPOs are, vetting, licensing, team configuration, standards to verify | "close protection officers {city}", "CPO {city}" |

**Per-silo structural recipe (applied per city, kept city-specific):**
- **bodyguard-hire:** intro frames a short-notice, trip-tied hire; components emphasise engagement, per-visit scaling, officer + driver + vehicle package; FAQs keep how-much / how-fast / what-a-bodyguard-does; cross-link to EP ("for a corporate programme") and CPO ("to check credentials").
- **executive-protection:** intro frames a corporate programme + duty of care; components emphasise advance work, threat assessment, ops controller, venue/accommodation assessment, incident response; FAQs keep programme / duty-of-care / sectors; cross-link to bodyguard-hire ("for short-term single-principal hire") and CPO ("the operators behind the programme").
- **close-protection-officers:** intro frames the operators and their credentials; components emphasise vetting, licensing, team size, armed-CPO standards; FAQs keep licence / team-size / vetting; cross-link to bodyguard-hire and EP.
- **Every intro must carry a city-specific hook** (the city's signature threat + named regulator), or it fails the "name-swap = worse than nothing" guardrail.

**Proof sample authored + signed off:** Lagos × 3 silos (see chat 2026-07-02). Distinct buyer, question, and emphasis confirmed.

**Rollout (Batch 5) — HONEST SCOPE:** this is a ~824-page content programme, not a single batch. It must be staged in approval-gated sub-batches (~10 cities per run = 30 pages), each: author 3 city-specific ledes + reframe components/FAQs + add cross-links → build check → QA gate → preview → approve → commit. Opus authors the rubric and each sub-batch's first sample; Sonnet may extend within a sub-batch only under the "genuinely specific or leave unset" guardrail. Priority order = the 15 answer-block cities first (already have direct-answer copy to align with), then the rest of the network.

---

# BATCH 5 — Execute the cannibalisation rollout (CRITICAL)
**Model: [SONNET], driven strictly by the Batch 4 memo.**
- Execute exactly what the memo specifies. If the memo is option A, apply canonical tags; if C, apply redirects + deletions; if B, apply the authored differentiation.
- Because this touches ~810 pages, split into approval-gated sub-batches (per CLAUDE.md's "up to 4 blocks per run" cadence — treat e.g. ~10 cities as a block). Do not push all 810 in one run.
- Build check + QA gate each sub-batch. Preview, approve, commit, push per sub-batch.
- **Sequence note:** complete this BEFORE Batch 7 (internal links) so you don't hard-wire links into pages you are about to canonicalise or redirect.

---

# BATCH 6 — Direct-answer / AI Overview block (MEDIUM)
**Fixes Finding 8. Template = [SONNET]; copy pattern + first tranche = [OPUS-REQUIRED].**

### 6.1 Template (Sonnet)
- Add an `answer` front-matter field convention.
- In `_default/single.html` and `cities/single.html`, render it as a styled lead block directly under the H1 (before the hero narrative), falling back to `.Description` when `answer` is absent:
```go-html-template
{{ with .Params.answer }}<div class="direct-answer"><p>{{ . | markdownify }}</p></div>{{ end }}
```
- Style `.direct-answer` in `site/static/css/custom.css` (append-only — do not edit `style.css`).

### 6.2 Copy pattern + first tranche — **[OPUS-REQUIRED]** — sub-plan
Render path (6.1) is live and is a no-op until `answer:` front matter is populated. This step authors that copy. **Runs on Opus** (rule 2): non-boilerplate authoring at scale, needs a rubric + a hand-checked sample before any bulk pass.

**6.2.1 — Decide scope (DECISION for user, before authoring):**
- **Q(6.2-a) Which page types get an `answer` first?** Options: (i) city pages only, (ii) the 3 CPO-intent silos only, (iii) city pages + all 6 silos. *Recommendation: city pages first (highest-intent, fewest pages, cleanest win), then extend to silos after Batch 4/5 resolves the cannibalisation model — authoring silo answers before that risks writing copy for pages that may be canonicalised.*
- **Q(6.2-b) First-tranche size?** ~15 priority cities (matches llms.txt set) vs ~40. *Recommendation: 15 first, review, then scale.*

**6.2.2 — Write the rubric (Opus):** a 40–55 word answer that (a) names the service + city in the first clause, (b) states the single most decision-relevant local fact (a named regulator, a specific threat, a licensing constraint) drawn from the page's own sourced `components`, (c) ends with the practical implication for a principal. British English, no em dashes, no safety-guarantee language.

**6.2.3 — Author + hand-check a 3-page sample (Opus):** write 3, verify each is genuinely city-specific (fails if it reads as a template with the name swapped), confirm QA gate. Get user sign-off on the sample before the tranche.

**6.2.4 — Author the tranche (Opus), add `answer:` to each page's front matter.** Build check + QA gate. Preview, approve, commit, push.

**6.2.5 — Extension (Sonnet OK, later):** once the rubric + sample are locked, Sonnet may extend city-by-city under the normal QA gate, but **must** apply the "genuinely specific or leave unset" guardrail — identical name-swapped answers re-create the thin-content problem and are worse than no answer.

**6.2.6 — Maintenance hook:** after the tranche, update `llms.txt` link descriptions to reuse these answer sentences (per Batch 1B.3).

---

# BATCH 7 — Internal link graph (MEDIUM)
**Fixes Finding 9. Model: [SONNET]. Run AFTER Batch 5.**
- Add two template-driven blocks (to `_default/single.html`), driven by `.Params.city` / `.Params.country`:
  1. **"Related security services in {city}"** — links the sibling silos for the same city (respecting any canonical/redirect decisions from Batch 5 — do not link to pages that were canonicalised away).
  2. **"Nearby cities / same country"** — links other cities sharing `.Params.country`.
- Use descriptive anchor text (never "click here"), relative URLs.
- Build the sibling-service links by convention (`/{silo}/{city-slug}/`), verifying the target exists via Hugo's `.Site.GetPage` so you never emit a dead link.
- Build check, preview, approve, commit, push.

---

# BATCH 8 — Blog Article schema (MEDIUM)
**Fixes Finding 10. Model: [SONNET]. File: `site/layouts/blog/single.html`.**
- Add to the Article JSON-LD: `image` (the hero, absolute URL), `mainEntityOfPage` (the permalink).
- Replace the hardcoded author `description` with a per-persona lookup. The two personas (James Calloway, Marcus Webb) are defined in `AGENTS.md`; build a small dict keyed on `.Params.author` giving each its correct bio and (real) `sameAs` if any exist.
- **Guardrail:** do not attach a real individual's credentials to a persona byline misleadingly. Bios must match the persona system already in use.
- Build check, preview, approve, commit, push.

---

# BATCH 9 — Sitemap tuning (LOW, optional)
**Fixes Finding 12. Model: [SONNET].**
- Optional, low leverage (Google largely ignores sitemap priority). If done: per-section priority via a custom `sitemap.xml` template or front-matter `sitemap` params — homepage/city hubs higher (0.8), deep combinatorial pages lower (0.4).
- Do this only after Batches 1–8 ship. Do not prioritise over anything above.

---

## Post-implementation verification checklist
- [ ] `hugo --gc --minify` clean (0 errors) after every batch.
- [ ] Sample silo page HTML now contains rendered components + 3 JSON-LD blocks (Batch 1).
- [ ] Rich Results Test passes for one page each of: silo, city, blog, country.
- [ ] Social card preview (LinkedIn Post Inspector / X card validator) shows an image (Batch 2).
- [ ] No `/countries/uk/` or `/countries/usa/` internal links remain (Batch 3).
- [ ] Cannibalisation memo committed before any Batch 5 edit (Batch 4).
- [ ] Re-indexing checked via **URL Inspection tool**, not the lagged GSC bulk report.
- [ ] Position tracking (Ahrefs/Semrush) set as the movement monitor, not Semrush Sensor.
- [ ] `BUILD-PLAN.md`, `build_state.json`, `bodyguard-cascading-build-plan.html` updated once per batch; session log entry added.

## Summary: what needs Opus
| Step | Why Opus |
|---|---|
| **Batch 4** — cannibalisation decision | Judgement under ambiguity across ~810 pages; wrong call is hard to reverse. |
| **Batch 6.2** — direct-answer copy pattern + first tranche | Non-boilerplate authoring at scale; templated answers re-create thin content. |

Everything else (Batches 1, 2, 3, 5-exec, 6.1, 7, 8, 9) is safe on **Sonnet** with the build-check + QA gate discipline above.

---

## Changes made and why
*(Append-only log. Written so entries can be lifted straight into the routine build prompts. Each entry: finding ID · files/lines · what · why · verification.)*

### 2026-07-02 — Batch 1: Repair fallback template (Findings F1, F3, F4, F11)
- **File:** `site/layouts/_default/single.html`
  - **Added `{{ define "schema" }}` block (new, top of file, ~48 lines).** Emits three JSON-LD scripts: `Service` (guarded by `{{ if .Params.city }}`), `FAQPage` (guarded by `{{ with .Params.faqs }}`, ranges the `faqs` array), and `BreadcrumbList` (Home → Section → Page, always). All interpolated strings use `| jsonify` to prevent quote-injection build breaks.
    - *Why:* the 6 service silos (1,638 pages) fell through this template, which had **no** schema block, so they emitted zero structured data (F3). FAQ was microdata-only (F4) and there was no BreadcrumbList anywhere (F11). Service+FAQ+Breadcrumb JSON-LD is what Google uses for entity binding and AI-Overview eligibility.
    - *Correctness guard added vs. the original plan:* Service node wrapped in `{{ if .Params.city }}` so utility/guide pages (about, contact, guides) don't emit nonsense `"About in About"` Service schema.
  - **Added `{{/* SERVICE COMPONENTS */}}` section** between `.Content` and the FAQ partial (~26 lines). Ports the `event-security` card-grid pattern: ranges `.Params.components`, renders `title`/`description` per component in a 3-col grid, using the safe backtick `printf` (`printf \`%.1fs\``) for the WOW stagger.
    - *Why (F1, highest ROI):* every silo page carried 6 sourced intelligence components (~900 words) in front matter that the fallback template **never rendered**. 1,638 pages were shipping ~250 visible words while their best, sourced content was invisible to Google — the exact thin/scaled-content profile the June 2026 spam update targets. Now rendered.
- **Verification:** `hugo --gc --minify` clean, 2,413 pages, 0 errors (baseline was also 2,413/0). Components confirmed rendering on `bodyguard-hire/abidjan`. JSON-LD validated by parser across 120 random silo pages: 359 blocks, 0 parse errors. Guard confirmed: `about` page has BreadcrumbList only, no Service. Pages without FAQs correctly emit 2 blocks not 3.
- **Status:** committed to `claude/close-protection-seo-audit-0yjirj` (deploy to `master` is via PR/merge, not direct push). Deferred question resolved by default (user said "continue" after the approval prompt failed to deliver).
- **Decision 1.3 (resolved — leave as-is):** the redundant FAQ microdata in `partials/faq-accordion.html` was LEFT in place. It is harmless (JSON-LD is the primary signal) and stripping it carried a small risk of disturbing the Bootstrap accordion. Revisit only if a validator flags a double-declaration warning.

### 2026-07-02 — Batch 1B: llms.txt (session rule 5 — overrides audit Finding 13)
- **File:** `site/static/llms.txt` (new, ~6 KB, 40 curated links).
  - Hub-level map (decision 1B-a = curated, not exhaustive): H1 + `>` summary noting sourcing (FCDO/OSAC/ACLED/national licensing), then sections — Core services (7 silo hubs + services overview), Locations (cities hub + 14 priority cities + countries hub), Regulations and guides, Travel safety guides, Risk assessments, Intelligence/blog, Company (about/contact/faq).
  - Decision 1B-b = single `llms.txt` for now; `llms-full.txt` deferred until Batch 6 answer-blocks exist to feed richer descriptions.
  - *Why:* other AI systems read llms.txt and it drives referral traffic; the site's `robots.txt` already advertised `# LLM map: …/llms.txt` but the file was a 404. Now live.
- **Verification:** all 40 links resolve to real rendered pages (parser-checked against `content/` + confirmed `public/*/index.html`); QA clean (no em dashes, no safety-guarantee language); build clean, lands at `public/llms.txt`.
- **Status:** committed to `claude/close-protection-seo-audit-0yjirj`.
- **Maintenance hooks live:** after Batch 3 re-check for retired country slugs; after Batch 6 swap link descriptions for the direct-answer sentences.

### 2026-07-02 — Batch 2.1: Social cards (Finding F5)
- **File:** `site/layouts/_default/baseof.html` (head). Added an `$ogImg` fallback chain (`.Params.og_image` → `.Params.hero_image` → `Close-Protection-2560.webp`), resolved to an absolute URL via `absURL`. Added `og:site_name`, `og:locale=en_GB`, an always-present `og:image`, and a full Twitter `summary_large_image` card (title/description/image).
  - *Why:* 0 content files set `og_image` and there were no Twitter tags, so every share/AI preview rendered a blank card on a referral-driven business.
- **Verification:** build clean (0 errors). Confirmed absolute `og:image` on silo, homepage, and blog pages; Twitter card present on blog; per-page `hero_image` respected (Almaty uses its own image, not the default).
- **Status:** committed to `claude/close-protection-seo-audit-0yjirj`.
- **NOTE:** Batch 2.2 (Organization entity) is intentionally NOT done in this commit — it needs real business facts (address vs service-area, real social profiles for `sameAs`, phone). Held for user decision per session rule 1.

### 2026-07-02 — Batch 2.2: Organization entity (Finding F6)
- **Decisions (user, 2026-07-02):** model as a **service-area business** (no postal address); **omit `sameAs`** (no real profiles yet); **email-only** contactPoint.
- **File:** `site/layouts/_default/baseof.html` (head) — added a sitewide `Organization` JSON-LD node with a stable `@id` (`https://closeprotectionhire.com/#organization`), `name`, `url`, `description`, and an email `contactPoint`. Present on every page.
- **Files:** wired every `Service` node's `provider` to reference that `@id` instead of re-declaring a bare name — `_default/single.html`, `cities/single.html`, `services/single.html`, `event-security/single.html`, `countries/single.html`.
  - *Why:* the provider Organization was a name-only stub on a YMYL site; a single `@id`-referenced entity is the E-E-A-T anchor Google binds Service pages to.
- **Verification:** build clean; JSON-LD parser-validated across silo/city/country/event/home/about — all valid, Organization `@id` present on every page, Service `provider` resolves to `@id`.
- **FOLLOW-UPS (noted, not fake-filled):**
  1. **No logo asset exists** in `static/images/` — `logo` was intentionally omitted rather than pass the hero photo off as a logo. When a real logo is added, append `"logo"` to the Organization node.
  2. `sameAs` to be added when real social/directory profiles exist.
  3. Latent hardening: `cities/services/event-security/countries` Service nodes still interpolate `"description": "{{ .Description }}"` without `| jsonify` (pre-existing). Low risk (controlled front matter) but should be `jsonify`-hardened in a later pass.

### 2026-07-02 — Batch 3: Duplicate country pages (Finding F7)
- **Decision (user):** keep full-word slugs `united-kingdom` / `united-states` (also the richer pages: 6096/5963 vs 5534/5620 bytes).
- **Deleted:** `content/countries/uk.md`, `content/countries/usa.md`.
- **Redirects (belt-and-braces):** added Hugo `aliases` to the survivors (`united-kingdom.md` → `/countries/uk/`, `united-states.md` → `/countries/usa/`) which generate meta-refresh stubs, AND server 301s in `static/_redirects` matching the existing `301!` Netlify-style format.
  - *Why both:* `_redirects` gives a true server 301 if the host honours it, but the deploy targets Hostinger where Netlify-style `_redirects` may not fire; Hugo aliases guarantee a client-side redirect regardless. 0 internal links pointed at the old slugs, so no repointing was needed.
- **Verification:** build clean; alias stubs confirmed at `public/countries/uk/` and `public/countries/usa/` pointing to the full-word URLs; survivors build; `_redirects` present in `public/`.

### 2026-07-02 — Batch 6.1: Direct-answer render path (Finding F8, template half)
- **Files:** `site/layouts/_default/single.html` and `site/layouts/cities/single.html` — added a `{{ with .Params.answer }}` block rendering a `.direct-answer` lead box high on the page (after hero/CTA, before main narrative). `site/static/css/custom.css` — appended `.direct-answer` / `.direct-answer-section` styles (append-only; `style.css` untouched).
  - *Why:* gives the answer-first (AI Overview) copy a prominent, extractable home. Uses `{{ with }}` so it is a **no-op until `answer:` front matter is authored** — safe to ship ahead of the copy.
- **Verification:** build clean; confirmed 0 pages render `.direct-answer` yet (correct no-op); CSS present in `public/css/custom.css`.
- **Status:** committed. The copy itself (6.2) is **[OPUS-REQUIRED]** and is NOT done here — handed off for a model switch.

### 2026-07-02 — Batch 6.2: Direct-answer copy, 15 priority cities (Finding F8, Opus) [OPUS-AUTHORED]
- **Model:** authored on Opus (`claude-opus-4-8`), user-approved sample gate passed before the bulk pass.
- **Decisions (user):** city pages first; ~15-city tranche; ran in this Opus session.
- **RUBRIC (reusable for routine extension — 40–55 words):** (1) open naming service + city; (2) state the single most decision-relevant local fact — the signature threat and/or the named regulator + armed-cover constraint, taken from that page's own sourced `threats`/`regulations`; (3) close with the practical implication for a principal. British English; no em dashes; no safety-guarantee language; nothing fabricated. Each answer must be genuinely city-specific — a name-swapped template fails and must be left unset instead.
- **Files:** added a top-level `answer:` field to 15 `content/cities/*.md`: london, dubai, lagos, nairobi, johannesburg, mexico-city, bogota, sao-paulo, istanbul, riyadh, mumbai, moscow, bangkok, manila, jakarta. Each cites its own regulator (SIA, SIRA, NSCDC, PSIRA, SEDENA, SVSP, Federal Police/Portaria 3233/2012, Law 5188, MoI, PSARA, Rosgvardiya, Security Guard Business Act, PNP/SOSIA, POLRI) and signature threat.
- **Verification:** all 15 within 40–55 words; QA gate clean (no em dashes, no banned safety language in the new fields — two pre-existing FAQ hedges in abu-dhabi/bangalore are unrelated and were not touched); build clean; all 15 render `.direct-answer`; non-tranche cities remain a correct no-op (abuja verified).
- **Status:** committed.
- **Extension (6.2.5, Sonnet OK later):** remaining cities can follow this rubric under the QA gate, applying the "genuinely specific or leave unset" guardrail.
- **DEFERRED (6.2.6):** optionally tighten `llms.txt` city one-liners to echo each answer's signature threat/regulator. Left as-is for now (current descriptions are accurate); revisit in a later llms.txt upgrade pass.

### 2026-07-02 — Batch 8: Blog Article schema (Finding F10)
- **File:** `site/layouts/blog/single.html` schema block. Added `image` (hero, absolute URL, fallback to site default) and `mainEntityOfPage` (permalink). Replaced the single hardcoded author `description` with a per-persona `dict` lookup keyed on `.Params.author` (James Calloway → regulation/licensing bio; Marcus Webb → operational/transport bio, per `AGENTS.md`), with a generic fallback. Changed `publisher` to reference the sitewide Organization `@id` (from Batch 2.2).
  - *Why:* Article schema lacked an image (needed for article rich results) and applied one consultant's bio to every byline regardless of persona. `sameAs` for authors omitted (no real profiles — consistent with the Organization decision).
- **Verification:** build clean; confirmed Calloway vs Webb posts each get the correct bio; `image`/`mainEntityOfPage`/`publisher @id` present; all 216 blog JSON-LD blocks parse, 0 errors.
- **Status:** committed.

### 2026-07-02 — Batch 4: Cannibalisation decision (Finding F2) [OPUS-DECIDED]
- User chose **Option B (differentiate intent)**. Full model recorded in the Batch 4 section above (transactional / programme / operators split, per-silo recipe, rollout scope). Lagos × 3 proof sample authored and signed off.

### 2026-07-02 — Batch 5 (sub-batch 1 of N): Differentiation rollout, 10 priority cities (Finding F2) [OPUS-AUTHORED]
- **Scope (user):** Lagos reference + first ~10-city sub-batch; treatment = **lede + intent cross-links + FAQ angle** (components left as already-city-specific).
- **Cities (10):** lagos, dubai, london, nairobi, johannesburg, mexico-city, bogota, sao-paulo, istanbul, riyadh. **Files: 30** (3 silos each).
- **Change per page:** (1) replaced the opening body lede with an intent-framed, city-specific paragraph (bodyguard-hire = transactional hire; executive-protection = corporate programme/duty of care; close-protection-officers = operators/credentials), each 72–85 words citing the city's own regulator + signature threat; (2) appended an intent-specific cross-link paragraph linking the two sibling silos (also advances Batch 7 internal-linking for these cities).
- **Verification:** build clean (0 errors); each silo's unique lede phrase renders once per page; all three siblings confirmed distinct across sampled cities (dubai, lagos, riyadh, sao-paulo); sibling cross-links resolve; QA gate clean (no em dashes, no safety-guarantee language) across all 30.
- **Status:** committed.
- **REMAINING (Batch 5 sub-batches 2..N):** ~254 more cities × 3 silos (~760 pages) still on the old overlapping ledes. Apply the SAME model + treatment, staged ~10 cities per run, Opus-authored ledes (or Sonnet under the "genuinely specific or leave" guardrail). Priority: finish the remaining 5 answer-block cities (mumbai, moscow, bangkok, manila, jakarta) next, then the wider network.

### 2026-07-02 — Plan maintenance
- Added **Batch 1B (llms.txt)** to the plan per session rule 5, overriding the audit's "skip llms.txt" note.
- Annotated Batch 1.2 with the city-guard correctness note.
- Expanded **Batch 6.2** into a numbered Opus sub-plan (6.2.1–6.2.6) with scope decisions (Q6.2-a page types, Q6.2-b tranche size), a rubric spec, and a hand-checked-sample gate.
- Recorded **Batch 4 decision (Option B)** with the full differentiation model, and split **Batch 5** into staged sub-batches.
