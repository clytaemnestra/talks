import importlib

from fastapi import FastAPI


class Application:
    def __init__(self, name, version, port, host):
        self._name = name
        self._port = port
        self._version = version
        self._host = host

        self.app = FastAPI(title=self._name, version=self._version, host=self._host)

    def init(self, route_factories):
        self._load_routes(route_factories)
        return self

    def _load_routes(self, route_factories):
        for router_module_path, prefix, tags in route_factories:
            router_module = importlib.import_module(router_module_path)
            self.app.include_router(
                getattr(router_module, "router"),
                tags=tags,
                prefix=prefix,
            )

    def get_asgi_app(self):
        return self.app
