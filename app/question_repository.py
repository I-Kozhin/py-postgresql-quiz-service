# Здесь реализуют create, delete, update, read
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session  # type: ignore

from . import question
from app.database import SessionLocal, engine
from app.question import Question
from app.question_dto import QuestionDto


class QuestionRepository:
    __session: SessionLocal

    def __init__(self):
        # self.__session = self.__get_session()
        self.__session = SessionLocal()

    def get_last_question_nullable(self) -> Question:
        return self.__session.query(Question).order_by(desc(Question.id)).first()

    def is_question_exist(self, question_text: str) -> bool:
        return self.__session.query(Question).filter(Question.question_text == question_text).first() is not None

    def create_questions(self, collection_dto: List[QuestionDto]) -> None:
        for question in collection_dto:
            self.__session.add(Question(question))

        try:
            self.__session.commit()
        except:
            pass  # логирую

    # создать один класс dto

    @staticmethod
    def __get_session():
        session = SessionLocal()
        try:
            yield session
        finally:
            session.close()
