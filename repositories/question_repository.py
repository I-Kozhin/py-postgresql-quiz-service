import logging
import sys
from typing import List, Type

from sqlalchemy import desc
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session  # type: ignore

from database.question import Question
from dto.question_dto import QuestionDto

# Create a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class CommitError(Exception):
    def __init__(self, message):
        super().__init__(message)
        # Terminate the program
        sys.exit(1)


class QuestionRepository:
    @staticmethod
    async def get_last_question_nullable(session: AsyncSession) -> Type[Question] | None:
        query = select(Question).order_by(desc(Question.id))
        result = await session.execute(query)
        return result.scalars().first()
        #  return self.__session.query(Question).order_by(desc(Question.id)).first()

    @staticmethod
    async def is_question_exist(question_text: str, session: AsyncSession) -> bool:
        query = select(Question).filter(Question.question_text == question_text).first()
        result = await session.execute(query)
        return result is not None

    @staticmethod
    async def create_questions(collection_dto: List[QuestionDto], session: AsyncSession) -> None:
        for question in collection_dto:
            session.add(Question.from_dto(question))

        try:
            await session.commit()
        except SQLAlchemyError as error:
            # Log the exception
            logger.error(f"An error occurred: {error}")
            raise CommitError("Commit failed. Program terminated.")
