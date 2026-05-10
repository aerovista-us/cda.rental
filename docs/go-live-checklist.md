# Go-live checklist (Heart of Awl landing page)

Single-page site: `index.html` + `images/` + satellite pages. Form submissions use Formspree (`BOOKING.formAction`).

## Implemented in repo

- **SEO / sharing** — Canonical URL placeholder, Open Graph, Twitter Card, JSON-LD `LodgingBusiness`, theme color (see **`REPLACE_SITE_PUBLIC_URL`** in [`DEPLOY.md`](DEPLOY.md)).
- **Favicon** — `favicon.svg`; linked from all pages.
- **Typography** — Inter loaded via Google Fonts (matches CSS stack).
- **Accessibility** — Skip link, `:focus-visible` outlines, `main` skip target with `tabindex="-1"`.
- **Tax copy** — No more “TBD”; taxes described as itemized at confirmation.
- **Status board** — Rewritten as numbered **typical steps**, not live submission state.
- **Form** — Email **required**; privacy consent line + link to `privacy.html`; honeypot field `_gotcha`; Formspree POST unchanged.
- **Legal pages** — `privacy.html`, `terms.html`; footer links + short-term rental note on index.
- **404** — `404.html` (configure host to use it if supported).
- **robots.txt** / **sitemap.xml** — Present; require **`REPLACE_SITE_PUBLIC_URL`** (see [`DEPLOY.md`](DEPLOY.md)).
- **Security headers** — `_headers` for Netlify-style hosts.
- **Gallery** — Missing map tiles and property photos hide via `error` handler on `.location-gallery-tiles img` and `.property-grid img` (whole `<figure>` hidden).
- **Pricing source of truth** — Comment above `nightlyRates` in `index.html` reminds operators to sync JS + calendar markup with real policy.
- **Analytics hook** — Plausible snippet commented in `index.html` (see [`DEPLOY.md`](DEPLOY.md)).

## You still do manually

1. **Find/replace `REPLACE_SITE_PUBLIC_URL`** everywhere (see [`DEPLOY.md`](DEPLOY.md)).
2. **Formspree** — Confirm production form settings, inbox, and domain verification in their UI.
3. **Rates & calendar** — Align `nightlyRates` and calendar day classes with **actual** availability and pricing.
4. **Deploy host** — HTTPS, optional custom domain, point **404** to `404.html` if the platform supports it.

## Already in good shape

- IRONMAN® disclaimer in hero notice and footer.
- Booking form POST wired to Formspree with `_subject` / `_next` for hosted deployments.
- Relative asset paths for local preview and HTTP(S).
