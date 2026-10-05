from fastapi import FastAPI
from sqlmodel import SQLModel, Session, select 
from models import Client
from database import engine, create_db_and_tables


app = FastAPI()
create_db_and_tables()

@app.get("/clients")
def list_clients():
    with Session(engine) as session:
        clients = session.exec(select(Client)).all()
        return clients      
@app.get("/clients/{client_id}")    
def get_client(client_id: int):
    with Session(engine) as session:
        client = session.get(Client, client_id)
        if client:
            return client
        
        return {"error": "Client not found"}
    