from sqlalchemy import create_engine, Column,Integer, String, Float,ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# constrói a URL de conexão do banco de dados usando as variáveis de ambiente
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# cria um motor de banco de dado SQLAlchemy que gerencia as conexões à base de dados
engine = create_engine(DATABASE_URL)

# cria uma fábrica de sessões do SQLAlchemy que será usada para criar sessões
SessionLocal = sessionmaker(bind = engine, autoflush = False, autocommit = False)

# cria uma classe base declarativa para os modelos do SQLAlchemy
Base = declarative_base()

# define uma função geradora que fornece uma sessão de banco de dados e garante o fechamento da sessão
def get_db():
    db = SessionLocal()
    try:
        yield db # fornece a sessão para a operação (utilizado em dependências do FastAPI)
    finally:
        db.close()
