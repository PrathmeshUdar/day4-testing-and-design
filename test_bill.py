from decimal import Decimal

import pytest

from bill import split_bill


# --- fixtures: reusable setup -------------------------------------------
@pytest.fixture
def dinner_total():
    return Decimal("100.00")


def test_even_split(dinner_total):
    assert split_bill(dinner_total, 4) == [Decimal("25.00")] * 4


# --- parametrize: one test, many cases (zero, one, many, huge) -----------
@pytest.mark.parametrize(
    "total, people, expected",
    [
        ("0", 3, ["0.00", "0.00", "0.00"]),          # zero total
        ("10.00", 1, ["10.00"]),                      # one person
        ("10.00", 3, ["3.34", "3.33", "3.33"]),       # does not divide evenly
        ("0.01", 3, ["0.01", "0.00", "0.00"]),        # smaller than people
        ("1000000000.00", 7,                          # huge
         ["142857142.86"] * 5 + ["142857142.85"] * 2),
    ],
)
def test_split_cases(total, people, expected):
    assert split_bill(total, people) == [Decimal(x) for x in expected]


@pytest.mark.parametrize("total, people", [("10", 3), ("99.99", 7), ("0.05", 2)])
def test_shares_always_add_up_to_total(total, people):
    assert sum(split_bill(total, people)) == Decimal(total)


def test_shares_differ_by_at_most_one_cent():
    shares = split_bill("100.00", 7)
    assert max(shares) - min(shares) <= Decimal("0.01")


# --- failing fast with clear errors --------------------------------------
@pytest.mark.parametrize("people", [0, -2])
def test_zero_or_negative_people_rejected(people):
    with pytest.raises(ValueError, match="at least 1"):
        split_bill("10.00", people)


def test_negative_total_rejected():
    with pytest.raises(ValueError, match="negative"):
        split_bill("-5.00", 2)


def test_fraction_of_a_cent_rejected():
    with pytest.raises(ValueError, match="cent"):
        split_bill("10.005", 2)


def test_non_integer_people_rejected():
    with pytest.raises(TypeError):
        split_bill("10.00", 2.5)


# --- regression test: a bug we once had, pinned forever ------------------
def test_regression_float_total_does_not_lose_a_cent():
    # Bug: Decimal(0.1 + 0.2) carried float noise. Fixed by Decimal(str(x)).
    assert sum(split_bill(0.30, 3)) == Decimal("0.30")
