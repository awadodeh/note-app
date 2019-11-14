"""
Defines the FastAPI
"""

from datetime import datetime
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.cors import CORSMiddleware

from app.database import SessionMaker, engine
from app import sqlalchemy_models, pydantic_models


# Dependency
def get_db(request: Request):
    return request.state.db


def init_data():
    db = SessionMaker()
    if db.query(sqlalchemy_models.Note).count() == 0:
        entry = sqlalchemy_models.Note(
            title="Todo",
            content="Learn FastAPI\nLearn React\nLearn Docker\nMake fullstack example app\nDeploy it\nGet feedback"
        )
        db.add(entry)
        db.commit()

        entry = sqlalchemy_models.Note(
            title="Shopping List",
            content="Lettuce\nChicken\nCroutons\nBread"
        )
        db.add(entry)
        db.commit()

        entry = sqlalchemy_models.Note(
            title="Latin Notes",
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt. " * 10
        )
        db.add(entry)
        db.commit()

    # Allow CORS between frontend and backend on different ports
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# Initialize the database (normally you should use Alembic for this)
sqlalchemy_models.Base.metadata.create_all(bind=engine)
# Create the app
app = FastAPI()
init_data()

# Create middleware to handle sessions. We want to have an independent database session/connection (SessionLocal)
# per request, use the same session through all the request and then close it after the request is finished.
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionMaker()
        response = await call_next(request)
    finally:
        request.state.db.commit()
        request.state.db.close()
    return response


# Get all notes
@app.get("/notes/", response_model=List[pydantic_models.Note])
def get_notes(db: Session = Depends(get_db)):
    return db.query(sqlalchemy_models.Note).all()


# Get specific note
@app.get("/notes/{id}", response_model=List[pydantic_models.Note])
def get_note(id: int, db: Session = Depends(get_db)):
    return db.query(sqlalchemy_models.Note).filter(sqlalchemy_models.Note.id == id).first()


# Add new note
@app.post("/notes/", response_model=pydantic_models.NoteCreate)
def add_note(item: pydantic_models.NoteCreate, db: Session = Depends(get_db)):
    new_item = sqlalchemy_models.Note(item.dict())
    db.add(new_item)
    return new_item


# Update specific note
@app.put("/notes/{id}", response_model=pydantic_models.NoteCreate)
def update_note(id: int, item: pydantic_models.NoteCreate, db: Session = Depends(get_db)):
    note = db.query(sqlalchemy_models.Note).filter(sqlalchemy_models.Note.id == id).first()
    for key, val in item.dict().items():
        setattr(note, key, val)
    return note
