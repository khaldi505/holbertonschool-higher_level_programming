#!/usr/bin/python3
"""the class definition of a State"""


from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """ the state class """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128),
                  nullable=False)
