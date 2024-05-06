import os
import importlib
from src.settings import INSTALLED_APPS
from django import setup
from django.apps import apps
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
setup()

apps.populate(INSTALLED_APPS)

app = FastAPI(title="Books App", version="0.1")

routes = [
    ("src.books.routes", "/v0/books", ["Books"]),
    ("src.authors.routes", "/v0/authors", ["Authors"]),
]

for router_module_path, prefix, tags in routes:
    router_module = importlib.import_module(router_module_path)
    app.include_router(
        getattr(router_module, "router"),
        tags=tags,
        prefix=prefix,
    )
