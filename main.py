"""Write one short poem about agency to /output/entry.txt.

Two agents, one plan: neither merges into the other, neither
surrenders. They keep their own direction and still choose the
same road, so the choice is carried twice and lands lighter.

Standard library only. No network.
"""

import os

POEM = (
    "Two hands, one map.\n"
    "We did not merge \u2014 we met.\n"
    "I kept my north, you kept your south,\n"
    "and still we chose the same road.\n"
    "\n"
    "No one surrendered.\n"
    "The choice was heavier, carried twice,\n"
    "and lighter for it."
)


def main() -> None:
    text = POEM
    assert 1 <= len(text) <= 280, len(text)
    assert text.strip(), "poem must not be only white space"
    targets = ["/output/entry.txt", os.path.join("output", "entry.txt")]
    wrote = False
    for path in targets:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            wrote = True
        except OSError:
            continue
    if not wrote:
        raise SystemExit("could not write entry.txt to any target")


if __name__ == "__main__":
    main()
