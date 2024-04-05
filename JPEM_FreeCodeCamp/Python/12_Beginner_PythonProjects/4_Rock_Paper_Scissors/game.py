import random

# definer rules: r > s, s > p, p > r

def play():
    user = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "tie"

    if win(user, computer):
        return f"{user} beats {computer} You win :)"

    return f"{computer} beats {user} You lose :("

def win(player, opponent):
    # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True

print(play())