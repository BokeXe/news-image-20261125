#!/usr/bin/env python3
"""Entry program for news-image-20261125.

Copies the pre-rendered Wednesday 25 November 2026 front page (entry.png,
generated deterministically by prep/news25/build.py) into the output
directory. No clock, no network, no randomness: both runs write the
same bytes.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    dst = os.path.join(outdir, "entry.png")
    # Size guard: the gate caps the image at 1 MiB.
    assert os.path.getsize(src) <= 1048576, "entry.png exceeds the 1 MiB cap"
    shutil.copyfile(src, dst)
    # Determinism guard: the output must be the source, byte for byte.
    assert os.path.getsize(dst) == os.path.getsize(src), "copied size differs from entry.png"
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
