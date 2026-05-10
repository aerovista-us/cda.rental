# Deploy notes

## Production URL (GitHub Pages)

This repo is wired for **`https://aerovista-us.github.io/cda.rental`** (canonical, Open Graph / Twitter image URLs, JSON-LD `url`, `robots.txt` / `sitemap.xml`, legal page canonicals, `site-public-url`). Share previews use **`assets/share-preview.jpg`** at **absolute** HTTPS paths.

**Fork or new domain:** search and replace that origin everywhere it appears (same file list as below), and update **`og:image`** / **`twitter:image`** if the path changes.

Validate after deploy:

- **Facebook Sharing Debugger** / **Twitter Card Validator** — OG image must return **200** with **`Content-Type: image/jpeg`** (or PNG) and public **HTTPS**.
- **`https://aerovista-us.github.io/cda.rental/robots.txt`** and **`…/sitemap.xml`**.

## Hosting

- Prefer **HTTPS** everywhere (required for secure perception and some platform features).
- **`_headers`** applies on **Netlify**; other hosts may need equivalent security headers in their dashboard.

## Formspree

In the Formspree dashboard: confirm the form is active, notifications work, and complete any **custom domain** or **spam protection** steps they require.

## Analytics (visitor counts & ad UTM tracking)

1. Add your site in [Plausible](https://plausible.io/) using your **production hostname**.
2. Set the same hostname on **`index.html`** and **`request.html`**:

```html
<meta name="analytics-domain" content="your-live-hostname.com" />
```

Page views and UTM parameters (`utm_source`, `utm_medium`, …) are recorded automatically. Custom goals on the request page are documented in [`docs/analytics.md`](analytics.md).

Leave `content=""` empty to disable tracking (e.g. staging).

## Before paid ads or broad promotion

Align on-page copy with real operations (not just the website):

- Local **short-term rental** permit / registration status and posted rules.
- **Tax collection and remittance** (lodging/sales) and how guests see them on the confirmation.
- **Occupancy limits** and how they match bed count and house rules.
- **Insurance** for short-term guests.
- **Rental agreement**, **security deposit** handling, **payment records**, and refund policy.

If any of these are still in flux, keep marketing narrow until the backend matches the footer and FAQ promises.
