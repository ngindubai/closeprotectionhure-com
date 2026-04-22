---
applyTo: "**/*.md, **/*.html"
---

# SEO Rules — CloseProtectionHire.com

This is a YMYL lead generation site. SEO placement is the primary business driver. These rules are non-negotiable on every page.

## Title Tags (Hugo `title` front matter)
- Format: `[Primary Keyword] in [City] | CloseProtectionHire`
- Length: 50-60 characters strictly.
- Must contain the primary target keyword.
- Every page title must be unique across the entire site.

## Meta Descriptions (Hugo `description` front matter)
- Length: 140-160 characters strictly.
- Must include a call to action (e.g. "Get a free quote today", "Contact our vetted network").
- Must contain the primary keyword naturally.
- Every page description must be unique.

## Headings
- Exactly one H1 per page. Contains primary keyword and city name for city/service pages.
- H2s for major sections, H3s for subsections. Logical hierarchy only.
- No keyword stuffing in headings. One target keyword per heading maximum.

## Content Requirements
- Primary keyword in first 100 words of body copy.
- City and country names used naturally throughout (not forced).
- All risk statistics and advisories must cite a named, dated source (e.g. "FCDO Travel Advisory, March 2026").
- No claims of guaranteed safety or zero risk — this is a liability issue and an E-E-A-T issue.

## Internal Linking
- Minimum 2 internal links per new page with descriptive anchor text.
- Never use "click here", "read more", or "here" as anchor text.
- City pages must link to: (1) their country hub page, (2) at least one service silo page.
- Service silo pages must link to the top 3-5 most relevant city pages.

## Schema Markup
- FAQ schema (JSON-LD) required on all service pages and informational pages. Minimum 4 Q&As.
- LocalBusiness schema: homepage and contact page.
- Article schema: blog posts and guide pages.
- Place schema: city pages where applicable.

## City and Location Pages
- City name in: H1, URL slug, meta title, first paragraph. All four — non-negotiable.
- Include risk level context drawn from `data/city_risk_profiles.json` or `data/city_risk_profiles_p2.json`.
- Include emergency contact numbers for the city.
- Reference local security regulations from `data/security_regulations_v1_backup.json`.

## Duplicate Content Prevention
- Every city + service combination must have unique body copy.
- Do not reuse paragraphs across city pages. Rewrite with city-specific details.
- Use varied anchor text when linking to the same destination from multiple pages.

## Banned SEO Practices
- No keyword stuffing in copy or headings.
- No hidden text.
- No doorway pages with thin content.
- No fabricated statistics — every number needs a named source.
