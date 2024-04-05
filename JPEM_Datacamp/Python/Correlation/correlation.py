import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

divorce = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/divorce.csv", parse_dates=["marriage_date", "dob_woman", "dob_man", "divorce_date"])
divorce.dtypes

divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce["marriage_month"] = divorce["marriage_date"].dt.month
df = divorce[["income_man", "income_woman", "num_kids", "marriage_duration", "marriage_year", "marriage_month"]]

#.corr() measure the Pearson Correlation, or linear relationship between two variables

df.corr()

sns.heatmap(df.corr(), annot=True) # annot=True labels each cell
plt.show()

sns.scatterplot(data=divorce, x="income_man", y="income_woman")
plt.show()


sns.pairplot(data=divorce)
plt.show()

# limit the number of variables displayed by using the vars argument
sns.pairplot(data=divorce, vars=["income_man", "income_woman", "marriage_duration"])
plt.show()