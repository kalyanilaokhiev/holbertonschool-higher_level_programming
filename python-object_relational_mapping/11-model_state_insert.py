#!/usr/bin/python3
"""Write a script that prints the State
object with the name passed as argument from the
database hbtn_0e_6_usa"""
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

    # add
    add_state = State(name='Louisiana')
    session.add(add_state)
    session.commit

    # print results
    print(add_state.id)

    session.close()
