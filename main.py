#!/usr/bin/env python3
"""Entrypoint for make.fun bounty u-irvan-motion-seventeen-syllables-of-debugging-d194b605
("Seventeen Syllables of Debugging").

The entry is entry.txt, beside this file: one haiku about debugging,
three lines in the 5-7-5 syllable shape, 66 characters. The grader
runs this program twice, with no network, and both runs must write
the same bytes to /output/entry.txt, so the program is a plain
byte-for-byte copy using only the Python standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.txt")
    dst = os.path.join(out_dir, "entry.txt")
    with open(src, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    # Mirror the bounty's gate locally: fail loudly if the shipped text
    # could not pass it (UTF-8, 1 to 200 characters, not only white
    # space), and check the haiku shape the brief demands — exactly
    # three lines — instead of writing an invalid entry.
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text.strip(), "entry must not be only white space"
    assert len(text.split("\n")) == 3, "entry must be three lines"
    with open(dst, "wb") as f:
        f.write(data)
    assert os.path.getsize(dst) == len(data), "copied text size mismatch"


if __name__ == "__main__":
    main()
