
class Library :
    def __init__(self,name):
        self.name = name
        self.shelfs = [shelve(i + 1) for i in range(3)] # בעיקרון אפשר אין סוף מדפים
        self.readers =[]  #שימת הקוראים הריקה שלי


# בדיקה של מקום לספר החדש אם ישנו
 # - is_there_place_for_new_book() - Returns True if there is space to add a new book to any
    # shelf; otherwise, returns False.

    def SpaceForNewBok(self):
        for shelf in self.shelfs:
            if not shelf.shalveIsFull:
               return True
        return False
#הוספת ספר
  # add_new_book(book) – Adds the given Book to the first shelf that has free space.

    def AddingNewBook (self, book):
        for shelf in self.shelfs:
            if not shelf.ShelfIsFull:
                shelf.OneMoreBook(book)
                return
        print("no available place for a new book ")

#מחיקת ספר לפי השם שלו
    # - delete_book(title) – Searches  for a book by title and removes it from the library.

    def DeleteABook (self,title):
        for shelf in self.shelfs:
            for i in  range(5):
                book = shelf.books[i]
                if book is not None and book.title == title:
                    shelf.books[i] = None
                    shelf.ShelfIsFull = False
                    print(f"The book - {title} - Removed from library. ")
                    return
        print(f"No book by the name of- {title} -found .")

# - register_reader(name, reader_id) – Creates a new Reader object and adds it to the list of
# readers.
# רישום משתמש חדש

    def RegisterReader(self, name, reader_id):
        reader = Reader(reader_id,name)
        self.readers.append(reader)
        print(f" Reader {name} registered successfully. ")

# remove_reader(name) – Removes a reader from the readers list based on their name.

    def RemoveReader(self,name):
        for reader in self.readers:
             if reader.name == name:
                 self.reader.remove(reader)
                 print(f" The reader{name} deleted from list.")

# - search_by_author(author) – Returns a list of titles written by the specified author.

    def SertchByAthor(self,author):
        results = []
        for shelf in self.shelfs:
            for book in shelf.books:
                if book is not Name and book.author == author:
                    results.append(book.title)
        return results





# מחלקה שלוקחת נתונים ממחלקה נמוכה יותר
class Shelf:
    def __init__(self,shelf_number):
        self.shelve_number = shelf_number
        self.books = [None] *5 # עשיתי עדכון שיספור , משתנה שיספור כמה ספרים יש במדף
        self.shalfIsFull = False

    def OneMoreBook (self, book):   # פונקצית הוסמפת ספר
        for i in range(5):
            if self.books[i] is None:
                self.books [i] = book
                # בודק מצב ספרים על המדף ריק או מלא
                self.shalfIsFull = all(self.books)
                return
                print("Sorry shelf is full")

# חלפת ספרים
    def replace_books_pos(self,position1,position2):
       location1 = position1 -1
       location2 = position2 -1
       if not (0<= location1 < 5 and 0 <= location2 < 5):
           print ("bad location  between 1 to 5 only try again ")
           return

       if self.books[location1] is None or self.books[location2] is None:
            print("One of the locations is empty cant replace ")
            return

       self.books[location1] , self.books[location2] = self.books[location2],self.books[location1]
       print("books swapped positions ")

# קלאס לספרים 

class Book:
    def __init__(self,author,title,num_of_pages):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages


# קלאס לקורא
class Reader:
    def __init__(self, reader_id, name):
        self.reader_id = reader_id
        self.name = name
        self.read_books = []



#  השאלת ספר מהספריה פונקציה שמוסיפה ספר לקורא
    def Take_A_New_Book (self,book):
        if len(self.read_books) > 3 : #  אפשר לשנות למספר אין סופי לצורך העניין
            print(f" {self.name}  - can't tack more than 3 books ")
        else:
            self.read_books.append(book.title)
            print(f" {self.name}, - taken a book named: {book.title}. ")


    #החזרת ספר לספריה
    def Book_Return(self,title):
        if title in self.read_books:
            self.read_books.remove(title)
            print(f"{self.name} - returned the book {title} ")
        else:
            print(f"{self.name} -didnt take the book : {title}, so you cant return it ")


    # הצגת הספרים שכבר הושאלו ע"י הקורא

    def show_borrowed_books(self):
        if not self.read_books:
            print(f"{self.name} - didnt read any books yet. ")
        else:
            print(f"{self.name} - read the folowing books : ")
            for title in self.read_books:
                print(f"- {title} -")

