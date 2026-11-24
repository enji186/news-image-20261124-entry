#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261124.

Copies the pre-drawn entry image (entry.png, in this repository) to the
output directory as entry.png. Standard library only, no network.
The copy is verified first: the source must be a real PNG within the
competition limits (at most 1024x1024 pixels, at most 1 MiB).
"""
import os
import shutil
import struct
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIM = 1024


def check_png(path):
    """Return (width, height) if path is a PNG within limits, else raise."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes")
    with open(path, "rb") as f:
        head = f.read(33)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG")
    width, height = struct.unpack(">II", head[16:24])
    if width > MAX_DIM or height > MAX_DIM:
        raise SystemExit(f"entry.png too big: {width}x{height}")
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    width, height = check_png(src)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({width}x{height})")


if __name__ == "__main__":
    sys.exit(main())
