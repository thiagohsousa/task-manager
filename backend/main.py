from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
#from database import SessionLocal, engine, Base
#from models import User, Task
#from auth import hash_password, verify_password

app = FastAPI()