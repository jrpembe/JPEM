balance = 0 # global variable that can't be changed

"""need to inform the two functions below main (deposit and withdraw) 
that the variable balance is global and can be changed. We do this by
adding the line 'global balance' to each function"""

def main():
    # balance = 0  # local variable
    print("Balance: $", balance)
    deposit(100)
    withdraw(50)
    print("Balance: $", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n    


if __name__ == "__main__":
    main()