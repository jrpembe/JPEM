import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.catplot(
    x = "day",
    y = "total_bill",
    data = tips,
    kind = "point",
    # hue = "sex",
    capsize = 0.2,
    # ci = None
    #join = False,
    #estimator = mean
)

plt.show()