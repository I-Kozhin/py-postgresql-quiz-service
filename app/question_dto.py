from datetime import datetime

from pydantic import BaseModel

from app.question import Question


# Здесь можно добавить проверку полей через pydantic.Field

class QuestionDto(BaseModel):
    """
    This is data-transfer-object in case of input question from api
    """
    question_id: int | None = None
    question: str | None = None
    answer: str | None = None
    creation_date: datetime | None = None

    def __init__(self, question: Question):
        super().__init__(question_id=question.id, answer=question.answer_text,
                         question=question.question_text, creation_date=question.creation_date)
