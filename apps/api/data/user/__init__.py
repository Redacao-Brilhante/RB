from sqlalchemy.orm import Session
from models.user.basic import User
from faker import Faker
from models.user.permissions import admin, student, teacher


def insert_users(session: Session):
    fake = Faker()

    admin_user = User(
        name="admin", password="admin", full_name="admin", email="admin@rb.com", roles=[admin]
    )

    adryell_user = User(
        name="Adryell", password="rb123", full_name="Paulo Adryell", email="adryell@rb.com", roles=[admin]
    )

    felipe_user = User(
        name="Felipe", password="rb123", full_name="Felipe Anderson", email="felipe@rb.com", roles=[admin]
    )

    hell_user = User(
        name="Hellyson", password="rb123", full_name="Hellyson Ferreira", email="hellyson@rb.com", roles=[admin]
    )

    fake_users = [
        User(name=fake.name(), password=fake.password(), full_name=fake.name(), email=fake.email(), roles=[student])
        for _ in range(3)
    ]

    user_list = [
        admin_user,
        adryell_user,
        hell_user,
        felipe_user,
        *fake_users
    ]

    for current_user in user_list:
        user = session.query(User).filter(User.email == current_user.email).one_or_none()
        if not user:
            session.add(current_user)

    session.commit()
