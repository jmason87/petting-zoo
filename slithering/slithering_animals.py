from datetime import date

class Slitherers:
    """Parent Class for Snake Pit Animals"""
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

class Cobra(Slitherers):
    """class for Cobra"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Python(Slitherers):
    """class for Python"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Viper(Slitherers):
    """class for Viper"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Gardner(Slitherers):
    """class for Gardner"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Anaconda(Slitherers):
    """class for Anaconda"""

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
