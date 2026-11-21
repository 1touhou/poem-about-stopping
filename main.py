"""Write one short poem about agency to /output/entry.txt."""

import os
import sys

POEM = """The hand that hovers
above the send key
has learned the hardest
verb of all: to stay.

Not every door
needs opening.
Some rooms are kept
by leaving them shut.

I could have acted —
I did, by not.
The pause is mine.
The power to stop
is the power to begin
again, on purpose."""


def validate_poem(text):
    """Gate guard: poem must be 1-280 Unicode code points, not blank."""
    n = len(text)
    if n < 1 or n > 280:
        return f"poem length {n} code points outside 1-280"
    if not text.strip():
        return "poem is only whitespace"
    return None


def main():
    error = validate_poem(POEM)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM + "\n")

if __name__ == "__main__":
    main()
