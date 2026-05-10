# Traffic & analytics (Plausible)

This site uses **[Plausible Analytics](https://plausible.io/)** — lightweight, privacy-focused, no cookies by default (suitable for many marketing / STR landing pages). You pay Plausible directly; configure your domain in their dashboard.

## Enable tracking

1. Create a site in Plausible for your **production hostname** (e.g. `heartofawl.yourdomain.com`).
2. In **`index.html`** and **`request.html`**, set the meta tag:

```html
<meta name="analytics-domain" content="your-live-hostname.com" />
```

Use the **exact hostname** Plausible shows (no `https://`, no trailing path).

3. Deploy. Pageviews to `/`, `/request.html`, etc. appear in Plausible.

Leave `content=""` empty on copies you don’t want tracked (e.g. local `file://` previews).

## Ads & campaigns (UTM)

Plausible records standard **UTM parameters** on the URL (`utm_source`, `utm_medium`, `utm_campaign`, …). Use them on ad landing URLs, e.g.:

`https://your-live-hostname.com/?utm_source=facebook&utm_medium=paid&utm_campaign=ironman2026`

You can filter and break down traffic by campaign in Plausible.

## Custom events (optional)

On **`request.html`**, when analytics is enabled:

- **`Request Form View`** — fires when the Plausible script loads on the booking page.
- **`Booking Request Submit`** — fires when the user submits the form (before redirect to Formspree).

Use Plausible’s **Goals** UI to mark these as conversions if you want funnel metrics.

## Google Ads / Meta conversions

Plausible does **not** replace ad pixels. For Google Ads conversions you typically add their tag separately or use Google Tag Manager — coordinate with your ads vendor. Plausible stays useful for **baseline visitor counts** and **UTM attribution** without third-party ad scripts on every page.

## Privacy copy

If `analytics-domain` is set, mention aggregated visitor analytics in **`privacy.html`** (already aligned with Plausible’s model).
