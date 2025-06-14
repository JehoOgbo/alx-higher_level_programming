#!/usr/bin/python3
""" prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa """
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
                                                       argv[2], argv[3])
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

objective = session.query(State).filter(State.name == argv[4]).scalar()
if objective is None:
    print("Not found")
else:
    print(objective.id)
