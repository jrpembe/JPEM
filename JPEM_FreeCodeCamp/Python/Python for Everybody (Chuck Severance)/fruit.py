# indexing through strings


fruit = "banana"

for letter in fruit:
    print(letter)

# TO accomplish the same result with a while loop:

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1
    
# The "for" loop is simpler and less prone to mistakes

# Looping and counting

word = "avocado"
count = 0
for letter in word:
    if letter == "a" or letter == "o":
        count += 1
print(count)

