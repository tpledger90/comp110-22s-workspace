
from lessons.sum import sum

def test_sum_empty() -> None:
    assert sum([]) == 0

def test_sum_single_item() -> None:
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0

def test_sum_many_items() -> None:
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0

def test_sum_many_items_2() -> None:
    xs: list[float] = [-1.0, 1.0, -2.0, 2.0]
    assert sum(xs) == 0
