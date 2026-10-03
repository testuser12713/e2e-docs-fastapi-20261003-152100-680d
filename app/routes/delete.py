from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.delete("/notes/{id}", status_code=204)
def delete_note(id: int) -> None:
    raise HTTPException(status_code=501, detail="DELETE /notes/{id} implements this")
