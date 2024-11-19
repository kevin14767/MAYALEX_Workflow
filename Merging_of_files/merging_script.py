from IPython.display import display
import pandas as pd

second_file = pd.read_excel("./Merging_of_files/Mayas_file.xlsx")
first_file = pd.read_excel("./Merging_of_files/First_file.xlsx", sheet_name="Master")

mapping = dict(zip(second_file['ID'], second_file['Part of Speech']))
first_file["Part of Speechh From Maya's File"] = first_file['ID'].map(mapping)
output_file_path = r"Merged_Database.xlsx"
first_file.to_excel(output_file_path, index=False)