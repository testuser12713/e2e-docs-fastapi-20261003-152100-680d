from fastapi import APIRouter, HTTPException

from app.schemas import Note

router = APIRouter()


@router.get("/notes", response_model=list[Note])
def list_notes(tag: str | None = None) -> list[Note]:
    raise HTTPException(status_code=501, detail="GET /notes implements this")
