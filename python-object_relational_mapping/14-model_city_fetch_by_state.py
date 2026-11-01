#!/usr/bin/python3
"""Write a script that deletes all State objects with
a name containing the letter a from the database
hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City

import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # ready to start talking to the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    queries = session.query(State, City)
    queries = queries.filter(State.id == City.state_id)
    queries = queries.order_by(City.id.asc()).all()

    # print results
    for state, city in queries:
        print("{}: ({}) {}".format(state.name, state.id, city.name))

    session.close()
