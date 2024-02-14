# LEGB Rule
# Local Scope
# Enclosing Functions
# Global
# Built-In

def mod2plus5(x1, x2, x3):
    """Returns the remainder plus 5 of three variables"""
    
    def inner(x):
        """Returns the remainder plus 5 of a value"""
        return x % 2 + 5
    
    return (inner(x1), inner(x2), inner(x3))

print(mod2plus5(1, 2, 3))

#################################################################

def rasied_val(n):
    """Return the inner function"""
    
    def inner(x):
        """Rasied to the power of n"""
        raised = x ** n
        return raised
    
    return inner

square = rasied_val(2)
cube = rasied_val(3)

print(square(2), cube(4))

#################################################################

def outer():
    """Prints the value of n"""
    n = 1
    
    def inner():
        nonlocal n
        n = 2
        print(n)
        
    inner()
    print(n)

outer()