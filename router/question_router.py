from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session  # type: ignore

from service.question_service import QuestionService, QuestionServiceError
from dto.question_dto import QuestionDto

questionrouter = APIRouter()


@questionrouter.post("/create-questions/")
def create_questions(questions_num: int, question_service: QuestionService = Depends(QuestionService))\
        -> Union[QuestionDto, dict]:
    last_question = question_service.get_last_question()
    try:
        question_service.create_unique_questions(questions_num)
    except QuestionServiceError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if last_question is None:
        return {}

    return QuestionDto.from_question(last_question)
