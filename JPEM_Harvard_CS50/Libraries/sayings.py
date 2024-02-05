def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")
    
if __name__ == "__main()__":  # This will prevent main from being called if this file is imported by another file
    main()

