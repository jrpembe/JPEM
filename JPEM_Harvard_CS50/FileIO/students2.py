import csv

name = input("What's your name? ")
home = input("Where is your home? ")

# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

with open("students.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name":name, "home": home})