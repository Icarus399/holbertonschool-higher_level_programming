#!/usr/bin/python3
''' Write a script that adds the State object
"Louisiana" to the database '''

import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, orm

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        *argv[1:4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = orm.sessionmaker(bind=engine)()
    Louisiana = State(name="Louisiana")
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)
    session.close()
