import pytest
from fastapi import FastAPI


from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def books_app() -> "FastAPI":
    from books.main import app

    yield app


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
    import os
    from books.settings import INSTALLED_APPS
    from django import setup
    from django.apps import apps
    from django.core import management

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
    setup()
    apps.populate(INSTALLED_APPS)

    management.call_command("migrate")


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
