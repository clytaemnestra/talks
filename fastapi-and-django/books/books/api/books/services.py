from books.api.books.schema import ReadBookSchema, CreateBookRequest
from books.core.db_utils import db_sync_to_async
from django.db import transaction


class BookService:
    def __init__(self, repository):
        self._repository = repository

    @db_sync_to_async
    def get_all_books(self) -> list[ReadBookSchema]:
        books_queryset = self._repository.get_all()
        books = [ReadBookSchema.from_orm(book) for book in books_queryset]
        return books

    @db_sync_to_async
    def get_book(self, book_id: int) -> ReadBookSchema:
        book = self._repository.get(book_id)
        return ReadBookSchema.from_orm(book)

    @db_sync_to_async
    def delete_book(self, book_id: int) -> None:
        return self._repository.delete(book_id)

    @db_sync_to_async
    @transaction.atomic
    def create_book(self, request: CreateBookRequest) -> ReadBookSchema:
        book = self._repository.create(
            title=request.title,
            author=request.title,
            isbn=request.isbn,
            publication_date=request.publication_date,
        )
        return ReadBookSchema.from_orm(book)
