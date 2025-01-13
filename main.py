from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Form(BaseModel):
    Nombre: str
    Apellido: str
    Correo_electronico: str
    Descripcion: str | None = None
    Curso: int
    Ano: int
    Direccion: str
    Codigo_postal: int | None = None
    Password: str









