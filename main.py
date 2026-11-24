#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one original patch note to /output/entry.txt and asserts the
competition gate: UTF-8 text, 1 to 160 characters, not only whitespace.
Standard library only; fully deterministic.
"""

import os

LINE = (
    "v2.0.3: fixed a bug where walking through a doorway deleted your "
    "reason for entering the room; standing still and staring at nothing "
    "no longer helps."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
