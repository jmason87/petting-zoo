from datetime import date

class Walkers:
    """Parent Class for Petting Zoo Animals"""
    def __init__(self, name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.shift = shift
        self.food = food
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        """returns chip number"""
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass


class Monkey(Walkers):
    """class for Monkey"""
    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Tiger(Walkers):
    """class for Tiger"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Bear(Walkers):
    """class for Bear"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Lion(Walkers):
    """class for Lion"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Zebra(Walkers):
    """class for Zebra"""

    def feed(self):
        """tells you what the animal was fed on date"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"
