import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("Your guess is too low. Try again")
        elif guess > random_number:
            print("Your guess is too high. Try again")
            
    print(f"Congratulations, you guessed {random_number}, that was the random number!")
        

guess(10)