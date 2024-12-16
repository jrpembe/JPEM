import pandas as pd

# Load the dataset
data = pd.read_csv('C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 460/Potential FInal Projects/Superstore Sales/fact_superstore_clean.csv')

# Grouping the data by Customer Segment and aggregating Sales and Profit
segment_profit_sales = data.groupby('segment').agg(
    total_sales=('sales', 'sum'),
    total_profit=('profit', 'sum')
).reset_index()

# Calculate the target profit (20% increase)
segment_profit_sales['target_profit'] = segment_profit_sales['total_profit'] * 1.20

# Calculate the contribution to the 20% profit increase
segment_profit_sales['contribution_to_increase'] = segment_profit_sales['target_profit'] - segment_profit_sales['total_profit']

# Sort by contribution to the 20% increase in profit (descending order)
segment_profit_sales = segment_profit_sales.sort_values(by='contribution_to_increase', ascending=False)

# Display the results
print(segment_profit_sales[['segment', 'total_profit', 'target_profit', 'contribution_to_increase']])

# If you want to visualize it, you can use matplotlib or seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Plotting the contribution to the 20% profit increase by segment
plt.figure(figsize=(10, 6))
sns.barplot(x='contribution_to_increase', y='segment', data=segment_profit_sales, palette='viridis')
plt.title('Contribution to 20% Profit Increase by Customer Segment')
plt.xlabel('Contribution to 20% Profit Increase')
plt.ylabel('Customer Segment')
plt.tight_layout()
plt.show()
