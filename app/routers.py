from fastapi import APIRouter
from sqlalchemy.orm import Session  # type: ignore
from .service import get_unique_questions

questionrouter = APIRouter()


# session.close() нужно куда-то поставить, иначе работа с бд - бесконечна
@questionrouter.get("/questions/")  # это будет get??
def create_questions(questions_num: int):
    # В контроллере нужно просто сделать вызов сервиса
    # Проверка на уникальность вопросов и сохранение в базу данных
    unique_questions = []
    unique_questions = get_unique_questions(questions_num)

    if len(unique_questions) == 0:
        return {}

    return unique_questions[-1]

# @questionrouter.get("/questions/")
# def create_questions(questions_num: int):
#     unique_questions = get_unique_questions(questions_num)
