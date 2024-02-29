class Student:
    def __init__(self, name, house, patronus):    # implements the initialization mthod of an object
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name                # creating an instance variable
        self.house = house
        self.patronus = patronus
        
    """Class allows you to define a custom container with a custom name that contains pieces of data.
    Whenever you use class, you are creating an Object (OOP). By defining these inside the class, they are called methods"""
    
    def __str__(self):
        return f"{self.name} from {self.house}"   
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "(horse)"
            case "Otter":
                return "(otter)"
            case "Jack Russell terrier":
                return "(dog)"
            case _:
                return "wand"
        

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # passing arguments to the Student class



if __name__ == "__main__":
    main()