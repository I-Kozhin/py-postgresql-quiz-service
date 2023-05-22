# Здесь реализуют create, delete, update, read

# Нужно создать класс-прослойку, обёртку для json и приводить нужно к QuestionDto (data-transfer-object)
# и из get_random_questions я получаю прослойку QuestionDto, а её передаю в crud или в нужную функцию
# inputdto - то что я получаю, outputdto - то что я возвращаею, если информация на вход и выход - разная
# буфер dto обязателен - получаю из бд что-то - оборачиваю в дто

# 1) вынесение логики фичи в методы QuestionService
# 2) JSON полученный из их апи - оборачиваем в QuestionDto
# 3) Уточнить как создаются ID в БД. Идеально было бы, чтобы БД сама делала ID 1, 2, 3, 4.... Но если гуиды будешь
# делать, то тоже норм
# 4) Конструктор модели вопроса БД (Question) принимает dto модель
# 5) Get запрос, а не POST.
# 6) Session будет создаваться в сервисе.
# Результат - json предыдущего вопроса или пусто если его нет. Но думай над этим, кода приведешь код в порядок, а
# пока возвращай json вопроса который создал.

from sqlalchemy.orm import Session  # type: ignore

from .models import Question

from .schemas import QuestionDtoInput, QuestionDtoOutput
from . import models
from .database import SessionLocal, engine

from sqlalchemy.exc import SQLAlchemyError

from typing import Type

models.Base.metadata.create_all(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# def get_question_by_id(session: get_session(), id: int) -> Type[Question] | None:
#     return session.query(Question).filter(Question.id == id).first()

def get_question_by_text(session: SessionLocal, question_text: str) -> Type[QuestionDtoOutput] | None:
    return session.query(Question).filter(Question.question_text == question_text).first()


def create_question(question: QuestionDtoInput) -> QuestionDtoOutput | bool:
    session = SessionLocal()  # потом на get_session
    try:
        # Проверяем, есть ли вопрос в базе данных
        existing_question = get_question_by_text(session, question.question)

        # Если вопрос уже существует, возвращаем его
        if existing_question:
            return True

        new_question = Question(question_text=question.question, answer_text=question.answer,
                                creation_date=question.created_at)
        session.add(new_question)
        session.commit()
        session.refresh(new_question)
        return new_question

    except SQLAlchemyError as error:
        session.rollback()
        print(str(error))
        return False
