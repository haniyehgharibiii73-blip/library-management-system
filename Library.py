class Book:
    def __init__(self, title, author, is_available = True):
        if not title.strip():
            raise ValueError("Book title cannot be empty")

        if not author.strip():
            raise ValueError ("Book author cannot be empty")

        self.title = title.strip()
        self.author = author.strip()
        self.is_available =is_available
        
    def display_info(self):
        print(f"title: {self.title}\nauthor: {self.author}\navailable: {self.is_available}")
        
    def borrow(self):
        if self.is_available:
            print(f"we have a {self.title} book")
            self.is_available = False
            return True
        else:
            print(f"we have not a {self.title} book")
            return False
            
    def return_book(self):
        if not self.is_available:
            print(f"{self.title} Book returned successfully")
            self.is_available = True
            return True

        print(f"{self.title} Book is already available")
        return False
            
            

class Member:
    def __init__(self, name, member_id):

        if not name.strip():
            raise ValueError("Member name cannot be empty!")

        if type(member_id) is not int or member_id <= 0:
            raise ValueError("Member ID must be a positive integer!")
        
        self.name = name.strip()
        self.member_id = member_id
        self.borrowed_books=[]
        
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{book.title} was borrowed successfully!") 
        else:
            print(f"{book.title} was not availble")


    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                return True

        print(f"You haven't borrowed {book.title}")
        return False    
            



class Library:
    def __init__ (self):
       self.books= []
       self.members =[]
    
    def add_book(self, book):
        if book in self.books:
            print("already book exists")
            return False
        
        self.books.append(book)
        print("the book add seccessfully")
        return True
    
    def add_member(self, member):
        for existing_member in self.members:
            if existing_member.member_id == member.member_id:
                print("This member already exists")
                return False

        self.members.append(member)
        print("Member added successfully")
        return True

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
            
        return None
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None
    
    def search_book(self, keyword):
        results = []

        for book in self.books:
            if keyword.lower() in book.title.lower():
                results.append(book)

        return results

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:

                borrowed = False

                for member in self.members:
                    if book in member.borrowed_books:
                        borrowed = True
                        break

                if not borrowed:
                    self.books.remove(book)
                    print(f"{title} removed successfully")
                    return True

        print("No available copy found for this book")
        return False
        

    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                 if member.borrowed_books:
                    print("You must return your borrowed books first!")
                    return False

                 self.members.remove(member)
                 print(f"{member.member_id} removed")
                 return True
        print("Member not found")
        return False

    def borrow_book(self, member_id, book):
        member = self.find_member(member_id)
        if member is None:
            print("Mmber not found")
            return

        else:
            if book in self.books:
                member.borrow_book(book)
            else:
                print("Book not found in Library")
