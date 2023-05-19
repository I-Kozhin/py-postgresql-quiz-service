from datetime import datetime

from pydantic import BaseModel


# Здесь можно добавить проверку полей через pydantic.Field

class QuestionBase(BaseModel):
    question_text: str
    answer_text: str


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int
    created_at: datetime
