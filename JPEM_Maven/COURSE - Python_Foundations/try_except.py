price_list = [5.99, None, 19.99, 24.99, 0, '74.99', 99.99]

# loop to calculate how many of each item I can buy

for price in price_list:
    try:
        affordability_quantity = 50//price # budget is 50
        print(f"I can buy {affordability_quantity} of these")
    except:
        print("The price is missing")