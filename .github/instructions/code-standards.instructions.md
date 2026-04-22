---
applyTo: "**/*.md, **/*.html, **/*.toml"
---

# Code Standards — CloseProtectionHire.com

## Hugo Content Pages
- Front matter: TOML format between `+++` delimiters. Never YAML (`---`).
- Required front matter for city pages: `title`, `description`, `date`, `draft = false`, `city`, `country`
- Required front matter for country pages: `title`, `description`, `date`, `draft = false`, `country`
- Content pages live in `site/content/` — follow the existing subdirectory structure exactly.
- Do not create new top-level content directories without asking first.

## URL and File Naming
- All slugs: lowercase, hyphen-separated, no underscores.
- City pages: `site/content/cities/[city-name]/_index.md`
- Country hub pages: `site/content/countries/[country-name]/_index.md`
- Service pages: `site/content/services/[silo-name]/_index.md`
- Risk assessment pages: `site/content/risk-assessments/[name].md`
- Guide pages: `site/content/guides/[name].md`

## Templates and Layouts
- Hugo Go template syntax only. No JavaScript frameworks.
- Extend existing layouts in `site/layouts/` — do not rewrite base templates unless explicitly asked.
- Check `site/layouts/shortcodes/` before creating new shortcodes — the component may already exist.
- No inline CSS in templates. Use existing CSS classes from `site/static/css/`.
- No new JavaScript dependencies.

## Content Quality
- Every new page follows an existing page of the same type as its template — match structure exactly.
- City pages: minimum 800 words of real, researched content.
- Service pages: minimum 600 words.
- All pages: minimum 2 internal links with descriptive anchor text.
- No placeholder text. Every section must have real content derived from the city/country risk data in `data/`.
- Risk data source files: `data/city_risk_profiles.json` (P1), `data/city_risk_profiles_p2.json` (P2), `data/fcdo_advisories.json`, `data/state_dept_data.json`

## Front Matter Example Pattern
```toml
+++
title = "Bodyguard Hire in Dubai | Hire Vetted Security Professionals"
description = "Planning travel or business in Dubai? Our vetted security professionals reduce risk in UAE's most complex environments. Get a free quote today."
date = 2024-01-01
draft = false
city = "Dubai"
country = "UAE"
+++
```

## Do Not
- Do not restructure existing files or rename anything without explicit instruction.
- Do not change conventions already in use — this project has 121 pages built on established patterns.
- Do not modify `site/config.toml` without explicit instruction.
- Do not commit the `public/` directory — it is generated output.
