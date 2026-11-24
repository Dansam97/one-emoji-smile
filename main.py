"""One Emoji, One Smile — entry program.

Writes exactly one emoji to entry.txt in the output directory:
the smiling face with open hands, a warm, friendly gesture any
stranger reads instantly, with no words and no flirtation.
"""

import os

ENTRY_TEXT = "🤗"


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the gate.

    The gate accepts UTF-8 text of 1 to 8 characters that is not only
    white space; this entry is stricter — exactly one emoji code point.
    """
    text = ENTRY_TEXT
    encoded = text.encode("utf-8")  # raises if not UTF-8 encodable
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    if not 1 <= len(text) <= 8:
        raise ValueError("entry outside the 1-8 character gate")
    if text.strip() == "":
        raise ValueError("entry must not be white space")
    if len(encoded) == 0:
        raise ValueError("entry encodes to no bytes")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (validated_text() + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("entry.txt read-back does not match what was written")


if __name__ == "__main__":
    main()
