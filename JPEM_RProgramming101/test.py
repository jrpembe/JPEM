import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("C:/Users/jason/OneDrive/Desktop/employee.csv")

# Create the 3D scatter plot with color based on 'Occupation'
fig = px.scatter_3d(df, 
                     x="Outdoor", 
                     y="Sociability", 
                     z="Conservativeness", 
                     color="Occupation",  # Color by categorical variable
                     title="3D Scatter Plot Colored by Occupation")

# Show the plot
fig.show()