# Booking form wiring

The **Submit Booking Request** form in `index.html` is controlled by the `BOOKING` object near the bottom of the page (same `<script>` block as the pricing logic).

## Navigation and CTAs (anchors)

These links scroll to sections on the same page and are valid as long as the matching `id` exists:

| Link text | Target |
|-----------|--------|
| Brand / home | `#top` (`<main id="top">`) |
| Location | `#location` |
| Dates | `#calendar` |
| Estimate | `#payment` |
| Request booking (header, hero, calendar sidebar, footer) | `#request` |

No broken hash targets.

## Real submissions

Configure **one** of the following in `BOOKING`:

### 1. HTTPS form endpoint (`formAction`)

This project is wired to **Formspree**:

```javascript
const BOOKING = {
  formAction: 'https://formspree.io/f/xeenpaby',
  mailto: '',
  thankYouUrl: '' // optional; overrides redirect after submit
};
```

On load, the script sets `method="POST"` and, for `formspree.io`, adds `_subject` and `_next` (returns visitors to this page at `#request` when the site is served over `http`/`https`; optional override via `thankYouUrl`).

**FormSubmit** is also supported: for `formsubmit.co` URLs the script adds `_subject`, `_template`, and `_next`.

Any provider that accepts a normal browser `POST` with fields matching the form inputs (`name`, `phone`, `email`, dates, etc.) works if you set `formAction` to its endpoint.

### 2. Mailto fallback (`mailto`)

If you do not use an HTTPS endpoint, set an inbox address:

```javascript
const BOOKING = {
  formAction: '',
  mailto: 'you@yourdomain.com',
  thankYouUrl: ''
};
```

Submitting opens the visitor’s default mail client with subject and body filled from the form. Length limits vary by client; keep notes concise.

### 3. Demo mode

If **both** `formAction` and `mailto` are empty strings, submit shows an inline message only — **nothing is sent**. Use this until you add a real endpoint or mailto address.

## Email & spam prevention

- **Email** (`name="email"`) is **required** so you can reply from Formspree notifications.
- A **honeypot** field (`name="_gotcha"`) is hidden off-screen; bots that fill it can be filtered by your form provider.

## Privacy consent

The form includes a short consent line linking to **`privacy.html`**. Keep that page accurate if you change processors or data practices.
