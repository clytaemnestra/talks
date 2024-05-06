from typing import Annotated

from fastapi import Depends

from src.books.repository import BookRepository
from src.books.services import BookService


def attach_book_service() -> BookService:
    repository = BookRepository()
    return BookService(repository=repository)


BookServiceDependency = Annotated[BookService, Depends(attach_book_service)]
