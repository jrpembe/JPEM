import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

nobel = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/nobel.csv")

#print(nobel.select_dtypes("object").head())

# count of categories
#print(nobel["category"].value_counts())

# count of unique birth country
print(nobel["birth_country"].nunique())

# Define the color palette
colors = sns.color_palette("husl", len(nobel['category'].unique()))

#Plotting
sns.countplot(data=nobel, x="category", order=nobel['category'].value_counts().index, palette=colors)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

nobel["prize"].str.contains("Physics")

nobel["prize"].str.contains("Physics|Chemistry")

nobel["motivation"].str.contains("^poet")



