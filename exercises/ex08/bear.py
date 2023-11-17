"""File to define Bear class."""

__author__ = "730387751"


class Bear:
    """Class to represent a Bear."""

    age: int 
    hunger_score: int
    
    def __init__(self):
        """New Bear with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Increase age by 1 and decrease hunger_score by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Increase hunger_score by num_fish."""
        self.hunger_score += num_fish
        return None