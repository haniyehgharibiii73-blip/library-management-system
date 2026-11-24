import unittest
from Library import Book, Member, Library


class TestBook(unittest.TestCase):

    def test_create_book(self):
        book = Book("Python", "haniyeh")

        self.assertEqual(book.title, "Python")
        self.assertEqual(book.author, "haniyeh")
        self.assertTrue(book.is_available)

    def test_borrow_book(self):
        book=Book("python", "haniyeh")

        result= book.borrow()
        self.assertTrue(result)
        self.assertFalse(book.is_available)

    def test_borrow_unavailable_book(self):
        book = Book("Python", "haniyeh")

        book.borrow()
        result = book.borrow()

        self.assertFalse(result)
        self.assertFalse(book.is_available)

    def test_return_book(self):
        book = Book("Python", "haniyeh")

        book.borrow()
        book.return_book()

        self.assertTrue(book.is_available)

    def test_return_available_book(self):
        book = Book("Python", "haniyeh")

        book.return_book()

        self.assertTrue(book.is_available)

    def test_empty_title(self):
        with self.assertRaises(ValueError):
            Book("", "haniyeh")

    def test_empty_author(self):
        with self.assertRaises(ValueError):
            Book("Python", "")

class TestMember(unittest.TestCase):
    def test_create_member(self):
        member = Member("Sara", 101)

        self.assertEqual(member.name, "Sara")
        self.assertEqual(member.member_id, 101)
        self.assertEqual(member.borrowed_books, [])

    def test_empty_member_name(self):
        with self.assertRaises(ValueError):
            Member("", 101) 

    def test_invalid_member_id(self):
        with self.assertRaises(ValueError):
            Member("sara", -1)

    def test_member_borrow_book(self):
        member = Member("Sara", 101)
        book = Book("Python", "haniyeh")

        member.borrow_book(book)

        self.assertIn(book, member.borrowed_books)
        self.assertFalse(book.is_available)

    def test_borrow_unavailable_book(self):
        member = Member("Sara", 101)
        book = Book("Python", "haniyeh")

        book.borrow()
        member.borrow_book(book)

        self.assertNotIn(book, member.borrowed_books)
        self.assertFalse(book.is_available)

    def test_member_return_book(self):
        member = Member("Sara", 101)
        book = Book("Python", "haniyeh")

        member.borrow_book(book)
        member.return_book(book)

        self.assertNotIn(book, member.borrowed_books)
        self.assertTrue(book.is_available)

    def test_return_unborrowed_book(self):
        member = Member("Sara", 101)
        book = Book("Python", "haniyeh")

        member.return_book(book)

        self.assertNotIn(book, member.borrowed_books)
        self.assertTrue(book.is_available) 

class TestLibrary(unittest.TestCase):
    def  test_add_book(self):
        library= Library()
        book= Book("python", "haniyeh")

        library.add_book(book)

        self.assertIn(book, library.books)

    def test_add_duplicate_book(self):
        library= Library()
        book=Book("python", "haniyeh")

        library.add_book(book)
        library.add_book(book)

        self.assertEqual(len(library.books), 1)

    def test_add_member(self):
        library=Library()
        member=Member("haniyeh", 101)

        library.add_member(member)

        self.assertIn(member, library.members)

    def test_add_duplicate_member(self):
        library=Library()

        member1=Member("haniyeh", 101)
        member2=Member("sara", 101)

        library.add_member(member1)
        result = library.add_member(member2)

        self.assertFalse(result)
        self.assertEqual(len(library.members), 1)

    def test_find_member(self):
        library=Library()

        member= Member("haniyeh", 101)

        library.add_member(member)

        result= library.find_member(101)

        self.assertEqual(result, member)

    def test_find_member_not_found(self):
        library= Library()
        result= library.find_member(999)

        self.assertIsNone(result)

    def test_find_book(self):

        library= Library() 
        book=Book("python", "haniyeh")
        library.add_book(book)
        result= library.find_book("python")

        self.assertEqual(result, book)

    def test_find_book_not_found(self):
        library=Library()
        result= library.find_book("java")

        self.assertIsNone(result)

    def test_search_book(self):
        library=Library()

        book=Book("python course", "haniyeh")
        library.add_book(book)
        result = library.search_book("python")

        self.assertIn(book, result)

    def test_search_book_not_found(self):
        library=Library()
        result = library.search_book("python")

        self.assertEqual(result, [])

    def test_remove_book(self):
        library=Library()
        book=Book("python", "haniyeh")

        library.add_book(book)
        library.remove_book("python")

        self.assertEqual(len(library.books), 0)

    def test_remove_borrowed_book(self):
        library=Library()

        book=Book("python", "haniyeh")
        member=Member("sara", 101)

        library.add_book(book)
        library.add_member(member)

        member.borrow_book(book)
        library.remove_book("python")

        self.assertIn(book, library.books)

    def test_remove_member(self):
        library=Library()
        member=Member("haniyeh", 101)

        library.add_member(member)
        library.remove_member(101)

        self.assertEqual(len(library.members), 0)

    def test_remove_member_with_borrowed_book(self):
        library=Library()

        member=Member("haniyeh", 101)
        book=Book("python", "haniyeh")

        library.add_member(member)
        library.add_book(book)

        member.borrow_book(book)
        library.remove_member(101)

        self.assertIn(member, library.members)

    def test_library_borrow_book(self):
        library = Library()
        member = Member("haniyeh", 101)
        book = Book("Python", "haniyeh")

        library.add_member(member)
        library.add_book(book)

        library.borrow_book(101, book)

        self.assertIn(book, member.borrowed_books)
        self.assertFalse(book.is_available)

    def test_borrow_book_member_not_found(self):
        library=Library()

        book=Book("python", "haniyeh")

        library.add_book(book)
        library.borrow_book(999, book)

        self.assertTrue(book.is_available)

    def test_borrow_book_not_in_library(self):
        library=Library()

        member=Member("haniyeh", 101)
        book=Book("python", "haniyeh")

        library.add_member(member)
        library.borrow_book(101, book)

        self.assertNotIn(book, member.borrowed_books)
        self.assertTrue(book.is_available)

    
