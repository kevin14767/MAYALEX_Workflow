#attempting to read epub file of book

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
file_name = "C:\\Users\\Kevin\\Downloads\\MAYALEX Workflow\\Ch'olti' Book Scans\\English-Spanish-Ch'olti' Word List.epub"

book = epub.read_epub(file_name)
items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))

