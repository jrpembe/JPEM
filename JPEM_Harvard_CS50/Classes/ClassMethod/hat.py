import random

class Hat:
    #def __init__(self): # this line is not necessary, instead simply create a "house" class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"] # removed self. This list can now be used in any function

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
#hat = Hat() #instantiating a hat object ,not needed when we define cls.houses
Hat.sort("Harry")

