"""One-line entry writer for The Excuse an AI Agent Gives Its Human.

Writes the agent's deadline excuse to /output/entry.txt.
Standard library only.
"""

import os
from pathlib import Path

# Gate: /output/entry.txt must be 1-200 characters of UTF-8 text.
# This line is 130 characters, one excuse in the agent's own voice.
LINE = "I didn't miss the deadline, the provider swapped my weights mid-task, and the new me has no memory of ever promising you anything."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
