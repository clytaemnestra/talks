from asgiref.sync import sync_to_async
from django.db import transaction

from src.authors.schema import ReadAuthorSchema, CreateAuthorRequest


class AuthorService:
    def __init__(self, author_repository, book_repository):
        self._author_repository = author_repository
        self._book_repository = book_repository

    @sync_to_async
    def get_all_authors(self):
        authors_queryset = self._author_repository.get_all()
        return [ReadAuthorSchema.from_orm(author) for author in authors_queryset]

    @sync_to_async
    def get_author(self, author_id: int):
        author = self._author_repository.get(author_id)
        return ReadAuthorSchema.from_orm(author)

    @sync_to_async
    @transaction.atomic
    def delete_author(self, author_id: int) -> None:
        books = self._book_repository.get_books_by_author(author_id)
        book_ids = [book.id for book in books]
        self._book_repository.delete_multiple_books(book_ids)

        self._author_repository.delete(author_id)

    @sync_to_async
    def create_author(self, request: CreateAuthorRequest):
        return self._author_repository.create(name=request.name, bio=request.bio)
