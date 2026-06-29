# Program: Library Management System
# Description: Models a library where members can borrow and return books.
# Covers: Classes, objects, encapsulation, properties,
#         instance methods, and static methods.

class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._available = True

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    def info(self):
        return f"{self._title} by {self._author}"

class Member:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow(self, book: Book):
        if not book.available:
            return "Book is currently unavailable."
        book.available = False
        self.books.append(book)
        return f"{self.name} borrowed {book.info()}"

    def return_book(self, book: Book):
        if book not in self.books:
            return "This book is not in your borrowed list."
        book.available = True
        self.books.remove(book)
        return f"{self.name} returned {book.info()}"

class Librarian:
    @staticmethod
    def welcome():
        return "Welcome to the library."

b1 = Book("Book A", "Author X")
m = Member("abc")
print(m.borrow(b1))
print(m.return_book(b1))
print(Librarian.welcome())
