import unittest
from books.api.books.services import BookService
from books.api.books.schema import CreateBookRequest, ReadBookSchema
from datetime import date


class TestBookRepository:
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


class TestBookServiceWithFakeRepository(unittest.TestCase):
    async def setUp(self):
        self.test_book_repository = TestBookRepository()
        self.book_service = BookService(repository=self.test_book_repository)

    async def test_create_book(self):
        request = CreateBookRequest(
            title="Test Book",
            author_id=1,
            isbn="123-4567890123",
            publication_date=date.today(),
        )

        await self.book_service.create_book(request)

        created_book = self.fake_repository.books[-1]

        self.assertEqual(created_book["title"], request.title)
        self.assertEqual(created_book["author_id"], request.author_id)
        self.assertEqual(created_book["isbn"], request.isbn)
        self.assertEqual(created_book["publication_date"], request.publication_date)
