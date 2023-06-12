from sqlalchemy import Column, Integer, String, DateTime
from app.database.database import Base
from app.dto import QuestionDto
from datetime import datetime


class Question(Base):
    """
    Defines the questions model
    """

    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    question_text = Column(String, index=True)
    answer_text = Column(String)
    creation_date = Column(DateTime, default=datetime.utcnow)

    @classmethod
    def from_dto(cls, dto: QuestionDto):
        return cls(
            question_text=dto.question,
            answer_text=dto.answer,
            creation_date=dto.creation_date
        )
