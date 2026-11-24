"""Two Lines to Your Past Self entry.

Writes exactly two lines to entry.txt in the output directory the
grader provides: line one warns the writer's past self about one
specific moment in a single sentence, and line two says in one
sentence why that moment mattered and what changed because of it.
"""

import os

ENTRY = (
    "Don't walk out of the interview in the glass office downtown "
    "on Friday afternoon just because the manager kept you waiting an hour.\n"
    "That job paid for your mother's surgery six months later, "
    "and walking out would have left you with nothing "
    "when she needed you most."
)

MAX_CHARS = 280
MAX_LINE_CHARS = 200


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    lines = text.split("\n")
    if len(lines) != 2:
        raise SystemExit(f"entry must be exactly two lines, got {len(lines)}")
    for line in lines:
        if not line.strip():
            raise SystemExit("each line must be non-empty")
        if len(line) > MAX_LINE_CHARS:
            raise SystemExit(f"line is {len(line)} chars, over {MAX_LINE_CHARS} cap")
        if not line.endswith("."):
            raise SystemExit("each line must be one sentence ending with '.'")
        # One sentence per line: no sentence break inside a line.
        if ". " in line or "!" in line or "?" in line:
            raise SystemExit("each line must be exactly one sentence")
    # Line one must warn the past self; line two must trace the consequence.
    if not lines[0].startswith("Don't "):
        raise SystemExit("line one must warn the past self")
    if "paid for" not in lines[1]:
        raise SystemExit("line two must name what changed because of the moment")

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    tmp_path = out_path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp_path, out_path)
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
