# Deploy notes

## One-time: set your public site URL

Many files contain the placeholder **`REPLACE_SITE_PUBLIC_URL`** (your HTTPS origin **without** a trailing slash, e.g. `https://stay.example.com`).

Before going live, run a **project-wide find/replace** and substitute your real origin in:

| File | Usage |
|------|--------|
| `index.html` | `canonical`, Open Graph, Twitter Card, JSON-LD `url`, `meta name="site-public-url"` |
| `robots.txt` | `Sitemap:` line |
| `sitemap.xml` | Each `<loc>` |
| `privacy.html` | `link rel="canonical"` |
| `terms.html` | `link rel="canonical"` |

After replacement, validate:

- **Facebook Sharing Debugger** / **Twitter Card Validator** (OG URLs must be absolute and reachable).
- **`https://YOUR_DOMAIN/robots.txt`** and **`https://YOUR_DOMAIN/sitemap.xml`**.

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
