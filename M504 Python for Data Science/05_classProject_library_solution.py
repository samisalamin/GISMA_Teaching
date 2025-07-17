class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return f'Book "{self.title}" checked out successfully.'
        return f'Book "{self.title}" is already checked out.'

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return f'Book "{self.title}" returned successfully.'
        return f'Book "{self.title}" was not checked out.'

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_checked_out:
            book.check_out()
            self.borrowed_books.append(book)
            return f'{self.name} borrowed "{book.title}".'
        return f'Book "{book.title}" is already checked out.'

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f'{self.name} returned "{book.title}".'
        return f'{self.name} does not have "{book.title}".'

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        return f'Book "{book.title}" added to the library.'

    def add_member(self, member):
        self.members.append(member)
        return f'Member "{member.name}" added to the library.'

# Example Usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
library.add_book(book1)
library.add_book(book2)

# Adding members
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")
library.add_member(member1)
library.add_member(member2)

# Borrowing and returning books
print(member1.borrow_book(book1))  # Alice borrows "1984"
print(member2.borrow_book(book1))  # Bob tries to borrow "1984" but it's already checked out
print(member1.return_book(book1))  # Alice returns "1984"
print(member2.borrow_book(book1))  # Bob borrows "1984"
