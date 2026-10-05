import csv 
from sqlmodel import Session
from database import engine , create_db_and_tables
from models import Client   

create_db_and_tables()



with open ('clientes_customerflow.csv', 'r', encoding='utf-8 sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        client = Client(
            name=row['nome'],
            email=row['email'],
            phone=row['telefone']
        )
        with Session(engine) as session:
            session.add(client)
            session.commit()    
