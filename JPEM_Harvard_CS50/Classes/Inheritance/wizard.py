
# define third class Wizard, that has common attributes of Students and Professors
# then remove redundancies from the Student and Professor classes
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name 

    ...

class Student(Wizard):  # When you define a Student class it inherits all the attributes of Wizard
    def __init__(self, name, house):
        super().__init__(name)
        # if not name:
        #     raise ValueError("Missing name")
        # self.name = name
        self.house = house
        
    ...
    
class Professor(Wizard):    # When you define a Professor class it inherits all the attributes of Wizard
    def __init__(self, name, subject):
        super().__init__(name)
        # if not name:
        #     raise ValueError("Missing name")
        # self.name = name
        self.subject = subject
        
    ...
    
wizard = Wizard("Albus") # calls init method of Wizard class
student = Student("Harry", "Gryffindor") # calls init method of Student class and Wizard class
professor = Professor("Severus", "Defense Against the Dark Arts") # calls init method of Professor class and Wizard class

