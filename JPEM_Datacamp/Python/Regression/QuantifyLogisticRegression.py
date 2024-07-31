import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import ols
from statsmodels.formula.api import logit
import numpy as np

from statsmodels.graphics.mosaicplot import mosaic

churn = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/churn.csv")

actual_response = churn["has_churned"]

mdl_recency = logit("has_churned ~ time_since_last_purchase", data=churn).fit()

# these predicted values are probabilities
predicted_response = np.round(mdl_recency.predict())

outcomes = pd.DataFrame({"actual_response": actual_response,
                         "predicted_response": predicted_response})

print(outcomes.value_counts(sort=False))

conf_matrix = mdl_recency.pred_table()
print(conf_matrix)

mosaic(conf_matrix)

# Accuracy = (TN + TP) / (TN + FN + FP + TP)

TN = conf_matrix[0,0]
TP = conf_matrix[1,1]
FN = conf_matrix[1,0]
FP = conf_matrix[0,1]
mdl_accuracy = (TN+TP) / (TN+FN+FP+TP)
print(mdl_accuracy)

# Sensitivity = (TP) / (FN + TP)

mdl_sensitivity = (TP) / (FN+TP)
print(mdl_sensitivity)

# Specificity = (TN) / (TN + FP)

mdl_specficity = (TN) / (TN+FP)
print(mdl_sensitivity)
