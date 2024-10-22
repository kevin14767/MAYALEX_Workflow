#attempting to read epub file of book

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
file_name = "C:\\Users\\Kevin\\Downloads\\MAYALEX Workflow\\Ch'olti' Book Scans\\English-Spanish-Ch'olti' Word List.epub"


# Function to extract and display the content of an EPUB file
def read_epub_to_text(file_path, output_file):
    # Open the EPUB file
    book = epub.read_epub(file_path)
    
    # Open the output text file in write mode
    with open(output_file, 'w', encoding='utf-8') as f:
        # Loop through all items in the book
        for item in book.get_items():
            # Check if the item is an XHTML document (Type 9)
            if item.get_type() == 9 and item.media_type == 'application/xhtml+xml':
                # Parse the XHTML content using BeautifulSoup
                soup = BeautifulSoup(item.get_body_content(), 'html.parser')
                
                # Extract the text and write it to the text file
                f.write(soup.get_text())
                f.write('\n' + '-' * 40 + '\n')  # Add a separator between sections

# Replace 'your_file.epub' with the actual file path of your EPUB file
# Replace 'output.txt' with the desired output file name
read_epub_to_text(file_name, 'output.txt')
