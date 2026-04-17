from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from database import Base
from schema import statustask


class Usuario(Base):
    __tablename__ = "Usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)


class Task(Base):
    __tablename__ = "Tarefas"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    status = Column(Enum(statustask), default=statustask.PENDENTE)
    usuario_id = Column(Integer, ForeignKey("Usuarios.id"), nullable=False)
