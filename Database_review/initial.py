import pandas as pd
import numpy as np

def track_pos_origins(dataframes):
    """
    Track the origins of parts of speech across multiple dataframes
    
    Parameters:
    -----------
    dataframes : list
        List of pandas DataFrames to analyze
    
    Returns:
    --------
    pd.DataFrame: A DataFrame with parts of speech and their origins
    """
    # Dictionary to track origins
    pos_origins = {}
    
    # List of dataframe names (assuming order matches input)
    df_names = ['Cholti', 'Kiche', 'Kaqchikel', 'Kaufman', 'Yukatek']
    
    for df_name, frame in zip(df_names, dataframes):
        # Normalize and extract parts of speech
        part_col = frame["Part of Speech"].apply(lambda x: str(x).lower().strip() if pd.notna(x) else np.nan)
        
        # Track origins for each unique part of speech
        for pos in part_col.dropna().unique():
            if pos not in pos_origins:
                pos_origins[pos] = set()
            pos_origins[pos].add(df_name)
    
    # Convert to DataFrame
    pos_list = sorted(list(pos_origins.keys()))
    df = pd.DataFrame({
        'Part of Speech': pos_list,
        'English Equivalent': [''] * len(pos_list),
        'Spanish Equivalent': [''] * len(pos_list)
    })
    
    # Add origin columns
    for df_name in df_names:
        df[f'Origin_{df_name}'] = df['Part of Speech'].apply(
            lambda pos: df_name in pos_origins.get(pos, set())
        )
    
    # Add a column showing all origins for each part of speech
    df['Origins'] = df['Part of Speech'].apply(
        lambda pos: ', '.join(sorted(pos_origins.get(pos, set())))
    )
    
    return df

# Example usage (to be replaced with actual file loading)
def main():
    # Placeholder for actual file loading
    cholti = pd.read_excel("All_Databases.xlsx", sheet_name="Cholti")
    kiche = pd.read_excel("All_Databases.xlsx", sheet_name="Kiche")
    kaqchikel = pd.read_excel("All_Databases.xlsx", sheet_name="Kaqchikel")
    kaufman = pd.read_excel("All_Databases.xlsx", sheet_name="Kaufman")
    yukatek = pd.read_excel("All_Databases.xlsx", sheet_name="Yukatek")
    
    dataframes = [cholti, kiche, kaqchikel, kaufman, yukatek]
    
    # Track and export parts of speech
    pos_df = track_pos_origins(dataframes)
    
    # Export to Excel
    pos_df.to_excel("parts_of_speeches_with_origins.xlsx", index=False)
    
    # Print unique parts of speech and their origins
    print(pos_df)

# Uncomment and modify when ready to run
if __name__ == "__main__":
    main()