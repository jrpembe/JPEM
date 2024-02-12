def power(number, pow=1):
    """Raise number to the power of pow"""
    new_value = number ** pow
    return new_value

power(9,2)


power(2,10)


#######################################################

def add_all(*args): # *args turns all arguments passed to sum_all into a tuple
    """Sum all values in (*args together)"""
    
    # Initialize sum
    sum_all = 0
    
    # Accumulate the sum
    for num in args:
        sum_all += num
        
    return sum_all

add_all(1,3,7)

#######################################################

# kwargs - keyword arguments, that is arguments preeded by identifiers

def print_all(**kwargs):
    """Print out all key-value pairs in **kwargs"""
    
    # Print out the key-value pairs
    for key, value in kwargs.items():
        print(key + ": " + value)
        
print_all(name = "Jason Pemberton", title = "Data Analyst")
        