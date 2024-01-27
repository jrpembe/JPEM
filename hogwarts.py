# LISTS: Using [] Square Brackets
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# for student in students:
#     print(student)
    

for i in range(len(students)):
    print(i+1, students[i])
    

# DICTIONARIES: Using {} Curly Brackets - {key1 : value1, key2 : value2, ... key_n : value_n}
# When using a for loop to itterate over a dictionary it prints out the keys

students_house = {
    "Hermione" : "Gryffindor",
    "Harry": "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
    }

for student in students_house:
    print(student, students_house[student], sep=", ")

# Student House Patronus List (square brackets) that contains a dictionary (curly brackets)
student_house_pet = [
    {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for student in student_house_pet:
    print(student["name"], student["house"], student["patronus"], sep=", ")