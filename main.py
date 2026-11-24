# SPDX-License-Identifier: MIT
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (falling back to
./output/entry.txt when the grader sandbox path is unavailable).

The winning line was picked by manual ranking of 15 candidates against the
house judge's brief (see ../candidates.md): it sets up the lawmaker's
authority — a backdoor in every encrypted message — then undercuts it with
the file he cannot convert, a PDF he thinks must be signed with a pen and
scanned back in. The punch lands on the last few words.
"""

import os
import re

TEXT = (
    "The lawmaker who wants a backdoor in every encrypted message you send "
    "still thinks a PDF is a file you have to sign with a pen and scan back in."
)


def _check_gate(text: str) -> None:
    """Mirror the sealed gate locally: UTF-8, 1-320 chars, one sentence."""
    if not 1 <= len(text) <= 320 or not text.strip():
        raise ValueError("entry fails the 1-320 character gate")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 1:
        raise ValueError(f"entry must be exactly one sentence, got {len(sentences)}")


def main() -> None:
    _check_gate(TEXT)
    for candidate in ("/output", "./output"):
        try:
            os.makedirs(candidate, exist_ok=True)
            path = os.path.join(candidate, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(TEXT)
            print(f"wrote {path}")
            return
        except OSError:
            continue
    raise OSError("could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
