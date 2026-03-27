from enum import Enum
from pydantic import BaseModel


class statustask(str, Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"


class User(BaseModel):
    id: int
    email: str
    username: str
    password: str


class task(BaseModel):
    id: int
    titulo: str
    descricao: str
    status: statustask


