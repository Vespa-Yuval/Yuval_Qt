# המחלקה הגבוהה ביותר שלוקחת נתונים מכל המחלקות שמתחת
### כנסתי להערה בגלל שיוצר קונפליקט עם המחלקה של  המדף צריך לברר למה
# class Library (Shelve):
#     def __int__(self,name):
#         self.name = name

# מחלקה שלוקחת נתונים ממחלקה נמוכה יותר
class Shelve:
    def __int__(self,shelve_number):
        self.shelve_number = shelve_number
        self.books = [None] *5 # עשיתי עדכון שיספור , משתנה שיספור כמה ספרים יש במדף
        self.shalveIsFull = False

    def OneMoreBook (self, book):   # פונקצית הוסמפת ספר
        for i in range(5):
            if self.books[i] is None:
                self.books [i] = book
                # בודק מצב ספרים על המדף ריק או מלא
                self.shalveIsFull = all(self.books)
                return
                print("Sorry shelve is full")


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



class Book:
    def __int__(self,author,title,num_of_pages):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages


# הקורא לא יורש
class Reader:
    def __int__(self, reader_id, name, books_read):
        self.reader_id = reader_id
        self.name = name
        self.books_read = books_read



