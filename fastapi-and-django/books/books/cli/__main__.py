from typer import Typer

from books.asgi import initialize_books_app
from books.asgi_server import ApplicationServer
from books.django_utils import with_django_initialized

app = Typer()


@app.command(name="books-api")
@with_django_initialized
def launch_api(host: str = "0.0.0.0"):
    application_server = ApplicationServer(
        application_factory=initialize_books_app, host=host, port=8000
    )

    application_server.serve()


if __name__ == "__main__":
    app()
