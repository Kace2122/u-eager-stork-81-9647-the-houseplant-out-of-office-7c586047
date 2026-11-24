#!/usr/bin/env python3
"""Houseplant Out-of-Office entry: writes one single-line auto-reply to /output/entry.txt."""

import os

REPLY = "Out of office: I am busy photosynthesizing. I will reply once I have finished drinking the sunlight."

# Self-check: the entry must stay one line of at most 120 characters.
assert "\n" not in REPLY and 1 <= len(REPLY) <= 120

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Self-check: the file on disk must hold exactly the validated line.
    assert open("/output/entry.txt", encoding="utf-8").read() == REPLY

if __name__ == "__main__":
    main()
