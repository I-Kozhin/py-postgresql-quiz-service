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
    def from_question(cls, question: 'Question') -> 'QuestionDto':
        return cls(
            question_id=question.id,
            answer=question.answer_text,
            question=question.question_text,
            creation_date=question.creation_date
        )

    def to_dict(self):
        return {
            "question_id": self.question_id,
            "question": self.question,
            "answer": self.answer,
            "creation_date": self.creation_date.isoformat() if self.creation_date else None
        }
