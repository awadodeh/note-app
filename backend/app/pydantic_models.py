"""
Create the Pydantic models used for request and response data validation.
"""

from pydantic import BaseModel


class Note(BaseModel):
    id: int = None
    title: str = None
    content: str = None

    class Config:
        orm_mode = True


class NoteCreate(BaseModel):
    title: str = None
    content: str = None

    class Config:
        orm_mode = True
