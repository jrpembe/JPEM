import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Ensure numbers are not displayed in scientific notation for NumPy
np.set_printoptions(suppress=True)

# Set Pandas display options to avoid scientific notation
pd.set_option('display.float_format', '{:.2f}'.format)

# Data points
prices = np.array([15, 20], dtype=float)  # Prices at $15 and $20
subscriptions = np.array([1500, 1000], dtype=float)  # Corresponding subscriptions
unit_cost = 9.0  # Unit cost is $9

# Perform linear regression to find the demand equation
coefficients = np.polyfit(prices, subscriptions, 1)  # Degree 1 polynomial (linear)
slope = coefficients[0]
intercept = coefficients[1]
print(f"Slope (m): {slope}")
print(f"Intercept (b): {intercept}")

# Demand equation
# Subscriptions = slope * Price + intercept

# Profit function
def profit_function(price):
    subscriptions = slope * price + intercept
    # Ensure subscriptions cannot be negative
    subscriptions = max(subscriptions, 0)
    profit = (price - unit_cost) * subscriptions
    return profit

# Generate a range of prices for plotting
price_range = np.linspace(10, 30, 200)
profits = [profit_function(p) for p in price_range]

# Plotting Profit vs. Price
plt.figure(figsize=(10, 6))
plt.plot(price_range, profits, label='Profit')
plt.title('Profit vs. Price')
plt.xlabel('Price ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.legend()
plt.show()

# Optimization to find the optimal price
def objective(price):
    return -profit_function(price)

bounds = (0, 30)
result = minimize_scalar(objective, bounds=bounds, method='bounded')
optimal_price = result.x
max_profit = -result.fun
print(f"Optimal Price: ${optimal_price:.2f}")
print(f"Maximum Profit: ${max_profit:.2f}")

# Verify subscriptions at optimal price
optimal_subscriptions = slope * optimal_price + intercept
optimal_subscriptions = max(optimal_subscriptions, 0)
print(f"Subscriptions at Optimal Price: {optimal_subscriptions:.0f}")

# Recalculate profit to double-check
calculated_profit = (optimal_price - unit_cost) * optimal_subscriptions
print(f"Calculated Profit: ${calculated_profit:.2f}")

# Plotting the optimal point
plt.figure(figsize=(10, 6))
plt.plot(price_range, profits, label='Profit Curve')
plt.plot(optimal_price, max_profit, 'ro', label='Optimal Point')
plt.title('Profit vs. Price with Optimal Point')
plt.xlabel('Price ($)')
plt.ylabel('Profit ($)')
plt.grid(True)
plt.legend()
plt.show()

# Create DataFrame of profits at different prices
price_points = np.arange(10, 31, 1)
profit_points = [profit_function(p) for p in price_points]
subscriptions_points = [max(slope * p + intercept, 0) for p in price_points]

# Create DataFrame
data = {
    'Price ($)': price_points,
    'Subscriptions': subscriptions_points,
    'Profit ($)': profit_points
}

df = pd.DataFrame(data)
print(df.to_string(index=False))