import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load your dataset
data = pd.read_csv('C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 460/Potential FInal Projects/Superstore Sales/fact_superstore_clean.csv')

# Convert 'Order Date' to datetime for easier manipulation
data['order_date'] = pd.to_datetime(data['order_date'])

# Step 1: Calculate Frequency of Purchases
customer_frequency = data.groupby('customer_id')['order_date'].nunique().reset_index()
customer_frequency.columns = ['customer_id', 'frequency_of_purchases']

# Step 2: Add Total Sales and Total Profit per Customer
customer_sales = data.groupby('customer_id')['sales'].sum().reset_index()
customer_sales.columns = ['customer_id', 'total_sales']

customer_profit = data.groupby('customer_id')['profit'].sum().reset_index()
customer_profit.columns = ['customer_id', 'total_profit']

# Merge all metrics into one DataFrame
customer_data = customer_frequency.merge(customer_sales, on='customer_id').merge(customer_profit, on='customer_id')

# Step 3: Normalize Features for Clustering
scaler = StandardScaler()
normalized_features = scaler.fit_transform(customer_data[['frequency_of_purchases', 'total_sales', 'total_profit']])

# Step 4: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
customer_data['cluster'] = kmeans.fit_predict(normalized_features)

# Save the clustered data for Power BI
customer_data.to_csv('customer_segments.csv', index=False)

# Display results for verification
print(customer_data.head())
