import pandas as pd

# Load data from files
df = pd.read_excel("./Ch'olti' Book Scans/English_Spanish Word List.xlsx")
master = pd.read_excel("./Merging_Master_Ch'olti'_File/Ch'olti'_database.xlsx", sheet_name="Master")

# Add new column for updated English translations in master
master['Updated English'] = None

# Iterate through each row in master to find matches in df
for master_index, master_row in master.iterrows():
    manuscript_spn = master_row['Manuscript Spanish']
    if pd.isna(manuscript_spn):
        continue
    
    # Iterate through df to check for matching Spanish words
    for df_index, feature in df.iterrows():
        spanish = feature["Spanish"]
        if pd.isna(spanish):
            continue
        
        # If a match is found, update the 'Updated English' column
        if spanish == manuscript_spn:
            master.at[master_index, 'Updated English'] = feature['English']
            #break  # Exit inner loop once a match is found

# Save the updated master DataFrame to a new Excel file
master.to_excel("./Merging_Master_Ch'olti'_File/Ch'olti'_database_with_English.xlsx", index=False)
print("Master file updated with new English translations.")
