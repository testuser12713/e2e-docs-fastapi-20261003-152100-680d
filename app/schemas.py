from datetime import datetime

from pydantic import BaseModel, Field


class Note(BaseModel):
    id: int
    titel: str
    inhalt: str
    tags: list[str]
    erstellt_am: datetime


class NoteCreate(BaseModel):
    titel: str = Field(min_length=1, max_length=100)
    inhalt: str
    tags: list[str] = Field(default_factory=list, max_length=5)
