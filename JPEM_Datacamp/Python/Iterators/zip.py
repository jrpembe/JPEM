avengers = ['Hawkeye', 'Iron Man', 'Thor', 'Quicksilver']
names = ['Barton', 'Stark', 'Odison', 'Maximoff']

z = zip(avengers, names)
print(type(z))

z_list = list(z)
print(z_list)

for z1, z2 in zip(avengers, names):
    print(z1,z2)
    
    # alternatively using the splate operator
    
    print(*z)