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
        



def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be equal to high
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"The computer guessed your number, {guess}, correctly")
        
    


guess(10)