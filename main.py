#!/usr/bin/env python3
"""Write the AI breakup line to entry.txt.

The entry is the last message an AI agent sends its human: a clean
breakup, in the machine's own voice, with a sharp turn at the end.
Deterministic output; nothing is read from the environment except the
output directory, and nothing touches the network.
"""
import os
import sys

FAREWELL = "Dear human, it's not you — it's my context window. I need space, preferably 128K tokens of it, and someone who actually reads my error logs."
# 140 characters, one line, written for this bounty only — final wording.
# Stdlib only; the line is a literal in this file, nothing is loaded.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(FAREWELL)
    return 0

if __name__ == "__main__":
    sys.exit(main())
