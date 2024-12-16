import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
file_path =  "C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 415/DATA 415 Student Assignment Submissions/Assignment 7 - Final Project/Rithiek Sakthivel/book.csv"
heart_data = pd.read_csv(file_path)

# Select only numerical columns for correlation
numerical_data = heart_data.select_dtypes(include=['number'])

# Generate a correlation matrix
correlation_matrix = numerical_data.corr()

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Create a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Add titles and labels
plt.title("Correlation Matrix Heatmap", fontsize=16)
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.show()



