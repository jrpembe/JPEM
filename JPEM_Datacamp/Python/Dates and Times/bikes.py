import pandas as pd
from datetime import datetime, timedelta

# use parse dates to use start and end as datetime
rides = pd.read_csv('C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/capital-onebike.csv', 
                    parse_dates=['Start date', 'End date'])

print(rides.head(3))

# or we could use to_datetime

# rides['Start date'] = pd.to_datetime(rides['Start date'], format = "%Y-%m-%d %H:%M:%S")

rides['Start date'].iloc[2]

rides['Duration'] = rides['End date'] - rides['Start date']

print(rides['Duration'].head(5))

# chainging methods together 
rides['Duration']\
    .dt.total_seconds()\
    .head(5)
    
rides['Duration'].mean()
rides['Duration'].sum()

# Percent of time out of the dock
rides['Duration'].sum() / timedelta(days=91)

# Count how many times the bike started at each station
rides['Member type'].value_counts()

# Percent of rides by members
rides['Member type'].value_counts() / len(rides)

# Add duration in seconds column
rides['Duration seconds'] = rides['Duration'].dt.total_seconds

non_numeric_mask = rides['Duration seconds'].apply(lambda x: isinstance(x, (int, float)))
rides = rides[non_numeric_mask]
rides['Duration seconds'] = rides['Duration seconds'].astype(float)
rides.dtypes

# Average duration by member type (grouping)
rides.groupby('Member type')['Duration seconds'].mean()

# Summarizing results in Pandas
rides\
    .resample('D', on = 'Start date')\
    ['Duration seconds']\
    .mean()\
    .plot()
    
rides['Start date'].head(3)\
    .dt.tz_localize('America/New_York')
    
rides['Start date'] = rides['Start date']\
    .dt.tz_localize('America/New_York')

# handling ambiguous datetimes
rides['Start date'] = rides['Start date']\
    .dt.tz_localize('America/New_York', ambiguous='NaT')

rides['End date'] = rides['End date']\
    .dt.tz_localize('America/New_York', ambiguous='NaT')

rides.iloc[1]