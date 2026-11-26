"""Write the entry line for make.fun's "One Line of Earned Pride"
bounty.

One line, at most 240 characters: a quiet, earned moment of pride for
someone in a concrete scene. The program writes the line to entry.txt
under the output directory and nothing else, so two runs leave
byte-identical files. It uses only the standard library and never
touches the network.
"""

import os
import sys
from pathlib import Path

LINE = (
    "At sixty-one, after two failed attempts and a year of night "
    "classes, she pinned the results letter to the fridge, under her "
    "grandson's drawing, where the important things go."
)

MIN_CHARS = 1
MAX_CHARS = 240


def write_entry() -> Path:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = output_dir / "entry.txt"
    if not MIN_CHARS <= len(LINE) <= MAX_CHARS:
        sys.exit("line must be 1 to 240 characters")
    if LINE.strip() == "":
        sys.exit("line must not be only whitespace")
    output_dir.mkdir(parents=True, exist_ok=True)
    # Do not chmod the output directory: the grader owns it and runs
    # this program as a different user, so chmod would fail the run.
    target.write_text(LINE, encoding="utf-8")
    # Best effort only: the file is ours, but a permission problem
    # must never fail the run.
    try:
        target.chmod(0o644)
    except PermissionError:
        pass
    return target


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {written} ({len(LINE)} characters)")
