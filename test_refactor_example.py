import pytest
from refactor_example import process, order_total

@pytest.mark.parametrize("items", [[], [(10, 1)], [(30, 2), (25, 3)]])
def test_refactor_keeps_behaviour(items, capsys):
    assert order_total(items) == pytest.approx(process(items))
