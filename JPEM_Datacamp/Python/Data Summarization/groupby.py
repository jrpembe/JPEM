import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/baseball.csv")

df.info()

numeric_columns = ['Height', 'Weight', 'Age']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# mean_by_pos_category = df.groupby("PosCategory")[numeric_columns].mean()
mean_by_pos_category = df.groupby("PosCategory")[numeric_columns].mean()
print(mean_by_pos_category)

df[numeric_columns].agg(["mean", "std"])

# we can also choose which aggregation to apply to which columns
# using dictionary notation
df[numeric_columns].agg({"Height": ["mean", "std"], "Weight" : ["min", "max"], "Age" : ["std"] })

# naming the summary columns using named tuples
df[numeric_columns].agg(
    mean_height = ("Height", "mean"),
    std_weight = ("Weight", "std"),
    median_age = ("Age", "median")
)

sns.barplot(data=df, x="Height", y="PosCategory")
plt.show()
