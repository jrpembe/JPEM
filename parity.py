# Is a given number even or odd?

# number = int(input("Please enter a number: "))

# if number % 2 == 0:
#     print("Your number is even")
# else:
#     print("Your number is odd")

def main():
    number = int(input("Please enter a number: "))
    if is_even(number):
        print("Your number is even")
    else:
        print("Your number is odd")
        

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    
    # return True if n % 2 == 0 else False

    return (n % 2 == 0)
        
main()