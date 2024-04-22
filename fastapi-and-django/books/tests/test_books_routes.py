import pytest


from deepdiff import DeepDiff


@pytest.mark.usefixtures("db")
def test_get_all_books(books_app, client, books):
    response = client.get("v0/books")
    assert response.status_code == 200

    expected = [
        {
            "title": "Siddharta",
            "isbn": "9780553208849",
            "publication_date": "1922-01-01",
        },
        {
            "title": "Steppenwolf",
            "isbn": "9783518031599",
            "publication_date": "1924-01-01",
        },
        {
            "title": "The Glass Bead Game",
            "isbn": "9780030818516",
            "publication_date": "1943-01-01",
        },
    ]

    assert (
        DeepDiff(
            response.json(),
            expected,
            exclude_paths=[
                "root[0]['id']",
                "root[1]['id']",
                "root[2]['id']",
                "root[0]['author_id']",
                "root[1]['author_id']",
                "root[2]['author_id']",
            ],
        )
        == {}
    )
