# Import necessary modules from SQLAlchemy
import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# Create a base class for declarative models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'  # Specify the table name

    # Define the columns for the table 'users'
    id = Column(Integer, primary_key=True)  # id column (primary key)
    username = Column(String)  # username column
    password = Column(String)  # password column
    # favorites column will be defined later as a relationship

# Define the Character model
class Character(Base):
    __tablename__ = 'characters'  # Specify the table name

    # Define the columns for the table 'characters'
    id = Column(Integer, primary_key=True)  # id column (primary key)
    name = Column(String)  # name column
    # favorites column will be defined later as a relationship

# Define the Planet model
class Planet(Base):
    __tablename__ = 'planets'  # Specify the table name

    # Define the columns for the table 'planets'
    id = Column(Integer, primary_key=True)  # id column (primary key)
    name = Column(String)  # name column
    # favorites column will be defined later as a relationship

# Define the Starship model
class Starship(Base):
    __tablename__ = 'starships'  # Specify the table name

    # Define the columns for the table 'starships'
    id = Column(Integer, primary_key=True)  # id column (primary key)
    name = Column(String)  # name column
    # favorites column will be defined later as a relationship

# Define the Favorite model
class Favorite(Base):
    __tablename__ = 'favorites'  # Specify the table name

    # Define the columns for the table 'favorites'
    id = Column(Integer, primary_key=True)  # id column (primary key)
    user_id = Column(Integer, ForeignKey('users.id'))  # user_id column (foreign key)
    character_id = Column(Integer, ForeignKey('characters.id'))  # character_id column (foreign key)
    planet_id = Column(Integer, ForeignKey('planets.id'))  # planet_id column (foreign key)
    starship_id = Column(Integer, ForeignKey('starships.id'))  # starship_id column (foreign key)

    # Define the relationships
    user = relationship(User, backref='favorites')  # relationship with User
    character = relationship(Character, backref='favorites')  # relationship with Character
    planet = relationship(Planet, backref='favorites')  # relationship with Planet
    starship = relationship(Starship, backref='favorites')  # relationship with Starship


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')