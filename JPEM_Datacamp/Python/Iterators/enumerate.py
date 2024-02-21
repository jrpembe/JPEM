avengers = ['Hawkeye', 'Iron Man', 'Thor', 'Quicksilver']
e = enumerate(avengers)

print(type(e))

e_list = list(e)

e_list

for index, value in enumerate(avengers, start=1):  # start specifies which index number to begin with
    print(index, value)