#!/usr/bin/python3
""" This module contains the class definition of a city"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetaData = MetaData()
Base = declarative_base(metadata=mymetaData)

class City(Base):
    """ Defines a table called cities"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
