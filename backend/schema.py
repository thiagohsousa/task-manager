from enum import Enum
from pydantic import BaseModel


class statustask(str, Enum):
    PENDENTE = "PENDENTE"
    EM_ANDAMENTO = "EM_ANDAMENTO"
    CONCLUIDA = "CONCLUIDA"


class User(BaseModel):
    id: int
    email: str
    username: str


class Task(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: statustask
    usuario_id: int


