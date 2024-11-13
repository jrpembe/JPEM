import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Set seed for reproducibility
np.random.seed(42)

# Generating independent variables
num_rows = 1000
customer_age = np.random.randint(18, 70, num_rows)
annual_income = np.random.randint(20000, 200000, num_rows)
website_visits = np.random.randint(0, 20, num_rows)

# Create a matrix of independent variables
X = np.column_stack((customer_age, annual_income, website_visits))

# Coefficients ensuring reasonable correlation
coefficients = [250, 0.1, 500]

# Generating Sales_Prediction with some noise
noise = np.random.normal(0, 10000, num_rows)  # Adding noise for realistic data
sales_prediction = X @ coefficients + noise

# Ensuring R-Squared is between 60% and 90%
model = LinearRegression()
model.fit(X, sales_prediction)
r_squared = model.score(X, sales_prediction)

attempts = 0
while (r_squared < 0.4 or r_squared > 0.8) and attempts < 100000:
    noise = np.random.normal(0, 10000, num_rows)
    sales_prediction = X @ coefficients + noise
    model.fit(X, sales_prediction)
    r_squared = model.score(X, sales_prediction)
    attempts += 1

if attempts >= 10:
    print(f"Couldn't achieve desired R-squared in {attempts} attempts.")
else:
    # Create DataFrame
    data = {
        'Customer_Age': customer_age,
        'Annual_Income': annual_income,
        'Website_Visits': website_visits,
        'Sales_Prediction': sales_prediction
    }
    df = pd.DataFrame(data)