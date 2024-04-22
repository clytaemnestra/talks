import importlib
from fastapi import FastAPI


class Application:
    def __init__(self, name, host, version="0.1"):
        self._initialize_django()

        self.app = FastAPI(title=name, version=version)

        self._setup_routes(
            [
                ("books.api.books.routes", "/v0/books", ["Books"]),
                ("books.api.authors.routes", "/v0/authors", ["Authors"]),
            ]
        )

    def _initialize_django(self):
        import os
        from django import setup

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "books.settings")
        setup()

    def _setup_routes(self, route_factories):
        for router_module_path, prefix, tags in route_factories:
            router_module = importlib.import_module(router_module_path)
            self.app.include_router(
                getattr(router_module, "router"),
                tags=tags,
                prefix=prefix,
            )

    def get_asgi_app(self):
        return self.app
