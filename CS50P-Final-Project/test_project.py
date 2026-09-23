import project
import requests


def test_special_string():
    assert (
        project.special_string(
            "this was cs50, an introduction to programming with python", "+"
        )
        == "this+was+cs50+an+introduction+to+programming+with+python"
    )
    assert project.special_string("j. k. rowling", "%20") == r"j%20k%20rowling"
    assert project.special_string("non-fiction", "_") == "non_fiction"


class MockingBird:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data


def test_search(monkeypatch, capsys):
    monkeypatch.setattr(
        "builtins.input",
        lambda useless_value: "Harry Potter and the Philosopher's Stone",
    )

    monkeypatch.setattr(
        requests,
        "get",
        lambda link: (
            MockingBird(
                {
                    "docs": [
                        {
                            "title": "Harry Potter and the Philosopher's Stone",
                            "author_name": ["J. K. Rowling"],
                            "first_publish_year": 1997,
                            "key": "/works/OL82563W",
                            "edition_count": 120,
                        }
                    ]
                }
            )
            if "search.json" in link
            else MockingBird({"summary": {"average": 4.8}})
        ),
    )

    project.search()
    output = capsys.readouterr().out

    assert "Harry Potter and the Philosopher's Stone" in output
    assert "J. K. Rowling" in output
    assert "1997" in output
    assert "4.80" in output


def test_recommend_by_genre(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda usless_value: "fantasy")

    monkeypatch.setattr(
        requests,
        "get",
        lambda link: MockingBird(
            {
                "works": [
                    {"title": "Harry Potter and the Philosopher's Stone"},
                    {"title": "A Song of Ice and Fire"},
                    {"title": "To Kill a MockingBird"},
                ]
            }
        ),
    )

    project.recommend_by_genre()
    output = capsys.readouterr().out

    assert "Harry Potter and the Philosopher's Stone" in output
    assert "A Song of Ice and Fire" in output
    assert "To Kill a MockingBird" in output


def test_view_author(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda useless_value: "J. K. Rowling")

    def get(link):
        if "search/authors.json" in link:
            return MockingBird({"docs": [{"key": "/authors/OL23919A"}]})
        elif "authors/OL23919A.json" in link:
            return MockingBird(
                {
                    "bio": {
                        "value": "The most famous of Authors who gave birth to the Harry Potter series."
                    }
                }
            )
        elif "authors/OL23919A/works.json" in link:
            return MockingBird(
                {
                    "entries": [
                        {"title": "Harry Potter and the Philosopher's Stone"},
                        {"title": "Harry Potter and the Chamber of Secrets"},
                        {"title": "Harry Potter and the Prisoner of Azkaban"},
                    ]
                }
            )
        return MockingBird({})

    monkeypatch.setattr(requests, "get", get)

    project.view_author()
    output = capsys.readouterr().out

    assert "Author: J. K. Rowling" in output
    assert "Harry Potter and the Philosopher's Stone" in output
    assert "Harry Potter and the Chamber of Secrets" in output
    assert "Harry Potter and the Prisoner of Azkaban" in output
