import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

divorce = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/divorce.csv", parse_dates=["marriage_date", "dob_woman"])

divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])
# divorce_date, dob, and marriage_date are etype "object" when they should be "date"

divorce.dtypes

# extracting part of a date (dt.month, dt.day, or dt.year)
divorce["marriage_month"] = divorce["marriage_date"].dt.month
divorce["marriage_day"] = divorce["marriage_date"].dt.day
divorce["marriage_year"] = divorce["marriage_date"].dt.year
divorce.head(2)

sns.lineplot(data=divorce, x = "marriage_month", y = "marriage_duration")
plt.show()

sns.lineplot(data=divorce, x = "marriage_year", y = "num_kids")
plt.show()

divorce["dob_woman_year"] = divorce["dob_woman"].dt.year

sns.lineplot(data=divorce, x = "dob_woman_year", y = "num_kids")
plt.show()