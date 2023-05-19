from fastapi import APIRouter
from sqlalchemy.orm import Session  # type: ignore

from . import models
from .crud import get_random_questions
from .database import SessionLocal, engine
from .models import Question

models.Base.metadata.create_all(bind=engine)
questionrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@questionrouter.post("/questions/")
def create_questions(questions_num: int):
    session = SessionLocal()

    # Получение случайных вопросов
    random_questions = get_random_questions(questions_num)

    # Проверка на уникальность вопросов и сохранение в базу данных
    saved_questions = []
    for question_data in random_questions:
        question_text = question_data["question"]
        answer_text = question_data["answer"]

        # Проверка наличия вопроса в базе данных
        existing_question = session.query(Question).filter(Question.question_text == question_text).first()
        if existing_question:
            continue  # Если вопрос уже сохранен, пропустить его

        # Создание нового объекта вопроса и сохранение в базе данных
        new_question = Question(question_text=question_text, answer_text=answer_text)
        session.add(new_question)
        session.commit()

        saved_questions.append(new_question)

    session.close()

    # Возвращение сохраненных вопросов
    return saved_questions[-1] if saved_questions else {}
