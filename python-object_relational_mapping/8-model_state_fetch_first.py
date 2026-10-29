#!/usr/bin/python3
"""Write a script that prints the first State object
 from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
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
    states = session.query(State)
    states = states.order_by(State.id.asc()).all()

    # print results
    if states is None:
        print("Nothing\n")
    else:
        print("{}: {}".format(states[0].id, states[0].name))

    session.close()
