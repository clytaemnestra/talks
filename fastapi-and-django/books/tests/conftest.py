import pytest


from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def books_app() -> "FastAPI":
    from django.core import management
    from books.application import Application

    management.call_command("migrate")

    app = Application(name="Test App", host="0.0.0.0")
    yield app.get_asgi_app()


@pytest.fixture(scope="function")
def db(django_db_setup):
    import django.apps
    from django.db import connection

    all_models = django.apps.apps.get_models()
    tables = [model._meta.db_table for model in all_models]

    with connection.cursor() as cursor:
        for table in tables:
            cursor.execute(f"TRUNCATE TABLE {table} CASCADE;")


def pytest_sessionstart():
    from books.django_utils import initialize_django

    initialize_django()


@pytest.fixture(scope="session")
def client(books_app) -> TestClient:
    yield TestClient(books_app, base_url="http://testserver:8001")


@pytest.fixture
def books():
    from datetime import date

    from books.core.authors.models import Author
    from books.core.books.models import Book

    author = Author(
        name="Herman Hesse",
        bio="Hermann Karl Hesse was a German-Swiss poet, novelist, and painter.",
    )
    author.save()

    books = []

    books_data = [
        {"title": "Steppenwolf", "isbn": "9783518031599", "publication_year": 1924},
        {
            "title": "The Glass Bead Game",
            "isbn": "9780030818516",
            "publication_year": 1943,
        },
        {"title": "Siddharta", "isbn": "9780553208849", "publication_year": 1922},
    ]

    for book_data in books_data:
        book = Book(
            title=book_data["title"],
            author=author,
            isbn=book_data["isbn"],
            publication_date=date(book_data["publication_year"], 1, 1),
        )
        book.save()
        books.append(book)

    return books
