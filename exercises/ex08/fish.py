"""File to define Fish class."""

__author__ = "730387751"


class Fish:
    """Class to represent a Fish."""

    age: int
    
    def __init__(self):
        """New Fish with age 0."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase age by 1."""
        self.age += 1
        return None