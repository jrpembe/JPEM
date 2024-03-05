students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"}
]
# the long way of printing out the unique house names in this list of dictionaries
# houses = []

# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
        
# for house in sorted(houses):
#     print(house)
    
# a more efficient way
houses2 = set()

for student in students:
    houses2.add(student["house"])
    
for house in sorted(houses2):
    print(house)
    

