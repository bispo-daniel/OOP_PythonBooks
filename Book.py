from Author import Author

class Book:
    def __init__(self, bookId, bookName, author):
        self.bookId = bookId
        self.bookName = bookName
        self.author = Author