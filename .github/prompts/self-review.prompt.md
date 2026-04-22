# Self-Review Checklist

Review the work just completed against every criterion below.
Report each check as PASS or FAIL with a brief reason.
If any check FAILS, fix it before reporting done.

## Content Quality
- [ ] No banned vocabulary used (delve, tapestry, vibrant, robust, seamless, leverage, synergy, transformative, paramount, multifaceted, myriad, cornerstone, reimagine, empower, catalyst, invaluable, bustling, nestled, realm, groundbreaking, comprehensive, meticulous, embark, crucial)
- [ ] No em dashes (—) or en dashes (–) used anywhere in the content
- [ ] Sentence rhythm is varied — not metronomic or uniform
- [ ] Authority voice maintained — reads like a senior security consultant, not a travel blog or marketing brochure
- [ ] No safety guarantees implied ("stay safe", "guaranteed protection", "ensure your safety" are banned)
- [ ] All factual claims (risk statistics, crime indices, advisory levels) have named, dated sources

## SEO Compliance
- [ ] Unique title tag, 50-60 characters, contains primary keyword
- [ ] Meta description is 140-160 characters, contains keyword, includes a call to action
- [ ] Exactly one H1 per page, contains primary keyword and city/location name
- [ ] Primary keyword appears in the first 100 words of body copy
- [ ] At least 2 internal links with descriptive anchor text (not "click here" or "here")
- [ ] FAQ schema JSON-LD included if this is a service or informational page (minimum 4 Q&As)
- [ ] Page content is unique — no copy-pasted paragraphs from other city pages

## Technical
- [ ] Front matter uses TOML format (`+++` delimiters, not `---`)
- [ ] All required front matter fields present (title, description, date, draft = false, city/country where applicable)
- [ ] URL slug is lowercase and hyphen-separated
- [ ] Hugo build passes with 0 errors: run `hugo --gc --minify` from `site/`
- [ ] No inline CSS added to templates

## Build Plan
- [ ] `BUILD-PLAN.md` updated to mark this task complete
- [ ] `bodyguard-cascading-build-plan.html` updated with current stage status (DONE/IN PROGRESS)
- [ ] Session log entry added to `BUILD-PLAN.md` (date, stage, pages added, notes)
- [ ] Next recommended task identified from the build plan

## Output
List all files created or changed, with their paths.
Write a 2-sentence summary of what was done.
State clearly: **"Ready for next task"** or **"Issues found: [list each issue]"**.
