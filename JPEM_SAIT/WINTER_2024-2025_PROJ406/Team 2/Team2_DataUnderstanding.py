import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from statsmodels.stats.outliers_influence import variance_inflation_factor
import statsmodels.api as sm

# File path
file_path = r"C:/JPEM_Git_Main/JPEM/JPEM_SAIT/data/test.csv"

# Read the CSV file
try:
    data = pd.read_csv(file_path)

    # Display the first few rows of the dataset to understand its structure
    print("Dataset preview:")
    print(data.head())

    # Check for non-numeric columns and exclude them
    numeric_data = data.select_dtypes(include=['number'])
    print("/nNumeric columns used for correlation:")
    print(numeric_data.columns)

    # Create the correlation matrix
    corr_matrix = numeric_data.corr()

    # Display the correlation matrix
    print("/nCorrelation Matrix:")
    print(corr_matrix)

    # Plot the correlation matrix using a heatmap (Seaborn)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", cbar=True)
    plt.title('Correlation Matrix (Seaborn)')
    plt.show()

    # Plot the correlation matrix using Plotly (Interactive Heatmap)
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Correlation Matrix (Interactive)",
        labels=dict(color="Correlation"),
    )
    fig.update_layout(
        xaxis_title="Variables",
        yaxis_title="Variables",
        width=800,
        height=800,
        xaxis_tickangle=45,
    )
    fig.show()

    # Calculate VIF for numeric columns
    X = numeric_data  # Use your numeric DataFrame
    vif = pd.DataFrame()
    vif['Variable'] = X.columns
    vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print(vif)

    # Correlation of X14 and X17 with all other variables
    correlations = numeric_data.corr()
    print("X14 Correlations:/n", correlations.iloc[:, 14])
    print("/nX17 Correlations:/n", correlations.iloc[:, 17])

    # Regress X14 and X17 on all other variables to check for exact linear dependence
    # Regress X14
    X = numeric_data.drop(columns=numeric_data.columns[14])  # Drop X14
    y = numeric_data.iloc[:, 14]  # X14 as target
    X = sm.add_constant(X)  # Add intercept
    model_X14 = sm.OLS(y, X).fit()
    print("X14 Regression Summary:/n", model_X14.summary())

    # Regress X17
    X = numeric_data.drop(columns=numeric_data.columns[17])  # Drop X17
    y = numeric_data.iloc[:, 17]  # X17 as target
    X = sm.add_constant(X)  # Add intercept
    model_X17 = sm.OLS(y, X).fit()
    print("X17 Regression Summary:/n", model_X17.summary())

except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
