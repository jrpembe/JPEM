# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",") # strip any whitespace, then split using comma delimiter
#         print(f"{name} is in House {house}")
        
        

# Alternative

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # define dictionary items
        students.append(student)

# sorting a list of dictionaries
# specify what key should be used to srot the list of dictionaries

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name, reverse=True): # sort by house, replace get_name with get_house, and change function name to get_house, and "name" to "house"
    print(f"{student['name']} is in House {student['house']}")      

# Shorter, alternative version

# get rid of defining function chunk
# lambda is an anonymous function and can be used as many times as you wish
# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in House {student['house']}")
        