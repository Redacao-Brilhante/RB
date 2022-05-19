from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from models.user.basic import User


class Essay(Base):
    __tablename__ = "essay"

    id: int = Column("id", Integer, primary_key=True)

    writing_skill_1: int = Column(Integer, nullable=False)
    writing_skill_2: int = Column(Integer, nullable=False)
    writing_skill_3: int = Column(Integer, nullable=False)
    writing_skill_4: int = Column(Integer, nullable=False)
    writing_skill_5: int = Column(Integer, nullable=False)

    user_id: int = Column(Integer, ForeignKey("user.id"))
    user: User = relationship("User", back_populates="essays")
