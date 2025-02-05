# first, last = input("What is your name? ").split(" ")

# print(f"Hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

# print(total(100, 50, 25), "Knuts")

print(total(coins[0], coins[1], coins[2]), "Knuts")

# print(total(coins), "Knuts") will produce an error since everything in coins will be passed to galleons as a list

# unpacking
print(total(*coins), "Knuts") # for lists, use one asterick * to unpack


# Alternatively

coins2 = {"galleons" : 100, "sickles" : 50, "knuts" : 25}

print(total(coins2["galleons"], coins2["sickles"], coins2["knuts"]), "Knuts")
print(total(**coins2), "Knuts") # for dictionaries, use two astericks ** to unpack


# Using arguments

def f(*args, **kwargs):  # positional arguments then named arguments
    print("Named:", kwargs)
    
#  f(100, 50, 25) # for args
f(galleons=100, sickles=50, knuts=25)


