nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: num ** 2, nums)

print(square_all) # square_all is a map object

print(list(square_all))


def square_numbers(nums):
    return [num ** 2 for num in nums]

squared_nums = square_numbers(nums)
print(squared_nums)