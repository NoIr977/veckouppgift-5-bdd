class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = False

    def borrow(self):
        self.status = True

    def return_book(self):
        self.status = False

    def check_status(self):
        return self.status


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_title(self,title):
        for book in self.books:
            if book.title == title:
                return book

    def find_by_author(self,author):
        for book in self.books:
            if book.author == author:
                return book

    def borrow_book(self, title):
        book = self.find_by_title(title)
        book.borrow()

    def return_book(self, title):
        book = self.find_by_title(title)
        book.return_book()
