import pandas as pd
import numpy as np

data = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/hospital_fact_modified.csv')
data['Treatment_Cost'] = pd.to_numeric(data['Treatment_Cost'].str.replace('$', '').str.replace(',', ''), errors='coerce')
data['Insured_Coverage'] = pd.to_numeric(data['Insured_Coverage'].str.replace('$', '').str.replace(',', ''), errors='coerce')

data['Treatment_Cost_Smoothed'] = data['Treatment_Cost'] * (1 + np.random.uniform(-0.03, 0.03, len(data)))
data['Insured_Coverage_Smoothed'] = data['Insured_Coverage'] * (1 + np.random.uniform(-0.03, 0.03, len(data)))
data['Treatment_Cost_Rolling'] = data['Treatment_Cost_Smoothed'].rolling(window=3, min_periods=1).mean()
data['Insured_Coverage_Rolling'] = data['Insured_Coverage_Smoothed'].rolling(window=3, min_periods=1).mean()

data.to_csv('hospital_fact_smoothed.csv', index=False)
