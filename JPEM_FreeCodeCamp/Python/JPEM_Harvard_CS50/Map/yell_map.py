def main():
    yell("This", "is", "CS50")

# using mapping
def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()