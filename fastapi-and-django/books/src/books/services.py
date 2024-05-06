from asgiref.sync import sync_to_async

from src.books.schema import ReadBookSchema, CreateBookRequest


class BookService:
    def __init__(self, repository):
        self._repository = repository

    @sync_to_async
    def get_all_books(self) -> list[ReadBookSchema]:
        books_queryset = self._repository.get_all()
        books = [ReadBookSchema.from_orm(book) for book in books_queryset]
        return books

    @sync_to_async
    def get_book(self, book_id: int) -> ReadBookSchema:
        book = self._repository.get(book_id)
        return ReadBookSchema.from_orm(book)

    @sync_to_async
    def delete_book(self, book_id: int) -> None:
        return self._repository.delete(book_id)

    @sync_to_async
    def create_book(self, request: CreateBookRequest) -> ReadBookSchema:
        book = self._repository.create(
            title=request.title,
            author_id=request.author_id,
            isbn=request.isbn,
            publication_date=request.publication_date,
        )
        return ReadBookSchema.from_orm(book)
