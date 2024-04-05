import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

divorce = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/divorce.csv", parse_dates=["marriage_date", "dob_woman", "dob_man", "divorce_date"])
divorce.dtypes

divorce["education_man"].value_counts()
divorce["marriage_year"] = divorce["marriage_date"].dt.year
# using an ordered category like education to control hue isn't very clean as they plot over one another.
sns.histplot(data=divorce, x = "marriage_duration", hue="education_man", binwidth=1)
plt.show()

# use kde plot instead
sns.kdeplot(data=divorce, x = "marriage_duration", hue="education_man")
plt.show()

# the smoothing in kde plots can create values that do not make sense, such as marriage_duration < 0
sns.kdeplot(data=divorce, x = "marriage_duration", hue="education_man", cut=0)
plt.show()

# probability that marriage duration is <= value on x-axis for each level of male partner education
sns.kdeplot(data=divorce, x = "marriage_duration", hue="education_man", cut=0, cumulative=True)
plt.show()

divorce["man_age_marriage"] = divorce["marriage_year"] - divorce["dob_man"].dt.year
divorce["woman_age_marriage"] = divorce["marriage_year"] - divorce["dob_woman"].dt.year

sns.scatterplot(data=divorce, x = "man_age_marriage", y = "woman_age_marriage", hue="education_man")
plt.show()