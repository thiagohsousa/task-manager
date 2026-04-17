from contextlib import asynccontextmanager
from fastapi import FastAPI, Form, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db, criar_tabelas
from models import Task, Usuario
from crud import criar_usuario, criar_task, listar_task_usuario, deletar_task
from auth import router as auth_router, hash_password


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    criar_tabelas()
    yield
    # Shutdown


app = FastAPI(lifespan=lifespan)
    
templates = Jinja2Templates(directory="template")

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return RedirectResponse(url="/auth/login", status_code=303)

@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_page(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})


@app.post("/cadastro")
def cadastrar(db: Session = Depends(get_db), username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    
    print("SENHA RECEBIDA:", password)
    print("TAMANHO:", len(password))

    senha_hash = hash_password(password)

    novo_usuario = Usuario(
        username=username,
        email=email,
        password=senha_hash
    )

    db.add(novo_usuario)
    db.commit()

    return RedirectResponse(url="/auth/login", status_code=303)



@app.get("/auth/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


app.include_router(auth_router)

# 🔹 DASHBOARD
@app.get("/dashboard/{usuario_id}", response_class=HTMLResponse)
def dashboard(request: Request, usuario_id: int, db: Session = Depends(get_db)):

    tarefas = listar_task_usuario(db, usuario_id)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "tarefas": tarefas,
        "usuario_id": usuario_id
    })


# 🔹 CRIAR TAREFA
@app.post("/tarefa/criar")
def criar_tarefa(
    titulo: str = Form(...),
    descricao: str = Form(...),
    status: str = Form(...),
    usuario_id: int = Form(...),
    db: Session = Depends(get_db)
):
    criar_task(db, titulo, descricao, status, usuario_id)

    return RedirectResponse(url=f"/dashboard/{usuario_id}", status_code=303)


# 🔹 DELETAR
@app.post("/tarefas/deletar/{task_id}/{usuario_id}")
def deletar(task_id: int, usuario_id: int, db: Session = Depends(get_db)):

    deletar_task(db, task_id)

    return RedirectResponse(url=f"/dashboard/{usuario_id}", status_code=303)

@app.get("/tarefas/{usuario_id}")
def pagina_tarefas(request: Request, usuario_id: int, db: Session = Depends(get_db)):
    tarefas = listar_task_usuario(db, usuario_id)

    return templates.TemplateResponse("tarefas.html", {
        "request": request,
        "tarefas": tarefas,
        "usuario_id": usuario_id
    })