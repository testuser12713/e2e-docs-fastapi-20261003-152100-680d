from fastapi import APIRouter, HTTPException

from app.state import notes

router = APIRouter()


@router.delete("/notes/{id}", status_code=204)
def delete_note(id: int) -> None:
    if id not in notes:
        raise HTTPException(status_code=404, detail="Notiz nicht gefunden")
    del notes[id]
