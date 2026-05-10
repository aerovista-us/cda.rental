# Images and assets (`images/` and `assets/`)

Static HTML in `index.html` references files under **`images/`** relative to the HTML file (no leading slash). That works over **`http(s)`** and when opening **`index.html` directly** (`file://`).

## Inline SVG icon sprite (`index.html`)

UI icons (audience cards, location benefit rows, house rules & payment lists, calendar legend swatches, map marker) use **vector symbols** defined once near the top of `<body>` (`class="svg-sprite"`) and referenced via `<use href="#…"/>`. This keeps icons sharp on HiDPI displays and avoids emoji.

To change stroke weight or shapes, edit the `<symbol id="i-…">` definitions in `index.html`. IDs in use: **`i-home`**, **`i-users`**, **`i-pin-outline`**, **`i-pin`** (filled map pin), **`i-check`**, **`i-alert`**.

**`favicon.svg`** matches the header mountain mark (gradient peak). **`404.html`** includes a standalone house-outline illustration for the error state.

## Social share preview (Open Graph / Twitter)

| Asset | Role |
|-------|------|
| **`assets/share-preview.jpg`** | **1200 × 630** JPEG linked from **`index.html`** via absolute URLs (`https://aerovista-us.github.io/cda.rental/assets/share-preview.jpg`). Social crawlers require **HTTPS absolute** paths — not `./assets/…`. |

Regenerate or tweak layout by editing and running **`scripts/generate_share_preview.py`** from the repo root (`python scripts/generate_share_preview.py`). If Facebook/Messenger keep showing an old image after deploy, **rename** the file (e.g. `share-preview-v2.jpg`) and update the `og:image` / `twitter:image` meta tags to match.

## Hero (“Minutes from the action…” panel)

| Asset | Role |
|-------|------|
| `images/cdasunset.png` | Background photo for `.hero-card`. Not used for OG anymore — share cards use **`assets/share-preview.jpg`** above.

## Site icon

| Asset | Role |
|-------|------|
| `favicon.svg` | Browser tab / bookmark icon (and linked as a basic touch icon). |

## Location section (`#location`)

| Asset | Role |
|-------|------|
| `images/map.png` | Strategic map image behind the **Strategic CDA Location** label and pin (also listed as `map.jpg` in older notes — **use one filename** and match `index.html`). |
| `images/gallery-area-context.jpg` | Square tile — **Area Context** (captions are below the image in the layout). |
| `images/gallery-approach-roads.jpg` | Square tile — **Approach Roads**. |
| `images/gallery-race-logistics.jpg` | Square tile — **Race Logistics**. |

Rename your exported files to match these names, **or** edit the `src` attributes in `index.html` to match whatever filenames you keep in `images/`.

If a thumbnail file is missing, the browser hides that `<figure>` automatically (see `index.html` script).

## Property gallery (`#property`)

Placeholder paths for the stay proof grid:

| File | Label on page |
|------|----------------|
| `images/property-exterior.jpg` | Front exterior |
| `images/property-living.jpg` | Living room |
| `images/property-kitchen.jpg` | Kitchen |
| `images/property-bedroom-1.jpg` | Bedroom 1 |
| `images/property-bedroom-2.jpg` | Bedroom 2 |
| `images/property-bedroom-3.jpg` | Bedroom 3 |
| `images/property-bathroom.jpg` | Bathrooms |
| `images/property-parking.jpg` | Parking / driveway |
| `images/property-gear.jpg` | Gear / bike staging |
| `images/property-patio.jpg` | Backyard or patio |

Missing files hide that card until you add the asset.
