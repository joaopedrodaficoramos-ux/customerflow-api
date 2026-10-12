# Customerflow API

API de consulta de clientes com FastAPI, SQLModel e SQLite. Projeto de portfólio que demonstra modelagem de uma tabela, importação de CSV e leitura de registros por endpoints.

## Executar (Python 3.10+)
Na raiz do repositório:
```bash
python -m pip install -r requirements.txt
python import_csv.py
python -m uvicorn main:app --reload
```
Abra http://127.0.0.1:8000/docs para testar pela documentação interativa.

## Funcionalidades
- `GET /clients?limit=100&offset=0`: lista paginada, ordenada pelo ID.
- `GET /clients/{client_id}`: consulta individual; retorna HTTP 404 quando não há registro.
- Importação do CSV em uma transação, validação de campos obrigatórios e prevenção de duplicações por e-mail na reexecução do importador.
- Banco local criado automaticamente; caminhos independem da pasta atual do terminal.

## Estrutura
- `main.py`: aplicação e endpoints.
- `models.py`: modelo Client (ID, nome, e-mail e telefone).
- `database.py`: configuração e criação do SQLite.
- `import_csv.py`: importação de dados.
- `data/clientes_customerflow.csv`: base de exemplo existente.
- `requirements.txt` e `.gitignore`: dependências e exclusão de arquivos gerados.

## Escopo
A aplicação oferece consulta e importação local; não implementa criação, alteração e exclusão por API. É uma demonstração para uso local, sem autenticação. A prevenção por e-mail ocorre no importador sequencial, não é uma restrição de unicidade no banco. Antes de disponibilizar uma API com dados pessoais, use uma base fictícia e implemente os controles necessários.
