def main():
    yell("This", "is", "CS50")


# using list comprehension
def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()