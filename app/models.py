from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .database import Base


class Question(Base):
    """
    Defines the questions model
    """

    __tablename__ = "questions"
    # генерить uuid4 primary key
    # или генерить уникальный id через число (просто инт или через дату) 1, 2, 3, 4, 5...
    # unique=True – if True, create a unique index
    question_id = Column(Integer, primary_key=True, index=True, unique=True)
    question_text = Column(String)  # нужен ли unique ?
    answer_text = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, question_id: int, question_text: str, answer_text: str, creation_date: datetime):
        self.question_id = question_id
        self.question_text = question_text
        self.answer_text = answer_text
        self.creation_date = creation_date
