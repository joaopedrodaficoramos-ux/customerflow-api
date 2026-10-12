"""Importa o CSV em uma transação; reexecuções não duplicam e-mails."""
import csv
from pathlib import Path
from sqlmodel import Session, select
from database import engine, create_db_and_tables
from models import Client
CSV_PATH = Path(__file__).resolve().parent / 'data/clientes_customerflow.csv'
def importar():
    with CSV_PATH.open('r', encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)
        if not {'nome', 'email', 'telefone'}.issubset(reader.fieldnames or []):
            raise ValueError('CSV deve conter nome, email e telefone')
        rows = list(reader)
    for number, row in enumerate(rows, start=2):
        if any(not row[field] or not row[field].strip() for field in ('nome', 'email', 'telefone')):
            raise ValueError(f'Linha {number}: campos obrigatórios ausentes')
    create_db_and_tables()
    count = 0
    with Session(engine) as session:
        existing = set(session.exec(select(Client.email)).all())
        for row in rows:
            email = row['email'].strip()
            if email in existing:
                continue
            session.add(Client(name=row['nome'].strip(), email=email, phone=row['telefone'].strip()))
            existing.add(email)
            count += 1
        session.commit()
    print(f'{count} clientes importados')
if __name__ == '__main__':
    importar()
