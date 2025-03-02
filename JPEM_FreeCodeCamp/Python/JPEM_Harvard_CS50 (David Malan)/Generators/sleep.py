def main():
    n = int(input("What is n?"))
    for s in sheep(n):
        print(s)

"""
this helper function is great for small numbers, but at larger "n" this can excede your computer's memory.
We can define a function as a generator to avoid this. The generator will return a little bit of data at a time
to do this we need "yield" instead of "return"
"""

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("sheep" * i) 
#     return flock


# alternatively using yield
""" "yield" returns one value for you for each iteration (each value of i), rather than "return" which runs the whole process before returning anything"""

def sheep(n):
    for i in range(n):
        yield "sheep" * i

if __name__ == "__main__":
    main()