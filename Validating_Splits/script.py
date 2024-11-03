import pandas as pd

df = pd.read_excel("./Validating_Splits/Ch'olti'_Database_pastversion.xlsx")

result_array = []

# Iterate through each row in the column
for row in df['Headword (Practical Orthography)']:
    # Split by semicolon if it exists, otherwise just add the value
    if pd.isna(row):
        continue
    values = row.split(';')  # split will return a single-item list if there's no semicolon
    result_array.extend(values)  # add all elements to the array

with open("output.txt", 'a') as file:
    for value in result_array:
        file.write(value.strip() + "\n")