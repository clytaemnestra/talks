from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["title", "author"]

    def __str__(self):
        return self.title
