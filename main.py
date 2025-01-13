from fastapi import FastAPI
from pydantic import BaseModel, Field
import psycopg2 as pg
from connection import create_connection

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

@app.post("/insert/user")
async def add_user(user: Form):
    insert_user(user)
    return {"usuari": user}

def insert_user(user):
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = "INSERT INTO USUARIS(Nombre, Apellido, Email, Descripcion, Curso, Ano, Direccion, Codigo_Postal, Password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        values = (user.Nombre, user.Apellido, user.Correo_electronico, user.Descripcion, user.Curso, user.Ano, user.Direccion, user.Codigo_postal, user.Password)

        cursor.execute(query, values,)
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)

def user_schema(user) -> dict:
    return {
        "Nombre": user[0],
        "Apellido": user[1], # Aquí user[2] y user[3] serían password e email que son datos sensibles
        "Dirección": user[4],
        "Código postal": user[5],
        "Descripción": user[6],
        "Edad": user[7]
    }

def create_table_users():
    try:
        conn = create_connection()
        cursor = conn.cursor()

        query = """
                CREATE TABLE USUARIS(
                    Nombre VARCHAR,
                    Apellido VARCHAR,
                    Email VARCHAR,
                    Descripcion VARCHAR,
                    Curso INT,
                    Ano INT,
                    Direccion VARCHAR,
                    Codigo_Postal INT,
                    Password VARCHAR
                );
        """
        cursor.execute(query)
        conn.commit()
    except(Exception, pg.Error) as error:
        print("Error: ", error)
create_table_users()






