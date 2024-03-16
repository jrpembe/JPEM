def myfunc(a,b):
    # return 5% of sum of a and b
    return sum((a,b)) * 0.05

myfunc(2,3)

# If the user wants to input an arbitrary number of arguments we can use *args which returns a tuple
# the word args isn't necessary, you cana use any word you want but it is best practice
# to use args

def myfunc2(*args):
    return sum(args) * 0.05

myfunc2(200,10,30,50,100)

# key word arguments **kwargs - returns a dictionary

def myfunc3(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("I didn't find any fruit in here")
        
        
myfunc3(fruit = 'apple', vegetable = 'carrot')

# args and kwargs in combination
def myfunc4(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0],kwargs['food']))

myfunc4(10,20,30,40,50, fruit='orange', food='pizzas', animal='dog')
