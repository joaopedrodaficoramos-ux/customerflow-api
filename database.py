from pathlib import Path
from sqlmodel import SQLModel, create_engine
from models import Client  # Registra a tabela no metadata.
DATABASE_PATH = Path(__file__).resolve().parent / 'customerflow.db'
DATABASE_URL = f'sqlite:///{DATABASE_PATH.as_posix()}'
engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
