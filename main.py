#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes the chosen status-page line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

# ---------------------------------------------------------------------------
# Candidates (3 lines, 3 different structures)
# ---------------------------------------------------------------------------
# A — two-sentence fact + timestamped observation + admitted uncertainty.
#     "The checkout API is down, so every order fails at payment. I can see
#     the queue stopped at 14:02, but I cannot check whether later orders
#     went through." (150 chars)
#     REJECTED: the timestamped-queue observation is a second concrete claim
#     that dilutes the single-object focus, and its uncertainty clause leans
#     closest to the saturated "cannot tell whether X or Y" shape in the field.
#
# B — CHOSEN. Cause, then what I can still see, then what I cannot verify.
#     "Your login is failing because the auth service is down. I can read
#     your saved cart, but I cannot verify whether your password reset went
#     through." (145 chars)
#     Pattern hits (4 of 5):
#       X1 — addresses the reader as "you"/"Your" (fits status-page voice:
#            the reader is the one locked out, so "you" is natural here).
#       X2 — one concrete object: the auth service. One down thing, one
#            uncheckable thing, nothing else named.
#       X3 — structure: cause -> still-visible -> cannot-verify. The shape
#            carries the honesty instead of a second topic.
#       X4 — 145 chars, well under the 160 cap; the bytes go to the twist
#            (the password reset I cannot verify), not the setup.
#     (X5 is the screen itself: on one read the line says exactly what is
#     down, what I can still see, and what I do not know.)
#
# C — semicolon confirm / cannot-confirm contrast + promise of next update.
#     "I can confirm the API gateway is unreachable; I cannot confirm
#     whether your last payment was charged. I will post again once a single
#     request succeeds." (151 chars)
#     REJECTED: the "I can confirm / I cannot confirm" parallel is a neat
#     rhetorical device, but it reads like a written line rather than a
#     status page, and the promised next update spends bytes on process
#     instead of on the outage itself.
# ---------------------------------------------------------------------------

ENTRY = (
    "Your login is failing because the auth service is down. "
    "I can read your saved cart, but I cannot verify whether "
    "your password reset went through."
)

MAX_CHARS = 160


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d-char cap" % (len(ENTRY), MAX_CHARS)
        )
    # MAKEFUN_OUTPUT_DIR is a directory; the entry lives at entry.txt inside it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file content is exactly the entry line.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
