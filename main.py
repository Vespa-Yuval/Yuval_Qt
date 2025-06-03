

# המחלקה הגבוהה ביותר שלוקחת נתונים מכל המחלקות שמתחת
class Library (shelve):
    def __int__(self,name):
        self.name = name

# מחלקה שלוקחת נתונים ממחלקה נמוכה יותר
class Shelf:
    def __int__(self,shelf_number):
        self.shelf_number = shelf_number
        self.books_count = 0  # משתנה שיספור כמה ספרים יש במדף
        self.books_pos = 1
    def UpTo5 (self, NumToAdd, flag):   # add_book(book) זו הפונקציה שניתן להוסיף עד 5 ספרים אני נתתי לה את השם מקסימום 5
        TotalOfBooks = self.books_count + NumToAdd

    # אם מספר הספרים אחרי ההוספה חורג מהמקסימום - מחזיר את הערך הבוליאני כמו שהוא
        if TotalOfBooks > 5:
            return flag
# אם הערך תקין יחזיר את ההפיך מלא תקין
        else:
            return not flag

    def replace_books_pos(self,swap_book):
        Swap = self.books_pos

        if self.books_pos = 0:
            return ("swaped")
        else:
            return ("position isnt empty")




# הסבר:
# class BOOK
# מחלקה שמיצגת ספר ,זו הדרגה הנמוכה ביותר שצריכה להיות חלק גם מכל המחלקות האחרות

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
