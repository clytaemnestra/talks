from books.core.books.models import Book


class BookRepository:
    def __init__(self):
        pass

    def get_all(self):
        return Book.objects.all()
