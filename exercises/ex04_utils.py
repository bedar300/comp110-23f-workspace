"""Exercise 4!"""

__author__ = '730387751'


def all(list: list[int], number: int) -> bool:
    """Return true if all numbers in list are equal to number."""
    if len(list) == 0:
        return False
    idx = 0
    while idx < len(list):
        if list[idx] != number:
            return False
        idx += 1
    return True  # If we get here then all numbers in list are equal to number


def max(input: list[int]) -> int:
    """Return the maximum number in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx = 0
    max_num = input[idx]
    while idx < len(input):
        if input[idx] > max_num:
            max_num = input[idx]
        idx += 1
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if every int in each list is the same."""
    if len(list1) != len(list2):
        return False
    idx = 0
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False
        idx += 1
    return True  # If we get here then all numbers in list are equal to number