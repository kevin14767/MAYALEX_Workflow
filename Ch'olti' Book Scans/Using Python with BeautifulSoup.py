from bs4 import BeautifulSoup

# Correct file path
file_path = r"C:\Users\Kevin\Downloads\MAYALEX Workflow\Ch'olti' Book Scans\file\main-3.xhtml"
output_file_path = r"C:\Users\Kevin\Downloads\MAYALEX Workflow\Ch'olti' Book Scans\file\output.txt"

# Open the file and read its content
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Open the output file in write mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Find all <tr> tags
    rows = soup.find_all('tr')

    # Loop through each row
    for row in rows:
        # Find all <p> tags within the <td> of the row
        p_tags = row.find_all('p')
        if len(p_tags) > 1:
            # Write the text inside the second <p> tag to the file
            output_file.write(p_tags[1].text + '\n')

print(f"Output written to {output_file_path}")
