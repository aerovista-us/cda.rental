# Booking form wiring

The **booking request** UI lives on **`request.html`**. The `BOOKING` object and Formspree wiring are in the `<script>` block at the bottom of that file.

Selections from the homepage calendar are passed via:

- Query string: `request.html?nights=2026-06-12,2026-06-13,...`
- **`sessionStorage`** key `heartofawl.selectedNights` (JSON array), used when the query string is absent.

Links with class **`href-request`** on `index.html` save the current calendar selection and navigate to `request.html` with the `nights` parameter.

## Navigation on `index.html`

| Link / section | Target |
|----------------|--------|
| Brand / home | `#top` (`<main id="main-content">`, hero has `#top`) |
| Location | `#location` |
| Dates | `#calendar` |
| Estimate | `#payment` |
| Continue to booking | `#request` (CTA strip) or **`request.html`** (header / buttons with `href-request`) |

Peak nights **Jun 18–21** must be selected or cleared **together** on the calendar; the request page re-validates that rule before submit.

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

On load, the script sets `method="POST"` and, for `formspree.io`, adds `_subject` and `_next` (defaults to **`request.html?thanks=1`** after submit when not using `file://`; override via `thankYouUrl`).

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
