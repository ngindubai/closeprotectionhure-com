# CloseProtectionHire.com — Agents and Workers

## Copilot Subagent: bodyguard

The `bodyguard` subagent executes the cascading build plan stage-by-stage, loading worker souls, research data, and enforcing content/design/SEO rules.

**This subagent must be manually recreated in the new standalone VS Code instance.**

To recreate it, go to VS Code Settings and add the following agent definition:
- **Name:** `bodyguard`
- **Description:** `Security & Bodyguard website build agent. Executes the cascading build plan stage-by-stage, loading worker souls, research data, and enforcing content/design/SEO rules. Use for: building stages, continuing the build, 'go', 'next stage', any security-bodyguard project work.`

---

## Worker Souls (14 Specialist Roles)

Full soul files are in `workforce/`. Each defines a role, rules, quality gates, and domain-specific instructions.

| Worker | File | Role |
|--------|------|------|
| The Architect | `workforce/leadership/the-architect.md` | Orchestration, planning, phase gates |
| The Auditor | `workforce/leadership/the-auditor.md` | Legal liability, regulatory accuracy, QA |
| The Wordsmith | `workforce/content/the-wordsmith.md` | Copywriting, editorial, authority voice |
| The Chameleon | `workforce/content/the-chameleon.md` | Anti-AI humaniser, 24 anti-patterns, banned vocabulary |
| The Interrogator | `workforce/content/the-interrogator.md` | FAQ generation, research questions |
| The Geographer | `workforce/intelligence/the-geographer.md` | Risk analysis, geographic intelligence |
| The Scout | `workforce/intelligence/the-scout.md` | Market reconnaissance, keyword research |
| The Spider | `workforce/intelligence/the-spider.md` | Web scraping, data extraction |
| The Builder | `workforce/development/the-builder.md` | Templates, page generation, deployment |
| The Librarian | `workforce/development/the-librarian.md` | Data management, schema, databases |
| The Optimiser | `workforce/seo/the-optimiser.md` | On-page SEO, schema markup, E-E-A-T |
| The Connector | `workforce/seo/the-connector.md` | Internal linking, backlink strategy |
| The Analyst | `workforce/monitoring/the-analyst.md` | Performance tracking, analytics |
| The Watchdog | `workforce/monitoring/the-watchdog.md` | Security monitoring, uptime |

Vetting framework: `workforce/vetting_framework.md` — Bronze/Silver/Gold operator tiers.

---

## Reviewer Agent

A read-only Site Reviewer agent is defined in `.github/agents/reviewer.agent.md`.
It analyses pages for SEO, YMYL compliance, and content quality without making changes.

---

## New Standalone Instance: First Session Setup

1. Open `C:\Users\garet\Desktop\security-bodyguard\` as the VS Code workspace (File > Open Folder).
2. Recreate the `bodyguard` subagent (see above).
3. Start a new Copilot chat and send:

```
New session. Read #file:MEMORY.md #file:BUILD-PLAN.md

Confirm you understand:
- The site's purpose and current build status (121 pages live)
- The next stage from BUILD-PLAN.md (Stage 2G — Event Security Silo)
- The code conventions from copilot-instructions.md

Do not start any work yet. Confirm your understanding and ask if anything is unclear.
```

4. Verify the summary is correct, then proceed with Stage 2G.
