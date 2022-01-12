from datetime import date

class Turtle:
    """class for Turtle"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

tom = Turtle("Tom", "Snapping Turtle")
print(tom.swimming)


class Dolphin:
    """class for Dolphin"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

dorris = Dolphin("Dorris", "Bottlenose Dolphin")
print(dorris)


class Shark:
    """class for Shark"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

sam = Shark("Sam", "Great White")
print(sam)

class Crab:
    """class for Crab"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

corey = Crab("Corey", "King Crab")
print(corey)

class Whale:
    """class for Whale"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

wally = Whale("Wally", "Blue Whale")
print(wally)
