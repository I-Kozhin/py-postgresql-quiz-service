from typing import List, Type
from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session  # type: ignore

from app.schemas.question import Question
from app.dto.question_dto import QuestionDto
from app.errors import logger, CommitError


class QuestionRepository:
    @staticmethod
    async def get_last_question_nullable(session: AsyncSession) -> Type[Question] | None:
        try:
            query = select(Question).order_by(desc(Question.id))
            result = await session.execute(query)
            return result.scalar()
        except SQLAlchemyError as e:
            logger.error(f"An error occurred while executing the last question from database: {e}")
            raise HTTPException(status_code=500,
                                detail=f'An unexpected error occurred while executing question from database.')

    @staticmethod
    async def create_questions(collection_dto: List[QuestionDto], session: AsyncSession) -> None:
        for question in collection_dto:
            session.add(Question.from_dto(question))

        try:
            await session.commit()
        except SQLAlchemyError as error:
            logger.error(f"An error occurred while committing in the User repository: {error}")
            raise CommitError("Commit failed. users table.")
