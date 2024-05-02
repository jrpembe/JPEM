filename = "file.txt"
file = open(filename, mode='r') # is "read only"

text = file.read()

file.close()

print(text)

# how to avoid forgetting to close the file using a 'with' statement
with open('file.txt', 'r') as file:
    print(file.read())

# 'with' is called a "context manager". You are binding a variable in a context manager construct.
# The file is automatically closed when you are finished
