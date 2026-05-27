# AGENTS.md

> Full workforce-soul index and routing rules. Load the soul whose domain matches the task; do not load all of them.

This repo follows the pet-transport "souls" pattern. Each soul is a single Markdown brief defining a specialist voice or function. Souls live in `workforce/` and are referenced in `CLAUDE.md` for routing.

---

## Routing rules (load only what you need)

| If the task is… | Load |
|---|---|
| Authoring new copy for a blog article, city page, or service page | `workforce/content/the-wordsmith.md` |
| Rewriting AI-flavoured copy to read human | `workforce/content/the-chameleon.md` |
| Building structured page front matter, SEO titles, descriptions, FAQ schema | `workforce/seo/the-optimiser.md` |
| Running the QA gate, banned-word check, YMYL audit | `workforce/seo/the-auditor.md` |
| City risk analysis, FCDO/State Dept summarisation | `workforce/intelligence/the-geographer.md` |
| Regulatory framework (SIA, PSARA, SIRA, OGG, etc.) writeups | `workforce/intelligence/the-regulator.md` |
| Internal link graph, sitemap, cross-silo cohesion | `workforce/seo/the-architect.md` |
| Hugo template debugging or partial edits | `workforce/build/the-engineer.md` |

If a soul listed above is missing from `workforce/`, fall back to its general intent: e.g. for `the-regulator` use the regulatory section conventions established in `bodyguard-licence-uae.md`, `bodyguard-licensing-south-africa.md`, `private-security-regulations-turkey.md`, and `bodyguard-licence-india-psara.md`.

---

## Authoring personas (used in `author:` front matter)

| Persona | Domain | Voice |
|---|---|---|
| **James Calloway, Senior Security Consultant** | Regulation, licensing, vetting, risk frameworks, residential security | Measured, evidentiary, cites Acts/regs by name and year |
| **Marcus Webb, Security Operations Adviser** | Operational close protection, secure transport, city-specific safety, women-traveller safety | Operational, pragmatic, draws on FCDO/State Dept and lived-pattern analysis |

Every blog article must use one of the two personas. City pages and service pages do not carry an author byline (they read as institutional pages).

---

## Pipeline (every published page runs through this in order)

1. **Wordsmith** writes the first draft against the keyword brief.
2. **Chameleon** humanises: strip AI-tells, vary sentence length, kill banned vocabulary, replace em dashes.
3. **Optimiser** sets title/description/FAQ schema, confirms 2+ internal links, places primary keyword.
4. **Auditor** runs `scripts/qa_audit.py` + `scripts/check_titles.py` + `scripts/check_descriptions.py`. Blocks on errors.
5. **HTML preview → approve → commit → stop.** Engine 7 discipline. One block per session.

---

## Banned vocabulary (loaded by Chameleon and Auditor)

Maintained in `scripts/qa_audit.py` (`BANNED_WORDS`). The list is the universal AI-tell set inherited from pet-transport; identical across both repos. Add domain-specific entries only after seeing them appear in real published copy.

## YMYL safety-guarantee patterns (loaded by Auditor)

Maintained in `scripts/qa_audit.py` (`SAFETY_GUARANTEE_PATTERNS`). These are security-domain-specific. Hard fail on any match. "Reduce risk" / "trained professionals" only — never "guarantee safety", "100% safe", "keep you safe", "risk-free", "foolproof".
