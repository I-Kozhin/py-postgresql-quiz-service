from typing import Union

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database_session_manager import get_session
from app.service.question_service import QuestionService, QuestionApiServiceError
from app.dto.question_dto import QuestionDto
from app.errors import logger

question_router = APIRouter()
question_service = QuestionService()


@question_router.post("/create-questions/", response_model=dict)
async def create_questions(questions_num: int,
                           session: AsyncSession = Depends(get_session)) -> Union[dict, QuestionDto]:
    try:
        last_question = await question_service.get_last_question(session)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f'Failed to perform {create_questions} func: {e}')
        raise HTTPException(status_code=500,
                            detail=f'An unexpected error occurred while getting last question')

    try:
        await question_service.create_unique_questions(questions_num, session)
    except QuestionApiServiceError as e:
        logger.exception(f'Failed to perform {question_service.create_unique_questions} func: {e}')
        raise HTTPException(status_code=500,
                            detail=f'The server cannot get the last question from https://jservice.io')
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(f'Failed to perform {create_questions} func: {e}')
        raise HTTPException(status_code=500, detail=f'An unexpected error occurred while creating questions')

    if last_question is None:
        return {}

    return QuestionDto.from_question(last_question)
