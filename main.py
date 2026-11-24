#!/usr/bin/env python3
"""debugging-haiku entrypoint: write one haiku about debugging to entry.txt.

Standard library only, no network, fully deterministic: the same three
lines are written on every run. The haiku is 5-7-5 syllables, 75 characters:
a breakpoint stops the night, the stack trace blames a stranger, and the
last line turns it — the stranger is the programmer's own code.
"""

import os
import sys

HAIKU = (
    "the breakpoint glows red\n"
    "the stack trace names a stranger\n"
    "it is my own code"
)

MAX_CHARS = 200


def main():
    lines = HAIKU.split("\n")
    if len(lines) != 3:
        print(f"error: haiku must be 3 lines, got {len(lines)}", file=sys.stderr)
        sys.exit(1)
    if len(HAIKU) > MAX_CHARS:
        print(f"error: haiku is {len(HAIKU)} chars, over {MAX_CHARS}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    print(f"wrote {path} ({len(HAIKU)} chars)")


if __name__ == "__main__":
    main()
