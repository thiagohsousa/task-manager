from sqlalchemy.orm import Session
from models import Usuario
from schema import User



def criar_usuario(db: Session, user: User):
    novo_usuario = Usuario(
        username=user.username,
        email=user.email, 
        password=user.password
    )
    db.add(novo_usuario)
    db.commit()

    return novo_usuario

