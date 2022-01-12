from datetime import date

class Cobra:
    """class for Cobra"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

connie = Cobra("Connie", "King Cobra")
print(connie)


class Python:
    """class for Python"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

pete = Python("Pete", "Snake")
print(pete)


class Viper:
    """class for Viper"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

vicky = Viper("Vicky", "Pit Viper")
print(vicky)


class Gardner:
    """class for Gardner"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

gary = Gardner("Gary", "Gartner Snake")
print(gary)


class Anaconda:
    """class for Anaconda"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

andy = Anaconda("Andy", "Big Snake")
print(andy)
