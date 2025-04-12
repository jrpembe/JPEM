stock_portfolio = 200000
year_counter = 0

while stock_portfolio < 1000000:
    investment_income = stock_portfolio * 0.07
    stock_portfolio += investment_income
    year_counter += 1
    print(f"Year {year_counter}: ${stock_portfolio:.2f}")
    # break if I can not retire in 30 years
    if year_counter >= 30:
        print("You can't retire in 30 years.")
        break
