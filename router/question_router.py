from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session  # type: ignore
from starlette.responses import JSONResponse

from service.question_service import QuestionService, QuestionServiceError
from dto.question_dto import QuestionDto

questionrouter = APIRouter()


@questionrouter.post("/create-questions/", response_model=Union[QuestionDto, dict])
def create_questions(questions_num: int, question_service: QuestionService = Depends(QuestionService)) -> JSONResponse:
    last_question = question_service.get_last_question()
    try:
        question_service.create_unique_questions(questions_num)
    except QuestionServiceError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if last_question is None:
        return JSONResponse(content={})

    return JSONResponse(content=QuestionDto.from_question(last_question).to_dict())
