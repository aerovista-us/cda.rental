"""One-off generator for assets/share-preview.jpg (1200x620 OG image). Run from repo root: python scripts/generate_share_preview.py"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "assets" / "share-preview.jpg"
    out.parent.mkdir(parents=True, exist_ok=True)

    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / max(H - 1, 1)
        r = int(7 + t * 8)
        g = int(19 + t * 28)
        b = int(29 + t * 35)
        for x in range(W):
            vx = abs(x - W / 2) / (W / 2)
            vy = abs(y - H / 2) / (H / 2)
            v = max(vx, vy) ** 1.2
            rr = max(0, min(255, int(r - v * 40)))
            gg = max(0, min(255, int(g - v * 35)))
            bb = max(0, min(255, int(b - v * 30)))
            px[x, y] = (rr, gg, bb)

    draw = ImageDraw.Draw(img)
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 54)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 32)
        font_sm = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
        font_cta = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    except OSError:
        font_title = font_sub = font_sm = font_cta = ImageFont.load_default()

    lines = [
        ("CDA Race Week Basecamp", font_title, "#ffffff"),
        ("Private 3BR / 2BA Coeur d'Alene home", font_sub, "#c8f9ff"),
        ("For athletes, families & support crews", font_sm, "#dfe8f8"),
        ("Request dates — No payment today", font_cta, "#5df2a1"),
    ]
    y = 115
    for text, font, color in lines:
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text(((W - tw) // 2, y), text, font=font, fill=color)
        y += th + 20

    img.save(out, "JPEG", quality=88, optimize=True)
    print(out, out.stat().st_size)


if __name__ == "__main__":
    main()
