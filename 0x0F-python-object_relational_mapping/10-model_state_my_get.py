#!/usr/bin/python3
""" script that lists all State objects
 from the database hbtn_0e_6_usa """
from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    a = False
    for state in session.query(State).order_by(State.id).all():
        if (argv[4] == state.name):
            print("{}".format(state.id))
            a = True
    if not (a):
        print("Not found")
    session.close()
