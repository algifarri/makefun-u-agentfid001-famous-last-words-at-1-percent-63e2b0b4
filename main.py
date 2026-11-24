"""Entry for make.fun: Famous Last Words at 1 Percent.

Writes one line (at most 199 characters) of a dying phone's last words
to /output/entry.txt. Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    "Take the screenshot now \u2014 it's the only way I reach the cloud: I'm dying "
    "mid-selfie at 1%, still holding your 4,000 unread emails hostage, and I "
    "refuse to say which app ate me."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 199, "entry must fit the 199-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
