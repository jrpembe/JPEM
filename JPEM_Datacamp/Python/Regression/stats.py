import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


smi = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/SwedishMotorInsurance.csv')

print(smi.mean())

print(smi['Claims'].corr(smi['Payment']))

sns.scatterplot(x="Claims",
                y="Payment",
                data=smi)

plt.show()

sns.regplot(x="Claims",
            y="Payment",
            data=smi,
            ci=None)