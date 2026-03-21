from sqlalchemy import Column, String, Enum
from sqlalchemy.dialects.mysql import CHAR
from uuid import uuid4
from database import Base
from database import criar_tabelas
from schema import statustask


class Usuario(Base):
    __tablename__ = "Usuarios"
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    

class Task(Base):
    __tablename__ = "Tarefas"
    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    status = Column(Enum(statustask), default=statustask.PENDENTE)


criar_tabelas()
