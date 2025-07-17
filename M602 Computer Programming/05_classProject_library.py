
"""
Scenario: Building a Simple Library System
Imagine you’re tasked with creating a simple library system to manage books and members. Using OOP principles, you can create a structured and efficient solution.

Step 1: Define the Classes
Book Class: Represents a book in the library.
Member Class: Represents a library member.
Library Class: Manages the collection of books and members.

Problem Description
You need to create a simple library system to manage books and members. 
The system should allow members to borrow and return books, and the library should keep track of which books are available and which are checked out.

Requirements:
------------------
Book Management:
    Add new books to the library.
    Check out books to members.
    Return books to the library.
Member Management:
    Add new members to the library.
    Allow members to borrow and return books.
Library Management:
    Maintain a collection of books.
    Maintain a list of members.
    
UML Design
Here's a UML class diagram to illustrate the design:

+------------------------------------+
|                Library             |
+------------------------------------+
|         - books:   List<Book>      |
|         - members: List<Member>    |
+------------------------------------+
|  + add_book(book: Book): str       |
|  + add_member(member: Member): str |
+------------------------------------+

+-------------------------+
|           Book          |
+-------------------------+
|  - title: str           |
|  - author: str          |
|  - isbn: str            |
|  - is_checked_out: bool |
+-------------------------+
|  + check_out(): str     |
| + return_book(): str    |
+-------------------------+

+--------------------------------+
|           Member               |
+--------------------------------+
| - name: str                    |
| - member_id: str               |
| - borrowed_books: List<Book>   |
+--------------------------------+
| + borrow_book(book: Book): str |
| + return_book(book: Book): str |
+--------------------------------+

Explanation of the UML
----------------------
Library Class:
    Attributes: books (a list of Book objects), members (a list of Member objects).
    Methods: add_book to add a new book, add_member to add a new member.
Book Class:
    Attributes: title, author, isbn, is_checked_out (a boolean indicating if the book is checked out).
    Methods: check_out to mark the book as checked out, return_book to mark the book as returned.
Member Class:
    Attributes: name, member_id, borrowed_books (a list of Book objects the member has borrowed).
    Methods: borrow_book to borrow a book, return_book to return a book.    
"""
