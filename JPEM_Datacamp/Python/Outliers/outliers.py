import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

salaries = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/ds_salaries_clean.csv")

print(salaries["Salary_USD"].describe())

# Interquartile Range
sns.boxplot(data=salaries, y="Salary_USD")
plt.show()

# IQR = 75th - 25th percentile
# Upper Outliers > 75th Percentile + (1.5 * IQR)
# Lower Outliers < 25th Percentile - (1.5 * IQR)

seventy_fifth = salaries["Salary_USD"].quantile(0.75)
twenty_fifth = salaries["Salary_USD"].quantile(0.25)

salaries_IQR = seventy_fifth - twenty_fifth

print(salaries_IQR)

# Upper Threshold
upper = seventy_fifth + (1.5 * salaries_IQR)
lower = twenty_fifth - (1.5 * salaries_IQR)

# The lower limit is a negative number which is not possible 
print(upper, lower)

# using these values to subset our data
salaries[(salaries["Salary_USD"] < lower) | (salaries["Salary_USD"] > upper)] [["Experience", "Employee_Location", "Salary_USD"]]

no_outliers = salaries[(salaries["Salary_USD"] > lower) & (salaries["Salary_USD"] < upper)]

print(no_outliers["Salary_USD"].describe())

# plotting histogram before and after removing outliers
sns.histplot(data=salaries, x="Salary_USD")
plt.show()

sns.histplot(data=no_outliers, x="Salary_USD")
plt.show()