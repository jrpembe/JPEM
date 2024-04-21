for i in range (1,13):
    print("{0} squared is {1} and cubed is {2}".format(i, i**2, i**3))


# formatted to look better
for i in range (1,13):
    print("{0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))


# formatted to look better left aligned
for i in range (1,13):
    print("{0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))