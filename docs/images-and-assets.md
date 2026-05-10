# Images and assets (`images/`)

Static HTML in `index.html` references files under **`images/`** in the same folder as `index.html` (no leading slash). That layout works when you open the page over **`http(s)`** and when you open **`index.html` directly** (`file://`): the browser resolves `images/…` relative to the HTML file.

## Hero (“Minutes from the action…” panel)

| Asset | Role |
|-------|------|
| `images/cdasunset.png` | Background photo for `.hero-card` (panel with “Minutes from the action. Far enough to breathe.”). Also referenced as **`og:image`** / **`twitter:image`** after you set **`REPLACE_SITE_PUBLIC_URL`** in `index.html` (see `docs/DEPLOY.md`). |

For share previews, you can swap `og:image` / `twitter:image` to a dedicated **`images/og-share.jpg`** (1200×630 or similar) once exported — keep URLs absolute after deploy.

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
