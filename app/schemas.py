from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Здесь можно добавить проверку полей через pydantic.Field
# class Category(BaseModel):
#     id: int | None = None
#     title: str | None = None
#     created_at: datetime | None = None
#     updated_at: datetime | None = None
#     clues_count: int | None = None
#
#     def __init__(
#         self,
#         id: Optional[int] = None,
#         title: Optional[str] = None,
#         created_at: Optional[datetime] = None,
#         updated_at: Optional[datetime] = None,
#         clues_count: Optional[int] = None
#     ):
#         self.id = id
#         self.title = title
#         self.created_at = created_at
#         self.updated_at = updated_at
#         self.clues_count = clues_count

class QuestionDtoOutput(BaseModel):
    """
    This is data-transfer-object in case of output from DB
    """
    question_id: int
    answer: str | None = None
    question: str | None = None
    created_at: datetime | None = None

    # def __init__(
    #         self,
    #         question_id: int,
    #         answer: Optional[str] = None,
    #         question: Optional[str] = None,
    #         created_at: Optional[datetime] = None
    # ):
    #     self.question_id = id
    #     self.answer = answer
    #     self.question = question
    #     self.created_at = created_at


class QuestionDtoInput(QuestionDtoOutput):
    """
    This is data-transfer-object in case of input question from api
    """
    airdate: datetime | None = None
    updated_at: datetime | None = None
    categoty_id: int | None = None
    game_id: int | None = None
    invalid_count: Optional[int] | None = None
    # categoty: Category | None = None

    # def __init__(
    #         self,
    #         id: int,
    #         answer: Optional[str] = None,
    #         question: Optional[str] = None,
    #         created_at: Optional[datetime] = None,
    #         airdate: Optional[datetime] = None,
    #         updated_at: Optional[datetime] = None,
    #         category_id: Optional[int] = None,
    #         game_id: Optional[int] = None,
    #         invalid_count: Optional[int] = None,
    #         # category: Optional[Category] = None
    # ):
    #     super().__init__(id, answer, question, created_at)
    #     self.airdate = airdate
    #     self.updated_at = updated_at
    #     self.category_id = category_id
    #     self.game_id = game_id
    #     self.invalid_count = invalid_count
    #     self.category = category

# class QuestionBase(BaseModel):
#
#     id: int
#     question_text: str | None = None
#     answer_text: str | None = None
#     creation_date: str | None = None
#
#
# class QuestionBase(BaseModel):
#     question_text: str
#     answer_text: str
#
#
# class QuestionCreate(QuestionBase):
#     pass
#
#
# class Question(QuestionBase):
#     id: int
#     created_at: datetime
