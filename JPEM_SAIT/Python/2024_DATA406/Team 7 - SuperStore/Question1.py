import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # For formatting date labels

# Load data
data = pd.read_csv('C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 460/Potential FInal Projects/Superstore Sales/fact_superstore_clean.csv')  # Replace with actual file
data['order_date'] = pd.to_datetime(data['order_date'])
data['Order Month'] = data['order_date'].dt.to_period('M')

# Group by Order Month and sum profits across all categories
monthly_profit = data.groupby('Order Month')['profit'].sum().reset_index()

# Convert 'Order Month' to timestamp and set as index
monthly_profit['Order Month'] = monthly_profit['Order Month'].dt.to_timestamp()
monthly_profit.set_index('Order Month', inplace=True)

# Fit ARIMA model on total profit across all categories
model = SARIMAX(monthly_profit['profit'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
results = model.fit()

# Forecast
forecast = results.get_forecast(steps=12)
forecasted_values = forecast.predicted_mean
confidence_intervals = forecast.conf_int()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(monthly_profit.index, monthly_profit['profit'], label='Historical Profit')
plt.plot(forecasted_values.index, forecasted_values, label='Forecast', color='orange')
plt.fill_between(forecasted_values.index, confidence_intervals.iloc[:, 0], confidence_intervals.iloc[:, 1], color='lightgrey', alpha=0.5)

# Customize x-axis to reduce labels
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # Format as 'Month Year'
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))  # Show every third month
plt.xticks(rotation=45)  # Rotate for better readability

plt.legend()
plt.title('Monthly Profit Forecast (All Categories Combined)')
plt.xlabel('Month')  # Explicitly label the x-axis
plt.ylabel('Profit')  # Label the y-axis
plt.tight_layout()
plt.show()
