# CloseProtectionHire.com — Design Plan

> **Authority:** This file documents the design system **as it exists** in the live site. Every new page must reuse these exact tokens and components. No one-off styles.

---

## Aesthetic Direction
Trustworthy, authoritative, conservative. A senior security consultancy — not a lifestyle brand, not a military supplier. Dark navy backgrounds, clear typography, restrained use of accent colour, data-and-clarity led. YMYL-grade trust signals on every page.

---

## Tech Stack
| Layer | Choice |
|---|---|
| Generator | Hugo v0.160.1 **extended** (Windows/AMD64) |
| Templates | Go HTML templates (`site/layouts/`) |
| Content | Markdown with **YAML** front matter (`---` delimiters, NEVER `+++`) |
| Base theme | CyberGuard (`site/static/css/style.css` — **DO NOT EDIT**) |
| Overrides | `site/static/css/custom.css` — append-only, never reorder |
| Build | `hugo --gc --minify` from `site/` |
| Deploy | GitHub Actions → FTP to Hostinger (`.github/workflows/deploy.yml`) |

---

## CSS Variables (defined in `style.css`)
| Token | Value | Usage |
|---|---|---|
| `--bg-dark-1` | `#1B1663` | Primary navy background |
| `--bg-dark-2` | `#120d4f` | Darker navy section |
| `--bg-dark-3` | `#1e1e1e` | Deep panel background |
| `--heading-font-color` | `#111013` | Light-section headings |
| `--primary-color` | site accent | Primary CTA / link accent |
| `--primary-color-rgb` | RGB version | For `rgba()` use |
| `--heading-font` | (theme) | All H1–H6 |
| `--body-font` | (theme) | Body copy |

Never introduce new colour or font tokens. Use the existing ones.

---

## Content File Structure (hard rules)
| Page type | Path |
|---|---|
| City | `site/content/cities/[city-name].md` (flat .md) |
| Country | `site/content/countries/[country-name].md` (flat .md) |
| Service | `site/content/services/[silo-name].md` (flat .md) |
| Guide | `site/content/guides/[city-name].md` (flat .md) |
| Risk assessment | `site/content/risk-assessments/[name].md` |

Slugs: lowercase, hyphen-separated, no underscores. Front matter is YAML — never TOML.

---

## Reusable Components

### Homepage — `site/layouts/index.html`
| Component | Class | Notes |
|---|---|---|
| Full-bleed hero | `.hero-fb` | `hero.jpg` background, gradient dim `.hero-fb-dim` (108deg, heavy left) |
| Floating glass form | `.hero-float-form` | `rgba(8,12,24,0.50)` + `backdrop-filter: blur(20px) saturate(150%)`, 3-layer shadow |
| Service cards | `.service-card-tall` | Shimmer sweep on hover (`::before` + `svc-shimmer` keyframe); accent underline (`::after` scaleX) |
| How It Works | `.hiw-step` | 3px top border in primary, decorative bg number `.hiw-n`, circular `.hiw-badge`, hover `translateY(-5px)` |

### Services template — `site/layouts/services/single.html`
| Component | Class | Notes |
|---|---|---|
| What's Included | `.incl-card` | 3px primary top border, 12px radius, decorative `.incl-n` bg number, h4 forced `#ffffff !important` |
| Location cards | `.loc-city-card` | Inline `background-image`, 140px tall, `.loc-city-dim` gradient overlay, `.loc-city-name` bottom-centred |

### Risk assessments — `site/layouts/risk-assessments/single.html`
Reuses `.incl-card` from services with `add $i 1` for 1-based numbering. Do not duplicate styles.

### Form contract (JS dependency — `site/assets/js/main.js`)
- Form **must** have class `de_form` (never `de_form hero-form`)
- `.quote-success` element **must** be a sibling inside the same `<section>` as `<form>` (JS uses `closest('section')`)
- Do not restructure form HTML or split the hero form out of `.hero-fb`

---

## Locked Design Fixes (DO NOT REVERT)

### 1. Dark-section text visibility
Any `.bg-dark` / `.bg-dark-2` section will render invisible text without the override block in `custom.css`:
```css
.bg-dark h1, .bg-dark h2, … { color: #ffffff !important; }
.bg-dark p,  .bg-dark li, … { color: rgba(255,255,255,0.82); }
/* Same block duplicated for .bg-dark-2 */
```
Never add a new dark section without confirming this fix applies.

### 2. Image extensions (mixed .webp / .jpg)
- `.webp`: `city-bogota-hero`, `city-istanbul-hero`, `city-manila-hero`, `city-mumbai-hero`, `city-lagos-hero`, `city-bogota-street`, `city-manila-street`
- `.jpg`: all service images, `city-mexico-city-hero`, `city-sao-paulo-hero`
- The services template uses a Go slice `$webpSlugs` to auto-detect. **Do not hardcode extensions** in front matter for standard city images.

### 3. Image compression
All hero/service images compressed via `scripts/compress_images.py` (Pillow). Never upload raw uncompressed images. Max widths:
| Image | Max width |
|---|---|
| Main homepage hero | 2560px |
| Homepage section | 1920px |
| Service hero | 1920px |
| City hero | 1600px |

---

## Responsive Behaviour
- **Mobile-first.** Every component must render correctly at 320px width before desktop is considered done.
- Hero form stacks below the headline on `< lg` breakpoint.
- Service / location card grids collapse to 1 column at `< md`.
- Tables (rate comparison, risk matrices) must scroll horizontally on small screens — never overflow.

---

## Content & Voice Rules (referenced from `.github/copilot-instructions.md`)
- YMYL compliance — author attribution, trust signals, dated sources on every page.
- No safety guarantees. "Reduce risk" / "trained professionals" — yes. "Stay safe" / "guaranteed protection" — no.
- Humaniser rules from `workforce/content/the-chameleon.md`. Banned vocabulary: delve, tapestry, robust, seamless, leverage, synergy, transformative, paramount, etc. No em/en dashes.
- Building names redacted as "Unit 1", "Unit 2".

---

## Pre-Publish Design Checklist
- [ ] Typography hierarchy correct (one H1, logical H2/H3 nesting)
- [ ] All text on dark sections passes WCAG AA contrast
- [ ] Spacing matches existing pages (no one-off margins/paddings)
- [ ] Tables legible and scrollable on 320px width
- [ ] Primary CTA visible above the fold on mobile
- [ ] Hero form (if present) submits and shows `.quote-success` correctly
- [ ] All images served at correct extension (`.webp` / `.jpg` per Fix 2)
- [ ] No new colour tokens or fonts introduced
- [ ] FAQ schema JSON-LD present on service/info pages
- [ ] Internal links: ≥ 2 per new page, descriptive anchor text
