#!/usr/bin/python3
''' Write a script that prints the State object
with the name passed as argument from the database '''

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        *argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(
        State.id).filter(State.name == argv[4]).all()
    if (states):
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
