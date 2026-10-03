from datetime import UTC, datetime

from fastapi.testclient import TestClient

from app.main import app
from app.schemas import Note
from app.state import notes


def test_get_existing_note_returns_200_with_correct_note() -> None:
    notes.clear()
    notes[1] = Note(
        id=1,
        titel="Einkaufsliste",
        inhalt="Milch, Butter, Brot",
        tags=["einkauf"],
        erstellt_am=datetime.now(UTC),
    )

    with TestClient(app) as client:
        response = client.get("/notes/1")

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == 1
    assert body["titel"] == "Einkaufsliste"
    assert body["inhalt"] == "Milch, Butter, Brot"
    assert body["tags"] == ["einkauf"]
    assert body["erstellt_am"] is not None


def test_get_unknown_note_returns_404() -> None:
    notes.clear()

    with TestClient(app) as client:
        response = client.get("/notes/999")

    assert response.status_code == 404
    assert "detail" in response.json()
