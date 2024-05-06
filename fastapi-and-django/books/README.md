# Books Demo App

The Books Demo App demonstrates how to integrate FastAPI with Django ORM within a single project. You can find the slides from my presentation [here]().

## Installation

This application is containerized using Docker and managed with Docker Compose. To start the application, execute the following command:

```bash
    make dev-stack-up
```

For a local setup without Docker, create a new virtual environment, install the requirements, and run the application using Uvicorn `uvicorn src.main:app --host 0.0.0.0 --port 8000`.

To run tests, use:

```bash
    make run-all-tests
```

## Usage

The app includes two database models, `Author` and `Book`. Its API supports basic CRUD operations such as adding, updating, or deleting books and authors.

After launching the app, you can access the API documentation at `localhost:8000/docs`.

To use the Django admin panel, first collect static files and create a superuser:

```bash
    python3 manage.py collectstatic
    python3 manage.py createsuperuser
```

Then, access the admin panel at `localhost:8001/admin`.

## Structure

Key components of the application are organized as follows:

- `src/settings.py`: Django settings configuration.
- `src/wsgi.py`: Standard Django WSGI application file.
- `src/main.py`: FastAPI setup and its integration with Django ORM.
- `src/urls.py`: Configures URLs for Django admin.
- `src/admin.py`: Registers models with the Django admin.
- `src/migrations`: Contains database migrations for both models.
- `src/books/`: Everything related to the book module.
- `src/authors/`: Everything related to the author module. 
