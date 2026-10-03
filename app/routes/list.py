from fastapi import APIRouter

from app.schemas import Note
from app.state import notes

router = APIRouter()


@router.get("/notes", response_model=list[Note])
def list_notes(tag: str | None = None) -> list[Note]:
    result = list(notes.values())
    if tag is not None:
        result = [note for note in result if tag in note.tags]
    return sorted(result, key=lambda note: note.id)
