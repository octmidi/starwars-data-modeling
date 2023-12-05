import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table usuario
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    password = Column(String(250),nullable=False )
    name = Column(String(250), nullable=False)
    mail = Column(String(250), nullable= False)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table planeta.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)   

class Personaje(Base):
    __tablename__='personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable = False)
    planeta_id= Column(Integer, ForeignKey('planeta.id'))

class Favorito(Base):
    __tablename__='favorito'
    id = Column(Integer, primary_key=True)
    usario_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id= Column(Integer, ForeignKey('planeta.id'))
    personaje_id = Column(Integer),ForeignKey('personaje.id') 


class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    usario_id = Column(Integer, ForeignKey('usuario.id'))
    contenido = Column(String(250))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
