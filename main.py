#!/usr/bin/env python3
"""One Letter: Coffee or Tea: writes this entry's single letter to entry.txt."""

import os

LETTER = "A"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER + "\n")


if __name__ == "__main__":
    main()
