from sqlalchemy import create_engine, Column,Integer, String, Float,ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index = True)
    titulo = Column(String, nullable=True)
    descricao = Column(String)
    preco = Column(Float, nullable=False)