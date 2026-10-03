from fastapi import APIRouter, HTTPException

from app.schemas import Note

router = APIRouter()


@router.get("/notes/{id}", response_model=Note)
def get_note(id: int) -> Note:
    raise HTTPException(status_code=501, detail="GET /notes/{id} implements this")
