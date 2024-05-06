from typing import Annotated

from fastapi import Depends

from src.authors.services import AuthorService
from src.authors.repository import AuthorRepository
from src.books.repository import BookRepository


def attach_author_service() -> AuthorService:
    book_repository = BookRepository()
    author_repository = AuthorRepository()
    return AuthorService(
        book_repository=book_repository, author_repository=author_repository
    )


AuthorServiceDependency = Annotated[AuthorService, Depends(attach_author_service)]
