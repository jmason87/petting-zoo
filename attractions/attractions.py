class Attractions:
    """Parent Class for all the attractions"""
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    @property
    def last_critter_added(self):
        """Gets [x] index for animals.lst"""
        return f'{self.animals[-2]}'

    def add_animal(self, animal):
        """adds animal to animals.list"""
        self.animals.append(animal)


class PettingZoo(Attractions):
    """Class for Petting Zoo"""
class Wetlands(Attractions):
    """class for WetLands"""
class SnakePit(Attractions):
    """class for SnakePit"""
