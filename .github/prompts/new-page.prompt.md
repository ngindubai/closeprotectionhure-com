# New Page Creation

Before starting, confirm these files have been read:
- `#file:MEMORY.md` (attach manually at session start with `#file:MEMORY.md`)
- `#file:BUILD-PLAN.md`
- `.github/copilot-instructions.md` (auto-loaded)
- `bodyguard-cascading-build-plan.html` (primary build tracker — check stage detail here)

## Before Building, Confirm

1. Page type (city, country hub, service silo, risk assessment, guide, blog post)?
2. City/country name and primary keyword target?
3. Search intent (informational / commercial / transactional)?
4. Which service silo does this belong to (if applicable)?
5. Which existing pages should this link to? Name at least 2.
6. Is there an existing page of this type to use as a template? Reference it with `#file:`.

## Then Build

Follow all conventions in `.github/copilot-instructions.md`. Use an existing page of the same type as the structural template. Draw city risk data from `data/city_risk_profiles.json` or `data/city_risk_profiles_p2.json`. Draw regulatory data from `data/security_regulations_v1_backup.json`.

## After Building

Run the self-review checklist automatically (reference `.github/prompts/self-review.prompt.md`).

Do not mark this task done until:
1. The self-review passes on all criteria.
2. The Hugo build runs with 0 errors (`hugo --gc --minify` from `site/`).
3. `BUILD-PLAN.md` and `bodyguard-cascading-build-plan.html` are updated.
