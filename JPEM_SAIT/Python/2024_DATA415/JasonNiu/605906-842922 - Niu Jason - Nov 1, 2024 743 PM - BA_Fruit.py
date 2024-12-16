import pandas as pd
import requests
from io import BytesIO
from collections import Counter
from itertools import combinations  # Add this import statement

MINIMUM_SUPPORT = 2

# URL of the file
url = 'https://dissidia.oss-cn-beijing.aliyuncs.com/test/20241024/Assign5.BA.fruit.xlsx'

# Download the file and load into a pandas ExcelFile
response = requests.get(url)
file = BytesIO(response.content)

# Load the Excel sheet
xls = pd.ExcelFile(file)

# Read the first sheet, starting from row 3 (index=2) and focusing on the 3rd column (usecols=2)
df = pd.read_excel(xls, sheet_name=0, usecols=[2], skiprows=1)

# Split the values by commas and trim any spaces, then convert to a list of lists
df['Items'] = df.iloc[:, 0].apply(lambda x: [item.strip() for item in str(x).split(',')])

# Convert the data to a list of lists
data = df['Items'].tolist()

# Display the data structure
print(data)

df = pd.DataFrame(data)


# Phase 1: Calculate support for each individual item
def calculate_item_support(df):
    # Flatten the DataFrame to create a single list of items
    all_items = df.stack().reset_index(drop=True)

    # Calculate the support for each unique item
    support = Counter(all_items)

    # Convert to DataFrame for better visualization
    support_df = pd.DataFrame(support.items(), columns=['Item', 'Support'])

    # Filter out items with support less than 2
    filtered_df = support_df[support_df['Support'] >= 2].reset_index(drop=True)

    return support_df, filtered_df


# Phase 2: Calculate support for two-item itemsets
def calculate_two_item_support(df):
    # Convert rows into list of sets to count combinations
    transactions = df.apply(lambda x: set(x.dropna()), axis=1).tolist()

    # Calculate support for two-item combinations
    two_item_combinations = [combo for transaction in transactions for combo in combinations(transaction, 2)]
    support = Counter(two_item_combinations)

    # Convert to DataFrame for better visualization
    support_df = pd.DataFrame(support.items(), columns=['Itemset', 'Support'])

    # Filter out two-item itemsets with support less than 2
    filtered_df = support_df[support_df['Support'] >= MINIMUM_SUPPORT].reset_index(drop=True)

    return support_df, filtered_df


# Phase 3: Calculate confidence for three-item itemsets
def calculate_three_item_confidence(df, filtered_two_items):
    # Convert rows into list of sets to count combinations
    transactions = df.apply(lambda x: set(x.dropna()), axis=1).tolist()

    # Calculate support for three-item combinations
    three_item_combinations = [combo for transaction in transactions for combo in combinations(transaction, 3)]
    support = Counter(three_item_combinations)

    # Calculate confidence: support(three-item) / support(two-item)
    confidence_data = []
    for itemset, support_value in support.items():
        for two_item_subset in combinations(itemset, 2):
            two_item_support = filtered_two_items[filtered_two_items['Itemset'] == two_item_subset]['Support'].values
            if two_item_support.size > 0:
                confidence = support_value / two_item_support[0]
                confidence_data.append((itemset, support_value, two_item_subset, confidence))

    # Convert to DataFrame for better visualization
    confidence_df = pd.DataFrame(confidence_data,
                                 columns=['Three-Item Itemset', 'Support', 'Two-Item Subset', 'Confidence'])

    return confidence_df


# Execute each phase
item_support_df, filtered_item_df = calculate_item_support(df)
two_item_support_df, filtered_two_item_df = calculate_two_item_support(df)
three_item_confidence_df = calculate_three_item_confidence(df, filtered_two_item_df)

# Create an Excel writer
with pd.ExcelWriter('C:/JPEM_Git_Main/JPEM/JPEM_SAIT/Python/2024_DATA415/Apriori_Analysis_corrected.xlsx', engine='xlsxwriter') as writer:
    # Write original data
    df.to_excel(writer, sheet_name='original', index=False)

    # Write phase 1 (support for individual items)
    item_support_df.to_excel(writer, sheet_name='phase1', index=False)
    filtered_item_df.to_excel(writer, sheet_name='phase1_filtered', index=False)

    # Write phase 2 (support for two-item itemsets)
    two_item_support_df.to_excel(writer, sheet_name='phase2', index=False)
    filtered_two_item_df.to_excel(writer, sheet_name='phase2_filtered', index=False)

    # Write phase 3 (confidence for three-item itemsets)
    three_item_confidence_df.to_excel(writer, sheet_name='phase3', index=False)

# File creation complete
print("Excel file 'Apriori_Analysis_corrected.xlsx' has been created successfully.")