"""Methods made for the use of practicing unit testing."""

__author__ = "730477982"


def only_evens(test_list: list[int]) -> list[int]:
    """Returns a new list of only the even #s of the list given."""
    even_list: list[int] = []

    for num in test_list:
        if num % 2 == 0:
            even_list.append(num)
    
    return even_list


def sub(test_list: list[int], start_i: int, end_i: int) -> list[int]:
    """Returns a new, sub list of the list argument, given the start index(inclusive) and end index(exclusive)."""
    sub_list: list[int] = []

    if start_i < 0:
        start_i = 0
    if end_i >= len(test_list):
        end_i = len(test_list)

    while start_i < end_i:
        sub_list.append(test_list[start_i])
        start_i += 1
    
    return sub_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Creates new list that includes all ints in first list followed by all ints in the second."""
    result_list: list[int] = []

    for item in list_1:
        result_list.append(item)
    for item in list_2:
        result_list.append(item)
    
    return result_list