import pandas as pd
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

baseball = pd.read_csv("C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/baseball.csv")
baseball.head()

mean_baseball_height = baseball['Height'].mean()

print(mean_baseball_height)


# Generating a bootstrap distribution
# Step 3. Repeat Steps 1 & 2 many times, appending to a lsit
so_boot_distn = []
for i in range(5000):
    so_boot_distn.append(
        # Step 2. Calculate point estimate
        np.mean(
            # Step 1. Resample
            baseball.sample(frac=1, replace=True)['Height']
        )
    )

std_error = np.std(so_boot_distn, ddof=1)
print(std_error)

plt.hist(so_boot_distn, bins=50)
plt.show()

# Lets hypothesize the average baseball player is 73.6 inches tall
mean_comp_hyp = 73.6

z_score = (mean_baseball_height - mean_comp_hyp) / std_error
print(z_score)

# Is this a high or low number?

# Calculate the sample proportion of a specific field position
catcher_count = baseball[baseball['Position'] == 'First_Baseman'].shape[0]
total_players = baseball.shape[0]
sample_proportion = catcher_count / total_players

# Hypothesized proportion
p0 = 0.09

# Sample size
n = total_players

# Calculate the test statistic (z)
z = (sample_proportion - p0) / np.sqrt((p0 * (1 - p0)) / n)

# Calculate the p-value (two-tailed test)
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

# Display the results
print(f"Sample Proportion: {sample_proportion}")
print(f"Test Statistic (z): {z}")
print(f"P-value: {p_value}")

# Conclusion
alpha = 0.09
if p_value < alpha:
    print("Reject the null hypothesis: The proportion of First_Baseman is significantly different from 9%.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to suggest the proportion of First_Baseman is different from 9%.")