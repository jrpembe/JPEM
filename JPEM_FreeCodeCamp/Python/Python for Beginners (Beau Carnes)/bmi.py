# Body Mass Calculator Function
# bmi = weight(kg) / height(m) ^ 2

def bmi(weight, height):
    bmi = weight / height ** 2
    print(f"Your BMI is: {round(bmi, 2)}")

bmi(80, 1.72)


# def bmi(weights, heights):
#     for weight, height in zip(weights, heights):
#         bmi_value = weight / height ** 2
#         print(f"Your BMI is: {round(bmi_value, 2)}")

# weights = [82, 70, 95]
# heights = [1.7, 1.8, 1.75]

# bmi(weights, heights)

def total_cost(price, quantity, tax_rate):
    cost = price * quantity
    total = cost + (cost * tax_rate / 100)
    print(f"Total cost after tax: ${round(total, 2)}")

total_cost(50, 3, 5.5)