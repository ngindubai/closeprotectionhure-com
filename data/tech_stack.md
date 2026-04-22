# Tech Stack Recommendation

## Status
Task 0.10 (strategic questions) is still PENDING. Some decisions here may shift depending on answers. Where a decision is blocked, I've flagged it and given a default recommendation that works for all likely scenarios.

---

## Recommended Stack

### Static Site Generator: Hugo

**Why Hugo over alternatives:**
- **Speed:** 2,200-3,500 pages (expanding to 5,000+). Hugo builds 5,000 pages in under 10 seconds. Next.js and Astro choke at this scale without significant optimisation.
- **Templating fits our model:** Our build is data-driven (JSON -> templates -> HTML). Hugo's `range` over data files is built for exactly this pattern.
- **No JavaScript runtime required:** Security site visitors don't need client-side interactivity. Pure static HTML = fastest possible page load, best Core Web Vitals, lowest attack surface.
- **Mature i18n support:** When we expand to multilingual content (Arabic for UAE/Saudi, Portuguese for Brazil, etc.), Hugo handles it natively.

**Alternatives considered:**
- Astro: Good for content sites but Node-based build is slower at 5,000+ pages. Better if we needed islands of interactivity.
- Next.js (SSG mode): Overkill. We don't need React. Build times are 10-50x slower at this page count. Introduces unnecessary complexity and dependency weight.
- 11ty: Close second. Slower than Hugo at scale but more flexible templating. Falls behind at 5,000+ pages.

### Hosting: Cloudflare Pages

**Why Cloudflare Pages:**
- **Global edge network:** Our visitors are in Lagos, Karachi, Mumbai, Bogota. Cloudflare has edge nodes in all these cities. Netlify and Vercel have weaker presence in Africa/South Asia/LATAM.
- **Free tier:** Unlimited sites, unlimited bandwidth, 500 builds/month. More generous than Netlify (100GB/month) or Vercel (100GB/month).
- **Cloudflare ecosystem:** If we add WAF, DDoS protection, rate limiting, or bot management later (likely for a security company site), it's all in one dashboard.
- **Build limits:** 25,000 files max. Our 5,000 pages + assets fit comfortably.

**Alternatives:**
- Netlify: Better DX (deploy previews, form handling). Bandwidth cap matters at scale. Falls behind on global edge coverage.
- Vercel: Next.js-first platform. Wasted if we're on Hugo.
- AWS S3 + CloudFront: Maximum control, more operational overhead. Consider if Cloudflare Pages limits become a problem.

### Contact Forms: Formspark + PGP Encryption

**Requirements from build plan:**
- Encrypted contact forms (security-conscious clients expect this)
- No data stored in plaintext anywhere
- GDPR/data protection compliance
- No third-party form processor that stores data long-term

**Approach:**
- **Formspark** for form submission (GDPR compliant, EU-hosted option, submissions can be auto-deleted after email delivery)
- **Client-side PGP encryption** via OpenPGP.js before submission. Form data is encrypted in the browser with our public key. Even Formspark only sees ciphertext.
- **Alternative:** Formspree (similar, better known), or a custom Cloudflare Worker endpoint that encrypts and forwards to email. The Worker approach has zero third-party dependency.

**Blocked by 0.10:** Which email/contact point receives encrypted enquiries? What's the response workflow?

### CMS: None (Phase 1). Decap CMS or Tina if needed (Phase 2).

**Phase 1 (launch):**
- Content is generated from JSON data files + Hugo templates via build scripts.
- Gareth or the team edits JSON files directly (risk scores, operator data) and pushes to Git.
- Blog/guide posts are Markdown files in `/content/blog/` and `/content/guides/`.
- No CMS overhead. The data pipeline IS the CMS.

**Phase 2 (if non-technical editors need access):**
- Decap CMS (formerly Netlify CMS): Git-based, no database, works with Hugo. Editors get a browser UI that commits to the repo.
- Tina CMS: Similar, more modern UX. Also Git-based.
- Neither requires a server. Both produce Markdown/JSON commits.

### Operator Database: JSON files (Phase 1). Supabase (Phase 2).

**Phase 1:**
- `/data/operators/` directory with JSON files per operator.
- Build scripts never expose operator data to public pages.
- Internal matching is manual: Gareth receives enquiry, checks operator JSON files, makes intro.

