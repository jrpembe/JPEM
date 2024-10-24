import pandas as pd
import numpy as np

# Set parameters for random data generation
n = 10000  # Number of rows

# Data generation based on input
np.random.seed(42)
year_built = np.random.randint(1954, 2025, n)
area_sq_m = np.random.randint(150, 501, n)
bedrooms = np.random.randint(2, 7, n)
garage = np.random.randint(1, 4, n)
bathrooms = np.random.choice([2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6], n)
pool = np.random.choice(['Yes', 'No'], n, p=[0.1, 0.9])  # Mostly 'No'
quadrant = np.random.choice(['NW', 'SW', 'SE', 'NE', 'Centre'], n)
property_tax_rate = np.round(3 + ((area_sq_m - 150) / 350) * (8 - 3), 1)  # proportional to area_sq_m
distance_to_c_train = np.random.randint(100, 5001, n)

# Create House ID
house_id = [f'CAL{str(i).zfill(5)}' for i in range(1, n+1)]

# Calculate house price based on various factors
base_price = 250000
max_price = 2000000
house_price = (
    base_price + 
    (area_sq_m * 1500) + 
    (bedrooms * 50000) + 
    (garage * 20000) + 
    (np.where(pool == 'Yes', 100000, 0)) + 
    (np.where(year_built > 2000, 50000, 0)) + 
    (np.where(distance_to_c_train < 1000, 50000, 0)) - 
    (distance_to_c_train * 10) +
    (property_tax_rate * 1000)
)

# Ensure the house price is within the specified range
house_price = np.clip(house_price, base_price, max_price)
house_price = np.round(house_price, -3)  # round to nearest thousand

# Create dataframe
df = pd.DataFrame({
    'House ID': house_id,
    'Year Built': year_built,
    'Area (Square Metre)': area_sq_m,
    'Bedrooms': bedrooms,
    'Bathrooms': bathrooms,
    'Garage (number of cars)': garage,
    'Pool': pool,
    'Quadrant (NW,SW,SE,NE,Centre)': quadrant,
    'Property Tax Rate': property_tax_rate,
    'Distance to C-Train (metres)': distance_to_c_train,
    'House Price ($)': house_price
})

# Save to CSV
df.to_csv("house_data_with_price.csv", index=False)

print("CSV file created: house_data_with_price.csv")
