# Módulo para definir los modelos de datos (SQLAlchemy)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500)) 
    completed = Column(Boolean, default=False)

def create_tables(engine):
    Base.metadata.create_all(engine)  # Crea las tablas si no existen