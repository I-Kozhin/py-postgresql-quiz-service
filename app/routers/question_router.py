from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database_session_manager import get_session
from app.services.question_service import QuestionService, QuestionServiceError
from app.dto.question_dto import QuestionDto

questionrouter = APIRouter()


@questionrouter.post("/create-questions/", response_model=dict)
async def create_questions(questions_num: int, question_service: QuestionService = Depends(QuestionService),
                           session: AsyncSession = Depends(get_session)) -> Union[dict, QuestionDto]:
    last_question = await question_service.get_last_question(session)
    try:
        await question_service.create_unique_questions(questions_num, session)
    except QuestionServiceError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if last_question is None:
        return JSONResponse(content={})

    return QuestionDto.from_question(last_question)

