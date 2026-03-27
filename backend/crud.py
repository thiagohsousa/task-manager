from sqlalchemy.orm import Session
from models import Usuario, Task


# ------------------ USUÁRIO ------------------

def criar_usuario(db: Session, username: str, email: str, password: str):
    novo_usuario = Usuario(
        username=username,
        email=email,
        password=password
    )
    db.add(novo_usuario)
    db.commit()
    return novo_usuario


def listar_usuarios_por_nome(db: Session, nome: str):
    return db.query(Usuario).filter(Usuario.username == nome).all()


def listar_usuarios_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).all()


def atualizar_usuario(db: Session, user_id: int, username: str, email: str, password: str):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()

    if usuario:
        usuario.username = username
        usuario.email = email
        usuario.password = password
        db.commit()
        return usuario

    raise ValueError("Usuário não encontrado")


def deletar_usuario(db: Session, user_id: int):
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()

    if usuario:
        db.delete(usuario)
        db.commit()
    else:
        raise ValueError("Usuário não encontrado")


# ------------------ TAREFAS ------------------

def criar_task(db: Session, titulo: str, descricao: str, status: str, usuario_id: int):
    nova_task = Task(
        titulo=titulo,
        descricao=descricao,
        status=status,
        usuario_id=usuario_id
    )
    db.add(nova_task)
    db.commit()
    return nova_task


def listar_task_usuario(db: Session, usuario_id: int):
    return db.query(Task).filter(Task.usuario_id == usuario_id).all()


def deletar_task(db: Session, task_id: int):
    tarefa = db.query(Task).filter(Task.id == task_id).first()

    if not tarefa:
        raise ValueError("Tarefa não encontrada")

    db.delete(tarefa)
    db.commit()