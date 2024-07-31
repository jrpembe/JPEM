import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
from statsmodels.formula.api import logit
import numpy as np

# Load the dataset
churn = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/churn.csv")

# Fit the logistic regression model
mdl_recency = logit("has_churned ~ time_since_last_purchase", data=churn).fit()

# Create the explanatory data
explanatory_data = pd.DataFrame(
    {"time_since_last_purchase": np.arange(-1, 6.25, 0.25)})

# Generate predictions
prediction_data = explanatory_data.assign(has_churned = mdl_recency.predict(explanatory_data))

# Print the first few rows of the prediction data
print(prediction_data.head())


sns.regplot(x = "time_since_last_purchase",
            y = "has_churned",
            data = churn,
            ci = None,
            logistic = True)

sns.scatterplot(x = "time_since_last_purchase",
            y = "has_churned",
            data = prediction_data,
            color="red")

plt.show()

# Calculating the "most likely" response
prediction_data = explanatory_data.assign(
    has_churned = mdl_recency.predict(explanatory_data)
)

prediction_data["most_likely_outcome"] = np.round(prediction_data["has_churned"])

sns.regplot(x = "time_since_last_purchase",
            y = "has_churned",
            data = churn,
            ci = None,
            logistic = True)

sns.scatterplot(x = "time_since_last_purchase",
            y = "most_likely_outcome",
            data = prediction_data,
            color="red")

plt.show()

# Calculating Odds Ratio (commonly used in gambling)

# Odds Ratio = Probability / (1 - Probability)
prediction_data["odds_ratio"] = prediction_data["has_churned"] / (1 - prediction_data["has_churned"])

sns.lineplot(x = "time_since_last_purchase",
            y = "odds_ratio",
            data = prediction_data)

plt.axhline(y=1, linestyle="dotted")
plt.yscale("log")
plt.show()

# Calculating Log Odds Ratio (commonly known as "logit", which we have been using all along)
prediction_data["log_odds_ratio"] = np.log(prediction_data["odds_ratio"])