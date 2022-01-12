from datetime import date


class Monkey:
    """class for Monkey"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

matt = Monkey("Matt", "Orangutan")
print(matt)

class Tiger:
    """class for Tiger"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

tim = Tiger("Tim", "Siberian Tiger")
print(tim)


class Bear:
    """class for Bear"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

benny = Bear("Benny", "Grizzly Bear")
print(benny)


class Lion:
    """class for Lion"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

leo = Lion("Leo", "Mountian Lion")
print(leo)


class Zebra:
    """class for Zebra"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

zach = Zebra("Zach", "Plains Zebra")
print(zach)
