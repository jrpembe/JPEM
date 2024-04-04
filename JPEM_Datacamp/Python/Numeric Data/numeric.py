import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

salaries = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/ds_salaries_clean.csv")

print(salaries.info())
print(salaries.head())
print(salaries["Salary_USD"].head())

# replacing values in a string to convert to number (eg commas)
# pd.series.str.replace("Character to remove", "Character to replace with")

salaries.groupby("Company_Size")["Salary_USD"].mean()

# adding summary statistics into a dataframe

salaries["std_dev"] = salaries.groupby("Experience")["Salary_USD"].transform(lambda x:x.std())

print(salaries.head())
print(salaries[["Experience", "std_dev"]].value_counts())

print(salaries[["Designation", "std_dev"]].value_counts())

salaries["median_by_company_size"] = salaries.groupby("Company_Size")["Salary_USD"].transform(lambda x: x.median())

print(salaries[["Company_Size", "median_by_company_size"]].head())