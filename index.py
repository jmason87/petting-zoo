from slithering import Cobra, Python, Viper, Gardner, Anaconda
from swimming import Turtle, Dolphin, Shark, Crab, Whale
from walking import Monkey, Bear, Tiger, Lion, Zebra
from attractions import PettingZoo, Wetlands, SnakePit

east_wing = Wetlands("East Wing", "A place for water creatures")
north_wing = PettingZoo("North Wing", "A place for land critters")
south_wing = SnakePit("South Wing", "A place for snakes and stuff")

connie = Cobra("Connie", "King Cobra", "animalFood")

pete = Python("Pete", "Snake", "animalFood")

vicky = Viper("Vicky", "Pit Viper", "animalFood")

gary = Gardner("Gary", "Gartner Snake", "animalFood")

andy = Anaconda("Andy", "Big Snake", "animalFood")

tom = Turtle("Tom", "Snapping Turtle", "animalFood")
print(tom.feed())

dorris = Dolphin("Dorris", "Bottlenose Dolphin", "animalFood")
print(dorris.feed())

sam = Shark("Sam", "Great White", "animalFood")
print(sam.feed())

corey = Crab("Corey", "King Crab", "animalFood")
print(corey.feed())

wally = Whale("Wally", "Blue Whale", "animalFood")
print(wally.feed())

matt = Monkey("Matt", "Orangutan", "Morning", "animalFood", 1)
matt.chip_number = 321321
print(matt.chip_number)

tim = Tiger("Tim", "Siberian Tiger", "Morning", "animalFood", 2)

benny = Bear("Benny", "Grizzly Bear", "Midday", "animalFood", 3)

leo = Lion("Leo", "Mountian Lion", "Afternoon", "animalFood", 4)

zach = Zebra("Zach", "Plains Zebra", "Afternoon", "animalFood", 5)

north_wing.animals.append(zach)
north_wing.animals.append(leo)
north_wing.add_animal(benny)
north_wing.add_animal(matt)
north_wing.add_animal(tim)

east_wing.add_animal(tom)
east_wing.add_animal(dorris)
east_wing.add_animal(sam)
east_wing.add_animal(corey)
east_wing.add_animal(wally)

south_wing.add_animal(connie)
south_wing.add_animal(pete)
south_wing.add_animal(vicky)
south_wing.add_animal(gary)
south_wing.add_animal(andy)




# print(f"{north_wing.attraction_name} is where you'll find animals like:")
# for animal in north_wing.animals:
#     print(f"  * {animal.name} the {animal.species}")

# print(f"{east_wing.attraction_name} is where you'll find animals like:")
# for animal in east_wing.animals:
#     print(f"  * {animal.name} the {animal.species}")

# print(f"{south_wing.attraction_name} is where you'll find animals like:")
# for animal in south_wing.animals:
#     print(f"  * {animal.name} the {animal.species}")
    