import pandas as pd
#i also need to remove spanish but perhaps thats after splitting on semicolons?
df = pd.read_excel("./Ch'olti' Book Scans/English_Spanish Word List.xlsx")


result_array = []

# Iterate through each row in the column
for row in df['OG file after updates']:
    if pd.isna(row):
        continue
    values = row.split(';')  # split will return a single-item list if there's no semicolon
    result_array.extend(values)  # add all elements to the array

with open("ogcholti_output.txt", 'a', encoding='utf-8') as file:
    for value in result_array:
        file.write(value.strip() + "\n")