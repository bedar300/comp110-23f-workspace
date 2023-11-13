"""Dictionary for exercise 06!"""

__author__ = "730387751"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    invert_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in invert_dict:
            raise KeyError("Duplicate key found!")
        else:
            invert_dict[dictionary[key]] = key
    return invert_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color that is the most frequent."""
    # Initilaize empty dictionary and variables
    color_count: dict[str, int] = {}
    current_max: int = 0
    color: str = ""
    # Create new dictionary of colors and their counts
    for key in dictionary:
        if dictionary[key] in color_count:
            color_count[dictionary[key]] += 1
        else: 
            color_count[dictionary[key]] = 1
    # Find the color with the highest count
    for key in color_count:
        if color_count[key] > current_max:
            current_max = color_count[key]
            color = key
        elif color_count[key] == current_max:
            color = color
    return color


def count(list: list[str]) -> dict[str, int]:
    """Counts the number of times the value appeared in list."""
    # Initialize empty dictionary
    count_dict: dict[str, int] = {}
    # Iterate through list and count the number of times the value appeared
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizes a list of strings."""
    # Initialize empty dictionary
    alpha_dict: dict[str, list[str]] = {}
    # Iterate through list and alphabetize the strings
    for item in words:
        # Check to see if the first letter is in the dictionary
        item = item.lower()
        if item[0] in alpha_dict:  # If it is, add it to the list
            alpha_dict[item[0]].append(item)
        else:  # If not, add it to the dictionary
            alpha_dict[item[0]] = [item]
    return alpha_dict


def update_attendance(roster: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Create dict with which students attended each day."""
    # Check to see if the day is in the roster
    if day in roster:  # Check if day is in roster
        # Check to see if student is in day already
        if student not in roster[day]:  # If not, add the student to the day
            roster[day].append(student)
    else:  # If not, add the day and student to the roster
        roster[day] = [student]
    return roster
       