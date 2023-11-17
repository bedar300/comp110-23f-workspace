"""File to define River class."""

__author__ = "730387751"


from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """Class to represent a River."""

    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove all Fish and Bears that are too old."""
        list_of_fish = []
        list_of_bears = []
        for fish in self.fish:
            if fish.age <= 3:
                list_of_fish.append(fish)  

        for bear in self.bears:    
            if bear.age <= 5:
                list_of_bears.append(bear)

        self.bears = list_of_bears
        self.fish = list_of_fish
        return None
    
    def remove_fish(self, amount: int):
        """Remove amount number of Fish from the river."""
        idx = 0
        amount = len(self.fish)
        while idx < amount and self.fish != []:
            self.fish.pop()
            idx += 1

        return None

    def bears_eating(self):
        """Have Bears eat fish if there are at least 5 fish in river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Remove all Bears that have a hunger_score < 0."""
        list_of_bears = []

        for bear in self.bears:
            if bear.hunger_score >= 0:
                list_of_bears.append(bear)

        self.bears = list_of_bears
        return None
        
    def repopulate_fish(self):
        """Have Fish reproduce if there are at least 2 Fish in river."""
        if len(self.fish) >= 2:
            num_of_new_fish: int = (len(self.fish) // 2) * 4
            while num_of_new_fish > 0:
                self.fish.append(Fish())
                num_of_new_fish -= 1
        return None
    
    def repopulate_bears(self):
        """Have Bears reproduce if there are at least 2 Bears in river."""
        if len(self.bears) >= 2:
            num_of_new_bears: int = len(self.bears) // 2
            while num_of_new_bears > 0:
                self.bears.append(Bear())
                num_of_new_bears -= 1       
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def view_river(self) -> None:
        """Print out the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_week(self):
        """Simulate one week of the river."""
        idx = 1
        while idx < 8:
            self.one_river_day()
            idx += 1
        return None