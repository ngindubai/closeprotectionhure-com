# CloseProtectionHire.com -- Claude App Workflow Guide

## What this project is

Programmatic SEO lead-generation site at closeprotectionhire.com. Built with Hugo (static site). Hosted on Hostinger. Repository on GitHub. GitHub Actions auto-deploys on every push to `master`.

**Always read `CLAUDE.md` first every session.** It is the master index and overrides everything else.

---

## Current build status (update each session)

- **Pages live:** 153
- **Blog articles live:** 10 (Batches 1 and 2)
- **Completed phases:** 0, 1, 2A through 2G (event security), 2K Batch 1, 2K Batch 2
- **Next stage:** 2H (Travel Safety Guides Batch 1) or 2K Batch 3 (blog)

For full status read `BUILD-PLAN.md` and `build_state.json`.

---

## How to say "go" -- three modes

### Mode 1: Write the next blog batch (standard)

When the user says **"next blog batch"** or **"write batch N"**:

1. Read `build_state.json` to find `next_batch` and `next_blog_batch_topics`
2. Read `data/keyword_matrix.json` to confirm keyword priorities and serp gaps
3. Read `CLAUDE.md` workforce section to confirm which souls to apply
4. Write 5 articles as Hugo Markdown files to `site/content/blog/`
5. Create `scripts/generate_blog_batchN.py` with all article bodies embedded (see Batch 2 script as the template)
6. Update `build_state.json`: increment `last_batch_completed`, `last_article_index`, `total_articles_live`, `next_batch`
7. Update `BUILD-PLAN.md` session log
8. Commit all files and push to `master` -- GitHub Actions builds Hugo and deploys to Hostinger

### Mode 2: Write the next stage page batch (city/country/service/guides)

When the user says **"next stage"** or **"build stage 2H"**:

1. Read `BUILD-PLAN.md` to identify the next TODO stage
2. Read `bodyguard-cascading-build-plan.html` for full scope
3. Read `DESIGN-PLAN.md` for design tokens and component constraints
4. Generate Markdown files using existing Hugo templates only
5. Update `BUILD-PLAN.md` and `build_state.json`
6. Commit and push to `master`

### Mode 3: QA and fixes

When the user says **"run QA"** or **"audit the site"**:

1. Check all blog articles in `site/content/blog/` for:
   - Em dashes (replace with comma, period, or colon)
   - Tier 1 banned vocabulary (see `workforce/content/the-chameleon.md`)
   - Safety guarantees (replace with "reduces risk" / "trained professionals")
   - Missing internal links (minimum 2 per article)
   - Missing or incomplete `faqs:` front matter
2. Report issues before fixing
3. Fix and commit

---

## Article format (blog)

All blog files go to: `site/content/blog/{slug}.md`

Front matter must include:
```yaml
---
title: "..."
description: "..."
date: "YYYY-MM-DD"
type: "blog"
author: "[Author Name], [Title]"
slug: "{slug}"
seo_title: "... | CloseProtectionHire.com"
tags:
  - "tag1"
  - "tag2"
faqs:
  - question: "..."
    answer: "..."
---
```

---

## Content rules (non-negotiable)

1. No em dashes (use commas, full stops, colons, or parentheses)
2. No banned vocabulary: "delve", "tapestry", "vibrant", "crucial", "comprehensive", "meticulous", "embark", "robust", "seamless", "groundbreaking", "leverage", "synergy", "transformative", "paramount", "multifaceted", "myriad", "cornerstone", "bustling", "nestled"
3. No safety guarantees -- "reduce risk" / "trained professionals" only
4. Every regulatory claim needs a named source (UK FCDO, SAPS, PSIRA, Ministry of Interior, OSAC, etc.)
5. British English throughout
6. Minimum 2 internal links per article to relevant city or service pages
7. FAQs: minimum 5 per article, populated in `faqs:` front matter for FAQ schema rendering
8. Author personas: James Calloway (regulation, risk assessment) or Marcus Webb (operational, logistics, transport)
9. No hardcoded bank details, live statistics, or rates without source attribution

---

## Workforce pipeline (per CLAUDE.md)

Apply in this order for each batch:

| Step | Soul | Role |
|------|------|------|
| 1 | The Wordsmith | Authority voice, British English, sourced facts, no filler |
| 2 | The Interrogator | City/service-specific FAQs, no safety guarantees |
| 3 | The Chameleon | Humaniser: no em dashes, no banned vocab, high burstiness |
| 4 | The Optimiser | SEO metadata, FAQ schema, internal links |
| 5 | The Auditor | QA gate: YMYL compliance, legal accuracy, named sources |

Souls are defined in `workforce/content/`. Load the relevant `.md` file before writing.

---

## After writing articles

```bash
# Hugo build check (run from site/ directory)
cd site && hugo --gc --minify
# Expected: 153+ pages, 0 errors

# Git push (triggers GitHub Actions -> auto-deploy to Hostinger)
git add site/content/blog/ scripts/ build_state.json BUILD-PLAN.md
git commit -m "feat(blog): Batch N -- [topic summary]"
git push origin master
```

---

## Keyword priority order for blog topics

Draw topics from `data/keyword_matrix.json`. Priority:

1. Informational clusters with HIGH volume and HIGH serp gap (e.g. "is [city] safe for business")
2. Regulation guides for HIGH serp gap cities (bodyguard licensing by country)
3. Operational guides for security driver / airport transfer queries (VERY HIGH serp gap)
4. EP cost and vetting guides (trust-building, mid-funnel)
5. City-specific risk assessments not yet covered in the risk-assessments silo

---

## Track progress

| File | Purpose |
|------|---------|
| `bodyguard-cascading-build-plan.html` | Master roadmap -- stages, scope, DONE/IN PROGRESS/TODO badges |
| `BUILD-PLAN.md` | Mirrored checklist + session log |
| `build_state.json` | Machine-readable batch tracker |
| `data/keyword_matrix.json` | 75 keyword clusters -- source for blog topics |
| `CLAUDE.md` | Master index and working rules |

---

## Deploy pipeline

Push to `master` -> GitHub Actions runs `.github/workflows/deploy.yml` -> Hugo builds `site/public/` -> FTP-syncs changed files to Hostinger `public_html/`.

Uses `SamKirkland/FTP-Deploy-Action` with `state-name` enabled for incremental (changed files only) deploys.

**Never edit `.github/workflows/deploy.yml` or the `FTP_PASSWORD` secret without approval.**
