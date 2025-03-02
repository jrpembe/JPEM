def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")

# This variable __name__ value is automatically set by python to "main" when you run a file from a command line
# when importing a file "main" will not get called by definition.

if __name__ == "__main__":  
    main()


