import pandas as pd
from sklearn.cluster import KMeans
import plotly.express as px

# Load the data
# Replace 'your_dataset.csv' with the path to your actual CSV file
data = pd.read_csv("C:/Users/jason/OneDrive/SAIT/SAIT Instructor/2024-2025/COURSE - DATA 415/DATA 415 Student Assignment Submissions/Assignment 7 - Final Project/Celeste Bernardo/Book3.csv")

# Select the columns for clustering (Age, Sex, ChestPainType)
X = data[['Age', 'Sex', 'ChestPainType']]

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['FinalCluster'] = kmeans.fit_predict(X)

# Plot 1: Initial cluster assignments
fig_initial = px.scatter_3d(
    data,
    x='Age', 
    y='Sex', 
    z='ChestPainType',
    color='Initial Cluster',  # Color points by initial cluster assignments
    title="3D Scatterplot of Initial Cluster Assignments",
    labels={'Age': 'Age', 'Sex': 'Sex', 'ChestPainType': 'Chest Pain Type'}
)

# Plot 2: Final cluster assignments from k-means
fig_final = px.scatter_3d(
    data,
    x='Age', 
    y='Sex', 
    z='ChestPainType',
    color='FinalCluster',  # Color points by final cluster assignments
    title="3D Scatterplot of K-Means Final Clusters",
    labels={'Age': 'Age', 'Sex': 'Sex', 'ChestPainType': 'Chest Pain Type'}
)

# Show both plots
fig_initial.show()
fig_final.show()
