#!/usr/bin/env python3
"""Create responsive WebP derivatives without changing original photographs.

Pillow is needed only to regenerate images: python3 -m pip install Pillow
The site and build.py have no third-party runtime dependencies.
"""
import json
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
DEST = ROOT / "photos/optimized"
DEST.mkdir(exist_ok=True)
manifest = {}

for source in sorted((ROOT / "photos").iterdir()):
    if source.suffix.lower() not in (".jpg", ".png"):
        continue
    with Image.open(source) as original:
        original = ImageOps.exif_transpose(original)
        original = original.convert("RGBA" if "A" in original.getbands() else "RGB")
        width, height = original.size
        icon = source.name.startswith("zynforge-")
        sizes = [128] if icon else sorted(set(min(size, width) for size in [480, 960, 1600]))
        variants = []
        for size in sizes:
            resized = original.resize((size, round(height * size / width)), Image.Resampling.LANCZOS)
            output = DEST / f"{source.stem}-{size}.webp"
            resized.save(output, "WEBP", quality=86 if icon else 78, method=6)
            variants.append({"src": str(output.relative_to(ROOT)), "width": resized.width, "height": resized.height})
        manifest[source.name] = {"width": width, "height": height, "variants": variants}

(DEST / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
print(f"Generated responsive images for {len(manifest)} originals.")
