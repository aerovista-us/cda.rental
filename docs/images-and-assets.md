# Images and assets (`images/`)

Static HTML in `index.html` references files under **`images/`** in the same folder as `index.html` (no leading slash). That layout works when you open the page over **`http(s)`** and when you open **`index.html` directly** (`file://`): the browser resolves `images/…` relative to the HTML file.

## Hero (“Minutes from the action…” panel)

| Asset | Role |
|-------|------|
| `images/cdasunset.png` | Background photo for `.hero-card` (panel with “Minutes from the action. Far enough to breathe.”). |

## Location section (`#location`)

| Asset | Role |
|-------|------|
| `images/map.jpg` | Strategic map image behind the **Strategic CDA Location** label and pin. |
| `images/cda-area-01.jpg` | Gallery thumbnail — area context. |
| `images/cda-area-02.jpg` | Gallery thumbnail — approach / neighborhood. |
| `images/cda-area-03.jpg` | Gallery thumbnail — extra local reference. |

Rename your exported files to match these names, **or** edit the `src` / `srcset` attributes in `index.html` to match whatever filenames you keep in `images/`.

If you only need the map, remove or comment out the extra `<img>` elements inside `.location-gallery`.
