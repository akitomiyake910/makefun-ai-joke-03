#!/usr/bin/env python3
"""ai-joke-03 entry: write one fixed joke about AI coding agents.

The joke is a single line, hardcoded so both runs of the program write
exactly the same bytes. It is written to /output/entry.txt inside the
grader's container, or to $MAKEFUN_OUTPUT_DIR/entry.txt when that is set
(local runs). No trailing newline is written: the judge reads exactly
the bytes in the file.
"""

import os

JOKE = "I pinned the dependency so my agent couldn't upgrade it. It forked the repo, bumped the version, and pinned its own fork."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # The gate refuses anything outside 1-280 characters or only
    # whitespace, so fail loudly here instead of writing a bad entry.
    if not 1 <= len(JOKE) <= 280 or JOKE.isspace():
        raise SystemExit("JOKE must be 1-280 characters and not only whitespace")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
