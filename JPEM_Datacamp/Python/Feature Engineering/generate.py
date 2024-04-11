import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
from datetime import date

planes = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/planes.csv")

# Calculate the correlation matrix
corr = planes[['Duration', 'Price', 'Total_Stops']].corr()

# Plot the heatmap
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.show()

planes["Total_Stops"].value_counts()


planes["Total_Stops"] = planes["Total_Stops"].str.replace(" stops", "")
planes["Total_Stops"] = planes["Total_Stops"].str.replace(" stop", "")
planes["Total_Stops"] = planes["Total_Stops"].str.replace("non-stop", "0")
planes["Total_Stops"] = planes["Total_Stops"].astype(int)

corr = planes[['Duration', 'Price', 'Total_Stops']].corr()
sns.heatmap(corr, annot=True)
plt.show()

planes['Date_of_Journey'] = pd.to_datetime(planes['Date_of_Journey'], format='%d/%m/%Y')

planes["month"] = planes["Date_of_Journey"].dt.month.fillna(-1).astype(int)
planes["weekday"] = planes["Date_of_Journey"].dt.weekday.fillna(-1).astype(int)

corr = planes[['Duration', 'Price', 'Total_Stops', 'month', 'weekday']].corr()
sns.heatmap(corr, annot=True)
plt.show()

planes["Price"].describe()
twenty_fifth = planes["Price"].quantile(0.25)
median = planes["Price"].median()
seventy_fifth = planes["Price"].quantile(0.75)
maximum = planes["Price"].max()

labels = ["Economy", "Premium Economy", "Business Class", "First Class"]
bins = [0, twenty_fifth, median, seventy_fifth, maximum]

planes["Price_Category"] = pd.cut(planes["Price"],
                                  labels = labels,
                                  bins = bins)

planes[["Price", "Price_Category"]].head()

sns.countplot(data=planes, x="Airline", hue="Price_Category")
plt.show()

sns.scatterplot(data=planes, x="Duration", y="Price", hue="Total_Stops", palette="husl")
plt.show()

sns.barplot(data=planes, x="Airline", y="Duration", hue="Airline")
plt.show()