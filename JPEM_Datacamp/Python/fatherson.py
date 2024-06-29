import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np
from statsmodels.formula.api import ols


father = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/fatherson.csv")

fig = plt.figure()

father.head()


sns.scatterplot(x = "Father", y = "Son", data=father)
plt.axline(xy1=(150,150),
           slope=1,
           linewidth=2,
           color="green")

plt.axis("equal")
plt.show()

fig = plt.figure()


sns.regplot(x = "Father",
            y = "Son",
            data=father,
            ci=None,
            line_kws={"color": "black"})

plt.axline(xy1=(150,150),
           slope=1,
           linewidth=2,
           color="green")

plt.axis("equal")
plt.show()

mdl_son_vs_father = ols("Son ~ Father", data = father).fit()
print(mdl_son_vs_father.params)

# Making predictions

really_tall_father = pd.DataFrame(
    {"Father": [190]}
)

mdl_son_vs_father.predict(really_tall_father)

really_short_father = pd.DataFrame(
    {"Father": [150]}
)

mdl_son_vs_father.predict(really_short_father)