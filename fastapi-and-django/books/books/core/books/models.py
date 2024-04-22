from django.db import models

from books.core.authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["title"]
