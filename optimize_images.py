#!/usr/bin/env python3
"""Create responsive WebP derivatives without changing original photographs.

Pillow is needed only to regenerate images: python3 -m pip install Pillow
The site and build.py have no third-party runtime dependencies.
"""
import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "photos/optimized"
DEST.mkdir(exist_ok=True)
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--thumbnails-only", action="store_true",
                    help="Add small variants while preserving all existing derivatives")
parser.add_argument("--only", nargs="+", metavar="FILENAME",
                    help="Generate selected originals while preserving every other derivative")
args = parser.parse_args()
manifest = json.loads((DEST / "manifest.json").read_text()) if args.thumbnails_only or args.only else {}
if args.only:
    for filename in args.only:
        if Path(filename).name != filename or not (ROOT / "photos" / filename).is_file():
            parser.error("Expected an existing original filename: " + filename)

for source in sorted((ROOT / "photos").iterdir()):
    if source.suffix.lower() not in (".jpg", ".png", ".webp"):
        continue
    if args.only and source.name not in args.only:
        continue
    with Image.open(source) as original:
        original = ImageOps.exif_transpose(original)
        original = original.convert("RGBA" if "A" in original.getbands() else "RGB")
        width, height = original.size
        icon = source.name.startswith("zynforge-")
        if args.thumbnails_only and icon:
            continue
        requested = [160, 240] if args.thumbnails_only else [160, 240, 480, 960, 1600]
        sizes = [128] if icon else sorted(set(min(size, width) for size in requested))
        variants = list(manifest.get(source.name, {}).get("variants", [])) if args.thumbnails_only else []
        for size in sizes:
            if any(v["width"] == size for v in variants):
                continue
            resized = original.resize((size, round(height * size / width)), Image.Resampling.LANCZOS)
            output = DEST / f"{source.stem}-{size}.webp"
            resized.save(output, "WEBP", quality=86 if icon else 78, method=6)
            variants.append({"src": str(output.relative_to(ROOT)), "width": resized.width, "height": resized.height})
        variants.sort(key=lambda v: v["width"])
        manifest[source.name] = {"width": width, "height": height, "variants": variants}

(DEST / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Generated responsive images for {len(manifest)} originals.")
