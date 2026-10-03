from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.schemas import Note
from app.state import notes


@pytest.fixture(autouse=True)
def reset_notes() -> None:
    notes.clear()
    yield
    notes.clear()


def _note(id: int, tags: list[str] | None = None) -> Note:
    return Note(
        id=id,
        titel=f"Titel {id}",
        inhalt=f"Inhalt {id}",
        tags=tags or [],
        erstellt_am=datetime(2026, 1, 1, 12, 0, 0),
    )


def test_list_notes_empty() -> None:
    with TestClient(app) as client:
        response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == []


def test_list_notes_returns_all_sorted_by_id() -> None:
    notes[3] = _note(3, tags=["arbeit"])
    notes[1] = _note(1, tags=["privat"])
    notes[2] = _note(2, tags=["arbeit", "privat"])

    with TestClient(app) as client:
        response = client.get("/notes")

    assert response.status_code == 200
    data = response.json()
    assert [note["id"] for note in data] == [1, 2, 3]
    assert data[0] == {
        "id": 1,
        "titel": "Titel 1",
        "inhalt": "Inhalt 1",
        "tags": ["privat"],
        "erstellt_am": "2026-01-01T12:00:00",
    }


def test_list_notes_filtered_by_tag() -> None:
    notes[1] = _note(1, tags=["arbeit"])
    notes[2] = _note(2, tags=["privat"])
    notes[3] = _note(3, tags=["arbeit", "privat"])

    with TestClient(app) as client:
        response = client.get("/notes", params={"tag": "arbeit"})

    assert response.status_code == 200
    data = response.json()
    assert [note["id"] for note in data] == [1, 3]


def test_list_notes_filtered_by_tag_no_match() -> None:
    notes[1] = _note(1, tags=["arbeit"])

    with TestClient(app) as client:
        response = client.get("/notes", params={"tag": "unbekannt"})

    assert response.status_code == 200
    assert response.json() == []
