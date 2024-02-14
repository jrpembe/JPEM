# names = []

# for _ in range(3):
#     #name = input("What is your name? ")
#     names.append(input("What is your name? "))
    
# for name in sorted(names):
#     print(f"Hello, {name}")
    
    
    
# open function
# name = input("What is your name? ")

# file = open("names.txt", "a") # w = write, a = append
# file.write(f"{name}\n")
# file.close


# with statement (open and automatically close)
name = input("What is your name? ")

with open("names.txt", "a") as file:# w = write, a = append
    file.write(f"{name}\n")
    
with open("names.txt", "r") as file:  # Corrected line
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())  # Corrected line, using strip() to remove trailing newline characters
    
# Alternatively

# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello, ", line.rstrip())





