from enum import Enum
from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
    username: str
    password: str


class statustask(str, Enum):
    PENDENTE = "Pendente"
    EM_ANDAMENTO = "Em Andamento"
    CONCLUIDA = "Concluída"