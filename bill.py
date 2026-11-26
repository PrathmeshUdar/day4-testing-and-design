"""Split a bill fairly between people, using Decimal so money is exact."""
from decimal import Decimal, ROUND_DOWN

CENT = Decimal("0.01")


def split_bill(total, people):
    """Return a list of `people` shares that add up to exactly `total`.

    Shares differ by at most one cent: the leftover cents go to the first
    people in the list. Raises ValueError on bad input (fail fast).
    """
    if isinstance(people, bool) or not isinstance(people, int):
        raise TypeError("people must be a whole number")
    if people <= 0:
        raise ValueError("people must be at least 1")

    total = Decimal(str(total))  # str() avoids float noise like 0.1 + 0.2
    if total < 0:
        raise ValueError("total cannot be negative")
    if total != total.quantize(CENT):
        raise ValueError("total cannot have fractions of a cent")

    total_cents = int(total / CENT)
    base, leftover = divmod(total_cents, people)
    return [Decimal(base + (1 if i < leftover else 0)) * CENT for i in range(people)]
