# recall list comprehension
result1 = [2 ** num for num in range(10)]
print(result1)

"""
use () instead of [] to create a generator object
like a list comprehension except it does not store the list in memory
it is an object we can iterate over to produce elements of the list as required
helps when dealing with large sequence of numbers and you don't want to store them
in memory. It generates them on the fly
"""


result2 = (2 ** num for num in range(10))
# print(result2)

# for num in result2:
#     print(num)

# lazy evaluation
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
