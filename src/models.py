import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}


class User(Base):
    __tablename__ = 'user'   
    id = Column(Integer, primary_key=True)
    user_name= Column(String(250), nullable=False)
    password= Column(String(250), nullable=False)



class Character(Base):
    __tablename__ = 'character'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    

class Planet(Base):
    __tablename__ = 'planet'  
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    


class Favorite(Base):
    __tablename__ = 'favorite'
   
    id = Column(Integer, primary_key=True)  
    name = Column(String(250), nullable=False) 
    user_id = Column(Integer, ForeignKey('user.id'))
    person = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)



    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
