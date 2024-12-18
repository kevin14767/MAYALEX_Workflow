import pandas as pd

all_databases_pos = pd.read_excel(r"C:\Users\Kevin\Downloads\MAYALEX Workflow\part_of_speech\parts_of_speeches_with_origins.xlsx")
old_pos_df = pd.read_excel(r"C:\Users\Kevin\Downloads\MAYALEX Workflow\part_of_speech\allpartofspeech.xlsx")

all_pos = all_databases_pos["Part of Speech"]
old_pos = old_pos_df["english"].dropna()

missing_in_old_pos = sorted(list(set(all_pos) - set(old_pos)))

# Method 2: Find and sort items in old_pos that are not in all_pos
missing_in_all_pos = sorted(list(set(old_pos) - set(all_pos)))

# Method 3: Detailed comparison with sorted output
comparison_df = pd.DataFrame({
    'all_pos': pd.Series(sorted(list(set(all_pos)))),
    'in_old_pos': pd.Series(sorted(list(set(all_pos)))).isin(old_pos)
})

comparison_df.to_excel("Missing_Part_of_speeches.xlsx",index=False)