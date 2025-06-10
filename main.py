
class Library :
    def __init__(self,name):
        self.name = name
# צריך להוסיף לקלאס של הסיפריה :
# רשימה של שלושה  מדפים
# רשימה של קוראים

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

