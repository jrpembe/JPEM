import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt

adult = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/adult.csv")

adult.info()

adult["Marital Status"].describe()

adult["Marital Status"].value_counts(normalize=True)

adult.dtypes
adult["Marital Status"].nbytes
adult["Marital Status"].dtype


adult["Marital Status"] = adult["Marital Status"].astype("category")

adult["Marital Status"].dtype

my_data = ["A", "A", "C", "B", "C", "A"]
my_series1 = pd.Series(my_data, dtype="category")
print(my_series1)

# categorical data saves memory
# before categorization this column used 260488 bytes, 
# after categorization it is down to 32617 bytes.
adult["Marital Status"].nbytes