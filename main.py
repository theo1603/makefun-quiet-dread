#!/usr/bin/env python3
"""Write one code-review comment that approves a pull request with quiet
existential dread, to /output/entry.txt.

Draft (first attempt):
    LGTM. The tests pass, the logic holds, and somewhere in this diff a
    future me is already apologizing.

Revised (the line actually written):
    LGTM. Tests pass, logic holds, and the part I don't understand is now
    officially our problem.

Why the revision is better: it is tighter, and the dread now comes from the
reviewer themself -- approving code they admit not understanding -- instead
of a "future me" gag. "Officially our problem" is flatter and fresher than
"already apologizing", and the approval still sounds like an approval.
"""

import os

TEXT = ("LGTM. Tests pass, logic holds, and the part I don't understand "
        "is now officially our problem.")

OUTPUT_PATH = "/output/entry.txt"

# The gate rejects anything outside 1-140 characters or more than one line,
# so check the text before writing instead of trusting it blindly.
assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
assert "\n" not in TEXT, "entry must be a single line"
assert TEXT.strip(), "entry must not be only whitespace"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
