from datetime import UTC, datetime

from fastapi import APIRouter

from app.schemas import Note, NoteCreate
from app.state import notes

router = APIRouter()


@router.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate) -> Note:
    note_id = max(notes.keys(), default=0) + 1
    created = Note(
        id=note_id,
        titel=note.titel,
        inhalt=note.inhalt,
        tags=note.tags,
        erstellt_am=datetime.now(UTC),
    )
    notes[note_id] = created
    return created
