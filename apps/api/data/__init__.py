from sqlalchemy.orm import Session
from data.user import insert_users


def populate_database(session: Session):
    insert_users(session)
