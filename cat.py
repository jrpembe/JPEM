# i = 3

# while i != 0:
#     print("meow")
#     i -= 1

# print("meow\n" * 3, end="")


# for i in range(3):
# print("meow")
    


# # use _ in place of the un-used i variable
    
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#        break

# for i in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(3)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
    
def meow(n):
    for _ in range(n):
        print("meow")

main()
