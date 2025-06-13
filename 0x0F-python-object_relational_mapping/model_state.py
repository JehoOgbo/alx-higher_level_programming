#!/usr/bin/python3
""" defines a state class """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetaData = MetaData()
Base = declarative_base()


class State(Base):
    """
    Class with id and name attributes of each state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
