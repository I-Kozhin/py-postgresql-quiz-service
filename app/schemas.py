from pydantic import BaseModel


class QuestionBase(BaseModel):
    # Здесь можно добавить проверку полей через pydantic.Field
    id: int
    question_text: str | None = None
    answer_text: str | None = None
    creation_date: str | None = None
