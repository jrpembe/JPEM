import pandas as pd
import numpy as np

# Define the hospital data
hospital_data = {
    'Hospital_ID': [
        'H003', 'H001', 'H006', 'H007', 'H010', 
        'H009', 'H004', 'H008', 'H005', 'H002'
    ],
    'Hospital_Name': [
        'Fleming, Griffin and Garcia', 'Bryan, Brown and Thomas', 
        'Mccormick-Valenzuela', 'Patterson, Miller and Baker', 
        'Schneider, Skinner and Kennedy', 'Sanchez Ltd', 
        'Foster PLC', 'Robinson, Garcia and Perez', 
        'Mcbride PLC', 'Collins, Long and Rodriguez'
    ]
}

# Create a DataFrame
hospital_df = pd.DataFrame(hospital_data)

# Set total rows and desired min/max count per hospital
total_rows = 10000
min_count = 400
max_count = 1500

# Randomly generate counts for each hospital within specified range
hospital_counts = np.random.randint(min_count, max_count + 1, size=len(hospital_df))

# Scale counts to ensure they sum to 10,000 rows
scaling_factor = total_rows / hospital_counts.sum()
hospital_counts = (hospital_counts * scaling_factor).astype(int)

# Adjust if there's any remaining difference
if hospital_counts.sum() != total_rows:
    difference = total_rows - hospital_counts.sum()
    hospital_counts[0] += difference

# Create the expanded DataFrame with randomized distribution
hospital_rows = pd.DataFrame({
    'Hospital_ID': np.repeat(hospital_df['Hospital_ID'], hospital_counts),
    'Hospital_Name': np.repeat(hospital_df['Hospital_Name'], hospital_counts)
})

# Shuffle rows for randomness
hospital_rows = hospital_rows.sample(frac=1, random_state=1).reset_index(drop=True)
import os
print("Current working directory:", os.getcwd())

# Save to CSV
hospital_rows.to_csv("c:/JPEM_Git_Main/JPEM/randomized_hospital_data.csv", index=False)

