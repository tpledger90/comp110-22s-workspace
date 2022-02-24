"""Test file."""

__author__ = "730477982"

from utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """Tests when list given is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_no_evens() -> None:
    """Tests when no evens are given in the list."""
    xs: list[int] = [3, 7, 23, 145]
    assert only_evens(xs) == []


def test_only_evens_two_evens() -> None:
    """Tests when there are 2 evens in the list given."""
    xs: list[int] = [3, 7, 60, 23, 145, 142]
    assert only_evens(xs) == [60, 142]


def test_only_evens_five_evens() -> None:
    """Tests when there a 5 evens in the list given."""
    xs: list[int] = [2, 3, 6, 7, 60, 23, 84, 145, 142]
    assert only_evens(xs) == [2, 6, 60, 84, 142]


def test_sub_negative_start_index() -> None:
    """Tests when the start index is negative."""
    xs: list[int] = [1, 5, 6, 12, 19]
    start_i: int = -1
    end_i: int = 3
    assert sub(xs, start_i, end_i) == [1, 5, 6]


def test_sub_high_end_index() -> None:
    """Tests when the end index given is higher than the highest index of the list."""
    xs: list[int] = [5, 6, 8, 9]
    start_i: int = 0
    end_i: int = 6
    assert sub(xs, start_i, end_i) == [5, 6, 8, 9]


def test_sub_length_four_sublist() -> None:
    """Tests when the sublist should have a length of 4."""
    xs: list[int] = [1, 5, 6, 12, 19, 25]
    start_i: int = 1
    end_i: int = 5
    assert sub(xs, start_i, end_i) == [5, 6, 12, 19]


def test_sub_length_six_sublist() -> None:
    """Tests when the sublist should have a length of 6."""
    xs: list[int] = [1, 5, 6, 12, 19, 25, 67, 125, 198, 200]
    start_i: int = 3
    end_i: int = 9
    assert sub(xs, start_i, end_i) == [12, 19, 25, 67, 125, 198]


def test_concat_two_empty_lists() -> None:
    """Tests when 2 empty lists are given."""
    xs_1: list[int] = []
    xs_2: list[int] = []
    assert concat(xs_1, xs_2) == []


def test_concat_four_total_elements() -> None:
    """Tests when you should have a total of 4 elements in your final list."""
    xs_1: list[int] = [12, 645]
    xs_2: list[int] = [239, 111]
    assert concat(xs_1, xs_2) == [12, 645, 239, 111]


def test_concat_8_total_elements() -> None:
    """Tests when you should have a total of 8 elements in your final list."""
    xs_1: list[int] = [37, 28, 35, 46]
    xs_2: list[int] = [67, 28, 47, 38]
    assert concat(xs_1, xs_2) == [37, 28, 35, 46, 67, 28, 47, 38]
