from django.db import models

from src.authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
