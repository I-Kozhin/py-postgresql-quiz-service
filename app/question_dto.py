from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Здесь можно добавить проверку полей через pydantic.Field

class QuestionDto(BaseModel):
    """
    This is data-transfer-object in case of input question from api
    """
    question_id: int | None = None
    answer: str | None = None
    question: str | None = None
    creation_date: datetime | None = None

    # def __init__(self, question_id: int, answer: Optional[str] = None, question: Optional[str] = None,
    #              creation_date: Optional[datetime] = None):
    #     super().__init__(question_id=question_id, answer=answer, question=question, creation_date=creation_date)
    #     self.question_id = question_id
    #     self.answer = answer
    #     self.question = question
    #     self.creation_date = creation_date
