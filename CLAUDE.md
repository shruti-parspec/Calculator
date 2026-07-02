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

## Guardrails — do NOT
- Do not modify anything under `.github/` (the workflows / this setup) unless
  explicitly asked to.
- Do not add dependencies, network calls, or `eval` / `exec` of user input.
- Do not commit secrets or change repository settings.
