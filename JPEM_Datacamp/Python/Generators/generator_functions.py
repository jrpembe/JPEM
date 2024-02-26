"""
Produce generator objects when called
Defined like a regular function
Yields a sequence of values instead of returning a single value
Generates a value with yield keyword
"""

def num_sequence(n):
    """Generate values from 0 to n"""
    i = 0
    while i < n:
        yield i 
        i += 1
        
result = num_sequence(5)
print(type(result))

for item in result:
    print(item)