from datetime import datetime
from pydantic import BaseModel


class QuestionDto(BaseModel):
    """
    This is data-transfer-object in case of input question from api
    """
    question_id: int | None = None
    question: str | None = None
    answer: str | None = None
    creation_date: datetime | None = None

    @classmethod
    def from_question(cls, question: 'Question'):
        return cls(
            question_id=question.id,
            answer=question.answer_text,
            question=question.question_text,
            creation_date=question.creation_date
        )
