import psycopg2 as pg

def create_connection():
    try:
        # Conexió a la base de dades
        # Retorna l'objecte de conexió per la resta de funcions SQL
        conn = pg.connect(
            database="postgres",
            user='admin',
            password='admin',
            host='localhost',
            port='5432'
        )
        return conn
    except(Exception, pg.Error) as error:
        print("Error: ", error)