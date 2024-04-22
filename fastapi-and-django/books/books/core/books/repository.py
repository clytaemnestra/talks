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

    def delete_multiple_books(self, books: list[int]) -> None:
        return Book.objects.filter(id__in=books).delete()

    def create(
        self, title: str, author_id: str, isbn: str, publication_date: datetime
    ) -> Book:
        book = Book.objects.create(
            title=title,
            author_id=author_id,
            isbn=isbn,
            publication_date=publication_date,
        )
        return book

    def get_books_by_author(self, author_id: int):
        return Book.objects.filter(authors__id=author_id)
