from books.api.books.schema import BookSchema
from books.core.db_utils import db_sync_to_async


class BookService:
    def __init__(self, repository):
        self._repository = repository

    @db_sync_to_async
    def get_all_books(self) -> list[BookSchema]:
        books_queryset = self._repository.get_all()
        books = [BookSchema.from_orm(book) for book in books_queryset]
        return books
