from fastapi import APIRouter, HTTPException

from app.schemas import Note
from app.state import notes

router = APIRouter()


@router.get("/notes/{id}", response_model=Note)
def get_note(id: int) -> Note:
    note = notes.get(id)
    if note is None:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    return note
