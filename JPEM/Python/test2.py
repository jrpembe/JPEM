import pandas as pd

# Paths to your Excel files
book1_path = 'C:/JPEM_Git_Main/JPEM/JPEM/data/Book1.xlsx'
book2_path = 'C:/JPEM_Git_Main/JPEM/JPEM/data/Book2.xlsx'
output_path = 'C:/JPEM_Git_Main/JPEM/JPEM/data/Book2_with_Cost.xlsx'

# Load the Excel files into pandas DataFrames
df_book1 = pd.read_excel(book1_path)
df_book2 = pd.read_excel(book2_path)

# Make sure 'ProjectID' columns in both dataframes are of the same type, this step is crucial for a successful merge
df_book1['ProjectID'] = df_book1['ProjectID'].astype(str)
df_book2['ProjectID'] = df_book2['ProjectID'].astype(str)

# Merge df_book2 with the relevant 'Cost' column from df_book1 based on 'ProjectID'
# This operation left-joins df_book2 (the 'left' dataframe) with the 'Cost' column of df_book1 (specified by the 'right' dataframe)
# 'how=left' ensures all records from df_book2 are kept, with matching records from df_book1 merged in based on 'ProjectID'
merged_df = pd.merge(df_book2, df_book1[['ProjectID', 'Cost']], on='ProjectID', how='left')

# Save the merged DataFrame to a new Excel file
merged_df.to_excel(output_path, index=False)

print(f'Merged file saved to {output_path}')
