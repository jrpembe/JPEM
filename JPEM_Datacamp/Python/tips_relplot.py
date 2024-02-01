import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

tips.head()

sns.relplot(
    x = "total_bill",
    y = "tip",
    data = tips,
    kind = "scatter",
    col = "day",
    col_wrap = 2,
    col_order = ["Thur",
                 "Fri",
                 "Sat",
                 "Sun"]
    )


