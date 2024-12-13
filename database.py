# Módulo para manejar la conexión a la base de datos

import mysql.connector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import create_tables  # Importa la función para crear tablas

# Configuración de la base de datos
DB_USER = 'root'
DB_PASSWORD = 'rokoopercp'
DB_HOST = 'localhost'
DB_NAME = 'todoapp'

# Crear conexión a MySQL para crear la base de datos
def create_database_if_not_exists():
    connection = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    connection.close()

# Llamar a la función para crear la base de datos
create_database_if_not_exists()

# Crear la URL de conexión para SQLAlchemy
DATABASE_URL = f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

# Crear el motor y la sesión
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()

# Crear las tablas si no existen
create_tables(engine)  # Pasa el engine a la función