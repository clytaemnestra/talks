from django.contrib import admin

from src.authors.models import Author
from src.books.models import Book

admin.site.register(Book)
admin.site.register(Author)
