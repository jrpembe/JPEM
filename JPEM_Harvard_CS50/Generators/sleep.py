def main():
    n = int(input("What is n?"))
    for s in sheep(n):
        print(s)

"""
this helper function is great for small numbers but at larger "n" this can excede your computers memory
we can define a function as a generator to avoid this. The generator wil lreturn a little bit of data at a time
to do this we need "yield" instead of "return"
"""

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("sheep" * i) 
    return flock

if __name__ == "__main__":
    main()
    
