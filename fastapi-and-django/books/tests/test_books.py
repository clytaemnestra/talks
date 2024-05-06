from src.books.services import BookService
from src.books.schema import CreateBookRequest
from datetime import date
import pytest


class FakeBookRepository:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def create(self, title, author_id, isbn, publication_date):
        book = {
            "id": self.next_id,
            "title": title,
            "author_id": author_id,
            "isbn": isbn,
            "publication_date": publication_date,
        }
        self.books.append(book)
        self.next_id += 1
        return book


@pytest.mark.asyncio
async def test_create_book():
    request = CreateBookRequest(
        title="Test Book",
        author_id=1,
        isbn="123-4567890123",
        publication_date=date.today(),
    )

    fake_book_repository = FakeBookRepository()
    book_service = BookService(repository=fake_book_repository)

    await book_service.create_book(request)

    created_book = fake_book_repository.books[-1]

    assert created_book["title"] == request.title
    assert created_book["author_id"] == request.author_id
    assert created_book["isbn"] == request.isbn
    assert created_book["publication_date"] == request.publication_date
