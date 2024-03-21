#!/usr/bin/python3
"""printing all city objects"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

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

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
