# def main():
#     print_column(3)
    
# def print_column(height):
#     for _ in range(height):
#         print("#\n" * height, end="")

# main()


# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)
    
# main()


# Using Nested For Loops

# def main():
#     print_square(3)
    
# def print_square(size):
#     for i in range(size): # For each row in square
#         for j in range(size): # For each brick in row
#             print("#", end="") # Print brick
#         print()
    
# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size): # For each row in square
        print_row(size)
        
def print_row(width):
    print("#" * width)

main()