from books.api.books.services import BookService
from books.core.books.repository import BookRepository


def attach_book_service() -> BookService:
    repository = BookRepository()
    return BookService(repository=repository)
