#!/usr/bin/python3
''' Write a script that prints all city objects from the database '''

import sqlalchemy
from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(*argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()
    cities = (session
              .query(State.name, City.id, City.name)
              .filter(City.state_id == State.id)
              .order_by(City.id))
    for city in cities:
        print("{}: ({}) {}".format(*city))
    session.close()
