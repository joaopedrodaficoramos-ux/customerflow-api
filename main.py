from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query
from sqlmodel import Session, select
from models import Client
from database import engine, create_db_and_tables
@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield
app = FastAPI(title='Customerflow - Consulta de clientes', lifespan=lifespan)
@app.get('/clients', response_model=list[Client])
def list_clients(limit: int = Query(100, ge=1, le=1000), offset: int = Query(0, ge=0)):
    with Session(engine) as session:
        return session.exec(select(Client).order_by(Client.id).offset(offset).limit(limit)).all()
@app.get('/clients/{client_id}', response_model=Client)
def get_client(client_id: int):
    with Session(engine) as session:
        client = session.get(Client, client_id)
        if client is None:
            raise HTTPException(status_code=404, detail='Cliente não encontrado')
        return client
