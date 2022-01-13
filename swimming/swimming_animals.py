from datetime import date
class Swimmers:
    """Parent Class for Wetlands Animals"""
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Turtle(Swimmers):
    """class for Turtle"""
    def feed(self):
        print(f'{self.name} was fed a double of {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Dolphin(Swimmers):
    """class for Dolphin"""

class Shark(Swimmers):
    """class for Shark"""

class Crab(Swimmers):
    """class for Crab"""

class Whale(Swimmers):
    """class for Whale"""
