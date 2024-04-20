import uvicorn


class ApplicationServer:
    def __init__(self, application_factory, host, port):
        config = uvicorn.Config(
            app=application_factory,
            factory=True,
            loop="uvloop",
            http="httptools",
        )

        self._server = uvicorn.Server(config=config)

    def serve(self):
        self._server.run()
