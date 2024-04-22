from books.api.authors.services import AuthorService
from books.core.authors.repository import AuthorRepository
from books.core.books.repository import BookRepository


def attach_author_service() -> AuthorService:
    book_repository = BookRepository()
    author_repository = AuthorRepository()
    return AuthorService(book_repository=book_repository, author_repository=author_repository)
