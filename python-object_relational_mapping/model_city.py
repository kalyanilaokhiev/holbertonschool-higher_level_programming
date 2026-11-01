#!/usr/bin/python3
"""Write a python file that contains the
class definition of a State"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """state class linking to mysql table"""
    __tablename__ = 'citites'

    # class attribute id that rep col of unique int, primary key
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)

    # class attr name represents a col of a string with max 128 chars
    name = Column(String(128), nullable=False)

    # state_id that represents a col of an int, and
    # is a foreign key to states.id
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
