from books.core.authors.models import Author


class AuthorRepository:
    def __init__(self):
        pass

    def get_all(self):
        return Author.objects.all()

    def get(self, author_id: int) -> Author:
        return Author.objects.get(id=author_id)

    def delete(self, author_id: int) -> None:
        return Author.objects.get(id=author_id).delete()

    def create(self, name: str, bio: str = "") -> Author:
        author = Author.objects.create(name=name, bio=bio)
        return author
