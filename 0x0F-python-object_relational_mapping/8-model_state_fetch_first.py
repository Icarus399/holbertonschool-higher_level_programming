#!/usr/bin/python3
''' Write a script that prints the first State object from the database '''

from sys import argv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        *argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    if first is not None:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
