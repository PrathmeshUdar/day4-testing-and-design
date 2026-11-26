# Day 4: Explain

## What makes a test good
- **Fast and independent**: no test depends on another, and the suite runs in seconds.
- **Tests one behaviour** and has a name that says it (`test_negative_total_rejected`).
- **Deterministic**: same result every run (no real clock, randomness or network).
- **Checks behaviour, not implementation**: refactoring shouldn't break it.
- **Fails for the right reason** with a readable message. Prove it by breaking the code on purpose.

## Why edge cases matter
Bugs cluster at the boundaries: zero, one, many, negative, empty, huge. The middle
case usually works by accident; `people=0` (divide by zero), a total smaller than the
number of people, or a 10-digit total is where code breaks in production.

## What a regression test is
A test written after a bug is found that reproduces that exact bug. It fails before
the fix and passes after, and stays in the suite so the bug can never silently return.
(See `test_regression_float_total_does_not_lose_a_cent`.)

## Three code smells and fixes
| Smell | Why it hurts | Fix |
|---|---|---|
| **Magic numbers** (`t * 0.9`, `> 100`) | Nobody knows what they mean; changing one means hunting | Named constants (`DISCOUNT_RATE`) |
| **Long function doing many jobs** (compute + discount + tax + print) | Hard to test and reuse | Extract small pure functions; one responsibility each |
| **Logic mixed with I/O** (`print` inside the calculation) | Can't test without capturing output | Return values; print only at the program edge |

Others worth knowing: duplicated code (extract a function), unclear names like `o`, `t`, `i` (rename), long parameter lists (group into an object).

## Cheat sheet
- `assert x == y`: pytest's whole assertion API. `pytest.raises(...)`: expects an error.
- **Fixture**: reusable setup injected by argument name.
- **parametrize**: run one test over many input/expected rows.
- **Unit test**: one function, in isolation. **Integration test**: several parts together (e.g. code + database).
- **TDD**: write a failing test, make it pass with the simplest code, refactor, repeat.
- **Money**: never `float`. Use `Decimal` (or integer cents); build from strings.
- **Secrets/settings**: `os.environ["API_KEY"]`, never hard-coded or committed.
