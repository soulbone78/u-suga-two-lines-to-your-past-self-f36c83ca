import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TEXT = (
    "Don't delete the voicemail your mother left from the hospital at 2 a.m. the night before her surgery.\n"
    "It holds the last time you ever heard her laugh, and once it's gone your daughter will never know how her grandmother sounded when she was happy.\n"
)


def _validate(text):
    lines = text.splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    assert text.strip(), "entry must not be only whitespace"


def main():
    _validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
