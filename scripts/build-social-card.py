#!/usr/bin/env python3
"""Render the original SVG social-share artwork to a PNG usable by OG/X crawlers."""
from pathlib import Path
from struct import unpack

from cairosvg import svg2png

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "public" / "assets" / "social-share.svg"
OUTPUT = ROOT / "public" / "assets" / "social-share.png"

if not INPUT.is_file():
    raise SystemExit(f"Missing social-share SVG: {INPUT}")
svg2png(url=str(INPUT), write_to=str(OUTPUT), output_width=1200, output_height=630)

header = OUTPUT.read_bytes()[:24]
if header[:8] != b"\x89PNG\r\n\x1a\n":
    raise SystemExit("Social card is not a PNG")
width, height = unpack(">II", header[16:24])
if (width, height) != (1200, 630) or OUTPUT.stat().st_size < 5000:
    raise SystemExit(f"Unexpected image dimensions or size: {width}x{height}")
print(f"SOCIAL_CARD_BUILD=PASS {width}x{height} bytes={OUTPUT.stat().st_size}")
