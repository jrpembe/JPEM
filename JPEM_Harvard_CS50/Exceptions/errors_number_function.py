# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try: # try is a statement not a function
#              x = int(input("Enter an integer? "))
#         except ValueError:
#             print("That was not an integer.")
#         else:
#             return x

# main()


# same thing using pass statement

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try: # try is a statement not a function
#              return int(input("Enter an integer? "))
#         except ValueError:
#             pass

# main()


# third option 

def main():
    x = get_int("Enter and integer ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: # try is a statement not a function
             return int(input(prompt))
        except ValueError:
            pass

main()