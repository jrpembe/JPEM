import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.catplot(
    x = "time",
    y = "total_bill",
    data = tips,
    kind = "box",
    order = ["Dinner", "Lunch"],
    # whis = 2.0
    whis = [5, 95]
    # sym="" # outliers extend to 1.5 IQR
)

plt.show()