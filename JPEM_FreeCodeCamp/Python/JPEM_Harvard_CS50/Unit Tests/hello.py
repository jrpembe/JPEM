def main():
    name = input("What's your name? ")
    print(hello(name))

    
def hello(to="World"):
    # print("Hello,", to) # print function does not return a value
    return f"Hello, {to}"

if __name__ == "__main__":
    main()  