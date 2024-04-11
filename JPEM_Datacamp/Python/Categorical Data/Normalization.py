import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

planes = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/planes.csv")

# Original data is heavily biased toward flights to Cochin and Bangalore, this data needs ot be normalized
planes["Destination"].value_counts()

# normalization
planes["Destination"].value_counts(normalize=True)

pd.crosstab(planes["Source"], planes["Destination"], values=planes["Price"], aggfunc="median")

