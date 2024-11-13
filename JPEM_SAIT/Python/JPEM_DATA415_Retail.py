import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker and set random seed for reproducibility
fake = Faker()
np.random.seed(42)

# Customer Demographics Table
n_customers = 1000
customer_data = {
    "Customer_ID": range(1, n_customers + 1),
    "Age": np.random.randint(18, 80, size=n_customers),
    "Gender": np.random.choice(["Male", "Female"], size=n_customers),
    "Income": np.random.choice(["Low", "Medium", "High"], size=n_customers),
    "Region": np.random.choice(["North", "South", "East", "West"], size=n_customers),
    "Marital_Status": np.random.choice(["Single", "Married", "Divorced"], size=n_customers),
    "Distance_to_Store": np.round(np.random.uniform(0.5, 50, size=n_customers), 2)
}

# Create Base Spending based on marital status, gender, age, income, and distance, with controlled noise for correlation.
age_effect = np.where((customer_data["Age"] >= 30) & (customer_data["Age"] <= 60), 1.2, 0.9)
gender_effect = np.where(customer_data["Gender"] == "Female", 1.3, 1.0)
marital_status_effect = np.where(customer_data["Marital_Status"] == "Married", 1.4,
                                np.where(customer_data["Marital_Status"] == "Divorced", 1.2, 0.8))
income_effect = np.where(customer_data["Income"] == "High", 1.5,
                         np.where(customer_data["Income"] == "Medium", 1.0, 0.7))
distance_effect = 1 + (customer_data["Distance_to_Store"] / 100)  # Farther increases spending

# Stronger correlation controls
base_spending = 2000 + (1500 * age_effect * gender_effect * marital_status_effect * income_effect * distance_effect)
customer_data["Annual_Spending"] = np.round(base_spending + np.random.normal(0, 300, size=n_customers), 2)

customer_df = pd.DataFrame(customer_data)

# Product Details Table
n_products = 200
product_data = {
    "Product_ID": range(1, n_products + 1),
    "Category": np.random.choice(["Electronics", "Apparel", "Groceries", "Home", "Sports"], size=n_products),
    "Brand": [fake.company() for _ in range(n_products)],
    "Price": np.round(np.random.uniform(5, 500, size=n_products), 2),
    "Discount": np.round(np.random.uniform(0, 30, size=n_products), 2)
}
product_df = pd.DataFrame(product_data)

# Store Information Table
n_stores = 50
store_data = {
    "Store_ID": range(1, n_stores + 1),
    "Location": [fake.city() for _ in range(n_stores)],
    "Store_Size": np.random.choice(["Small", "Medium", "Large"], size=n_stores),
    "Store_Type": np.random.choice(["Supermarket", "Department Store", "Specialty Store"], size=n_stores),
    "Monthly_Sales": np.round(np.random.uniform(20000, 200000, size=n_stores), 2),
    "Foot_Traffic": np.random.randint(100, 1000, size=n_stores)
}
store_df = pd.DataFrame(store_data)

# Generate Transaction Data Table with boosted correlation controls
n_transactions = 50000
start_date = datetime(2021, 1, 1)
end_date = datetime(2024, 11, 12)
date_range = (end_date - start_date).days

transaction_data = {
    "Transaction_ID": range(1, n_transactions + 1),
    "Customer_ID": np.random.choice(customer_df["Customer_ID"], size=n_transactions),
    "Product_ID": np.random.choice(product_df["Product_ID"], size=n_transactions),
    "Store_ID": np.random.choice(store_df["Store_ID"], size=n_transactions),
    "Date": [start_date + timedelta(days=np.random.randint(0, date_range)) for _ in range(n_transactions)],
    "Quantity": np.random.randint(1, 10, size=n_transactions)
}

transaction_df = pd.DataFrame(transaction_data)

# Merge with Product Price and Discount for Total Amount calculation
transaction_df = transaction_df.merge(product_df[['Product_ID', 'Price', 'Discount']], on='Product_ID')

# Map Customer-Specific Effects for Distance, Gender, and Marital Status to control Quantity and Total Spending
customer_effects = customer_df.set_index("Customer_ID")[["Distance_to_Store", "Gender", "Marital_Status"]]
transaction_df = transaction_df.merge(customer_effects, on="Customer_ID", how="left")

# Apply correlations directly:
# 1. Marital Status and Quantity
transaction_df["Quantity"] *= np.where(transaction_df["Marital_Status"] == "Married", 1.3,
                                        np.where(transaction_df["Marital_Status"] == "Divorced", 1.1, 0.9))

# 2. Distance to Store and Spending
transaction_df["Total_Amount"] = transaction_df["Quantity"] * transaction_df["Price"] * \
                                 (1 - transaction_df["Discount"] / 100) * (1 + transaction_df["Distance_to_Store"] / 50)

# 3. Gender Effect (Females spend more)
transaction_df["Total_Amount"] *= np.where(transaction_df["Gender"] == "Female", 1.3, 1.0)

# Generate Frankentable with all combined variables and control structure
frankentable = transaction_df \
    .merge(customer_df, on="Customer_ID", how="left") \
    .merge(product_df, on="Product_ID", how="left") \
    .merge(store_df, on="Store_ID", how="left")

# Date Dimension Table
date_dim = pd.DataFrame({"Date": pd.date_range(start=start_date, end=end_date)})

# Save final tables
customer_df.to_csv("customers.csv", index=False)
product_df.to_csv("products.csv", index=False)
store_df.to_csv("stores.csv", index=False)
transaction_df.to_csv("transactions.csv", index=False)
frankentable.to_csv("frankentable.csv", index=False)
date_dim.to_csv("date_dim.csv", index=False)

print("CSV files created: customers.csv, products.csv, stores.csv, transactions.csv, frankentable.csv, date_dim.csv")
