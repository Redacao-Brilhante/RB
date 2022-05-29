from sqlalchemy import Column, Integer, Table, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class Role(Base):
    __tablename__ = "role"

    id: int = Column("id", Integer, nullable=False, primary_key=True)

    name: str = Column(String, nullable=False)

    slug: str = Column(String, nullable=False)

    permissions: list['Permission'] = relationship("Permission", secondary="roles_permissions")

    users: list['User'] = relationship("User", secondary="users_roles")


class Permission(Base):
    __tablename__ = "permission"

    id: int = Column("id", Integer, nullable=False, primary_key=True)

    name: str = Column(String, nullable=False)

    description: str = Column("description", String, nullable=False)

    roles: list[Role] = relationship("Role", secondary="roles_permissions", back_populates="permissions")


role_permission_association = Table(
    "roles_permissions", Base.metadata,

    Column("role_id", Integer, ForeignKey("role.id")),
    Column("permission_id", Integer, ForeignKey("permission.id"))
)
