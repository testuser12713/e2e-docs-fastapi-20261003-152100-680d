from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.state import notes


@pytest.fixture(autouse=True)
def clear_notes() -> None:
    notes.clear()
    yield
    notes.clear()


def test_create_note_returns_201_with_id_and_erstellt_am() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/notes",
            json={"titel": "Einkaufsliste", "inhalt": "Milch, Brot", "tags": ["einkauf"]},
        )

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["titel"] == "Einkaufsliste"
    assert body["inhalt"] == "Milch, Brot"
    assert body["tags"] == ["einkauf"]
    assert "erstellt_am" in body
    datetime.fromisoformat(body["erstellt_am"])


def test_create_note_assigns_sequential_ids() -> None:
    with TestClient(app) as client:
        first = client.post("/notes", json={"titel": "A", "inhalt": "x"})
        second = client.post("/notes", json={"titel": "B", "inhalt": "y"})

    assert first.status_code == 201
    assert second.status_code == 201
    assert first.json()["id"] == 1
    assert second.json()["id"] == 2


def test_create_note_defaults_tags_to_empty_list() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "Ohne Tags", "inhalt": "x"})

    assert response.status_code == 201
    assert response.json()["tags"] == []


def test_create_note_with_empty_titel_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "", "inhalt": "x"})

    assert response.status_code == 422


def test_create_note_with_101_char_titel_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post("/notes", json={"titel": "a" * 101, "inhalt": "x"})

    assert response.status_code == 422


def test_create_note_with_more_than_5_tags_returns_422() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/notes",
            json={
                "titel": "Zu viele Tags",
                "inhalt": "x",
                "tags": ["a", "b", "c", "d", "e", "f"],
            },
        )

    assert response.status_code == 422
