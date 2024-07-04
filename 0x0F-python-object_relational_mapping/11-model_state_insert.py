#!/usr/bin/python3
""" Adds a state object to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Louis = State(name='Louisiana')
    session.add(Louis)
    session.commit()
    instance = session.query(State).filter_by(name='Louisiana').first()
    print(instance.id)
