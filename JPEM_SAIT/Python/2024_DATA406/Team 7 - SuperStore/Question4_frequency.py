import pandas as pd

# Load your dataset
data = pd.read_csv('C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 460/Potential FInal Projects/Superstore Sales/fact_superstore_clean.csv')

# Convert 'Order Date' to datetime for easier manipulation
data['order_date'] = pd.to_datetime(data['order_date'])

# Extract customer ID and order frequency
customer_frequency = data.groupby('customer_id')['order_date'].nunique().reset_index()

# Rename columns for clarity
customer_frequency.columns = ['customer_id', 'frequency_of_purchases']

# Save the results to a CSV file for import into Power BI
customer_frequency.to_csv('customer_frequency.csv', index=False)

# Display results
print(customer_frequency.head())
