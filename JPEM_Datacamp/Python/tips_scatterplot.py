import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

tips.head()

sns.scatterplot(
    x = "total_bill",
    y = "tip",
    data=tips,
    hue="smoker",
    hue_order=["No","Yes"])

plt.title = "Tips: Smokers vs Non-Smokers"
plt.xlabel = "Total Bill"
plt.ylabel = "Tip Amount"


plt.show()