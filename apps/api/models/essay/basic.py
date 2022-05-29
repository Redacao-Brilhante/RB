from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database.database import Base


class Essay(Base):
    __tablename__ = "essay"

    id: int = Column("id", Integer, primary_key=True)

    user_id: int = Column(Integer, ForeignKey("user.id"))
    user: 'User' = relationship("User", back_populates="essays")

    writing_skills: list['WritingSkill'] = relationship("WritingSkill", back_populates="essay")


class WritingSkill(Base):
    __tablename__ = "writing_skill"

    id: int = Column("id", Integer, primary_key=True)

    essay_id: int = Column(Integer, ForeignKey("essay.id"))
    essay: Essay = relationship("Essay", back_populates="writing_skills")

    name: str = Column(String, nullable=False)

    slug: str = Column(String, unique=True, nullable=False)

    description: str = Column(String, nullable=False)

    score: int = Column(Integer)
