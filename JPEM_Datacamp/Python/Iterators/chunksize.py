import pandas as pd
result = []
total = 0

for chunk in pd.read_csv('data.csv', chunksize=1000):
    result.append(sum(chunk['x']))
total = sum(result)

    # or replace previous two lines with
    # total += sum(chunk['x'])
print(total)