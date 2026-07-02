# Calculator

A small Python 3.14 command-line calculator.

## Run it

```bash
python calc.py
```

Then choose an operation from the menu: add, subtract, multiply, divide, power, or modulus.

## Ask Claude for changes

This repo is wired up with the [Claude Code GitHub Action](https://github.com/anthropics/claude-code-action).
Mention **`@claude`** in any issue or pull-request comment with a task, and Claude
will investigate and open (or update) a PR. For example:

> @claude add unit tests for every function in calc.py

Only users with write access to this repo can trigger Claude. See `CLAUDE.md`
for the conventions Claude follows here.
