# Intro to Python – Final Project

# Library Management System
# You are required to create a Python program that manages a library system. The program
# should be object-oriented and consist of the following classes:
#
# Class: Book
# Attributes:
# - author (string)
# - title (string)
# - num_of_pages (int)
#
# Class: Shelf
# Attributes:
# - books (a list of up to 5 Book objects)
# - is_shelf_full (boolean)
# Methods:
# - add_book(book) – Adds a Book object to the first available spot in the books list. If the
# shelf is full, prints an appropriate message. Updates is_shelf_full to True if the shelf reaches
# its maximum capacity, otherwise sets it to False.
# - replace_books(pos1, pos2) – Swaps two books located at pos1 and pos2 (positions
# between 1 and 5). If either position is empty, prints a message.
#
# Class: Reader
# Attributes:
# - reader_id (int)
# - name (string)
# - books_read (a list of book titles the reader has read)
# Methods:
# - read_book(title: str) – Adds the given book title to the list of books the reader has read.
#
# Class: Library
# Attributes:
# - shelves (a list of 3 Shelf objects)
# - readers (an empty list of Reader objects)
#
# Methods:
# - is_there_place_for_new_book() - Returns True if there is space to add a new book to any
# shelf; otherwise, returns False.
# - add_new_book(book) – Adds the given Book to the first shelf that has free space.
# - delete_book(title) – Searches for a book by title and removes it from the library.
# - register_reader(name, reader_id) – Creates a new Reader object and adds it to the list of
# readers.
# - remove_reader(name) – Removes a reader from the readers list based on their name.
# - search_by_author(author) – Returns a list of titles written by the specified author.
#
# Program Requirements
# - The system manages only one Library object.
# - The program starts with 2 predefined Book objects on each Shelf.
# - An infinite loop runs until the user chooses to exit.
# - The user is presented with the following menu:
# For adding a book - Press 1
# For deleting a book - Press 2
# For registering a new reader - Press 3
# For removing a reader - Press 4
# For searching books by author – Press 5
# For exit – Press 6
# Menu Functionality:
# - Press 1: Prompt the user for new book details and add it using add_new_book.
# - Press 2: Ask for the book title and delete it using delete_book.
# - Press 3: Ask for reader's name and ID, then register them using register_reader.
# - Press 4: Ask for the reader's name and remove them using remove_reader.
# - Press 5: Ask for an author’s name and display all their books using search_by_author.
# - Press 6: Exit the program.