import pandas as pd

# Read the Excel file
print("Reading Excel file...")
df = pd.read_excel(r"C:\Users\kevin barcenas\Downloads\MAYALEX_Workflow\MAYALEX_Workflow\split_src_pagenum\All_Databases.xlsx",sheet_name="Kaufman")
print("\nFirst few rows of original dataframe:")
print(df.head())

source_col = df['Source(s)']
print("\nFirst few values of Source(s) column:")
print(source_col.head())

print("\nSplitting on 'Pp'...")
df['Page_Numbers'] = source_col.str.split('Pp').str[1]
df['Source_Name'] = source_col.str.split('Pp').str[0]

print("\nFirst few rows after splitting:")
print(df.head())

print("\nChecking for NaN values:")
print("NaN in Page_Numbers:", df['Page_Numbers'].isna().sum())
print("NaN in Source_Name:", df['Source_Name'].isna().sum())


df.to_excel(r"C:\Users\kevin barcenas\Downloads\MAYALEX_Workflow\MAYALEX_Workflow\split_src_pagenum\Kaufman_Split.xlsx", index=False)