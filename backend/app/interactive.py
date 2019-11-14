"""
Run this to initiate the database session and imports for running code in iPython to interact with the db
"""

from app import sqlalchemy_models, pydantic_models
from app.database import SessionMaker, engine
db = SessionMaker()


item = pydantic_models.Note(id=1,title="test_title",content="test_content")
id = 1
note = db.query(sqlalchemy_models.Note).filter(sqlalchemy_models.Note.id == id).first()