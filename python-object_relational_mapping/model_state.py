#!/usr/bin/python3
"""Write a python file that contains the
class definition of a State"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """state class linking to mysql table"""
    __tablename__ = 'states'

    # class attribute id that rep col of unique int, primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)

    # class attr name represents a col of a string with max 128 chars
    name = Column(String(128), nullable=False)
