import sys

from sqlalchemy.orm import Session  # type: ignore
from typing import List, Type
import logging
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from database.database import SessionLocal
from database.database_session_manager import DatabaseSessionManager
from dto.question_dto import QuestionDto
from database.question import Question

# Create a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


class CommitError(Exception):
    def __init__(self, message):
        super().__init__(message)
        # Terminate the program
        sys.exit(1)


class QuestionRepository:
    __session: SessionLocal

    def __init__(self):
        self.__session = DatabaseSessionManager.get_session()

    def get_last_question_nullable(self) -> Type[Question] | None:
        return self.__session.query(Question).order_by(desc(Question.id)).first()

    def is_question_exist(self, question_text: str) -> bool:
        return self.__session.query(Question).filter(Question.question_text == question_text).first() is not None

    def create_questions(self, collection_dto: List[QuestionDto]) -> None:
        for question in collection_dto:
            self.__session.add(Question.from_dto(question))

        try:
            self.__session.commit()
        except SQLAlchemyError as error:
            # Log the exception
            logger.error(f"An error occurred: {error}")
            raise CommitError("Commit failed. Program terminated.")
