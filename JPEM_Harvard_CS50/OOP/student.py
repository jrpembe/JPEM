# def main():
#     # name = input("Name: ")
#     # house = input("House: ")
#     student = get_student()
#     # if student[0] == "Padma":  # doesn't work because we cannot change the contents of a tuple
#     #     student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")
    
# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# def get_student( ):
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house) # returns a tuple with two items rather than a list, more precise if you enclose in parenthesis



# alternative to get_student above
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student

    # or
    # name = input("Name: ")
    # house = input("House: ")
    # return {"name" : name, "house" : house}

if __name__ == "__main__":
    main()