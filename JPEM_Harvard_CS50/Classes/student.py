class Student:
    def __init__(self, name, house):    # implements the initialization of an object
        self.name = name    
        self.house = house
    """Class allows you to define a custom container with a custom name that contains pieces of data.
    Whenever you use class, you are creating an Object (OOP)"""

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student() # Constructor Call: creating an object from class
    student.name = input("Name: ")  # .name is an attribute of student
    student.house = input("House: ")  # .house is an attribute of student
    return student

    # alternatively
    # def get_student():
    #   name = input("Name: ")
    #   house = input("House: ")
    #   student = Student(name, house) # passing arguments to the Student class
    #   return student

if __name__ == "__main__":
    main()