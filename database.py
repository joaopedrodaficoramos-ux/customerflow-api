from sqlmodel import SQLModel, create_engine, Session
from models import Client   

DATABASE_URL = "sqlite:///customerflow.db"
engine = create_engine(DATABASE_URL, echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)    
