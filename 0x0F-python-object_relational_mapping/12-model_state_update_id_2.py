#!/usr/bin/python3
""" script that changes the name of a State object from the database...
    ...hbtn_0e_6_usa: Adding New Mexico to state.id.like(2) """


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).filter(State.id.like(2)):
        state.name = 'New Mexico'
    session.commit()
    session.close()
