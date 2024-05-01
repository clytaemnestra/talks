from django.contrib import admin

from books.core.authors.models import Author
from books.core.books.models import Book

admin.site.register(Book)
admin.site.register(Author)
