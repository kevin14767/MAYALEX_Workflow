import pandas as pd
import numpy as np

def lowercase_meanings(dataframes):
    """
    Lowercase the 'Meaning (English)' and 'Meaning (Spanish)' columns for all dataframes
    
    Parameters:
    -----------
    dataframes : list
        List of pandas DataFrames to process
    
    Returns:
    --------
    list: Modified dataframes with lowercased meanings
    """
    processed_dataframes = []
    
    for df in dataframes:
        # Create a copy to avoid modifying the original dataframe
        modified_df = df.copy()
        
        # Lowercase English meanings if column exists
        if 'Meaning (English)' in df.columns:
            modified_df['Meaning (English)'] = df['Meaning (English)'].apply(
                lambda x: str(x).lower().strip() if pd.notna(x) else x
            )
        
        # Lowercase Spanish meanings if column exists
        if 'Meaning (Spanish)' in df.columns:
            modified_df['Meaning (Spanish)'] = df['Meaning (Spanish)'].apply(
                lambda x: str(x).lower().strip() if pd.notna(x) else x
            )
        
        if 'Part of Speech' in df.columns:
            modified_df['Part of Speech'] = df['Part of Speech'].apply(
                lambda x: str(x).lower().strip() if pd.notna(x) else x
            )
            
        processed_dataframes.append(modified_df)
    
    return processed_dataframes

def main():
    # Placeholder for actual file loading
    cholti = pd.read_excel("All_Databases.xlsx", sheet_name="Cholti")
    kiche = pd.read_excel("All_Databases.xlsx", sheet_name="Kiche")
    kaqchikel = pd.read_excel("All_Databases.xlsx", sheet_name="Kaqchikel")
    kaufman = pd.read_excel("All_Databases.xlsx", sheet_name="Kaufman")
    yukatek = pd.read_excel("All_Databases.xlsx", sheet_name="Yukatek")
   
    dataframes = [cholti, kiche, kaqchikel, kaufman, yukatek]
    
    # Process dataframes to lowercase meanings
    processed_dataframes = lowercase_meanings(dataframes)
    
    # Optional: Save processed dataframes back to Excel
    database_names = ['Cholti', 'Kiche', 'Kaqchikel', 'Kaufman', 'Yukatek']
    
    for name, df in zip(database_names, processed_dataframes):
        df.to_excel(f"{name}_lowercased.xlsx", index=False)
    
    return processed_dataframes

# Uncomment and modify when ready to run
if __name__ == "__main__":
    processed_frames = main()