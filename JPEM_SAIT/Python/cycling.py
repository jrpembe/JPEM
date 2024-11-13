import pandas as pd
import random
from datetime import datetime, timedelta

# Generate list of dates from January 1, 2023 to December 31, 2023
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
delta = end_date - start_date

dates = [start_date + timedelta(days=i) for i in range(delta.days + 1)]

# Quadrants of the city
quadrants = ['NE', 'NW', 'SE', 'SW', 'S', 'N', 'E', 'W', 'Centre']

# Generate the number of cyclists injured with a bias for colder months
cyclists_injured = []

for date in dates:
    if date.month in [11, 12, 1, 2]:  # Winter months bias
        cyclists_injured.append(random.choices(range(10, 21), k=1)[0])
    else:
        cyclists_injured.append(random.choices(range(0, 11), k=1)[0])

# Generate random quadrants
random_quadrants = [random.choice(quadrants) for _ in dates]

# Create a DataFrame
data = {
    "Date": dates,
    "Quadrant": random_quadrants,
    "Cyclists Injured": cyclists_injured
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("cyclist_injuries_2023.csv", index=False)
