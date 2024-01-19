name = "Jason"

print("Hello " + name)

number = 7

guess = int(input("Pick a number between 1 and 10: "))

if guess > number:
    print("Too High")
elif guess < number:
    print("Too Low")
else:
    print("Good Guess!")