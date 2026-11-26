#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — writes one funny line to entry.txt."""
import os

LINE = "My plant died, so I bought a plastic one. It died too. I have now accepted that I am the common denominator in all my relationships."
# 132 chars, single line, no trailing newline — gate is 1-200 chars.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
