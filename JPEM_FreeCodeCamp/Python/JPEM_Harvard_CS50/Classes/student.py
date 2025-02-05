class Student:
    def __init__(self, name, house):    # implements the initialization method of an object
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name                # creating an instance variable
        self.house = house
    """Class allows you to define a custom container with a custom name that contains pieces of data.
    Whenever you use class, you are creating an Object (OOP)"""

    def __str__(self):
        return f"{self.name} from {self.house}"
        

def main():
    student = get_student()
    print(student)

# def get_student():
#     student = Student() # Constructor Call: creating an object from class
#     student.name = input("Name: ")  # .name is an attribute of student
#     student.house = input("House: ")  # .house is an attribute of student
#     return student

# alternatively
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # passing arguments to the Student class

# checks if the script is being run directly. If it is, then the main() 
# function (or any other code inside the conditional block) is executed. 
if __name__ == "__main__":
    main()