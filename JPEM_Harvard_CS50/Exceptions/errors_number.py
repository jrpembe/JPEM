# try:
#     x = int(input("Enter an integer? "))
#     print(f"x is {x}")
# except ValueError:
#     print("That was not an integer. Try again")
    
# alternatively

# try:
#     x = int(input("Enter an integer? "))
# except ValueError:
#     print("That was not an integer.")
# else:
#     print(f"x is {x}")  

# alternatively

while True:
    try:
        x = int(input("Enter an integer? "))
    except ValueError:
        print("That was not an integer.")
    else:
        break

print(f"x is {x}") 
        
        