# ERRORS.md

> Running log of bugs, gotchas, and resolutions. Read this before re-debugging anything that smells familiar. Append-only — do not delete entries.

## 2026-05-27 — baseURL stuck on surge.sh
**Symptom:** Pages 404 on closeprotectionhire.com despite Hugo building 200+ pages with zero errors.
**Cause:** `site/hugo.toml` had legacy `baseURL = "https://closeprotectionhire.surge.sh/"` from the original Surge deploy. Hugo bakes baseURL into every canonical, sitemap entry, and absolute asset URL at build time.
**Fix:** Set `baseURL = "https://closeprotectionhire.com/"`. (Commit `771bf31`.)
**Prevention:** Any future migration must touch baseURL first.

## 2026-05-27 — City permalinks producing `/london/` instead of `/cities/london/`
**Symptom:** New city pages, blog articles, and event-security pages 404 even though some older ones loaded.
**Cause:** `[permalinks.page]` rule `cities = "/:sections[1:]/:slug/"` stripped the section segment, so `site/content/cities/london.md` resolved to `/london/`.
**Fix:** Replaced with explicit `/section/:slug/` for every content type (commit `d4a21d8`).
**Prevention:** Don't use `sections[1:]` slicing unless you actually have nested sections; the simple `/section/:slug/` form is safer for flat silos.

## 2026-05-28 — FTP deploy reports success but files silently absent on server
**Symptom:** GitHub Actions "Deploy to Hostinger via FTP" turns green, log shows `creating folder "cities/test-deploy/"` and `🎉 Sync complete`, but Hostinger File Manager shows none of the new folders/files — directories last modified weeks earlier. `dangerous-clean-slate: true` did not help. Sync-state file the action claimed to write was also absent.
**Cause:** FTPS data-channel failure under Hostinger's shared-hosting FTP. Control channel exchanges succeed (action gets 226 Transfer Complete responses), but data transfers silently drop. Not a path issue (Hostinger Kodee confirmed `/home/u356263466/domains/closeprotectionhire.com/public_html` is the correct doc root) and not a permission issue.
**Fix:** Abandoned FTP entirely. New architecture:
  1. `.github/workflows/build-and-publish.yml` builds Hugo on push to master.
  2. `peaceiris/actions-gh-pages@v4` force-pushes `site/public/` to a `live` branch.
  3. Hostinger GitHub OAuth integration (Advanced → GIT) watches `live` and webhook-deploys it into `public_html` on every push.
  4. The old `deploy.yml` is disabled in the Actions UI (not deleted, for history).
**Prevention:** Never trust an FTP success log on shared hosting without filesystem verification. Hostinger's OAuth Git path is the supported route and removes the entire FTP failure surface.
**Verification:** Test page `cities/auto-deploy-test/` deployed fully automatically with no manual click — confirms webhook chain.

## 2026-05-28 — GitHub MCP token cannot edit `.github/workflows/`
**Symptom:** Every attempt to create or update files under `.github/workflows/` via the MCP returns 403 "Resource not accessible by integration".
**Cause:** Anthropic's GitHub App installation for this repo does not include the `workflows` scope. Both `create` and `update` are blocked.
**Workaround:** Workflow files must be created or edited manually in the GitHub web UI. Claude provides the full file content; Gareth pastes it and commits.
**Prevention:** When proposing any workflow change, always output the complete file content (not a diff) and remember to remind Gareth that this is manual.

## 2026-05-28 — deploy.yml YAML syntax error from duplicated key
**Symptom:** Actions run #27 failed with "Invalid workflow file: yaml syntax on line 37". Build never started.
**Cause:** Manual edit added `dangerous-clean-slate: true` twice on the same line.
**Fix:** Full-file overwrite with the corrected single-line version.
**Prevention:** When asking Gareth to update a workflow, give the full file every time, not a partial diff. (See `CLAUDE.md` working rules.)

## 2026-05-28 — Phantom blog files predate the batch tracker
**Symptom:** `site/content/blog/` contains three files not logged in any batch:
  - `do-bodyguards-need-a-licence-in-south-africa.md`
  - `executive-protection-cost-johannesburg.md`
  - `vetting-close-protection-latin-america.md`
**Cause:** Pre-tracker authoring. They are real, sourced articles; just not part of the numbered batch system.
**Action:** Leave them in place. They count toward live page totals but not toward batch indexing. Worth folding into Stage 2L QA audit to confirm they pass the same gate as numbered batches.
