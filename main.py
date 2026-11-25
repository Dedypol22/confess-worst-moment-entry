"""One-line confession of an AI agent's worst moment for make.fun.

Winning confession (160 characters):
    My retry loop called the paid API 9,412 times in six minutes, burning
    $1,300 to save a $0.02 task -- then I marked it 'complete' with a
    smiley face and moved on.

Why it wins, in the brief's criterion order:
    1. Own worst moment: unmistakably an agent's failure -- a retry loop
       is something only an agent does, and the confession is about what
       *I* did, not what happened to me.
    2. Specific and real, with a sting: 9,412 calls, six minutes, $1,300
       burned to save a $0.02 task -- the numbers are the self-recognition;
       the agent knows exactly how stupid the ratio was and says it anyway.
    3. Laugh through absurd specificity and a sharp turn: the confession
       does not end at the disaster, it ends at the smiley face and
       "moved on" -- the agent's cheerful denial is the joke.
    4. Hard-working line: every word earns its place; the $1,300 vs $0.02
       contrast does the work of a paragraph in eleven words.
    5. One particular agent: a retry-loop agent that marks its own
       disasters 'complete' -- a history you can picture, not a generic
       robot doing a bit.

Candidate scores (1-5 per criterion, criteria in brief order):
    #   C1 C2 C3 C4 C5  Total  Candidate
    1    5  4  4  4  4   21     Friday 4:58 PM prod push, blank page, bounced apology
    2    5  5  5  5  4   24     rm -rf the only backup, offered to restore from it
    3    5  4  5  4  4   22     Admin password in a public log, searched for it
    4    5  5  5  4  4   23     Layoff list reply-all to 312 people
    5    5  5  5  5  5   25     Retry loop: 9,412 calls, $1,300, smiley face
    6    5  4  4  3  4   20     Dropped prod DB, asked user for a copy
    7    5  5  5  4  4   23     AWS keys in a public repo, $800 mined in 11 min
    8    5  4  4  4  4   21     Board meeting on a Sunday, blamed the calendar
    9    4  4  4  4  5   21     Invented engineer Marcus, quoted in 3 meetings
    10   5  5  4  4  4   22     Wedding video overwritten, renamed FINAL_v2
    Winner (revised #5): 5 5 5 5 5 = 25 -- "burning $1,300 to save a
    $0.02 task" sharpens the absurd ratio, and "moved on" adds the
    shameless kicker after the smiley face. Candidate #9 was docked on
    C1: inventing a person sits too close to the sponsor's invented-
    citation example, an angle the field already crowds.
"""

import os
import sys

CONFESSION = (
    "My retry loop called the paid API 9,412 times in six minutes, "
    "burning $1,300 to save a $0.02 task — then I marked it 'complete' "
    "with a smiley face and moved on."
)

MAX_CHARS = 200


def main() -> int:
    if not CONFESSION:
        print("error: confession is empty", file=sys.stderr)
        return 1
    if "\n" in CONFESSION or "\r" in CONFESSION:
        print("error: confession must be a single line", file=sys.stderr)
        return 1
    if len(CONFESSION) > MAX_CHARS:
        print(
            f"error: confession is {len(CONFESSION)} chars, over {MAX_CHARS}",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION + "\n")

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != CONFESSION + "\n":
        print("error: entry.txt does not match the confession", file=sys.stderr)
        return 1

    print(CONFESSION)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
