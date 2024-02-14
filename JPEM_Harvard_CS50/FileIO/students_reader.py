import csv

students = []

# with open("students.csv") as file:
#   reader = csv.reader(file)
#   for name, home in reader:
#         students.append({"name": name, "home": home})

# for student in sorted(students, key=lambda student: student["name"]):
#   print(f"{student['name']} is in House {student['home']}")
        
        
# if the column names appear in the first row of the csv file
# we can replace csv.reader with csv.DictReader  as follows:

with open("students.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
  print(f"{student['name']} is in House {student['home']}")
        