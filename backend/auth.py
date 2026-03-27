from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from passlib.context import CryptContext
from passlib.context import CryptContext

from database import get_db
from models import Usuario

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)



bcrypt_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    return bcrypt_context.hash(password)

def verify_password(password: str, hashed_password: str):
    return bcrypt_context.verify(password, hashed_password)


def autenticar_usuario(db: Session, username: str, password: str):
    user = db.query(Usuario).filter(Usuario.username == username).first()

    if not user:
        return False

    if not verify_password(password, user.password):
        return False

    return user


@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = autenticar_usuario(db, username, password)

    if user:
        return RedirectResponse(url=f"/dashboard/{user.id}", status_code=303)

    return RedirectResponse(url="/login", status_code=303)
