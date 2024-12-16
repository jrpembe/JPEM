import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Load the dataset
data = pd.read_csv('C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 460/Potential FInal Projects/Superstore Sales/fact_superstore_clean.csv')

# Assuming 'Order Date' is in the data and renaming to 'order_date'
data['order_date'] = pd.to_datetime(data['order_date'])

# Set the data as index
data.set_index('order_date', inplace=True)

# Filter for profits and customer segments
profit_data = data[['profit', 'segment']].copy()

# Calculate total profit per segment for 2023 (assuming '2023' is the last year in your data)
total_profit_by_segment = profit_data.groupby('segment')['profit'].sum()

# Set target profit as 10% increase from the total profit in 2023
total_2023_profit = total_profit_by_segment.sum()  # Total profit across all segments
target_profit = total_2023_profit * 1.10  # Target profit is a 10% increase

# Debugging: Print out the target profit
print(f"Total profit in 2023: {total_2023_profit}")
print(f"Target profit (10% increase): {target_profit}")

# Forecasting for each segment
forecasted_contributions = []

for segment in total_profit_by_segment.index:
    # Filter data for the specific segment
    segment_data = profit_data[profit_data['segment'] == segment]
    
    # Fit SARIMAX model for each segment
    model = SARIMAX(segment_data['profit'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    results = model.fit()
    
    # Forecast the next 12 months
    forecast = results.get_forecast(steps=12)
    forecasted_values = forecast.predicted_mean.sum()  # Sum of forecasted profit for next 12 months
    
    # Calculate contribution to the 10% increase goal
    segment_contribution = forecasted_values / target_profit * 100
    
    # Append results to the list
    forecasted_contributions.append({
        'segment': segment,
        'forecasted_profit': forecasted_values,
        'contribution_to_target': segment_contribution
    })

# Convert the results into a DataFrame
forecast_df = pd.DataFrame(forecasted_contributions)

# Display results
print(forecast_df)

# Optionally, you can visualize the contribution with a bar chart
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(forecast_df['segment'], forecast_df['contribution_to_target'], color='skyblue')
plt.xlabel('Customer Segment')
plt.ylabel('Contribution to 10% Increase in Profit (%)')
plt.title('Contribution of Each Segment to 10% Increase in Profit')
plt.tight_layout()
plt.show()
