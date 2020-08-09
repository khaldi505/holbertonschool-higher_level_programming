#!/usr/bin/python3
''' i'll update this late '''
import sys
from model_state import Base, state
import sqlalchemy
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        "root", "root", "my_db"), pool_pre_ping=True)
    Base.metadata.create_all(engine)
