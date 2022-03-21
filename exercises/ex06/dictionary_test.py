"""Test file for methods in dictionary.py."""

__author__ = "730477982"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_blank_dict() -> None:
    """Tests when a blank dictionary is given."""
    names: dict[str, str] = {}
    assert invert(names) == {}


def test_invert_two_keys() -> None:
    """Tests when 2 key-value pairs are gievn."""
    names: dict[str, str] = {"Todd": "Pledger", "Brooks": "Miller"}
    assert invert(names) == {"Pledger": "Todd", "Miller": "Brooks"}


def test_invert_four_keys() -> None:
    """Tests when 4 key-value pairs are gievn."""
    names: dict[str, str] = {"Todd": "Pledger", "Brooks": "Miller", "Thomas": "Flynn", "Cole": "Maynard"}
    assert invert(names) == {"Pledger": "Todd", "Miller": "Brooks", "Flynn": 'Thomas', "Maynard": "Cole"}
"""

with pytest.raises(KeyError):
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)
"""

def test_favorite_color_tie() -> None:
    """Tests when there is a tie for the most prevalent color."""
    fav_colors: dict[str, str] = {"Todd": "Green", "Brooks": "Blue", "Cole": "Green", "Thomas": "Blue"}
    assert favorite_color(fav_colors) == "Green"


def test_favorite_color_blue_win() -> None:
    """Tests when the color blue wins."""
    fav_colors: dict[str, str] = {"Todd": "Blue", "Brooks": "Blue", "Cole": "Green", "Thomas": "Blue"}
    assert favorite_color(fav_colors) == "Blue"


def test_favorite_purple_win() -> None:
    """Tests when the color purple wins."""
    fav_colors: dict[str, str] = {"Todd": "Purple", "Brooks": "Blue", "Cole": "Green", "Thomas": "Orange", "Carter": "Purple"}
    assert favorite_color(fav_colors) == "Purple"


def test_count_blank_list() -> None:
    """Tests when a blank list is given."""
    sports: list[str] = []
    assert count(sports) == {}


def test_count_two_different_sports() -> None:
    """Tests when 2 different sports are given in the parameter list."""
    sports: list[str] = ["Baseball", "Football", "Football", "Football"]
    assert count(sports) == {"Baseball": 1, "Football": 3}


def test_count_four_different_sports() -> None:
    """Tests when 4 different sports are given in the parameter list."""
    sports: list[str] = ["Baseball", "Football", "Football", "Football", "Hockey", "Baseball", "Basketball", "Basketball"]
    assert count(sports) == {"Baseball": 2, "Football": 3, "Hockey": 1, "Basketball": 2}