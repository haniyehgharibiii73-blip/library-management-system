class Book:
    def __init__(self, title, author, is_available = True):
        self.title = title
        self.author = author
        self.is_available =is_available
        
    def display_info(self):
        print(f"title: {self.title}\nauthor: {self.author}\navailable: {self.is_available}")
        
    def borrow(self):
        if self.is_available == True:
            print(f"we have a {self.title} book")
            self.is_available = False
        else:
            print(f"we have not a {self.title} book")
            
    def return_book(self):
        if self.is_available == False:
            print(f"{self.title} Book returned successfully")
            self.is_available = True
        else:
            print(f"{self.title} Book is already available")
            
            
book1=Book("python basic", "john", True)
book1.display_info()
book1.borrow()
book1.return_book()
book2=Book("java", "hanie", True)
book2.display_info()
book2.borrow()
book3=Book("c", "hamed", True)
book3.display_info()
book3.borrow()

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books=[]
        
    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.borrow()
            print(f"{book.title} was borrowed successfully!") 
        else:
            print(f"{book.title} was not availble")


    def return_book(self,book):
        if book in self.borrowed_books:
            
            book.is_available = True
            self.borrowed_books.remove(book)
            print(f"{book.title} returned successfully")
        else:
            print(f"you havent borrowed {book.title}")
            book.is_available = False

member1=Member("hanie", 101)
print(member1.name)

member1.borrow_book(book1)
print(member1.borrowed_books)
member1.return_book(book1)

