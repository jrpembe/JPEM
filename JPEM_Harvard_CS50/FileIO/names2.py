names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
    
    
# alternatively

# with open("names.txt") as file:
#     for line in sorted(file):
#         names.append(line.rstrip())