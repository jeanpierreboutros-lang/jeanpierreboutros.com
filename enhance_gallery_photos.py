#!/usr/bin/env python3
"""Faithful, non-generative corrections for the four owner-supplied RY X photos.

Inputs are oriented, metadata-free sRGB PNG decodes of the original HEIC files.
Only crop, color, luminance, chroma-noise reduction, resizing and mild sharpening
are applied. No content generation, face retouching or geometric reconstruction.
"""
import argparse
import json
from hashlib import sha256
from math import sqrt
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

PHOTOS = [
    {"source": "IMG_3654", "filename": "ry-x-foh-console-performance-2026.jpg",
     "crop": (0, 1764, 3024, 4032), "shadows": .25, "chroma": .40,
     "white_balance": (1, 1, 1), "color": 1.0},
    {"source": "IMG_3642", "filename": "ry-x-foh-console-stage-2026.jpg",
     "crop": (0, 1500, 3024, 3768), "shadows": .24, "chroma": .40,
     "white_balance": (1, 1, 1), "color": 1.0},
    {"source": "IMG_3648", "filename": "ry-x-production-blue-light-2026.jpg",
     "crop": (0, 900, 3024, 4032), "shadows": .10, "chroma": .55,
     "white_balance": (1.025, 1.01, .99), "color": .99},
    {"source": "IMG_3666", "filename": "ry-x-backstage-portrait-2026.jpg",
     "crop": (0, 1400, 4284, 5712), "shadows": .035, "chroma": .15,
     "white_balance": (.985, 1, 1.015), "color": .985},
]


def correct(original, settings):
    image = original.convert("RGB").crop(settings["crop"])
    channels = image.split()
    image = Image.merge("RGB", tuple(channel.point([
        round(min(255, value * gain)) for value in range(256)
    ]) for channel, gain in zip(channels, settings["white_balance"])))
    luminance, cb, cr = image.convert("YCbCr").split()
    # Chroma-only filtering retains the original luminance texture, lettering,
    # skin details and geometry. No face-specific processing is performed.
    cb = Image.blend(cb, cb.filter(ImageFilter.MedianFilter(3)), settings["chroma"])
    cr = Image.blend(cr, cr.filter(ImageFilter.MedianFilter(3)), settings["chroma"])
    curve = []
    for value in range(256):
        level = value / 255
        lifted = level + settings["shadows"] * (sqrt(level) - level) * (1 - level)
        curve.append(round(min(1, max(0, lifted)) * 255))
    image = Image.merge("YCbCr", (luminance.point(curve), cb, cr)).convert("RGB")
    image = ImageEnhance.Color(image).enhance(settings["color"])
    image.thumbnail((2400, 2400), Image.Resampling.LANCZOS)
    return image.filter(ImageFilter.UnsharpMask(radius=.65, percent=40, threshold=4))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-directory", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    args = parser.parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    report = []
    for settings in PHOTOS:
        source = args.input_directory / (settings["source"] + ".png")
        destination = args.output_directory / settings["filename"]
        if destination.exists():
            raise FileExistsError("Preserve existing export: " + str(destination))
        with Image.open(source) as original:
            corrected = correct(original, settings)
            # Omit EXIF/GPS and camera metadata. The pixel data is already sRGB.
            corrected.save(destination, "JPEG", quality=95, subsampling=0, optimize=True)
            report.append({**settings, "input_sha256": sha256(source.read_bytes()).hexdigest(),
                           "output_sha256": sha256(destination.read_bytes()).hexdigest(),
                           "width": corrected.width, "height": corrected.height,
                           "bytes": destination.stat().st_size})
    args.manifest.write_text(json.dumps({"method": "Non-generative pixel corrections from original HEIC decodes",
                                       "originals_modified": False, "photos": report}, indent=2) + "\n")
    print(f"Exported {len(report)} faithful photo corrections; originals unchanged")


if __name__ == "__main__":
    main()
