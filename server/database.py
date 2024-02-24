from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHELMY_DATABASE_URI = 'sqlite:///./database.db'

engine = create_engine(SQLALCHELMY_DATABASE_URI, connect_args={"check_same_thread": False})

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    '''Get the database instance from the local session'''
    db = Session()
    try:
        yield db
    finally:
        db.close()