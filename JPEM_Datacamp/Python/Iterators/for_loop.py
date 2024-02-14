# Iterating over a list

employees = ['Nick', 'Jason', 'Steve']

for employee in sorted(employees):
    print(employee)
    

# Iterating over a string with splat
word = "gigantic"
it = iter(word)

print(*it) # splat

# Iterating over a dictionary
students = {'John' : 'Smith', 'Steve' : 'Nich'}

for key, value in students.items():
    print(key, value)

