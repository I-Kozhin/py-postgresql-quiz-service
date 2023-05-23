# Здесь реализуют create, delete, update, read
from sqlalchemy.orm import Session   # type: ignore
from typing import List
import logging
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from database.database import SessionLocal
from dto.question_dto import QuestionDto
from database.question import Question


# Create a logger
logger = logging.getLogger(__name__)


class QuestionRepository:
    __session: SessionLocal

    def __init__(self):
        self.__session = self.__get_session()

    def get_last_question_nullable(self) -> Question:
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

    @staticmethod
    def __get_session():
        session = SessionLocal()
        return session
