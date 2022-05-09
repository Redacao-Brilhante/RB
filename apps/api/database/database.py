import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


BASE_DIRECTORY = os.path.join(os.path.dirname(__file__), '..')

SQLALCHEMY_DATABASE_URL = f'sqlite:///{os.path.join(BASE_DIRECTORY, "app_event.db")}'

engine = create_engine(echo=True, url=SQLALCHEMY_DATABASE_URL, **{
    'connect_arginsert_userss': {
        'check_same_thread': False
    },
    'poolclass': StaticPool
})

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
Base = declarative_base()


def init_database():
    Base.metadata.create_all(engine)


def get_session():
    return session
