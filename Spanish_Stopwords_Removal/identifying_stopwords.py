import pandas as pd

# Define stopwords dictionary
stopwords = {
    "v°": "v[erb]o",
    "v°n°": "v[erb]o n[eutr]o",
    "v°neu°": "v[erb]o neu[tr]o",
    "ne°": "[verbo] ne[utr]o",
    "neu°": "verbo neutro",
    "v°act°": "verbo activo",
    "de": "de",
    "también": "también",
    "idem": "idem",
    "otro": "otro",
    "vº": "verbo",
    "neuº": "neutro",
    "actiuo": "activo",
    "verbo" : "verbo",
    "neutro" : "neutro",
    "activo" : "activo",
}

# Load the Excel file
df = pd.read_excel("./Spanish_Stopwords_Removal/cholti_db.xlsx", sheet_name="Master")

# Ensure the 'Stopwords' column exists or initialize it
if 'Stopwords' not in df.columns:
    df['Stopwords'] = ""
else:
    df['Stopwords'] = df['Stopwords'].fillna("")  # Replace NaN with an empty string

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    spanish_def = row.get("Meaning (Spanish)")
    if pd.isna(spanish_def):  # Skip rows with NaN in the Spanish definition
        continue

    split_words = spanish_def.split()
    new_def = []

    for word in split_words:
        word = word.strip()  # Remove any leading or trailing whitespace
        if word in stopwords:
            # Add the stopword to the 'Stopwords' column
            df.at[index, 'Stopwords'] += word + "; "
        else:
            # Keep the non-stopwords for the updated Spanish definition
            new_def.append(word)

    # Update the 'Meaning (Spanish)' column with the cleaned definition
    df.at[index, 'Meaning (Spanish)'] = ' '.join(new_def)  # Join with a space for readability

# Save the updated DataFrame back to Excel
df.to_excel("./Spanish_Stopwords_Removal/cholti_db_cleaned.xlsx", sheet_name="Master", index=False)
