"""Combining two lists into a dictionary!"""

__author__ = "730387751"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Combines two lists into a dictionary."""
    i = 0
    dictionary: dict[str, int] = {}
    for i in range(len(list1)):
        if len(list1) != len(list2):
            return {}
        else: 
            dictionary[list1[i]] = list2[i]
    return dictionary
