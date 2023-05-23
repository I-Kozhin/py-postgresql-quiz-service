from typing import Union

from fastapi import APIRouter
from sqlalchemy.orm import Session  # type: ignore

from service.question_service import QuestionService
from dto.question_dto import QuestionDto

questionrouter = APIRouter()


@questionrouter.post("/create-questions/")
def create_questions(questions_num: int) -> Union[QuestionDto, dict]:
    question_service = QuestionService()
    last_question = question_service.get_last_question()
    question_service.create_unique_questions(questions_num)

    if last_question is None:
        return {}

    return QuestionDto.from_question(last_question)
