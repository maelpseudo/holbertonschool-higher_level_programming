#!/usr/bin/python3
"""delete all State objects containing the letter a"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """Creating a connection to the MySQL server"""
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db))

    """Creating a session hight level interface"""
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).filter(State.name.ilike('%a%')):
        session.delete(state)

    session.commit()
    session.close()
