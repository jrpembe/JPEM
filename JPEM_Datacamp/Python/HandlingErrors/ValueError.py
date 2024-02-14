def sqrt(x):
    """Returns the square root of a number"""
    if x < 0:
        raise ValueError('X must be non-negative')
    try:
        return x ** 0.5
    except TypeError:
        print('x must be int or float')
        
sqrt('two')
