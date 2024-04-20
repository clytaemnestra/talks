import os
from . import settings
from books.application import Application


def set_up_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
    from django.apps import apps

    apps.populate(settings.INSTALLED_APPS)


def initialize_books_app():
    app = (
        Application(name="Books App", port=8000, version="0.1", host="0.0.0.0")
        .init(route_factories=_initialize_routes())
        .get_asgi_app()
    )

    return app


def create_books_api():
    set_up_django()
    app = initialize_books_app()
    return app


def _initialize_routes():
    routes = [("books.api.books.routes", "/v0/books", ["Books"])]
    return routes
