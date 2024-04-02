import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

salaries = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/ds_salaries_clean.csv")

print(salaries.select_dtypes("object").head())

# count of categories
print(salaries["Designation"].value_counts())

# count of unique birth country
print(salaries["Designation"].nunique())


# Define top five positions
top_5_designations = salaries["Designation"].value_counts().head(5).index

# Define the color palette
colors_top_5 = sns.color_palette("bright", 5)


#Plotting
sns.countplot(data=salaries, x="Designation", order=top_5_designations, palette=colors_top_5)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()