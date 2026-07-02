# Calculator — project guide for Claude

A small Python 3.14 command-line calculator. `calc.py` is the whole app: a set
of arithmetic functions plus an interactive menu loop.

## How to run
- `python calc.py` — starts the interactive menu.

## Conventions
- Python 3.14, **standard library only** — do not add third-party dependencies.
- Keep the code in `calc.py` unless a change clearly warrants splitting it.
- Match the existing style: plain functions, `snake_case`, f-strings.
- Every arithmetic function guards invalid input (e.g. division / modulus by
  zero raises `ZeroDivisionError`).

## When you open a PR
- Keep it small and focused on the single requested change.
- Say what changed and why in the PR description.
- If you add or change behavior, add a matching test. Create `test_calc.py`
  using `unittest` from the standard library if none exists, and make it pass.

## Fixing something from a comment on a pull request (stacked PR)

If an `@claude` comment on an existing pull request asks you to fix or change
something, do **not** commit to that PR's own branch. Open a *new* PR stacked on
top of it, and leave the original PR open and untouched:

1. Capture the current PR's head branch (you are already checked out on it):
   `BASE=$(git rev-parse --abbrev-ref HEAD)`.
2. Create a new branch off it: `git checkout -b claude/fix-<slug>`.
3. Make the requested change and commit it.
4. Push the new branch, then open a PR **based on the current PR's branch**:
   `gh pr create --base "$BASE" --head "$(git rev-parse --abbrev-ref HEAD)" --title "<title>" --body "<what changed and why>"`.
5. Reply with the new PR's URL. If you cannot open the PR, at least push the branch
   and reply with the compare link:
   `https://github.com/<owner>/<repo>/compare/$BASE...<new-branch>?quick_pull=1`.

Never push commits to the original PR's branch — the fix must arrive as a separate,
reviewable PR targeting that branch.

## Guardrails — do NOT
- Do not modify anything under `.github/` (the workflows / this setup) unless
  explicitly asked to.
- Do not add dependencies, network calls, or `eval` / `exec` of user input.
- Do not commit secrets or change repository settings.
