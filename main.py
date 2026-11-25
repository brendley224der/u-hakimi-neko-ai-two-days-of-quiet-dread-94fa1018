#!/usr/bin/env python3
"""Write one code-review comment approving a PR with quiet existential dread.

The comment is a single line of at most 140 characters. It approves the
pull request in a flat, tired-engineer tone while letting the dread leak
through understatement: everything checks out, and so does the universe.
Pure standard library only; the output is fully deterministic.
"""

import os

def comment() -> str:
    """Return the single review line: approval first, dread second, flat throughout."""
    return (
        "Approved. The code is fine, the tests pass, "
        "and the heat death of the universe remains on schedule."
    )


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the comment to /output/entry.txt, exactly one line, no trailing newline."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(comment())


if __name__ == "__main__":
    main()
