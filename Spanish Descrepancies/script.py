import pandas as pd

file = "C:\\Users\\Kevin\\Downloads\\MAYALEX Workflow\\Spanish Descrepancies\\master_cholti.xlsx"
sheet = "Master"
df = pd.read_excel(file, sheet_name=sheet)

#spn_meaning = df['Meaning (Spanish)']
#full_entry = df['Full Original Entry']
i = 0
for index, row in df.iterrows():
    spn = row['Meaning (Spanish)']
    full_entry = row['Full Original Entry']
    if pd.isna(full_entry) or pd.isna(spn):
        continue
    split = spn.split(';')
    for word in split:
        word = word.strip()
        if word not in full_entry:
            with open('output2.txt','a', encoding='utf-8') as file:
                file.write('\n' + word + "\n" + full_entry + '\n')
       