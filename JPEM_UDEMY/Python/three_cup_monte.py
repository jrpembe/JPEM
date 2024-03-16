# Creating the ball in three cups game. We will use a list to represent the random location of the ball
# rather than using visuals.

# how does the shuffle function work

# example = [1,2,3,4,5,6,7]
from random import shuffle

# shuffle(example)
# example

# you cannot save the results as the function does not 
# return anything. So we need to create our own shuffle function


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


# testing to see if it works
# result = shuffle_list(example)
# result

# mylist = [' ', 'O', ' ']
# shuffle_list(mylist)


def player_guess():
    """allow user to pick a number from 0, 1, or 2"""
    guess=''
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2: ")
        
    return int(guess)


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("You Win!")
    else:
        print("Wrong, the ball was under cup ", mylist)

# Initial List
mylist = [' ', 'O', ' ']
# Shuffle List
mixed_list = shuffle_list(mylist)
# User Guess
guess = player_guess()
# Check Guess
check_guess(mixed_list, guess)