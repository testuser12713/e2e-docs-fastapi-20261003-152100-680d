from datetime import datetime

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.schemas import Note
from app.state import notes


@pytest.fixture(autouse=True)
def _reset_notes() -> None:
    notes.clear()
    yield
    notes.clear()


def _seed_note(note_id: int = 1) -> None:
    notes[note_id] = Note(
        id=note_id,
        titel="Test",
        inhalt="Inhalt",
        tags=["a"],
        erstellt_am=datetime(2024, 1, 1, 12, 0, 0),
    )


def test_delete_existing_note_returns_204_and_removes_it() -> None:
    _seed_note(1)
    with TestClient(app) as client:
        response = client.delete("/notes/1")
    assert response.status_code == 204
    assert response.content == b""
    assert 1 not in notes


def test_delete_unknown_id_returns_404() -> None:
    with TestClient(app) as client:
        response = client.delete("/notes/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Notiz nicht gefunden"}
