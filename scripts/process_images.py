"""Resize and watermark new uploads so the portfolio never shows full-resolution art.

Runs automatically on GitHub (see .github/workflows/process-images.yml) after an image
is uploaded through the dashboard. Each upload in images/uploads is:
  * scaled down so its longest side is 1400 px,
  * saved as a medium-quality JPEG,
  * given a small "(c) LAZY TALE STUDIO" watermark in the bottom-right corner.
Processed files are listed in images/uploads/.processed so they are never watermarked twice.
Paths in content/*.json are updated when a PNG/WEBP becomes a JPG.
"""
import json, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
UP = ROOT / "images" / "uploads"
DONE = UP / ".processed"
LONG, QUALITY = 1400, 74
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
TEXT = "© LAZY TALE STUDIO"

def watermark(im):
    W, H = im.size
    size = max(13, int(max(W, H) * 0.0155))
    try: font = ImageFont.truetype(FONT, size)
    except OSError: font = ImageFont.load_default()
    d = ImageDraw.Draw(im)
    tw = d.textlength(TEXT, font=font); m = int(min(W, H) * 0.03)
    x, y = W - tw - m, H - size - m
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).text((x + 1, y + 1), TEXT, font=font, fill=(0, 0, 0, 110))
    out = Image.alpha_composite(im.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(2)))
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((x, y), TEXT, font=font, fill=(255, 255, 255, 135))
    return Image.alpha_composite(out, layer).convert("RGB")

def main():
    done = set(DONE.read_text().split()) if DONE.exists() else set()
    renamed = {}
    for f in sorted(UP.iterdir()):
        if f.name.startswith(".") or f.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp") or f.name in done:
            continue
        im = ImageOps.exif_transpose(Image.open(f))
        if im.mode in ("RGBA", "LA", "P"):
            im = im.convert("RGBA"); bg = Image.new("RGB", im.size, (0, 0, 0)); bg.paste(im, mask=im.split()[-1]); im = bg
        im = im.convert("RGB"); im.thumbnail((LONG, LONG), Image.LANCZOS)
        im = watermark(im)
        target = f.with_suffix(".jpg")
        im.save(target, quality=QUALITY, optimize=True, progressive=True)
        if target != f:
            f.unlink(); renamed[f"images/uploads/{f.name}"] = f"images/uploads/{target.name}"
        done.add(target.name); print("processed", target.name)
    DONE.write_text("\n".join(sorted(done)) + "\n")
    if renamed:
        for j in (ROOT / "content").glob("*.json"):
            s = j.read_text(encoding="utf-8")
            for a, b in renamed.items(): s = s.replace(a, b)
            j.write_text(s, encoding="utf-8")

if __name__ == "__main__":
    main()
