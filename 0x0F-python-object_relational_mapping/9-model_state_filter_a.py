#!/usr/bin/python3
"""lists all state objects that contain the letter a from the
    hbtn_0e_6_usa database"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == '__main__':
    url = "mysql+mysqldb://{}:{}@localhost:\
            3306/{}".format(argv[1], argv[2], argv[3])
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()

    ab = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for item in ab:
        print(item.id, item.name, sep=": ")
