import pdfplumber

# Initialize an empty string to store the extracted text
text = ""

# Extract text from PDF
with pdfplumber.open("./ErikBookCrossReference/cholti_moran1695_revised.pdf") as pdf:
    for page in pdf.pages:
        text += page.extract_text() + "\n"  # Append text and add a newline after each page

# Export the text to a file
output_file = "./extracted_text.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text successfully exported to {output_file}")
