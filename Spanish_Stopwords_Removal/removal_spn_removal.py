import pandas as pd

# Load the Excel file
df = pd.read_excel("./Spanish_Stopwords_Removal/cholti_db.xlsx", sheet_name="Master")

# Open a file to write the cleaned definitions
output_file = "cleaned_spn_def.txt"

# Write cleaned definitions to the file
with open(output_file, "w", encoding="utf-8") as file:
    for index, row in df.iterrows():
        iso = str(row['Isolated Manuscript Spanish']).strip()  # Ensure 'iso' is a string and remove extra spaces
        spn_def = str(row['Meaning (Spanish)']).strip()  # Ensure 'spn_def' is a string and remove extra spaces

        # Split the Spanish definition by ";", clean each part, and then join them back
        cleaned_parts = [
            part.strip() for part in spn_def.split(";") if part.strip() != iso
        ]
        cleaned_spn_def = "; ".join(cleaned_parts)  # Join the cleaned parts with ";"

        # Write to file
        if cleaned_spn_def is None or cleaned_spn_def == "":
            file.write(spn_def + "\n")
        else:
            file.write(cleaned_spn_def + "\n")

print(f"Cleaned definitions with ';' handling have been written to {output_file}")
