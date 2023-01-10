import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(String(250), unique=True, nullable=False)
    password = Column(String(8), nullable=False)

class User_Favorites(Base):
    __tablename__ = 'user_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id= Column(Integer, ForeignKey('character.characters_id'))
    user = relationship(User)
    characters = relationship(Characters)
  #  person = relationship(Person)

class Characters(Base):
    __tablename__ = 'characters'
    characters_id = Column(Integer, primary_key=True)
    characters_name = Column(String(80))
    status = Column(String(80))
    character_url = Column(String(100))
    species = Column(String(80))
    types = Column(String(80))
    gender = Column(String(80))
    image = Column(String(150))
    
class Episodes(Base):
    __tablename__='episodes'
    episode_id = Column(Integer, primary_key=True)
    name = Column(String(80))
    air_Date = Column(String(80))
    episode_numb = Column(String(80))

class Characters_Episodes(Base):
    __tablename__='Characters_Episodes'
    characters_episode_id = Column(Integer, primary_key=True)
    characters_id = Column(Integer,  ForeignKey('characters.characters_id'))
    episodes_id = Column(Integer, ForeignKey('episodes.episode_id'))
    characters = relationship(Characters)
    episodes = relationship(Episodes)
    
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