**Phase 2 (if volume justifies):**
- Supabase (hosted Postgres + REST API + auth).
- Internal dashboard for operator matching, availability tracking, performance logging.
- Row-level security ensures operator data never leaks to public endpoints.
- Cost: Free tier handles up to 500MB, then $25/month.

**Blocked by 0.10:** Marketplace vs. direct-match model determines how complex the operator database needs to be.

### Domain and DNS

**Blocked by 0.10.** Cannot select domain until business name is decided.

**Recommendations regardless:**
- Register via Cloudflare Registrar (at-cost pricing, integrates with Pages).
- Exact-match domain (e.g. bodyguard-hire.com, executiveprotection.co) preferred for SEO, but brand domain works if targeting brand search long-term.
- .com or .co TLD. Avoid country-specific TLDs since we're global.
- DNSSEC enabled. SSL/TLS via Cloudflare (automatic).

### Analytics: Plausible or Fathom

- Privacy-first. No cookie banners needed.
- Plausible: self-hosted option ($9/month hosted). Lightweight script (< 1KB). No cookies. GDPR compliant by default.
- Avoids Google Analytics data sharing (a security company shouldn't be sharing visitor behaviour data with Google).

### Monitoring and Uptime

- **Cloudflare Web Analytics** (free, integrated, no JS required, uses edge data).
- **Better Uptime or UptimeRobot** for downtime alerts.
- **Google Search Console** for SEO monitoring (mandatory, no privacy concern since it's first-party data).

---

## Build Pipeline

```
data/risk/*.json          \
data/operators/*.json      |
data/regulations/*.json    +--> build.py (validates + transforms) --> Hugo /data/ directory
data/keywords/*.json      /

content/                   --> Hugo Markdown/template content
layouts/                   --> Hugo HTML templates
static/                    --> CSS, images, fonts

Hugo build --> /public/    --> Cloudflare Pages deploy (via Git push or Wrangler CLI)
```

### Build Steps
1. `python build.py` validates all JSON against schema, generates Hugo data files, flags any missing/stale data.
2. `hugo --minify` builds the static site.
3. Git push to `main` triggers Cloudflare Pages auto-deploy.
4. Alternatively: `wrangler pages deploy public/` for manual deploy.

### Local Development
- `hugo server` for live preview with hot reload.
- Python 3.10+ for build scripts.
- Git for version control (private repo on GitHub).

---

## Security Considerations

This is a security company website. The site itself must demonstrate competence.

| Requirement | Solution |
|---|---|
| HTTPS everywhere | Cloudflare automatic SSL (HSTS enabled) |
| No data leaks | Operator data never in public HTML. Build script validates this. |
| Encrypted forms | Client-side PGP encryption before form submission |
| No tracking scripts | Plausible or Fathom only. No Google Analytics, no Facebook Pixel. |
| Minimal attack surface | Static HTML. No server. No database on the public site. |
| Content Security Policy | Strict CSP headers via Cloudflare Page Rules or _headers file |
| Bot protection | Cloudflare Bot Management (free tier included) |
| DDoS protection | Cloudflare automatic (free tier) |
| Email protection | No mailto links on site. Contact via encrypted form only. |
| Subresource integrity | SRI hashes on any external scripts (Plausible, OpenPGP.js) |

---

## Cost Estimate (Phase 1 Launch)

| Item | Monthly Cost |
|---|---|
| Cloudflare Pages hosting | $0 (free tier) |
| Cloudflare domain (annual) | ~$10-15/year |
| Formspark or custom Worker | $0-$25/month |
| Plausible Analytics | $9/month (or self-hosted for $0) |
| GitHub private repo | $0 (free tier) |
| **Total** | **$9-34/month** |

Phase 2 additions (when revenue justifies):
- Supabase: $0-25/month
- Cloudflare Pro (for advanced WAF rules): $20/month
- Email service (Postmark or similar for enquiry routing): $10/month

---

## Open Decisions (Blocked by Task 0.10)

These become final once Gareth answers the 10 strategic questions:

1. **Domain name** (needs business name decision)
2. **Armed vs unarmed focus** (affects content tone and which regulations get top-level pages)
3. **Marketplace vs direct match** (affects operator database complexity and whether Supabase is needed in Phase 1)
4. **Pricing transparency** (determines whether pricing data appears publicly or stays internal)
5. **Named security professional author** (YMYL requirement, needed for E-E-A-T signals)

None of these block the build starting. Hugo + Cloudflare + JSON data pipeline works for all scenarios. The content and configuration adapt once decisions are made.
