# Go-live checklist (Heart of Awl landing page)

Single-page site: `index.html` + `images/`. Form submissions use Formspree (`BOOKING.formAction`).

## Must verify before launch

- **Hosting & HTTPS** — Serve over TLS; relative asset paths assume same-origin deployment.
- **Formspree** — Confirm the form `https://formspree.io/f/xeenpaby` is **active**, notifications go to the right inbox, and complete any **domain / reCAPTCHA / spam** steps Formspree requires for production.
- **Pricing & calendar** — Nightly rates, fees, and blocked/open dates in JS (`nightlyRates`, calendar day classes) must match **real** availability and policy for June 2026 (or update date copy sitewide).
- **Tax line** — UI still shows **“Taxes TBD”**; replace with real wording or an approximate range when known.
- **Images** — Confirm `images/cdasunset.png`, `images/map.jpg`, and any gallery files exist on the server or remove broken `<img>` rows (see `images-and-assets.md`).
- **Legal / short-term rental** — Confirm local rules (permits, occupancy limits, transient lodging taxes) and that on-page claims match what you can legally offer.

## Strongly recommended

- **Social / SEO meta** — Add Open Graph and Twitter Card tags + a share image (`og:image`, dimensions ~1200×630). No `canonical` URL yet; add when the production domain is fixed.
- **Favicon** — Add `favicon.ico` or SVG + `apple-touch-icon`.
- **Privacy & form consent** — Short notice near the form: data goes to Formspree/email for booking inquiries; link to a **privacy policy** if you collect identifiable info across jurisdictions.
- **Contact fallback** — Optional visible phone or email for guests who cannot use the form.
- **Status board UX** — The pipeline labels (“Submitted”, etc.) read like live state; consider copy that reflects **typical next steps** instead of implying a request was already sent.

## Nice to have

- **Analytics** — Plausible, Fathom, or privacy-respecting GA4 with consent if required.
- **`robots.txt` / `sitemap.xml`** — Optional for a single URL; useful once the canonical domain is known.
- **Typography** — `Inter` is named in CSS but not loaded; either add a font link or rely on the existing system stack only.
- **404 page** — Only relevant if the host serves unknown paths (many static hosts already show a generic 404).

## Already in good shape

- IRONMAN® disclaimer in hero notice and footer.
- Booking form POST wired to Formspree with `_subject` / `_next` for hosted deployments.
- Relative image URLs work for both `file://` preview and HTTP(S).
- Responsive breakpoints and sticky header present.
