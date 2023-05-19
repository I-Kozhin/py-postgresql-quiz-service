from pydantic import BaseModel

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime

from .database import Base


class Question(Base):
    """
    Defines the questions model
    """

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(String(200), unique=True)
    answer_text = Column(String(200))
    creation_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, id: int, question_text: str, answer_text: str, creation_date: datetime):
        self.id = id
        self.question_text = question_text
        self.answer_text = answer_text
        self.creation_date = creation_date

    def __repr__(self) -> str:
        return f"<Question number {self.id}: {self.question_text}>"
