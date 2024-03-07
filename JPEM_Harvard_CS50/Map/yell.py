def main():
    # yell(["This", "is", "CS50"]) # we will unpack later in the yell function
    yell("This", "is", "CS50")
    
#def yell(words):
def yell(*words):
    #print(phrase.upper())
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased) # unpack uppercased
    
    
if __name__ == "__main__":
    main()
    
