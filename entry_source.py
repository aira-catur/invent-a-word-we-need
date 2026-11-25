import os
from pathlib import Path

FINAL_LINE = "Thoughtplied: certain you answered a message, though you only composed the reply in your head."


def emit(line: str) -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
