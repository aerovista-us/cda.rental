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

## Optional analytics

In `index.html`, uncomment the Plausible snippet (near the bottom of the page), set `data-domain` to your hostname, and remove the wrapping HTML comment.
