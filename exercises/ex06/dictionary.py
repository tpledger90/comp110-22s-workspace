"""File containing methods to practice complex uses of dictionaries."""

__author__ = "730477982"


def invert(main_dict: dict[str, str]) -> dict[str, str]:
    """Reverses the order of the key and key-value, and returns back the inverted dictionary."""
    invert_dict: dict[str, str] = dict()

    for key in main_dict:
        invert_dict[main_dict[key]] = key
    
    for key in invert_dict:
        for check in invert_dict:
            if key == 

    return invert_dict


def favorite_color(fav_colors: dict[str, str]) -> str:
    """Finds the most common favorite color among a dictionary that has a name and a favorite color respectively."""
    fav_color: str = ""
    color_counts: dict[str, int] = {}

    # creates a new dict that has each unique color and its count
    for key in fav_colors:
        if fav_colors[key] in color_counts:
            color_counts[fav_colors[key]] += 1
        else:
            color_counts[fav_colors[key]] = 1
    
    # assigns the fav_color to the first key in the color_counts
    fav_color = next(iter(color_counts))

    for key in color_counts:
        if color_counts[key] > color_counts[fav_color]:
            fav_color = key
    
    return fav_color


def count(main_list: list[str]) -> dict[str, int]:
    """Counts the number of times any given string appears in a list and return a dict with a string and the number of time it appears in the list."""
    counts: dict[str, int] = {}

    for key in main_list:
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    
    return counts