class Dog():
    
    def __init__(self, breed, name, age, spots):
        
        self.breed = breed # Expecting a string
        self.name = name # Expecting a string
        self.age = age # Expecting a number
        self.spots = spots # Expecting a binary response
        
my_dog = Dog(breed="Golden Retriever", name="Finnigan",age=12 ,spots=False)

my_dog.breed
my_dog.name
my_dog.age
my_dog.spots