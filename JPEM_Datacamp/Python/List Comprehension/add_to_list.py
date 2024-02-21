nums = [12, 8, 21, 3, 16]

new_nums = []

for num in nums:
    new_nums.append(num + 1)
print(new_nums)

# Alternatively using list comprehension

new_nums2 = [num + 1 for num in nums]
print(new_nums2)

# Nested loops

pairs_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))
print(pairs_1)

# Alternatively using list comprehension

paris_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(paris_2)

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
docs = [doc[0] for doc in doctor]
print(docs)
