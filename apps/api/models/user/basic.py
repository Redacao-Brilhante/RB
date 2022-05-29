import datetime

from sqlalchemy import Column, Table, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.database import Base


class User(Base):
    __tablename__ = "user"

    id: int = Column("id", Integer, primary_key=True)

    name: str = Column(String, nullable=False)

    full_name: str = Column(String, nullable=False)

    email: str = Column(String, unique=True, nullable=False)

    password: str = Column(String, nullable=False)

    active: bool = Column(Boolean, default=True)

    date_created: datetime = Column(DateTime, )

    roles: list['Role'] = relationship("Role", secondary="users_roles", back_populates="users")

    essays: list['Essay'] = relationship("Essay", back_populates="user")

    def __repr__(self):
        return f"User(name: {self.name}, id: {self.id})"


user_roles_association = Table(
    "users_roles", Base.metadata,

    Column("user_id", Integer, ForeignKey("user.id")),
    Column("role_id", Integer, ForeignKey("role.id"))
)
