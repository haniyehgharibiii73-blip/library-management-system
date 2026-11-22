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

class Library:
    def __init__ (self):
       self.books= []
       self.members =[]
    
    def add_book(self, book):
        if book in self.books:
            print("already book exists")
        else:
            self.books.append(book)
            print("the book add seccessfully")

    def add_member(self, member):
        if member in self.members:
            print("This member already exists")
        else:
            self.members.append(member)
            print("Member added successfully")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
            else:
                return None
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

library=Library()
library.add_book(book1)
library.add_book(book1)

for book in library.books:
    print(book.title)
print(library.books)

library.add_member(member1)
library.add_member(member1)

member=library.find_member(101)
print(member.name)

found_book=library.find_book("python basic")
print(found_book.title)
print(library.find_book("Unknown"))