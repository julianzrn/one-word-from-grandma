"""Entry for make.fun bounty: One Word From Grandma.

Writes the entry word to /output/entry.txt with no trailing newline.
Exactly one word: the word grandma would text about AI.
"""

from pathlib import Path

ENTRY_TEXT = "Robit"

OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> bytes:
    """Return the entry encoded exactly as it will be stored."""
    return ENTRY_TEXT.encode("utf-8")


def write_entry() -> None:
    """Write the entry text to the output file exactly as specified."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(render_entry())


if __name__ == "__main__":
    write_entry()
