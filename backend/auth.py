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
    print(f"Login attempt for username: '{username}'")
    user = autenticar_usuario(db, username, password)

    if user:
        print(f"Login SUCCESS for user.id: {user.id}")
        return RedirectResponse(url=f"/dashboard/{user.id}", status_code=303)

    print("Login FAILED - invalid creds")
    return RedirectResponse(url="/auth/login?error=1", status_code=303)
