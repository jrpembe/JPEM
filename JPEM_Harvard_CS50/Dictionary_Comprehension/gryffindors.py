# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"}
#     ]

students = ["Hermione", "Harry", "ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house" : "Gryffindor"})
    
# print(gryffindors)


# alternative 
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)

# dictionary comprehension

gryffindors = {student: "Gryffindor" for student in students}

print(gryffindors)