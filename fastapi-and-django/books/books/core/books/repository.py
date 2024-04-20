from datetime import datetime

from books.core.books.models import Book


class BookRepository:
    def __init__(self):
        pass

    def get_all(self):
        return Book.objects.all()

    def get(self, book_id: int) -> Book:
        return Book.objects.get(id=book_id)

    def delete(self, book_id: int) -> None:
        return Book.objects.get(id=book_id).delete()

    def create(
        self, title: str, author: str, isbn: str, publication_date: datetime
    ) -> Book:
        book = Book.objects.create(
            title=title, author=author, isbn=isbn, publication_date=publication_date
        )
        return book
