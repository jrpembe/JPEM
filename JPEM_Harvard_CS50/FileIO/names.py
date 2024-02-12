# names = []

# for _ in range(3):
#     #name = input("What is your name? ")
#     names.append(input("What is your name? "))
    
# for name in sorted(names):
#     print(f"Hello, {name}")
    
    
    
# open function
name = input("What is your name? ")

file = open("names.txt", "a") # w = write, a = append
file.write(f"{name}\n")
file.close
